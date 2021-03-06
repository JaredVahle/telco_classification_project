# Telco Classification Project

## Executive Summary

##### We found the leading 5 drivers of churn:
- Month-to-month contract type
- Fiber optics internet service type
- Electronic check payment type
- Tenure
- Two year contract type

##### I investigated streaming services and additional services.
- Our streaming services had a higher rate of churn then our normal churn rate indicating some kind of customer dissatisfaction with the service.
- I also found that our churn rate for additional services had higher churn rates in those that had 1-2 additional services and much lower churn rates in customers with 4-6.
- This indicates we need further inspection into the 6 additional columns.

##### For our modeling we used a random forest model.
- I was able to get an accuracy of ~80.5%
- This model is more than 7 points higher than our baseline model and can be extreamly helpful in the future.

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

### Custom Columns
- add_ons - a column I created that will take the total of each of the columns below for every individual in the telco dataset. This column ranges from 0-6 adding one for each service.
  - I added this column (addons) because these are all additional services, and are opt in this could potentially be a positive or negative driver of churn.
- auto_pay - a column I created using the payment_type column that will split the four different payment types into two groups. auto_pay represented by "1" containing (Credit card, Bank Transfer), and non auto payment types represented by "0" containing (Electronic check, Mailed check).
  - I added this column (auto_pay) because in my previous project I had found that weather or not a customer had autopay was a large driver of churn.
- streaming_movies_and_tv - a column I created using the streaming_movies, streaming_tv columns
  - I combined these two columns so that the numbers range from 0-2, 0 being no streaming service, 1 being only one service, and 2 meaning that the customer had both streaming services.

## Hypotheses
### Alpha
- ?? = .05

### Hypothesis 1
Null hypothesis - The number of additional services and the likelyhood of churn are independent of eachother.

Alternative hypothesis - The number of additional services and the likelyhood of churn are not independent of eachother.

### Hypothesis 2
Null hypothesis - Streaming television and churn are independent of eachother.

Alternative hypothesis - Streaming television and churn are not independent of eachother.

### Hypothesis 3
Null hypothesis - Streaming movies and churn are independent of eachother.

Alternative hypothesis - Streaming movies and churn are not independent of eachother.

### Hypothesis 4
Null hypothesis - Streaming movies and tv are independent on churn.

Alternative hypothesis - Streaming movies and tv are not independent of churn.

## Data Science Pipeline
#### Planning
- Make a README.md that will hold all of the project details including a data dictionary, key finding, initial hypotheses, and explain how my process can be replicated
- Create a MVP, originally and work through the iterative process of making improvements to that MVP.
- Define atleast 2 clear sets of null and alternative hypotheses set an alpha value.
- Create two .py scripts for both acquire and prepare, in order to automate the collection and cleaning of the data.
- Create a helper.py for any other functions I need implamented thoughout the pipeline.
- Properly anotate my code as I run though the process, in order for the code to be easily understood, and document any decisions that were made when cleaning, creating new columns, or removing rows of data.
#### Acquire
- Create an acquire.py (acquire_telco.py) was the name of my py file.
- Use that acquire_telco.py file to grab the data from the CodeUp SQL database and cache that file to a csv for ease of accessability.
- Render the csv into a pandas dataframe on python.
- Summarize the initial data and plot the distributions of individual variables.
#### Prepare
- Create a prepare.py (prepare_telco.py) was the name of my py file.
- Clean the data as I see fit, handling the missing values and encoding values as necessary in order to give numeric values that will work with the models
- There were 11 values with no current tenure, and I made the decision to remove those values. These customers have not payed their first bill, so there is no data on weather they are satisfied with the product.
- Add new columns that might be useful in modeling, might need more information from the explore for incite into columns that once combined will drive churn.
- I added two new columns (auto_pay - if payment type was automatic.),and (add_ons - A column that sums the six aditional services.)
#### Explore
- Awnser my initial hypotheses that was asked in my planning phase, and test those hypotheses using statistical tests, either accepting or rejecting the null hypothesis.
- Continue using statistical testing and visualizations to discover variable relationships in the data, and attempt to understand "how the data works".
- Summarize my conclusions giving clear awnsers to the questions I posed in the planning stage and summarize any takeaways that might be useful.
#### Modeling and Evaluation
- Train and evaluate multiple models comparing those models on different evaluation metrics.
- Validate the models and choose the best model that was found in the validation phase.
- Test the best model found and summarize the performance and document the results using a confusion matrix, predict methods, and classification reports.
- Save the test predictions to a .csv file.
#### Delivery
- Deliver my refined jupyter notebook to the CodeUp data science team.
- Summarize my findings, and build a narrative around the data, pulling from my knowledge on story telling.
- Walk though the notebook explaining finding, documentation, and decisions that were made.
- End with key takeaways and reccomendations.

## Modules

#### acquire_telco.py
- Acquires the data from the CodeUp SQL database and puts the table into a pandas dataframe
#### prepare_telco.py
- Cleans my data and gets it ready for use in modeling and explore.
#### helper.py
- Contains any function that would help me thoughout the process.
#### explore.py
- Contains functions that I used to help visualize the data.
#### telco_model.py
- Contains all of the models I will use for my final project.
- I used specifications on the function that I found had high accuracy scores on my validation data.

## Project Reproduction
- Random state or seed = **174**, and is used in my models and my split functions.
- In replication making use of the user defined function, in cunjunction with  my documented process should give a good guide and presaved models, and helpful functions that will make the process faster.
- Create and use your own env file that connects you to the sql database.
- Run the telco_classification_project_final

## Summary

### Key takeaways
top 5 churn predictors
- Month-to-month contract type
- Fiber optics internet service type
- Electronic check payment type
- Tenure
- Two year contract type

### Model takeaways
- The best model for accuracy was my decision tree model with an accuracy score of 80.67% on our test data.
- These are the model criteria that I used (n_estimators = 30, criterion = "gini",max_depth = 9, random_state = 174, min_samples_leaf = 3)

### Recommendations
- Although streaming was not the greatest indicator of churn I would still recommend further evaluation, and survaying of customers that had streaming services to gather their responses on why they churned.
- Offering some kind of incentive to bundle the streaming services at a small discount or improving on those services might lower churn.
- Investigate why customers are churning that have the fiber optics plan, is the price to high or is there some other factor causing it.
- Incentivise payment types other then electronic checks, in order to increase customer retention.

### Moving forward
If given more time
- I would adjust hyperperamaters and look for more features in the data, trying to find links between churn and multiple columns.
- I would also have a team focus on survaying customer complaints to find cheap fixes for any reoccuring drivers of churn.
- Additional effort in discovering the reason for the variations in churn for our add_ons column and discovering reasons for this data could give us actions we could use moving forward.