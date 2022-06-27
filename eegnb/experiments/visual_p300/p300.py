import os
from time import time
from glob import glob
from random import choice

import numpy as np
from pandas import DataFrame
from psychopy import visual, core, event

from eegnb import generate_save_fn
from eegnb.stimuli import CAT_DOG
from eegnb.devices.eeg import EEG
from eegnb.experiments.Experiment import Experiment as Experiment

class VisualP300(Experiment):
    
    def __init__(self, duration=120, eeg: EEG=None, save_fn=None,
            n_trials = 2010, iti = 0.4, soa = 0.3, jitter = 0.2):
        
        exp_name = "Visual P300"
        super().__init__(exp_name, duration, eeg, save_fn, n_trials, iti, soa, jitter)
        
    def load_stimulus(self):
        
        load_image = lambda fn: visual.ImageStim(win=self.mywin, image=fn)
        # Setup graphics
        self.targets = list(map(load_image, glob(os.path.join(CAT_DOG, "target-*.jpg"))))
        self.nontargets = list(map(load_image, glob(os.path.join(CAT_DOG, "nontarget-*.jpg"))))
        
        return [self.nontargets, self.targets]

    def present_stimulus(self, ii):

        label = self.trials["parameter"].iloc[ii]
        image = choice(self.targets if label == 1 else self.nontargets)
        image.draw()

        # Push sample
        if self.eeg:
            timestamp = time()
            if self.eeg.backend == "muselsl":
                marker = [self.markernames[label]]
            else:
                marker = self.markernames[label]
            self.eeg.push_sample(marker=marker, timestamp=timestamp)

        self.mywin.flip()