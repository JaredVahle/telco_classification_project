from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def baseline_acc(X,y, stratagy = "most_frequent",random_state = 174):
    # generates a baseline model using most frequent, since there are only two outcomes we are predicting.
    model = DummyClassifier(stratagy = stratagy, random_state = random_state)
    model.fit(X,y)
    # prints an accuracy for the baseline model.
    print(f"Baseline accuracy score is {baseline_proba.score(X,y):3%}")
    return model