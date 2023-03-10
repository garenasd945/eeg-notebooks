=============
EEG-Notebooks
=============

*Democratizing the cognitive neuroscience experiment*

|badge_test| |badge_binder|

.. |badge_test| image:: https://github.com/NeuroTechX/eeg-notebooks/workflows/Test/badge.svg
   :target: https://github.com/NeuroTechX/eeg-notebooks/actions

.. |badge_binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/NeuroTechX/eeg-notebooks/master

.. image:: https://github.com/NeuroTechX/eeg-notebooks/raw/master/doc/img/eeg-notebooks_logo.png
   :align: center

EEG-Notebooks is a collection of classic EEG experiments, implemented in Python 3 and Jupyter notebooks. The experimental protocols and analyses are quite generic, but are primarily taylored for low-budget / consumer EEG hardware such as the InteraXon MUSE and OpenBCI Cyton. The goal is to make cognitive neuroscience and neurotechnology more accessible, affordable, and scalable. 

- **For an intro talk on the eeg-notebooks project see:** `JG's Brainhack Ontario presentation <https://www.crowdcast.io/e/brainhack-ontario/7>`_.  
- **For documentation see:** `documentation site <https://neurotechx.github.io/eeg-notebooks/index.html>`_.
- **For code see:** `github site <https://github.com/neurotechx/eeg-notebooks>`_.
- **For instructions on running experiments see:** `running experiments <https://neurotechx.github.io/eeg-notebooks/getting_started/running_experiments.html>`_.
- **For instructions on initiating an EEG stream see:** `initiating an EEG stream <https://neurotechx.github.io/eeg-notebooks/getting_started/streaming.html>`_.
- **A series of tutorial videos will be coming soon!**  


----

**Note:** eeg-notebooks underwent major changes to the API in v0.2. The old v0.1 is still available if you need it, in `this repo <https://github.com/neurotechx/eeg-notebooks_v0.1>`_.

----


Overview
--------

Conventional lab-based EEG research typically uses research-grade (often high-density) EEG devices, dedicated stimulus delivery software and hardware, and dedicated technicians responsible for operating this equipment. The price tag for these items can easily extend into hundreds of thousands of dollars, which naturally places major limits on their acquisition and usage. 

In recent years, however, developments in hardware and software technologies are making it possible for many classic EEG cognitive neuroscience experiments to be conducted using a standard laptop/personal computer and a relatively cheap consumer-grade EEG device, with a combined minimum cost of less than 1000 dollars. This opens dramatic new possibilities for neurotechnology and cognitive neuroscience *education* (at both University and High School levels), as well as more ambitious and larger-scale *research* and *clinical* applications using large numbers of devices, and/or in more naturalistic (i.e. out-of-the-lab) settings. We like to think of this as contributing to the *democratization of the cognitive neuroscience experiment*.

The core aim of the EEG-Notebooks project is to provide the critical 'glue' that pulls together the various enabling technologies necessary for running these experiments and analyzing the data. This includes functionality for 

* streaming data from various relatively new wireless consumer-grade EEG devices  
* visual and auditory stimulus presentation, concurrent with and time-locked to the EEG recordings  
* a growing library of well-documented, ready-to-use, and ready-to-modify experiments 
* signal processing, statistical, and machine learning data analysis functionalities

A real one-stop-shop!

For more discussion on these social/scientific/technological contexts and trajectories, a) feel free to get in touch directly (see #Contact info below) and b) keep an eye out for the forthcoming eeg-notebooks research paper.


Documentation
-------------

The current version of eeg-notebooks is the 0.2.X series. The code-base and API are under major development and subject to change.

Check the `changelog <https://neurotechx.github.io/eeg-notebooks/changelog.html>`_ for notes on changes from previous versions.

**Installation instructions**, steps for **getting started**, common **troubleshooting** solutions and more can be found in the documentation for eeg-notebooks, available on the
`documentation site <https://neurotechx.github.io/eeg-notebooks/index.html>`_.

Acknowledgments
----------------

EEG-Notebooks was created by the `NeurotechX <https://neurotechx.com/>`_ hacker/developer/neuroscience community. The ininitial idea and majority of the groundwork was due to Alexandre Barachant - including the `muse-lsl <https://github.com/alexandrebarachant/muse-lsl/>`_ library, which is core dependency. Lead developer on the project is now `John Griffiths <www.grifflab.com>`_ . 

Key contributors include: Alexandre Barachant, Hubert Banville, Dano Morrison, Ben Shapiro, John Griffiths, Amanda Easson, Kyle Mathewson, Jadin Tredup, Erik Bjäreholt. 

Thanks also to Andrey Parfenov for the excellent `brainflow <https://github.com/brainflow-dev/brainflow/>`_ library, which has allowed us to dramatically expand the range of supporte devices; as well as the developers of `PsychoPy <https://github.com/psychopy/psychopy/>`_ and `MNE <https://github.com/mne-tools/mne-python/>`_, which together make up the central scaffolding of eeg-notebooks. 


Contribute
----------

This project welcomes and encourages contributions from the community!

If you have an idea of something to add to eeg-notebooks, please start by opening an
`issue <https://github.com/NeuroTechX/eeg-notebooks/issues/new/choose>`_.


Contact
-------------

The best place for general discussion on eeg-notebooks functionality is the `issues page <https://github.com/NeuroTechX/eeg-notebooks/issues/new/choose>`_. For more general questions and discussions, you can e-mail `john.griffiths@utoronto.ca`, or ping us on the `NeuroTechX Discord <https://discord.gg/zYCBfBf4W4>`_ or `NeuroTechX slack <https://neurotechx.herokuapp.com>`_.



.. image:: https://github.com/NeuroTechX/eeg-notebooks/raw/master/doc/img/eeg-notebooks_democratizing_the_cogneuro_experiment.png
   :align: center
   :scale: 50
   
##PsychoPy
PsychoPy 是一款用于编写心理学实验程序的Python库。它提供了一个可视化的编程界面，可以通过拖放和点选来创建心理学实验的各个组件，包括刺激呈现、响应记录、实验流程和数据收集等。此外，PsychoPy 还支持多种刺激类型，如文本、图像、声音和视频等，可以满足不同类型实验的需求。
PsychoPy 可以在多个平台上运行，包括 Windows、MacOS 和 Linux，同时也可以与其他 Python 库和软件集成，如 NumPy、Pandas、Matplotlib 和 OpenCV 等。
PsychoPy 还提供了许多有用的工具和函数，例如实验控制、刺激生成、响应记录和数据分析等，可以使心理学实验的编写和分析更加方便和高效。此外，PsychoPy 还有一个活跃的社区，用户可以分享自己的代码和经验，获取支持和反馈。
总之，PsychoPy 是一款功能强大、易于使用的 Python 库，可以帮助心理学研究人员和实验者创建和运行心理学实验。


