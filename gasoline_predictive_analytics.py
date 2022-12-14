# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lhrUqiO9bx0IwXRYscy-luh2J8G9v-ty

Nama = Anas Fikri Hanif\
SIB ID = M183X0321

#**Import Library**
"""

# Commented out IPython magic to ensure Python compatibility.
# Data loading and data analysis
import numpy as np
import pandas as pd
import zipfile
from google.colab import files

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Data preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

# Modeling
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

"""#**Preparing Dataset From Kaggle**"""

# Install kaggle 
!pip install -q kaggle

# Token API
uploaded = files.upload()

# Receive dataset config
!chmod 600 /content/kaggle.json

# Download dataset
! KAGGLE_CONFIG_DIR=/content/ kaggle datasets download -d mattiuzc/commodity-futures-price-history

# extract dataset
local_zip = '/content/commodity-futures-price-history.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content')
zip_ref.close()

"""#**Dataset Information**"""

df_dir = '/content/Commodity Data/RBOB Gasoline.csv'
gasoline = pd.read_csv(df_dir)
gasoline.head()

print(f'Data consist of {gasoline.shape[1]} columns')
print(f'Each column consists of {gasoline.shape[0]} records')

"""#**Exploratory Data Analysis**

**Variabel-variabel yang Ada dalam Dataset**

* Date : Tanggal pencatatan Data
* Open : Harga buka dihitung perhari
* High : Harga tertinggi perhari
* Low : Harga terendah perhari
* Close : Harga tutup dihitung perhari
* Adj Close : Harga penutupan pada hari tersebut setelah disesuaikan dengan aksi korporasi seperti right issue, stock split atau stock reverse.
* Volume : Volume transaksi

**Handling Missing Value**
"""

gasoline.info()

"""Pengecekan jumlah data yang null"""

gasoline.isnull().sum()

print('Jumlah data yang null adalah ', gasoline.isnull().sum().sum(), ' records')

"""Karena terdapat cukup banyak data yang null, maka kita akan mengisi data null dengan mean dari kolom masing-masing dengan bantuan SimpleImputer"""

missing_col = [col for col in gasoline.columns if gasoline[col].isnull().any()]

imputer = SimpleImputer()
gasoline[missing_col] = imputer.fit_transform(gasoline[missing_col])
gasoline.head()

print('Jumlah data yang null adalah ', gasoline.isnull().sum().sum(), ' records')

"""Sekarang dataframe kita sudah bersih dari data null

## **Explore Statistic Information**

**Berikut adalah beberapa informasi statistik yang ada pada masing-masing kolom:**

* **count** adalah jumlah sampel pada data.
* **mean** adalah nilai rata-rata.
* **std** adalah standar deviasi.
* **min** adalah nilai minimum.
* **25%** adalah kuartil pertama.
* **50%** adalah kuartil kedua (nilai tengah).
* **75%** adalah kuartil ketiga.
* **max** adalah nilai maksimum
"""

gasoline.describe()

"""## **Data Visualization**

Visualisasi data pertama ini akan kita manfaatkan untuk mencari outliers pada dataset
"""

numerical_data = [col for col in gasoline.columns if gasoline[col].dtype == 'float64']
plt.figure(figsize=(20, 10))
sns.boxplot(data=gasoline[numerical_data]).set_title('Gasoline Price Data')
plt.show()

"""Kolom 'Volume' terdeteksi memiliki outliers. Oleh karena itu kita akan mengatasi data-data outliers ini menggunakan IQR Method dengan cara kerja menghapus data-data yang berada di luar IQR"""

Q1 = gasoline.quantile(.25)
Q3 = gasoline.quantile(.75)
IQR = Q3 - Q1
gasoline=gasoline[~((gasoline<(Q1-1.5*IQR))|(gasoline>(Q3+1.5*IQR))).any(axis=1)]

"""Berikut adalah data kita setelah outliers dihilangkan"""

print(f'Data consist of {gasoline.shape[1]} columns')
print(f'Each column consists of {gasoline.shape[0]} records')

numerical_data = [col for col in gasoline.columns if gasoline[col].dtype == 'float64']
plt.figure(figsize=(20, 10))
sns.boxplot(data=gasoline[numerical_data]).set_title('Gasoline Price Data')
plt.show()

"""## **Univariate Analysis**

Kolom target kita adalah kolom 'Adj Close' sehingga kita hanya akan fokus ke sana
"""

cols = 3
rows = 2
fig = plt.figure(figsize=(cols * 5, rows * 5))

for i, col in enumerate(numerical_data):
  ax = fig.add_subplot(rows, cols, i + 1)
  sns.histplot(x=gasoline[col], bins=30, kde=True, ax=ax)
fig.tight_layout()
plt.show()

"""## **Multivariate Analysis**

Pada tahap ini kita akan melihat korelasi dari kolom 'Adj Close' dengan kolom-kolom lainnya. Pada plot di bawah kita hanya perlu untuk fokus pada plot baris ke-5. Di sana terlihat jelas bahwa kolom 'Adj Close' memiliki korelasi positif kuat terhadap kolom 'Open', 'High', 'Low', 'Close'. Sementara hubungan dengan kolom 'Volume' adalah korelasi yang lemah
"""

sns.pairplot(gasoline[numerical_data], diag_kind='kde')
plt.show()

"""Untuk melihat nilai korelasi dengan lebih jelas, kita bisa memanfaatkan Heatmap dari library Seaborn"""

plt.figure(figsize=(10, 8))
correlation_matrix = gasoline.corr().round(2)

