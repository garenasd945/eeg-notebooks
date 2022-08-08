"""

CLI Pipeline for Analysis of EEGNB Recorded Data

To do: 
1. Package parameters into a dictionary
2. Adapt for other experiments/create an easy user manual
3. Add additional analysis methods

Usage (for downloaded datasets): 

Visual N170:
raw, epochs = load_eeg_data('visual-n170', device_name='muse2016_bfn')
make_erp_plot(epochs)

Visual P300:
raw, epochs = load_eeg_data('visual-P300', device_name='muse2016', event_id={'Non-Target': 1, 'Target': 2})
make_erp_plot(epochs, conditions=OrderedDict(NonTarget=[1],Target=[2]))

Other Experiments to be added later eg. Visual SSVEP

Loading Recorded Data : 

raw, epochs = load_eeg_data(experiment, subject, session, device_name, tmin, tmax, reject)
make_erp_plot(epochs, title)

Changable parameters to adjust plot  

tmin, tmax - Start and end time of the epochs in seconds, relative to the time-locked event. 
The closest or matching samples corresponding to the start and end time are included.

reject - Reject epochs based on maximum peak-to-peak signal amplitude (PTP),
i.e. the absolute difference between the lowest and the highest signal value.

ci - confidence interval

n_boot - number of bootstrap samples

"""

# Some standard pythonic imports
import os
from collections import OrderedDict
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

# MNE functions
from mne import Epochs,find_events

# EEG-Notebooks functions
from eegnb.analysis.utils import load_data,plot_conditions
from eegnb.datasets import fetch_dataset


def load_eeg_data(experiment, subject=1, session=1, device_name='muse2016_bfn', tmin=-0.1, tmax=0.6, baseline=None, 
                    reject={'eeg': 5e-5}, preload=True, verbose=False,
                        picks=[0,1,2,3], event_id = OrderedDict(House=1,Face=2)):
    """
    Loads EEG data from the specified experiment, subject, session, and device.
    Returns the raw and epochs objects.

    Procedure
    1. Loads the data using file names and retrives if not already present
    2. Epochs the data
    3. Computes the ERP
    4. Returns the raw and ERP objects

    Parameters
    ----------
    experiment : Experiment Name
    subject : Subject ID of performed experiment
    session : Session ID of performed experiment
    device_name : Device used for performed experiment
    tmin : Start time of the epochs in seconds, relative to the time-locked event.
    tmax : End time of the epochs in seconds, relative to the time-locked event.
    baseline : Not very sure..?
    reject : Rejection parameters for the epochs.
    preload : If True, preload the epochs into memory.
    verbose : If True, print out messages.
    picks : Channels to include in the analysis.
    event_id : Dictionary of event_id's for the epochs
    """
    
    # Loading Data
    eegnb_data_path = os.path.join(os.path.expanduser('~/'),'.eegnb', 'data')
    n170_data_path = os.path.join(eegnb_data_path, experiment, 'eegnb_examples')

    # If dataset hasn't been downloaded yet, download it
    if not os.path.isdir(n170_data_path):
        fetch_dataset(data_dir=eegnb_data_path, experiment=experiment, site='eegnb_examples')

    raw = load_data(subject,session,
                    experiment=experiment, site='eegnb_examples', device_name=device_name,
                    data_dir = eegnb_data_path)

    # Visualising the power spectrum 
    raw.plot_psd()
    plt.show()

    raw.filter(1,30, method='iir')
    raw.plot_psd(fmin=1, fmax=30)
    plt.show()

    # Epoching
    # Create an array containing the timestamps and type of each stimulus (i.e. face or house)
    events = find_events(raw)

    # Create an MNE Epochs object representing all the epochs around stimulus presentation
    epochs = Epochs(raw, events=events, event_id=event_id,
                    tmin=tmin, tmax=tmax, baseline=baseline,
                    reject=reject, preload=preload,
                    verbose=verbose, picks=picks)

    print('sample drop %: ', (1 - len(epochs.events)/len(events)) * 100)
    print(epochs)

    return raw, epochs


def make_erp_plot(epochs, conditions=OrderedDict(House=[1],Face=[2]), ci=97.5, n_boot=1000, title='',
                   diff_waveform=None, #(1, 2))
                   channel_order=[1,0,2,3]):
    """
    Plots the ERP for the specified conditions.

    Parameters
    ----------
    epochs : MNE Epochs object
    conditions : OrderedDict holding the conditions to plot
    ci: confidence interval
    n_boot: number of bootstrap samples
    title: title of the plot
    diff_waveform: tuple of two integers indicating the channels to compare
    channel_order: list of integers indicating the order of the channels to plot
    """

    fig, ax = plot_conditions(epochs, conditions=conditions,
                            ci=97.5, n_boot=1000, title='',
                            diff_waveform=None, #(1, 2))
                            channel_order=[1,0,2,3]) # reordering of epochs.ch_names according to [[0,2],[1,3]] of subplot axes

    # Manually adjust the ylims
    for i in [0,2]: ax[i].set_ylim([-0.5,0.5])
    for i in [1,3]: ax[i].set_ylim([-1.5,2.5])

    plt.show()
