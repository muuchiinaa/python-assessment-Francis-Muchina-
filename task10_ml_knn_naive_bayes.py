import sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
 
 
def confirm_sklearn_installed():
    """(a) Confirm scikit-learn is installed and print its version."""
    print("scikit-learn version:", sklearn.__version__)
 
 
def load_data():
    """(b) Load the Iris dataset with Pandas and preview it."""
    iris = load_iris(as_frame=True)
    df = iris.frame  
    print("First 5 rows of the Iris dataset:")
    print(df.head())
    return df, iris.target_names
 
 
def prepare_train_test(df):
    """(c) Prepare features (X) and labels (y); split train/test."""
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    return X_train, X_test, y_train, y_test
 
 
def knn_classification(X_train, X_test, y_train, y_test):
    """(d) & (e) Train and evaluate a K-Nearest Neighbours classifier."""
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
 
    accuracy = accuracy_score(y_test, predictions)
    print("\nKNN Accuracy:", accuracy)
    print("KNN Classification Report:")
    print(classification_report(y_test, predictions))
 
    return knn
 
 
def naive_bayes_classification(X_train, X_test, y_train, y_test):
    """(g) & (h) Train and evaluate a Gaussian Naive Bayes classifier."""
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    predictions = nb.predict(X_test)
 
    accuracy = accuracy_score(y_test, predictions)
    print("\nNaive Bayes Accuracy:", accuracy)
    print("Naive Bayes Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))
  
    return nb
 
 
def main():
    confirm_sklearn_installed()
    df, target_names = load_data()
    X_train, X_test, y_train, y_test = prepare_train_test(df)
 
    knn_classification(X_train, X_test, y_train, y_test)
    naive_bayes_classification(X_train, X_test, y_train, y_test)
 
 
if __name__ == "__main__":
    main()
