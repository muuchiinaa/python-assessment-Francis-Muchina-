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
    df = iris.frame  # includes feature columns + 'target' column
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
 
    # (f) The mathematics behind KNN:
    #
    # KNN classifies a new point by looking at the 'k' training points
    # closest to it and taking a majority vote of their class labels.
    # Distance is usually measured with the Euclidean distance formula:
    #
    #     d(p, q) = sqrt( sum_i (p_i - q_i)^2 )
    #
    # where p and q are two feature vectors and p_i, q_i are their
    # individual feature values. Once distances to all training points
    # are computed, the k smallest distances are selected and the most
    # common class label among those k neighbours becomes the
    # prediction.
    #
    # Choosing k: a small k (e.g. k=1) is sensitive to noise/outliers
    # and can overfit, while a very large k oversmooths the decision
    # boundary and can underfit by pulling in points from other
    # classes. A common practical approach is to try a range of odd
    # values of k (to avoid ties in binary classification) and pick
    # the one that gives the best accuracy on a validation set - here
    # k=3 is used as a reasonable, commonly-used default for a small
    # dataset like Iris.
 
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
 
    # (i) The mathematics behind Naive Bayes:
    #
    # Naive Bayes is built on Bayes' theorem, which relates the
    # probability of a class C given evidence (features) X to the
    # reverse conditional probability:
    #
    #     P(C | X) = ( P(X | C) * P(C) ) / P(X)
    #
    # - P(C) is the prior probability of class C (how common it is).
    # - P(X | C) is the likelihood: how probable the observed
    #   features are, given that class.
    # - P(X) is the overall probability of the evidence (a
    #   normalising constant, the same for every class).
    #
    # The "naive" part is the assumption that all features are
    # conditionally independent given the class, so the joint
    # likelihood simplifies to a product of per-feature (class
    # conditional) probabilities:
    #
    #     P(X | C) = P(x_1 | C) * P(x_2 | C) * ... * P(x_n | C)
    #
    # For continuous features (as in Iris), GaussianNB assumes each
    # feature is normally distributed within a class, so each
    # P(x_i | C) is computed from a Gaussian probability density
    # function fitted to that feature's values in that class. The
    # class with the highest resulting posterior probability
    # P(C | X) is chosen as the prediction.
 
    return nb
 
 
def main():
    confirm_sklearn_installed()
    df, target_names = load_data()
    X_train, X_test, y_train, y_test = prepare_train_test(df)
 
    knn_classification(X_train, X_test, y_train, y_test)
    naive_bayes_classification(X_train, X_test, y_train, y_test)
 
 
if __name__ == "__main__":
    main()
