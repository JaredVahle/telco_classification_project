
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
- Codeup Data Science students, and staff.

## Project Deliverables
- Deliver a jupyter notebook containing my process through the datascience pipeline from planning to delivery.
- Use 2 statistical models on the data to correctly identify a driver of churn.
- Create 3 machine learning models, that are trained, validated, and tested. Returning the best models predictions to a csv file
- Make individual .py files that will hold functions to acquire, and prepare the telco data.

## Project Context
- Im using the Telco churn dataset from the Codeup SQL database.
- This dataset originally contained 27 columns and 7043 rows after all tables were joined together.

## Data Dictionary
### Joining columns:
- payment_type_id - used to join payment type information
- internet_service_type_id - used to join internet service type information
- contract_type_id - used to join contract type information
### addons
- addons - a column I created that will take the total of each of the columns below for every individual in the telco dataset. This column ranges from 0-6 adding one for each service.
  - I added this column (addons) because these are all additional services, and are opt in this could potentially be a positive or negative driver of churn.
- online_security - column indicating yes, no, or no internet service depending on the customers situation of having online security.
- online_backup - column indicating yes, no, or no internet service depending on the customers situation of having online backup.
- device_protection - column indicating yes, no, or no internet service depending on the customers situation of having device protection.
- tech_support - column indicating yes, no, or no internet service depending on the customers situation of having tech support.
- streaming_tv - column indicating yes, no, or no internet service depending on the customers situation of having tv streaming.
- streaming_movies -column indicating yes, no, or no internet service depending on the customers situation of having movie streaming.
### Customer information
- customer_id - 
- gender -
- senior_citizen -
- partner -
- dependents -
- tenure -
### Account information
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
## Initial hypotheses
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

