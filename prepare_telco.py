import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
def clean_telco(df):
    
    # replaces all the missing values with 0 and since all values are numeric, we change the total charges type to float
    df.total_charges.replace(to_replace = {" ":"0"}, inplace = True)
    df.total_charges = df.total_charges.astype("float")
    # takes the payment type and checks for the word auto and creates a new column that represents a 1 or 0, 1 for if they have auto pay 0 for if they do not.
    df["auto_pay"] = df.payment_type.str.contains("auto")
    df["auto_pay"] = df.auto_pay.replace(to_replace = [True,False],value = [1,0])
    # creating dummy variables for the catigorical values i can not easily change in pandas
    dummy_df = pd.get_dummies(df[['gender', 'payment_type',"internet_service_type","contract_type"]])
    dummy_df.columns = [col.lower().replace(" ","_") for col in dummy_df]
    # replacing the yes, no, and no service type to numeric values, (1 for yes) (0 for no, and 0 for no phone or internet service)
    df["partner"] = df.partner.replace(to_replace = ["Yes","No"],value = [1,0])
    df["dependents"] = df.dependents.replace(to_replace = ["Yes","No"],value = [1,0])
    df["churn"] = df.churn.replace(to_replace = ["Yes","No"],value = [1,0])
    df["multiple_lines"] = df.paperless_billing.replace(to_replace = ["Yes","No","No phone service"],value = [1,0,0])
    df["paperless_billing"] = df.paperless_billing.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["tech_support"] = df.tech_support.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["device_protection"] = df.device_protection.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["online_backup"] = df.online_backup.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["online_security"] = df.online_security.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["streaming_tv"] = df.streaming_tv.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["streaming_movies"] = df.streaming_movies.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["phone_service"] = df.phone_service.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["multiple_lines"] = df.multiple_lines.replace(to_replace = ["Yes","No","No phone service"],value = [1,0,0])
    # adding a column that sums the additional services and gives a total from (0-6)
    df["add_ons"] =  df.online_security + df.online_backup + df.device_protection + df.tech_support + df.streaming_tv + df.streaming_movies
    # dropping columns that are duplicated by the dummy variables, the customer id, and id's that connected the different tables from sql
    df.drop(columns = ["customer_id",
                       "gender",
                       "payment_type",
                       "internet_service_type",
                       "contract_type",
                   'internet_service_type_id',
                   "contract_type_id",
                   "payment_type_id",
                  "contract_type_id.1",
                   "internet_service_type_id.1",
                   "payment_type_id.1",
                   "Unnamed: 0"],inplace = True)
    return pd.concat([df, dummy_df], axis=1)

def remove_unwanted_values(df):
    # takes all the indexes where tenure is equal to 0
    no_tenure = df[df.tenure == 0].index.to_list()
    # drops all columns of the indexes given above
    df.drop(index = no_tenure, inplace = True)

def train_validate_test_split(df, target, seed=174):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test 

def num_distributions(df):
    '''
    property of Faith Kane
    This functions takes in a dataframe and displays
    the distribution of each numeric column.
    '''
    for col in df.columns:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.show()