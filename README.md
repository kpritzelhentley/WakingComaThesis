# Disorders of Consciousness Bachelor Thesis

## iPython Notes
- whos: See all created variables
- object?: see information on variable, object or function
- !ls: start system entry mode

## Technical Terms

*Paradigm*: a typical example or pattern of something; a pattern or model

*Frequenzbandrelationen*:

*Epoch*: a datasegment (e.g. eeg data) which was created by the onset of a stimulus

*Subtrial*: activation of different stimuli

*Trial*: Multiple repetitions of a subtrial which leads to a result of the machine 

*Baseline Correction*: A perfect curve shape of analytical 2D data objects include a constant base level value, where no signals are observed. This base level is called the baseline of a 2D data object. Because of changes in experimental conditions during measurement, temperature influences or any other interference, the baseline sometimes drifts away from its original base level. In this case, the baseline of a 2D data object might be corrected after a measurement has been completed using the baseline correction function of the software. (https://www.labcognition.com/onlinehelp/en/baseline_correction.htm) --> see also mne.epochs and mne.baseline

## ToDo
✓ plot single channels (from the 'data' array)
✓ calculate the average over all channels of one patient and extract data segments based on labels. The P300 spike should be visible for the novel and unexpected end of sentence labels.
- analyse relative frequency bands
- online calculation of relative frequency bands of eeg segments

## Data
First Plot of single channel and trigger points
![example plot](https://github.com/kpritzelhentley/WakingComaThesis/blob/master/Python%20Skipts/example_channel_and_trigger_plt.png)

## Sources and Sites
CITEC Projects Redmine: https://projects.cit-ec.uni-bielefeld.de/

## Issues and Errors
- python mne filter OSError: [Errno 12] Cannot allocate memory
