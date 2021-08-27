def splitting_target_var(train,validate,test):
    X_train = train.drop(columns=['churn'])
    y_train = train.churn

    X_validate = validate.drop(columns=['churn'])
    y_validate = validate.churn

    X_test = test.drop(columns=['churn'])
    y_test = test.churn
    return (X_train,y_train,X_validate,y_validate,X_test,y_test)