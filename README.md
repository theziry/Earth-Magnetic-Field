# Earth Magnetic Field
## Overview:

Very early in the study of the Earth’s magnetism, it had been realised that the magnetic field 𝐁 is changing with time. The proper description of this evolution came with the setting of magnetic observatories from the middle of the nineteenth century onward. The general assumption was that most of observed fast variations in 𝐁(t) were due to external fields perturbations, while the dominant core field varied slowly over time.

The accumulation of long time series of magnetic observations led to an evolution of this paradigm since, at observatory sites, the main field secular variation (SV), or rate of change of the field, 𝜕𝐁∕𝜕t ) often appeared as linear trends with abrupt changes of slopes. These singular events are clearly generated in the core and have been called $“geomagnetic jerks”$.
The evolution of this secular variation has also been studied in terms of secular acceleration (SA, or second time derivative, ${𝜕^2𝐁∕𝜕t^2}$).

The crucial issue regarding field models derived from magnetic data is their temporal resolution. Observatory time series show a temporal spectrum S(f) in the range of periods from ≈ 70 yrs down to a couple of years. This property, which is coherent with the existence of geomagnetic jerks, is also recovered in time series of the geomagnetic Gauss coefficients. 

# Project Description:

This project aims to study and model the Earth Magnetic Field Using Geomagnetic Observatory Data.

The remainder of this work is organised in three sections (three notebooks) as follows: 

## Section 1: Signal processing
## [1-EMF-Signal_Processing.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/1-EMF-Signal_Processing.ipynb)

In this first notebook, you will learn how to play with timeseries with python, with an application to the geomagnetic field recorded at the Chambon-la-Forêt $(CLF)$ observatory: performing a spectral analysis on the signals and applying a Butterworth filters and Smooth by means of a suitable filter with the attempt to preserve as much information as possible in the frequency band. 

Looking through a finite duration ‘window’ at the signal (Regard as a multiplication in the time domain.), taking samples but the Fourier Transform is periodic. Therefore, to extract information at a particular frequency at least two samples per cycle must be taken, and this leads to the concept of the $Nyquist$ $frequency$ e.g. if the sampling rate is 10Hz, the maximum resolvable frequency is 5Hz. If there are higher frequencies present in the signal they are aliased – they masquerade as lower frequencies. 

To resolve a sinusoidal signal it must be sampled at least twice per cycle. If the sampling rate is $f_{samp}$ then the maximum resolvable frequency is the $Nyquist$ $frequency$: $f_n= f_{samp}/2$ (Ideally, select the sampling rate to be at least the Nyquist rate required to resolve the maximum frequency component of a signal.).
In practice a signal may not be band-limited. If the signal includes frequency $f$ and the sampling rate is $f_{samp}$ then the samples of signals at frequencies $f ± nf_{samp}$ are indistinguishable from $f_{sig}$  – they are ‘aliases’. Fourier analysis will put all the aliased signals at $f_{sig}$.

I first started generating Synthetic timeseries data that contains a single harmonic component of period of $10 years$ sampled each month, than I deepen my analysis using real data; using long series of Chambon-la-Forêt $(CLF)$ observatory data which are monthly means, and discussing the observed Secular Variation evolutions over time. 

## Section 2: Data Visualisation
## [2-EMF-Observatory-Data-Visualisation.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/2-EMF-Observatory-Data-Visualisation.ipynb)

The aim of this notebook is to fetch & load Geomagnetic data at ground observatories; download the data for a given observatory for a given year, and load them as a Pandas Dataframe.

