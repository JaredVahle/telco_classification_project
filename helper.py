import pandas as pd
import os
from os.path import isfile
from acquire_telco import get_telco_data
from prepare_telco import final_report_clean, remove_unwanted_values, train_validate_test_split

def splitting_target_var(train,validate,test):
    '''
    This function takes in train, validate, and test and splits the values so that our target variable is
    stored to our y values, and the X values contain the rest of our dataframe.
    '''
    X_train = train.drop(columns=['churn'])
    y_train = train.churn

    X_validate = validate.drop(columns=['churn'])
    y_validate = validate.churn

    X_test = test.drop(columns=['churn'])
    y_test = test.churn
    return (X_train,y_train,X_validate,y_validate,X_test,y_test)

def pred_proba(model,X):
    # helper for my final report
    proba_df = pd.DataFrame(model.predict_proba(X), columns = ["retain","churn"])
    return proba_df.churn

def make_predictions(model,X):
    # helper for my final report
    predictions = model.predict(X)
    return predictions

def get_final_report(model, cashe = False):
    # checks if final_report is already a file
    if cashe == True or isfile("final_report.csv") == False:
        # gets a new dataframe so we can grab the customer id
        df = get_telco_data()
        # only difference from original clean is that we leave customer id
        final_report_clean(df)
        remove_unwanted_values(df)
        train,validate,test = train_validate_test_split(df,target = "churn",seed = 174)
        # make a final report dataframe that will contain customer id, prediction of churn, and our models prediction
        final_report_df = pd.DataFrame(test["customer_id"])
        final_report_df.reset_index(inplace = True)
        final_report_df.drop(columns = ["index"], inplace = True)
        X_train,y_train,X_validate,y_validate,X_test,y_test = splitting_target_var(train,validate,test)
        # drop customer id so that our model can preform the predictions
        X_test.drop(columns = ["customer_id"],inplace = True)
        final_report_df["prediction_proba"] = pred_proba(model,X_test)
        final_report_df["predictions"] = make_predictions(model,X_test)
        df = final_report_df
        # saves the final report to a csv
        df.to_csv("final_report.csv", index = False)
    else:
        # reads the csv if final report has already been saved
        df = pd.read_csv("final_report.csv")
    return df

cat_var = ["auto_pay","partner","add_ons","tech_support","online_security","senior_citizen"]