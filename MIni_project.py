import numpy as np
import pandas as pd 

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 

import matplotlib.pyplot as plt
import seaborn as sns


iris_data = pd.read_csv('Iris dataset.csv')

iris_data

iris_data['species'].unique()

iris_data.isnull().values.any()

iris_data['species'].value_counts()

sns.countplot(iris_data['species'])

iris_data.plot(kind = 'scatter', x = 'sepal_length', y = 'sepal_width')

sns.set_style('whitegrid')
sns.Facetgrid(iris_data, hue='species', size=6).map(plt.scatter, x = 'sepal_length', y = 'sepal_width').add_length()

sns.pairplot(iris_data, hue='species', size=2).add_length()

for column in iris_data.columns:
  if iris_data[column].dtype == np.number:
    continue

iris_data[column] = LabelEncoder().fit_transform(iris_data[column])

iris_data.dtype

iris_data.head()

X = iris_data.drop(['species'],axis = 1)

Y = iris_data['species']

X

Y

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)

k_range = list(range(1,12))

acc = []

for i in k_range:
  knn = KNeighborsClassifier(n_neighbors=i).fit(X_train,Y_train)
  Y_pred = knn.predeict(X_test)
  acc.append(metrics.accuracy_score(Y_test,Y_pred))

acc  

knn = KNeighborsClassifier(n_neighbors=1).fit(X_train, Y_train)
Y_pred = knn.predict(X_test)

metrics.accuracy_score(Y_test,Y_pred)








