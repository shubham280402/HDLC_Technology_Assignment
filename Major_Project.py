import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Step 1: Import the necessary libraries

# Step 2: Load the dataset using pandas
data = pd.read_csv("test.csv")

# Step 3: Preprocess the data
X = data.drop("price_range", axis=1)  # Features
y = data["price_range"]  # Target variable

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train an SVM classifier on the training data
svm = SVC()
svm.fit(X_train, y_train)

# Step 6: Evaluate the trained classifier on the testing data
y_pred = svm.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 7: Classify the mobile phone price range using the trained classifier
new_data = pd.read_csv("new_mobile_data.csv")  # Assuming you have new data to classify
new_predictions = svm.predict(new_data)
print(new_predictions)


data = pd.read_csv("train.csv")


X = data.drop("price_range", axis=1)
y = data["price_range"] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


svm = SVC()
svm.fit(X_train, y_train)


y_pred = svm.predict(X_test)
print(classification_report(y_test, y_pred))


new_data = pd.read_csv("new_mobile_data.csv")
new_predictions = svm.predict(new_data)
print(new_predictions)