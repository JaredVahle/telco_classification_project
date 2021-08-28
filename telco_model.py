from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def baseline_acc(X,y, strategy = "most_frequent",random_state = 174):
    # generates a baseline model using most frequent, since there are only two outcomes we are predicting.
    model = DummyClassifier(strategy = strategy, random_state = random_state)
    model.fit(X,y)
    # prints an accuracy for the baseline model.
    print(f"Baseline accuracy score is: {model.score(X,y):.3%}")
    # Returns the baseline model back for use.
    return model

def tree_model(X,y,max_depth = 5, criterion = "gini", splitter = "best", random_state = 174):
    dt_model = DecisionTreeClassifier(max_depth = max_depth, criterion = criterion, splitter = splitter, random_state = random_state)
    dt_model.fit(X,y)
    y_pred = dt_model.predict(X)
    print(f"This decision tree models accuracy score is: {dt_model.score(X,y):.3%}")
    print("")
    print(classification_report(y,y_pred))
    return model,y_pred

def rand_forest(X,y, n_estimators = 30, criterion = "gini",max_depth = 9, random_state = 174, min_samples_leaf = 3):
    rf_model = RandomForestClassifier(
        n_estimators = n_estimators,
        criterion = criterion,
        max_depth = max_depth,
        min_samples_leaf = min_samples_leaf,
        random_state = random_state )
    rf_model.fit(X,y)
    y_pred = rf_model.predict(X)
    print(f"This Random Forest models accuracy score is: {rf_model.score(X,y):.3%}")
    print("")
    print(classification_report(y,y_pred))
    return rf_model,y_pred

def knneighbors(X,y,n_neighbors = 5, weights = "uniform",leaf_size = 10,p = 2):
    knn_model = KNeighborsClassifier(
        n_neighbors = n_neighbors,
        weights = weights,
        leaf_size = leaf_size,
        p = p,)
    knn_model.fit(X,y)
    y_pred = knn_model.predict(X)
    print(f"This K Nearest Neighbor models accuracy score is: {knn_model.score(X,y):.3%}")
    print("")
    print(classification_report(y,y_pred))
    return knn_model,y_pred