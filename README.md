# Predicting Remaining Useful Life
<p style="margin:30px">
    <img style="display:inline; margin-right:50px" width=50% src="https://www.featuretools.com/wp-content/uploads/2017/12/FeatureLabs-Logo-Tangerine-800.png" alt="Featuretools" />
    <img style="display:inline" width=15% src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" alt="NASA" />
</p>

The general setup for the problem is a common one: we have a single table of sensor observations over time. Now that collecting information is easier than ever, most industries have already generated *time-series* type problems by the way that they store data. As such, it is crucial to be able to handle data in this form. Thankfully, built-in functionality from [Featuretools](https://www.featuretools.com) handles time varying data well.

We'll demonstrate an end-to-end workflow using a [Turbofan Engine Degradation Simulation Data Set](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#turbofan) from NASA. This notebook demonstrates a rapid way to predict the Remaining Useful Life (RUL) of an engine using an initial dataframe of time-series data. There are three sections of the notebook:
1. [Understand the Data](#Step-1:-Understanding-the-Data)
2. [Generate features](#Step-2:-DFS-and-Creating-a-Model)
3. [Make predictions with Machine Learning](#Step-3:-Using-the-Model)

*If you're running this notebook yourself, note that the Challenge Dataset will be downloaded into the data folder in this repository. If you'd prefer to download the data yourself, download and unzip the file from [https://ti.arc.nasa.gov/c/13/](https://ti.arc.nasa.gov/c/6/)*.

## Highlights
* Quickly make end-to-end workflow using time-series data
* Find interesting automatically generated features
* An advanced notebook using custom primitives and hyper-parameter tuning

## Running the tutorial
1. Clone the repo

    ```
    git clone https://github.com/Featuretools/predict-remaining-useful-life.git
    ```

2. Install the requirements

    ```
    pip install -r requirements.txt
    ```

3. Run the Tutorial notebooks:<br>
   *Note: The Challenge Dataset will be downloaded into the data folder in this repository, if not already downloaded.*
    - [Simple Featuretools RUL Demo](Simple%20Featuretools%20RUL%20Demo.ipynb)<br/>
    - [Advanced Featuretools RUL](Advanced%20Featuretools%20RUL.ipynb)<br/>

## Feature Labs
<a href="https://www.featurelabs.com/">
    <img src="http://www.featurelabs.com/wp-content/uploads/2017/12/logo.png" alt="Featuretools" />
</a>

Featuretools is an open source project created by [Feature Labs](https://www.featurelabs.com/). To see the other open source projects we're working on visit Feature Labs [Open Source](https://www.featurelabs.com/open). If building impactful data science pipelines is important to you or your business, please [get in touch](https://www.featurelabs.com/contact.html).

### Contact

Any questions can be directed to help@featurelabs.com
