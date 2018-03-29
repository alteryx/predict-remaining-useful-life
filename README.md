# Predicting Remaining Useful Life
<p style="margin:30px">
    <img style="display:inline; margin-right:50px" width=50% src="https://www.featuretools.com/wp-content/uploads/2017/12/FeatureLabs-Logo-Tangerine-800.png" alt="Featuretools" />
    <img style="display:inline" width=15% src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" alt="NASA" />
</p>

The general setup for the problem is a common one: we have a single table of sensor observations over time. Now that collecting information is easier than ever, most industries have already generated *time-series* type problems by the way that they store data. As such, it is crucial to be able to handle data in this form. Thankfully, built-in functionality from [Featuretools](https://www.featuretools.com) handles time varying data well. 

We'll demonstrate an end-to-end workflow using a [Challenge Dataset](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#phm08_challenge) from NASA (PHM 08 as provided by LL). This notebook demonstrates a rapid way to predicts the Remaining Useful Life (RUL) of an engine using an initial dataframe of time-series data. There are three sections of the notebook:
1. [Understand the Data](Simple%20Featuretools%20RUL%20Demo.ipynb#Step-1:-Understanding-the-Data)
2. [Generate features](Simple%20Featuretools%20RUL%20Demo.ipynb#Step-2:-DFS-and-Creating-a-Model)
3. [Make predictions with Machine Learning](Simple%20Featuretools%20RUL%20Demo.ipynb#Step-3:-Using-the-Model)

*If you're running this notebook yourself, note that the Challenge Dataset will be downloaded into the data folder in this repository. If you'd prefer to download the data yourself, download and unzip the file from [https://ti.arc.nasa.gov/c/13/](https://ti.arc.nasa.gov/c/13/)*.

## Highlights
* Quickly make end-to-end workflow using time-series data
* Find interesting automatically generated features
* An advanced notebook using custom primitives and hyperparameter tuning

## Demonstration
The main notebook can be found [here](Simple%20Featuretools%20RUL%20Demo.ipynb). To run that notebook, you will need to download Featuretools with
```
pip install featuretools
```
and the [data](https://ti.arc.nasa.gov/c/13/) from NASA. The function `load_data` in [utils.py](utils.py) takes the path to the text file and returns a pandas dataframe. With the notebook as written, we expect the path to the `train` data first.

## Feature Labs
<a href="https://www.featurelabs.com/">
    <img src="http://www.featurelabs.com/wp-content/uploads/2017/12/logo.png" alt="Featuretools" />
</a>

Featuretools was created by the developers at [Feature Labs](https://www.featurelabs.com/). If building impactful data science pipelines is important to you or your business, please [get in touch](https://www.featurelabs.com/contact.html).
