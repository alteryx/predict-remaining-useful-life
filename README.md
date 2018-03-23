# Predicting Remaining Useful Life
<a style="margin:30px" href="https://www.featuretools.com">
    <img width=50% src="https://www.featuretools.com/wp-content/uploads/2017/12/FeatureLabs-Logo-Tangerine-800.png" alt="Featuretools" />
</a>

We show how to use Featuretools on the [phm08 challenge dataset](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/) from NASA as provided by MIT Lincoln Labs. This notebook demonstrates a rapid way to create a model which predicts the Remaining Useful Life (RUL) of an engine using an initial dataframe of time-series data. 


## Highlights
* Quickly make an end-to-end workflow using time-series data
* Find interesting automatically generated features

## Demonstration
The main notebook can be found [here](Simple%20Featuretools%20RUL%20Demo.ipynb). To run the notebook, you will need to download Featuretools with
```
pip install featuretools
```
and the [data](https://ti.arc.nasa.gov/c/13/) from NASA. The function `load_data` in [utils.py](utils.py) takes the path to the text file and returns a pandas dataframe. With the notebook as written, we expect the path to the `train` data first.

## Feature Labs
<a href="https://www.featurelabs.com/">
    <img src="http://www.featurelabs.com/wp-content/uploads/2017/12/logo.png" alt="Featuretools" />
</a>

Featuretools was created by the developers at [Feature Labs](https://www.featurelabs.com/). If building impactful data science pipelines is important to you or your business, please [get in touch](https://www.featurelabs.com/contact.html).
