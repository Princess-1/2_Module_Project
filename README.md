# Module_2_Project

## The Project
We have been approached by a Real Estate company in _King-County, Settle WA_ who is looking to increase their profits and help their customers maximize the value of their homes by getting a better understanding of how different factors affect the price of a house. Our job is to analyze the data and create a presentation that explores the different types of features and how they affect house prices. We must then translate the findings into _Recommendations_ and _Actionable Insights_ that the company can use to decide which factors should be used to help maximize the profit and value of houses.

## The Dataset
For this project I was provided with a _Flatiron School_ variation of the _'kc_house_data'_, this dataset can also be found on _Kaggle_. In this repo you will also find copies of this data set at different stages of analysis:
* [**kc_house_data.csv**](/kc_house_data.csv): This is the original dataset provided.
* [**kc_cleaned**](/kc_cleaned.csv): This is a copy of the dataset after the data cleaning stage of the analysis.
* [**kc_reg.csv**](/kc_reg.csv): This is the final form of our data after cleaning and EDA. This is the dataset used to build _Regression Models_ and draw final conclusions on my findings.

## Working Files
Like the datasets, there are 3 different notebooks containing my data analysis stages from data cleaning down to my conclusion:
* [**Data_Cleaning.ipynb**](/Data_Cleaning.ipynb): Like the file name this notebook contains all my data cleaning process, including, but not limited to, importing data, dealing with missing values, checking for duplicates, etc. 
* [**EDA.ipynb**](/EDA.ipynb): In this notebook I got the explore and understand the data better by, taking care _Outliers_, _Feature Engineered_ new columns, dealing with _Categorical_ columns, and answering questions to get more insight into the data.
* [**Regression_Notebook.ipynb**](/Regression_Notebook.ipynb): This final notebook cotains all my _Regression Models_ and my final conclusions on the project.

## Insights
An important aspect of data analysis is knowing how to ask the right questions to better understand the data. The following questions are designed to do that:
* Q1: Which _Feature_ has the biggest impact on house prices?
* Q2: What effect does _Location_ have on house prices?
* Q3: Do _renovated_ houses cost more?
* Q4: What is the impact of _renovations_ on house _grades_ and how do they both affect house prices?

## Order of Operation
### Data Importing and Cleaning
As mentioned earlier the data cleaning process can be found in the [**Data_Cleaning.ipynb**](/Data_Cleaning.ipynb) notebook. I started by importing the data with the use of **_Pandas_** and taking a look at columns and some of the rows the data entails. Along with this repo is a file that explains what the values in each [**_Column_**](/column_names.md) represents. This is the list of what each _Column_ represents:
* **id** - unique identified for a house
* **dateDate** - house was sold
* **pricePrice** -  is prediction target
* **bedroomsNumber** -  of Bedrooms/House
* **bathroomsNumber** -  of bathrooms/bedrooms
* **sqft_livingsquare** -  footage of the home
* **sqft_lotsquare** -  footage of the lot
* **floorsTotal** -  floors (levels) in house
* **waterfront** - House which has a view to a waterfront
* **view** - Has been viewed
* **condition** - How good the condition is ( Overall )
* **grade** - overall grade given to the housing unit, based on King County grading system
* **sqft_above** - square footage of house apart from basement
* **sqft_basement** - square footage of the basement
* **yr_built** - Built Year
* **yr_renovated** - Year when house was renovated
* **zipcode** - zip
* **lat** - Latitude coordinate
* **long** - Longitude coordinate
* **sqft_living15** - The square footage of interior housing living space for the nearest 15 neighbors
* **sqft_lot15** - The square footage of the land lots of the nearest 15 neighbors

With the use of one of _Pandas_ many functions namely **.shape** I know that I am working with a dataset that contains **21597 Rows** and **21 Columns**. Once I got more acquainted to the dataset I moved on with the data cleaning process. which includes:
* Checking for _duplicates_ in dataset.
* Checking for and replacing _NULL Values_.
* Transform _Datatypes_ when necessary.

### EDA 
The next step in getting the data prepared for _Modeling_ is to perform some **_Exploratory Data Analysis_**. This process consists of:
* Identifying **Outliers** in the dataset and dealing with them appropriately.
* **Feature Engineering** new columns when necessary.
* Checking if data is **Normally Distributed**
* Checking for **Multicollinearity** among predictors.
* Dealing with **Categorical** variables, and creating dummy variables when needed.
* Formulating questions to get **Insights** on the data.