# untuk print nilai dalam kotak gunakan anot true
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matrix Correlation', size=25)

"""# **Preparing Data**

## **Drop Unused Data**

Pada bagian ini kita akan menghapus beberapa kolom yang dapat mengganggu proses training model. Kolom-kolom tersebut adalah kolom 'Date', 'Close', dan 'Volume'
"""

gasoline = gasoline.drop(['Date', 'Close', 'Volume'], axis=1)

gasoline.head()

"""## **Splitting Train and Test**"""

X = gasoline.iloc[:, :-1].values
y = gasoline.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print('x_train = ', (len(x_train)), ' records')
print('y_train = ', (len(y_train)), ' records')
print('x_test = ', (len(x_test)), ' records')
print('y_test = ', (len(y_test)), ' records')

"""## **Normalization**

Kita akan menormalisasi data dengan mengubahnya berada dalam rentang 0 hingg 1. Normalisasi ini akan menggunakan bantuan MinMaxScaler
"""

minmax = MinMaxScaler()
x_train = minmax.fit_transform(x_train)
x_test = minmax.transform(x_test)

"""# **Model Development**"""

models = pd.DataFrame(columns=['train_mse', 'test_mse'], index=['SVR', 'KNN', 'GradientBoosting'])

"""## **Hyperparameter Tuning**

Hyperparameter tuning adalah penambah model otomatis yang disediakan oleh AI Platform Training guna mencapai model terbaik. Akan tetapi, kita juga dapat menguah hyperparameter tuning secara manual dengan menggunakan bantuan GridSearch. GridSearch merupakan sebuah teknik yang memungkinkan kita untuk menguji beberapa hyperparameter sekaligus pada sebuah model
"""

def grid_search(model, hyperparameters):
  results = GridSearchCV(
      model,
      hyperparameters,
      cv=5,
      verbose=1,
      n_jobs=6
  )

  return results

svr = SVR()
hyperparameters = {
    'kernel': ['rbf'],
    'C': [0.001, 0.01, 0.1, 10, 100, 1000],
    'gamma': [0.3, 0.03, 0.003, 0.0003]
}

svr_search = grid_search(svr, hyperparameters)
svr_search.fit(x_train, y_train)
print(svr_search.best_params_)
print(svr_search.best_score_)

gradient_boost = GradientBoostingRegressor()
hyperparameters = {
    'learning_rate': [0.01, 0.001, 0.0001],
    'n_estimators': [250, 500, 750, 1000],
    'criterion': ['friedman_mse', 'squared_error']
}

gradient_boost_search = grid_search(gradient_boost, hyperparameters)
gradient_boost_search.fit(x_train, y_train)
print(gradient_boost_search.best_params_)
print(gradient_boost_search.best_score_)

knn = KNeighborsRegressor()
hyperparameters = {
    'n_neighbors': range(1, 10)
}

knn_search = grid_search(knn, hyperparameters)
knn_search.fit(x_train, y_train)
print(knn_search.best_params_)
print(knn_search.best_score_)

"""## **Fitting Model**

Setelah mendapatkan hyperparameter terbaik melalui proses hyperparameter tuning, maka sekarang adalah saatnya kita melatih model dengan hyperparameter terbaik. Di sini kita akan menggunakan tiga algoritma yaitu SVR, Gradient Boost, dan KNN
"""

svr = SVR(C=1000, gamma=0.003, kernel='rbf')
svr.fit(x_train, y_train)

gradient_boost = GradientBoostingRegressor(criterion='squared_error', learning_rate=0.01, n_estimators=1000)
gradient_boost.fit(x_train, y_train)

knn = KNeighborsRegressor(n_neighbors=6)
knn.fit(x_train, y_train)

"""## **Model Evaluation**

Setelah menerapkan tiga algoritma pada model kita, kali ini kita akan menghitung nilai MSE terkecil dari seluruh algoritma
"""

model_dict = {
    'SVR': svr,
    'GradientBoosting': gradient_boost,
    'KNN': knn,
}

for name, model in model_dict.items():
  models.loc[name, 'train_mse'] = mean_squared_error(y_train, model.predict(x_train))
  models.loc[name, 'test_mse'] = mean_squared_error(y_test, model.predict(x_test))

models.head()

models.sort_values(by='test_mse', ascending=False).plot(kind='bar', zorder=3)

"""Dari plot dan data di atas, KNN adalah algoritma terbaik yang memberikan MSE terkecil, untuk lebih jelasnya kita akan mencari akurasi dari setiap algoritma."""

svr_acc = svr.score(x_test, y_test)*100
boosting_acc = gradient_boost.score(x_test, y_test)*100
knn_acc = knn.score(x_test, y_test)*100

evaluation_list = [[svr_acc], [boosting_acc], [knn_acc]]
evaluation = pd.DataFrame(evaluation_list,
                          columns = ['Accuracy (%)'],
                          index = ['SVR', 'Gradient Boost', 'KNN'])

evaluation

"""Hasil evaluasi di atas juga menunjukkan bahwa KNN adalah algoritma terbaik untuk model kita dengan skor 99.94%

# **Forecasting**

Setelah mendapatkan algoritma KNN sebagai algoritma terbaik, maka sekarang kita akan mencoba meramal (forecasting) harga bensin selama satu minggu ke depan dengan menggunakan algoritma KNN
"""

X_7=X[-7:]
forecast=knn.predict(X_7)

forecast=pd.DataFrame(forecast,columns=['Forecast'])
gasoline1=gasoline.append(forecast)
gasoline1.drop(['High', 'Low', 'Open'],axis=1,inplace=True)

gasoline1.tail(14)