import pandas as pd
import os
from acquire_telco import get_telco_data
from prepare_telco import final_report_clean, remove_unwanted_values, train_validate_test_split

def splitting_target_var(train,validate,test):
    X_train = train.drop(columns=['churn'])
    y_train = train.churn

    X_validate = validate.drop(columns=['churn'])
    y_validate = validate.churn

    X_test = test.drop(columns=['churn'])
    y_test = test.churn
    return (X_train,y_train,X_validate,y_validate,X_test,y_test)

def pred_proba(model,X):
    proba_df = pd.DataFrame(model.predict_proba(X), columns = ["retain","churn"])
    return proba_df.churn

def get_final_report(model,target,cache = False):
    # Makes my final report for the telco churn data containing customer_id,probability of churn,
    # and prediction of churn
    if cache == True or isfile("final_report.csv") == False:
        df = get_telco_data()
        df,customer_ids = final_report_clean(df)
        df["prob_of_churn"] = pd.DataFrame()