[INTERMAGNET](https://intermagnet.github.io/) is the International Real-time Magnetic Observatory Network, is the global network of observatories, monitoring the Earth's magnetic field. The [INTERMAGNET](https://intermagnet.github.io/) programme establishes a global network of cooperating geomagnetic observatories. It helps adopting modern standard specifications for measuring and recording equipment in order to facilitate data exchanges and the production of geomagnetic data in close to real time. In this notebooK we demonstrate geomagnetic ground observatory data access through [VirES](https://vires.services/) to access some ground observatory data.

[VirES](https://vires.services/) (Virtual environments for Earth Scientists) is a platform for data & model access, analysis, and visualisation for ESA’s magnetic mission, Swarm. 

### VirES Configuration: 
viresclient is the Python interface to VirES.  In order to authenticate access to the VirES server, viresclient requires an access token - this ties communications between the server and the client to your account. 
If you are running viresclient on a different machine, you will need to follow these instructions:
- Create a user account at https://vires.services if you haven’t already done so
- Install viresclient in your Python environment - see https://viresclient.readthedocs.io/en/latest/installation.html
- Create a new code cell here and execute the following:
         >>    from viresclient import set_token
         >>    set_token("https://vires.services/ows", set_default=True)
- You will now be directed to the VirES token management page, and prompted to generate a new token and enter it here.

Your access token should now have been saved to your environment and you won’t need to provide it again. The token and its associated access URL are stored in a file: ~/.viresclient.ini (this file can also be edited directly). You may generate and set a new token, or revoke old tokens, at any point. These are similar to passwords, so should be kept secret - if you accidentally leak a token, you can revoke it at the token management page and generate a new one.

### Fetching some data:

Data are available as three collections: 1 second and 1 minute cadences (INTERMAGNET definitive & quasi-definitive data), as well as specially derived hourly means over the past century (WDC).

![Data_Load.png](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/image/Data_Load.png)

Please note the data are under different usage terms than the Swarm data:
- If you use the 1-second or 1-minute data, please refer to the INTERMAGNET data conditionsI
- f you use the 1-hour data, please also refer to the WDC usage rules and cite the article about the preparation of these data:
    Macmillan, S., Olsen, N. Observatory data and the Swarm mission. Earth Planet Sp 65, 15 (2013). https://doi.org/10.5047/eps.2013.07.011

The magnetic vector components have been rotated into the geocentric NEC (North: X, East: Y, Centre: Z) frame rather than the geodetic frame, so that they are consistent with the Swarm data. This is in contrast with the data provided directly from observatories.

![CLF_Data_XYZ.png](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/image/CLF_Data_XYZ.png)

The signals that you can see in this data are: 
- Daily oscillation: due to the rotation of the Earth driving ionospheric change through the day/night - this is the Sq variation ("solar quiet-day" variation)
- Shift in baseline over the year: due to the change in the main magnetic field from the core - this is the secular variation (SV)
- More random variations due to geomagnetic activity

Then, I fetched the hourly dataset - these data are specially processed to improve data quality, over the straightforward hourly means calculated above from the minute data. For more information, see the article of [Macmillan, S., Olsen, N. (2013)](https://doi.org/10.5047/eps.2013.07.011)

I evaluated the declination angle (D), the horizontal deviation of the field from geographic North.
Next we summarise the data further by aggregating measurements over each month, evaluating the mean values over hourly intervals. For example, the mean declination at 10am across all days in January, the mean at 11am, and so on, repeated for each time of day and for each month. We then evaluate the offset of these declinations from the mean over the whole of each month - this is stored in D_variation in the resulting dataframe.

![Declination_1936_2020.png](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/image/Declination_1936_2020.png) ![Declination_1986_2003.png](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/image/Declination_1986_2003.png) ![Declination_2000_2020.png](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/image/Declination_2000_2020.png)

In the following section, the hourly mean values for 2003 at CLF Observatory are plotted ordered by Bartels rotation number. (Solar rotations are numbered by the Bartels solar rotation number, with Day 1 of rotation 1 chosen as 8th February 1832).

![CLF_Bartels_rotation_number.png](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/image/CLF_Bartels_rotation_number.png)

The plot shows a number of the features of geomagnetic field behaviour:
- The annual mean is plotted as a horizontal line in each row dividing the plots into sections ‘above’ and ‘below’ the mean. The proportions of the plots above and below changes as the year progresses because of the slow core field changes with time the secular variation.
- The daily variation in each element is clear. Note the differences between winter and summer, which we also saw in the 3D contour plot above.
- Although substantially attenuated by taking hourly means, times of magnetic disturbances are obvious.
- The rows are plotted 27 days long because the equatorial rotation period, as seen from Earth, is approximately 27 days. As a result, if a region on the Sun responsible for a disturbance on one day survives a full rotation, it may cause a further disturbance 27 days later and this will line up vertically in the plots. 

#### Virtual Observatories:





## Section 3: Modelling the Geomagnetic Field
## [3-Spherical-Harmonic-Models.ipynb](https://github.com/thiziriamezza/Earth-Magnetic-Field/blob/main/3-Spherical-Harmonic-Models%20.ipynb)

In this section, I build a model capable of representing my data

### The International Geomagnetic Reference Field (IGRF):
IGRF is An IAGA ‘flagship product’
- First produced 1965
- The International Geomagnetic Reference Field (IGRF) is a series of mathematical models describing the large-scale internal part of the Earth’s magnetic field between epochs 1900 A.D. and the present.
- The IGRF is used by scientists in studies of dynamics of the core field, space weather, local crustal magnetic field. It is also used by commercial organizations as a source of orientation information.
- The latest version is IGRF-13

### IGRF – a collaborative effort:

[IGRF-13](https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html) is a Main Field Models every 5 years from 1900 with Nmax = 10 to 1995 and Nmax = 13 for 2000 to 2020. D(efinitive)GRF up to 2015

$V(r,\theta,\phi,t)$ = $a$ $\sum_{n=1}{^{N_{max}}}$ $(\frac{a}{r})^{n+1}$ $\sum_{m=0}{^n}$ $( g^m_n (t) cos(m\phi) + h^m_n (t) sin(m\phi) )$ $P^m_n (cos\theta)$

(Nmax = 13 is chosen to avoid contamination by crustal fields)

A linear predictive secular variation model for 5 years from 2015 with Nmax = 8 (Secular variation is taken as a linear interpolation between main field models at earlier epochs)

IGRF-13:
- 11 candidate MF models for 2015 (DGRF).
- 12 candidate MF models for 2020 (IGRF).
- 14 candidate SV models for 2020-2025.
A scientific disadvantage is that it’s difficult to include uncertainty estimates for the Gauss coefficients.



# References:
- S. R Malin,  & D. Barraclough,. (1981). An algorithm for synthesizing the geomagnetic field, Computers & Geosciences. Pergamon, 7(4), pp. 401–405. doi: 10.1016/0098-3004(81)90082-0.
- V. Lesur, N. Gillet, M. D. Hammer & M. Mandea,. (2022). Rapid Variations of Earth’s Core Magnetic Field, Surveys in Geophysics volume 43, pages41–69. doi: 10.1007/s10712-021-09662-4.
- S. Macmillan, & N. Olsen,. (2013). Observatory data and the Swarm mission,  Earth, Planets and Space volume 65, 1355–1362, doi:10.5047/eps.2013.07.011
