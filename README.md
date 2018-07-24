# Disorders of Consciousness Bachelor Thesis

## iPython Notes
- whos: See all created variables
- object?: see information on variable, object or function
- !ls: start system entry mode

## Technical Terms

__*Paradigm*__: a typical example or pattern of something; a pattern or model

__*Relative frequency bands*__: The oscillatory neural activity can be captured with the help of the electroencephalogram. The oscillations can be sperated into and are classified in frequency bands. Since every band has a different power level the bands must be compared relavtive to each other.

__*Classification of Frequency Bands*__: 
- Delta 1-3 Hz: Deep Sleep, Unconsciousness, Coma 
- Theta 4-7 Hz: Other Sleep Stages (REM), Emotions, Meditation, Short-Term-Memory 
- Alpha 8-12 Hz: Relaxation, Fatigue, Eyes Closed while Conscious 
- Beta 13-29 Hz: Awake, Aktive Thought, Concentration 
- Gamma > 30 Hz: Long-Time-Memory, Conscious Waking State, Will, Focus

__*Epoch*__: a datasegment (e.g. eeg data) which was created by the onset of a stimulus

__*Subtrial*__: activation of different stimuli

__*Trial*__: Multiple repetitions of a subtrial which leads to a result of the machine 

__*Baseline Correction*__: A perfect curve shape of analytical 2D data objects include a constant base level value, where no signals are observed. This base level is called the baseline of a 2D data object. Because of changes in experimental conditions during measurement, temperature influences or any other interference, the baseline sometimes drifts away from its original base level. In this case, the baseline of a 2D data object might be corrected after a measurement has been completed using the baseline correction function of the software. (https://www.labcognition.com/onlinehelp/en/baseline_correction.htm) --> see also mne.epochs and mne.baseline

__*Etiology*__: cause, origin; specifically : the cause of a disease or abnormal condition 

__*Pathological*__: involving or caused by a physical or mental disease

__*Anoxia*__: The term anoxia means a total depletion in the level of oxygen, an extreme form of hypoxia or "low oxygen". (Used to describe a type of Coma: Anoxic Coma)

__*Nociceptive Stimulus*__: a painful, sometimes detrimental or injurious, stimulus. A nociceptor is a sensory neuron that responds to damaging or potentially damaging stimuli.

__*Modulate*__: exert a modifying or controlling influence on.

__*Novelty*__: the quality of being new, original, or unusual. A novelty P300 component indicates attention orienting.

__*Elicit*__: evoke or draw out (a reaction, answer, or fact) from someone.

__*Contingent*__: occurring or existing only if (certain circumstances) are the case; dependent on

__*Putative*__: generally considered to be; generally thought to be the thing mentioned

__*Averages*__: 
- mean (Durchschnitt): sum of values divided by number of values
- median: middle value in a sorted list
- mode: value which occurs most often

__*Endogenous*__: having an internal cause or origin. (Antonym: Exogenous)

## ToDo
- ✓ plot single channels (from the 'data' array)
- ✓ calculate the average over all channels of one patient and extract data segments based on labels. The P300 spike should be visible for the novel and unexpected end of sentence labels.
- ✓ calculate relative frequency bands
- ✓ online calculation of relative frequency bands of eeg segments
- ✓ create gui with electrode positions
- __Change Visualization window so that there are two columns of plots each with 16 rows__
- ✓ Do online calculation of mean and standard deviation
- ✓ change colors of elctrodes depending on the highs and lows of the mean value inside a window
- ✓ be able to switch between frequency bands (drop down)
- ✓ create a legend for the electrode colors
- ✓ either *use* close button or delete it
- ✓ improve window and overlap size. be able to describe how the different sizes affect the visual output
- ✓ set limits over a longer period of time and make them less influenced by every sample
- __use a counter to dictate how often relband is calulated__
- __make window and overlap size adjustable in gui__
- __consider setting one upper and lower limit for all frequencies in order to see how hight one frequency is in relation to the others__

## Data
First Plot of single channel and trigger points
![example plot](https://github.com/kpritzelhentley/WakingComaThesis/blob/master/Python%20Skipts/example_channel_and_trigger_plt.png)

## Sources and Sites
- [CITEC Projects Redmine](https://projects.cit-ec.uni-bielefeld.de/)
--> This Site can only be reached within the TechFak Network. Visit [this](https://techfak.net/dienste/netz/vpn) site to arrange the linux VPN connection via GUI. Username: kpritzelhentley, Password: Netzwerk Passwort which can be looked up via ssh and the command "tfpasswd net"
- How to work with Git Submodules: https://git-scm.com/book/en/v2/Git-Tools-Submodules
- PyQt5 Tutorial: http://zetcode.com/gui/pyqt5/firstprograms/

- Resting-state EEG study of comatose patients: a connectivity and frequency analysis to find differences between vegetative and minimally conscious states: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3812750/

## Issues and Errors
