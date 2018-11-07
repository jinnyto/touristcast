# Touristcast

**Objective**: To predict monthly hotel stays from 2018-2019 for each of the 13 regions in France

3 time series forecasting methods were implemented and compared:

- Facebook Prophet
- Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors (SARIMAX)
- Vector Autoregressions (VAR)

This repository contains Jupyter Notebooks and other source files.

This was a group project completed as part of the [Datascientest.com](https://datascientest.com) Data Science Bootcamp from June to September 2018. See the Contributors section below for the list of group members and contributions.

## Results
1. **In repository**
- [Comparing models (SARIMAX, Prophet, VAR).ipynb](https://github.com/jinnyto/touristcast/blob/master/Comparing%20models%20(SARIMAX%2C%20Prophet%2C%20VAR).ipynb): Comparison of final results between all methods tested (SARIMAX, VAR, Prophet)
- [Hotel_stays_forecast_2018-2019.csv](https://github.com/jinnyto/touristcast/blob/master/Hotel_stays_forecast_2018-2019.csv): Generated CSV results using the best models for each region

2. **Interactive Heatmap by Aysun Akarsu**

    A heatmap showing magnitude of hotel stays from Jan 2013 to Jan 2019, created and hosted by [Aysun Akarsu](https://github.com/aysunakarsu)
    
    (2018 and 2019 are predicted values)
    
    http://touristcast.appspot.com/2015_2019_heatmapwithtime.html

3. **Presentation Slides**

    Check out the slides at [SpeakerDeck](https://speakerdeck.com/jinnyto/touristcast)

## Dependencies

- All code is written in Python 3
- See requirements.txt file

### Libraries used

**Library** | **Usage**
--- | ---
fbprophet | Modeling with Prophet
holidays | Generating dataset with number of days off 
jupyter | Writing code and previewing results
matplotlib | Visualizing results
numpy | Managing arrays and calculating error measures
pandas | Managing data and indices
pyramid-arima | Modeling with Auto ARIMA for SARIMAX
pytemperature | Convert temperatures to positive values
scikit-learn | Calculating error measures
seaborn | Visualizing results
statsmodels | Seasonal decomposition and modeling with VAR

## Description of files

**Folder** | **Description**
--- | ---
crossvalidation | Scripts that perform cross validation and resulting outputs for each model (SARIMAX, VAR, Prophet). Includes a demonstration of benchmark metric MASE.
datasets | Clean CSVs with input data
dataviz | Heatmap source files and graphs showing past data
tests | Intermediary files used for practice and adjustments before final implementation

## Contributors

[_Aysun Akarsu_](https://github.com/aysunakarsu)

- Collection and extraction of weather dataset 
- SARIMAX analysis, implementation, and cross validation
- Facebook Prophet analysis, implementation, and cross validation
- Interactive heatmap testing, drafting, and final implementation

[_Sekou Camara_](https://github.com/sekouu)

- Research and analysis of potential datasets
- Research and analysis of state of art forecasting methods
- VAR tests and cross validation testing and implementation 

[_Jinny To_](https://github.com/jinnyto)

- Generation of GDP and daysoff dataset and uniformization of datasets
- VAR tests, analysis, cross-validation testing and implementation
- Analysis of final models from cross-validation results
- Visualization of error measures from model comparison

[_Franck Tramond_](https://github.com/ftramond)

- Correlation analysis
- Generation of hotel nights datasets
- VAR test and cross validation implementation

## Dataset region naming

Code | Name
--- | ---
ARA | Auvergne-Rhône-Alpes
BFC | Bourgogne-Franche-Comté
BRE | Bretagne
CVL | Centre-Val de Loire
COR | Corse
GES | Grand Est
HDF | Hauts-de-France
IDF | Île-de-France
NOR | Normandie
NAQ | Nouvelle-Aquitaine
OCC | Occitanie
PDL | Pays de la Loire
PAC | Provence-Alpes-Côte d'Azur

## Data sources
- Regional GDP: [INSEE](https://www.insee.fr/fr/statistiques/1893220)
- Hotel stays: [INSEE](https://www.insee.fr/fr/statistiques/series/102414599)
- Number of days off per month: [holidays library](https://pypi.org/project/holidays/)
- Regional average temperatures: [Historique Météo](https://www.historique-meteo.net/france/)

## References
- [Forecasting: Principles and Practice textbook by Rob J. Hyndman](https://otexts.org/fpp2)
- [Statsmodels documentation on VAR](https://www.statsmodels.org/devel/vector_ar.html)
- Athanasopoulos, G., Hyndman, R. J., Song, H., & Wu, D. C. (2011). The tourism forecasting competition. International Journal of Forecasting, 27(3), 822-844.
[Blog post by Rob J Hyndman](https://robjhyndman.com/publications/the-tourism-forecasting-competition/)
- Song, H., & Li, G. (2008). Tourism demand modelling and forecasting—A review of recent research. Tourism management, 29(2), 203-220.
[Article on Science Direct](https://www.sciencedirect.com/science/article/pii/S0261517707001707)