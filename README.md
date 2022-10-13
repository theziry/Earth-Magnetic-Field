# Earth Magnetic Field
## Overview:

Very early in the study of the Earth’s magnetism, it had been realised that the magnetic field 𝐁 is changing with time. The proper description of this evolution came with the setting of magnetic observatories from the middle of the nineteenth century onward. The general assumption was that most of observed fast variations in 𝐁(t) were due to external fields perturbations, while the dominant core field varied slowly over time.

The accumulation of long time series of magnetic observations led to an evolution of this paradigm since, at observatory sites, the main field secular variation (SV), or rate of change of the field, 𝜕𝐁∕𝜕t ) often appeared as linear trends with abrupt changes of slopes. These singular events are clearly generated in the core and have been called “geomagnetic jerks”.
The evolution of this secular variation has also been studied in terms of secular acceleration (SA, or second time derivative, ${𝜕^2𝐁∕𝜕t^2}$).

The crucial issue regarding field models derived from magnetic data is their temporal resolution. Observatory time series show a temporal spectrum S(f) in the range of periods from ≈ 70 yrs down to a couple of years. This property, which is coherent with the existence of geomagnetic jerks, is also recovered in time series of the geomagnetic Gauss coefficients. 

# Project Description:

This project aims to study and model the Earth Magnetic Field Using Geomagnetic Observatory Data.

The remainder of this work is organised in three sections (three notebooks) as follows: 

## Section 1: Signal processing
### [1-EMF-Signal_Processing.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/1-EMF-Signal_Processing.ipynb)

In this first notebook, I first started generating Synthetic timeseries data that contains a single harmonic component of period of $10 years$ sampled each month, than I deepen my analysis using real data; using long series of Chambon-la-Forêt $(CLF)$ observatory data which are monthly means, and discussing the observed SV evolutions over time.  
In both parts (synthetic and real), I performed a spectral analysis on the signals and applied a Butterworth filters. 

Looking through a finite duration ‘window’ at the signal (Regard as a multiplication in the time domain.), taking samples but the Fourier Transform is periodic. Therefore, to extract information at a particular frequency at least two samples per cycle must be taken, and this leads to the concept of the $Nyquist$ $frequency$ e.g. if the sampling rate is 10Hz, the maximum resolvable frequency is 5Hz. If there are higher frequencies present in the signal they are aliased – they masquerade as lower frequencies. 

To resolve a sinusoidal signal it must be sampled at least twice per cycle. If the sampling rate is $f_{samp}$ then the maximum resolvable frequency is the $Nyquist$ $frequency$: $f_n= f_{samp}/2$ (Ideally, select the sampling rate to be at least the Nyquist rate required to resolve the maximum frequency component of a signal.).
In practice a signal may not be band-limited. If the signal includes frequency $f$ and the sampling rate is $f_{samp}$ then the samples of signals at frequencies $f ± nf_{samp}$ are indistinguishable from $f_{sig}$  – they are ‘aliases’. Fourier analysis will put all the aliased signals at $f_{sig}$.
Then Collect monthly samples and Smooth by means of a suitable filter attempt to preserve as much information as possible in the frequency band.


## Section 2: Data Visualisation
### [2-EMF-Observatory-Data-Visualisation.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/2-EMF-Observatory-Data-Visualisation.ipynb)

The goal of this notebooK is to 

## Section 3: Spherical Harmonic Model of Geomagnetic Field
### [3-Spherical-Harmonic-Models.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/3-Spherical-Harmonic-Models%20.ipynb)




# References:
- Malin, S. R. . and Barraclough, D., (1981). An algorithm for synthesizing the geomagnetic field, Computers & Geosciences. Pergamon, 7(4), pp. 401–405. doi: 10.1016/0098-3004(81)90082-0.
- Lesur,V. . Gillet, N. . Hammer M. D. & Mandea M. (2022). Rapid Variations of Earth’s Core Magnetic Field, Surveys in Geophysics volume 43, pages41–69. doi: 10.1007/s10712-021-09662-4.
