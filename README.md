# Telco Classification Project

## Project Description
- I will be running the Telco data through the data science pipeline, implementing both statistical modeling, and machine learning models to help indicate drivers of churn and build a model to beat baseline accuracy.

## Project Goals
- Break down and analyze the telco dataset, giving documentation and explination through that process.
- Construct a model to predict customer churn using classification techniques.
- Deliver a 5 minute presentation that is a deep dive walkthrough of the final jupyter notebook, and my documentation thoughout.

## Buisness Goals
- Deliver a model that can accuratly find our target (Churn) of customers.
- Highlight the main drivers of churn.

## Audience
- Codeup Data Science team.

## Project Deliverables
- Deliver a jupyter notebook containing my process through the datascience pipeline from planning to delivery.
- Use 2 statistical models on the data to correctly identify a driver of churn.
- Create 3 machine learning models, that are trained, validated, and tested. Returning the best models predictions to a csv file
- Make individual .py files that will hold functions to acquire, and prepare the telco data.

## Project Context
- Im using the Telco churn dataset from the Codeup SQL database.
- This dataset originally contained 27 columns and 7043 rows after all tables were joined together.
- An example of the Telco churn dataset can be found [here](https://www.kaggle.com/blastchar/telco-customer-churn).

## Data Dictionary
### Joining Columns:
- payment_type_id - used to join payment type information
- internet_service_type_id - used to join internet service type information
- contract_type_id - used to join contract type information
### Custom Columns
- addons - a column I created that will take the total of each of the columns below for every individual in the telco dataset. This column ranges from 0-6 adding one for each service.
  - I added this column (addons) because these are all additional services, and are opt in this could potentially be a positive or negative driver of churn.
- auto_pay - a column I created using the payment_type column that will split the four different payment types into two groups. auto_pay represented by "1" containing (Credit card, Bank Transfer), and non auto payment types represented by "0" containing (Electronic check, Mailed check)
### Additional Services
- online_security - column indicating yes, no, or no internet service depending on the customers situation of having online security.
- online_backup - column indicating yes, no, or no internet service depending on the customers situation of having online backup.
- device_protection - column indicating yes, no, or no internet service depending on the customers situation of having device protection.
- tech_support - column indicating yes, no, or no internet service depending on the customers situation of having tech support.
- streaming_tv - column indicating yes, no, or no internet service depending on the customers situation of having tv streaming.
- streaming_movies -column indicating yes, no, or no internet service depending on the customers situation of having movie streaming.
### Customer Information
- customer_id - A unique id given to each customer
- gender - Catagorizing each customer as male or female.
- senior_citizen - Catagorizing each customer depending on if they are a senior citizen.
- partner - Yes, or no indicating weather the customer has a partner.
- dependents - Yes, or no indicating weather the customer has dependents.
- tenure - Gives a whole number of how many months a customer has recieved a telco service.
### Account Information
- phone_service - 
- multiple_lines -
- paperless_billing -
- monthly_charges -
- total_charges -
- contract_type -
- payment_type -
- internet_service_type -
### Target
- churn - Indicates weather a customer has opted out of the telco services.
## Cleaned Data Dictionary
|Target|Datatype|Definition|
|:-------|:--------|:----------|
|churn|dtype('O')|Yes or no, if the customer churned|

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
|customer_id| dtype('O')|Identification number for customer|
|gender| dtype('O')|Customer gender, male or female|
|senior_citizen| dtype('int64')|Yes or no, is the customer a senior citizen|
|partner| dtype('O')|Yes or no, does the customer customer has a parter|
|dependents| dtype('O')|Number of dependents a customer has|
|tenure| dtype('int64')|Number of months a customer has been with the company|
|phone_service| dtype('O')|Type of phone service plan a customer has|
|multiple_lines| dtype('O')|Yes or no, does the customer have multiple lines|
|internet_service_type_id| dtype('int64')|1 for DSL, 2 for Fiber Optic, 3 for None|
|online_security| dtype('O')|Yes, no, or no internet service|
|online_backup | dtype('O')|Yes, no, or no internet service|
|device_protection| dtype('O')|Yes, no, or no internet service|
|tech_support| dtype('O')|Yes, no, or no internet service|
|streaming_tv| dtype('O')|Yes, no, or no internet service|
|streaming_movies| dtype('O')|Yes, no, or no internet service|
|contract_type_id| dtype('int64')|1 for month-to-month, 2 for year, and 3 for two-year contract|
|paperless_billing| dtype('O')| Yes or no, whether or not the customer uses paperless billing|
|payment_type_id | dtype('int64')|1 for electronic check, 2 for mailed check, 3 for automatic bank transfer, 4 for automatic credit card payment|
|monthly_charges| dtype('float64')|Monthly charges the customer pays|
|total_charges| dtype('O')|Total charges the customer has paid|
|contract_type| dtype('O')|Month-to-month, year, or two-year contract|
|internet_service_type| dtype('O')|DSL, Fiber Optic, or None|
|payment_type| dtype('O')|Electronic check, mailed check, automatic bank transfer, or automatic credit card payment|
- α = .05
### Initial hypothesis 1
#### Null Hypothises
-
#### Alternative Hypothisis
- 
### Initial hypothesis 2
#### Null Hypothises
-
#### Alternative Hypothisis
- 
### Initial hypothesis 3
#### Null Hypothises
-
#### Alternative Hypothisis
- 
## Executive Summary