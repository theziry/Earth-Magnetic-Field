# Earth Magnetic Field

This project aims to study and model the Earth Magnetic Field Using Geomagnetic Observatory Data.

# Project Description:

Very early in the study of the Earth’s magnetism, it had been realised that the magnetic field 𝐁 is changing with time. The proper description of this evolution came with the setting of magnetic observatories from the middle of the nineteenth century onward. The general assumption was that most of observed fast variations in 𝐁(t) were due to external fields perturbations, while the dominant core field varied slowly over time.

The accumulation of long time series of magnetic observations led to an evolution of this paradigm since, at observatory sites, the main field secular variation (SV), or rate of change of the field, 𝜕𝐁∕𝜕t ) often appeared as linear trends with abrupt changes of slopes. These singular events are clearly generated in the core and have been called “geomagnetic jerks”.
The evolution of this secular variation has also been studied in terms of secular acceleration (SA, or second time derivative, ${𝜕^2𝐁∕𝜕t^2}$).

The crucial issue regarding field models derived from magnetic data is their temporal resolution. Observatory time series show a temporal spectrum S(f) in the range of periods from ≈ 70 yrs down to a couple of years. This property, which is coherent with the existence of geomagnetic jerks, is also recovered in time series of the geomagnetic Gauss coefficients. 

The remainder of this work is organised in three sections as follows: 

## Section 1: 
### Signal processing: [1-EMF-Signal_Processing.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/1-EMF-Signal_Processing.ipynb)

In this section, I first started generating Synthetic timeseries data that contains a single harmonic component of period of 10 years sampled each month than I deepen my analysis using real data; using long series of Chambon-la-Forêt (CLF) observatory data which are monthly means, and we discuss the observed SV evolutions over time. 
In both parts (synthetic and real), I performed a spectral analysis on the signals and applied a Butterworth filters. 

## Section 2: 
### Data Visualisation: [2-EMF-Observatory-Data-Visualisation.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/2-EMF-Observatory-Data-Visualisation.ipynb)

The goal of this first noteboo

## Section 3: 
### – Spherical Harmonic Model of Geomagnetic Field : [3-Spherical-Harmonic-Models.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/3-Spherical-Harmonic-Models%20.ipynb)
