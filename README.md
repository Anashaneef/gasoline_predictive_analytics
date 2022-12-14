# Laporan Proyek Machine Learning - Anas Fikri Hanif
---

## Domain Proyek
Domain yang dipilih pada proyek ini adalah keuangan, ekonomi dan bisnis. Proyek ini sendiri mengusung judul _Gasoline Price Forecasting_

### Latar Belakang
Pemerintah Republik Indonesia resmi mengumumkan kenaikan harga BBM bersubsidi pada 3 September 2022. Hal ini memicu pecahnya keributan untuk menolak kenaikan harga BBM di berbagai daerah di Indonesia. Banyak pihak menentang kenaikan harga BBM ini karena mereka merasa dirugikan. Akan tetapi pemerintah tidak memiliki opsi lain untuk menghadapi inflasi dunia yang memang sudah terjadi sejak Rusia menginvasi Ukraina pada 24 Februari 2022. Tidak hanya Indonesia, negara-negara adidaya seperti Amerika Serikat pun terkena dampak dari inflasi ini dengan melonjaknya harga BBM di negara tersebut.

Kenaikan harga BBM akan sangat berpengaruh terhadap permintaan (_demand_) dan penawaran (_supply_). Permintaan adalah keinginan yang disertai dengan kesediaan serta kemampuan untuk membeli barang yang bersangkutan (Rosyidi, 2009:291). Sementara penawaran adalah banyaknya jumlah barang dan jasa yang ditawarkan oleh produsen pada tingkat harga dan waktu tertentu. Permintaan dari masyarakat akan berkurang karena harga barang dan jasa yang ditawarkan mengalami kenaikan. Begitu juga dengan penawaran, akan berkurang akibat permintaan dari masyarakat menurun. Harga barang-barang dan jasa-jasa menjadi melonjak akibat dari naiknya biaya produksi dari barang dan jasa. Ini adalah imbas dari kenaikan harga BBM. Hal ini sesuai dengan hukum permintaan, "Jika harga suatu barang naik, maka jumlah barang yang diminta akan turun, dan sebaliknya jika harga barang turun, jumlah barang yang diminta akan bertambah" (Jaka, 2007:58)

Di sisi lain, kenaikan harga BBM ini akan memberikan keuntungan yang luar biasa bagi para investor, termasuk para investor bensin. Investasi dalam dunia BBM terutama bensin memang sangat menjanjikan. Hal ini dikarenakan kebutuhan masyarakat yang terus meningkat serta harga bensin yang terus naik dari waktu ke waktu. Investasi sendiri dapat dibagi menjadi 2 kelompok dilihat dari dimensi waktunnya (Wiagustini, 2010:175) yaitu sebagai berikut: Investasi jangka pendek (satu tahun atau kurang), yaitu investasi pada aktiva lancar, seperti kas, piutang, inventori, dan surat-surat berharga. Investasi jangka panjang (lebih dari satu tahun), yaitu investasi pada aset riil, seperti tanah, bangunan, peralatan kantor, kendaraan, aset riil lainnya, dan investasi pada aset finansial seperti investasi pada saham dan obligasi. Melihat pernyataan ini, bensin sendiri termasuk ke dalam investasi jangka panjang.

Berdasarkan dari uraian-uraian di atas maka penulis memiliki sebuah ide guna membantu para investor bensin untuk memprediksi harga bensin di masa yang akan datang sehingga para investor bisa mendapatkan laba semaksimal mungkin. Oleh karena itu, penulis menyusun sebuah proyek dengan judul _Gasoline Price Forecasting_. Dengan adanya proyek ini, penulis berharap para investor bensin akan sangat terbantu.


## Business Understanding
---

### Problem Statement
Berdasarkan pada latar belakang di atas, permasalahan yang dapat diselesaikan pada proyek ini adalah sebagai berikut :
* Bagaimana cara memilih model dan algoritma terbaik untuk mengolah data harga *bensin*?
* Bagaimana cara melatih model dengan algoritma terbaik?
* Bagaimana cara memprediksi harga *bensin* dengan menggunakan _time series forecasting_?

### Goals
Tujuan atau _goals_ proyek ini dibuat adalah sebagai berikut :
* Mendapatkan model dan algoritma terbaik untuk mengolah data harga *bensin*.
* Melakukan pelatihan terhadap model menggunakan algoritma yang terbaik.
* Membantu para investor guna memprediksi harga *bensin* di masa yang akan datang.

### Solution Statement
Solusi yang dapat dilakukan agar goals terpenuhi adalah sebagai berikut :
* Melakukan _exploratory data analysis_ yang didalamnya terdapat analisa, eksplorasi, _processing_ data dengan memvisualisasikan data agar memperjelas gambaran mengenai karakteristik data tersebut. Berikut adalah analisa yang dapat dilakukan :
    * Menangani *missing value* pada data, dalam hal ini adalah data _null_.
    * Mencari korelasi pada data untuk menemukan *dependant variable* dan *independent variable*.
    * Menangani _outlier_ atau pencilan pada data dengan menggunakan Metode IQR.
    * Melakukan normalisasi pada data terutama pada fitur numerik.
    * Membuat model regresi untuk memprediksi bilangan kontinu untuk memprediksi harga yang akan datang. 
    
* Berikut beberapa algoritma yang digunakan pada proyek ini :
    * Support Vector Machine (Support Vector Regression)
    * K-Nearest Neighbors
    * Boosting Algorithm (Gradient Boosting Regression)
    
* Melakukan hyperparameter tuning agar model dapat berjalan pada performa terbaik dengan menggunakan teknik Grid Search.

* Melakukan prediksi harga (_forecasting_) dengan menggunakan model dan algoritma yang memiliki performa terbaik

## Data Understanding
---

Dataset yang digunakan dalam proyek ini merupakan dataset dari riwayat harga bensin dengan detail yang lengkap. Informasi mengenai dataset ini adalah sebagai berikut:
| Jenis                   | Keterangan                                                                                  |
|-------------------------|---------------------------------------------------------------------------------------------|
| Sumber                  | Dataset: [Kaggle](https://www.kaggle.com/datasets/mattiuzc/commodity-futures-price-history) |
| Dataset Owner           | mattiuzc                                                                                    |
| Usability               | 8.24                                                                                        |
| Jenis dan Ukuran Berkas | CSV (322.61 kB)                                                                             |

Dataset yang digunakan memiliki total 5246 _record_ dalam setiap kolom. Dataset ini sendiri memiliki dengan 7 kolom (*Date, Open, High, Low, Close, Adj Close, Volume*) yang memiliki 105 *missing value* pada masing-masing kolom *Open, High, Low, Close, Adj Close, Volume* dengan informasi sebagai berikut :
  * Date : Tanggal pencatatan Data
  * Open : Harga buka dihitung perhari
  * High : Harga tertinggi perhari
  * Low : Harga terendah perhari
  * Close : Harga tutup dihitung perhari
  * Adj Close : Harga penutupan pada hari tersebut setelah disesuaikan dengan aksi korporasi seperti right issue, stock split atau stock reverse.
  * Volume : Volume transaksi

### Exploratory Data Analysis
Sebelum melakukan pemrosesan data, kita harus mengetahui keadaan data. seperti mencari korelasi antar fitur, mencari outlier, melakukan analisis *univariate* dan *multivariate*.

- Menangani outlier
![outliers_visualization](https://user-images.githubusercontent.com/79641595/189601601-16e55dba-2222-437c-9dd8-47ce431e1718.png)
<br> Ketika kita menggunakan visualisasi data berkategori numerik seperti di atas, maka kita akan mendapati kolom 'Volume' memiliki data yang termasuk dalam outlier. Oleh karena itu, kita akan menghilangkan outlier ini dengan IQR Method. Metode ini bekerja dengan cara menghapus data-data yang berada di luar IQR (dalam rentang 25% hingga 75% data). Setelah melakukan penghapusan tehadap data outlier, maka didapatkan sebuah data baru dengan total 7 kolom di mana masing-masing kolom memiliki 5195 record.

- Univariate Analysis
<br>

![univariate_analysis ](https://user-images.githubusercontent.com/79641595/189610119-328247e6-b80e-41c3-b990-db6846b7ba1b.png)

<br> Kolom target kita adalah kolom 'Adj Close' sehingga kita hanya akan fokus ke sana.

- Multivariate Analysis
<br> Pada tahap ini kita akan melihat korelasi dari kolom 'Adj Close' dengan kolom-kolom lainnya. Pada plot di bawah kita hanya perlu untuk fokus pada plot baris ke-5. Di sana terlihat jelas bahwa kolom 'Adj Close' memiliki korelasi positif kuat terhadap kolom 'Open', 'High', 'Low', 'Close'. Sementara hubungan dengan kolom 'Volume' adalah korelasi yang lemah
<br>

![multivariate_analysis](https://user-images.githubusercontent.com/79641595/189610176-c1c88ee0-f65d-4545-a059-e14dbd8cee16.png)


<br> Untuk melihat nilai korelasi dengan lebih jelas, kita bisa memanfaatkan Heatmap dari library Seaborn. Dapat kita lihat bahwa 'Adj Close' memiliki korelasi positif tinggi pada setiap fitur yang ditandai dengan warna merah dan angka 1, kecuali fitur 'Volume' sehingga kita dapat menggunakan semua fitur sebagai dependant variable.

![heatmap](https://user-images.githubusercontent.com/79641595/189610633-eb1b6a89-9ec9-439a-9b10-14db8ec8fab7.png)

# Data Preparation
---

Berikut ini merupakan tahapan-tahapan dalam melakukan pra-pemrosesan data:
### Melakukan Penanganan Missing Value
Pada kasus ini dalam menangani Missing Value menggunakan library SimpleImputer, yang dimana library ini bertugas untuk mengisi kolom yang memiliki missing value dengan data mean (nilai rata-rata)

### Melakukan pembagian dataset
Kita akan membagi dataset menjadi 2 yaitu sebagai train data dan test data. Train data digunakan sebagai training model dan test data digunakan sebagai validasi apakah model sudah akurat atau belum. Ratio yang umum dalam splitting dataset adalah 80:20, 80% sebagai train data dan 20% sebagai test data, sehingga kita akan menggunakan Ratio tersebut. Pembagian dataset dilakukan dengan modul train_test_split dari scikit-learn. Setelah melakukan pembagian dataset, didapatkan jumlah sample pada data latih yaitu 3640 sampel dan jumlah sample pada data test yaitu 910 sampel dari total jumlah sample pada dataset yaitu 4550 sampel.
    
### Menghapus fitur yang tidak diperlukan
Karena kita tidak memerlukan fitur *Date* dan *Volume* kita akan menghapus fitur *Date* dan *Volume*. Juga kita tidak memerlukan fitur *Close* karena *Adj Close* lebih akurat dari pada *Close* sehingga kita menghapus fitur *Close*.

### Data Normalization
Normalisasi data digunakan agar model dapat bekerja lebih optimal karena model tidak perlu mengolah data dengan angka besar. Normalisasi biasanya mentransformasi data dalam skala tertentu. Untuk proyek ini kita akan normalisasi data 0 hingga 1 menggunakan MinMaxScaler.

# Modeling
---

Model yang akan digunakan proyek kali ini yaitu *Support Vector Regression, Gradient Boosting,* dan *K-Nearest Neighbors*.

### Support Vector Regression
*Support Vector Regression* memiliki prinsip yang sama dengan SVM, namun SVM biasa digunakan dalam klasifikasi. Pada SVM, algoritma tersebut berusaha mencari jalan terbesar yang bisa memisahkan sampel dari kelas berbeda, sedangkan SVR mencari jalan yang dapat menampung sebanyak mungkin sampel di jalan. Untuk hyper parameter yang digunakan pada model ini adalah sebagai berikut :
* *kernel* : Hyperparameter ini digunakan untuk menghitung kernel matriks sebelumnya. Pada dataset yang kita gunakan, kernel yang dipilih adalah 'rbf'. Kernel RBF atau juga disebut kernel Gaussian adalah konsep kernel yang paling banyak digunakan untuk memecahkan masalah klasifikasi data yang tidak dapat dipisahkan secara linear. Kernel ini dikenal memiliki performa yang baik dengan parameter tertentu, dan hasil dari pelatihan memiliki nilai error yang kecil dibandingkan dengan kernel lainnya.
* *C* : Hyperparameter ini adalah parameter regularisasi digunakan untuk menukar klasifikasi yang benar dari contoh *training* terhadap maksimalisasi margin fungsi keputusan. Dalam fitting model yang kita gunakan, hyperparameter C diberikan nilai 1000.
* *gamma* : Hyperparameter ini digunakan untk menetukan seberapa jauh pengaruh satu contoh pelatihan mencapai, dengan nilai rendah berarti jauh dan nilai tinggi berarti dekat. Dalam fitting model yang kita gunakan, hyperparameter gamma diberikan nilai 0.003.

##### Kelebihan
* Lebih efektif pada data dimensi tinggi (data dengan jumlah fitur yang banyak)
* Memori lebih efisien karena menggunakan subset poin pelatihan

##### Kekurangan
* Sulit dipakai pada data skala besar

### K-Nearest Neighbors
*K-Nearest Neighbors* merupakan algoritma machine learning yang bekerja dengan mengklasifikasikan data baru menggunakan kemiripan antara data baru dengan sejumlah data (k) pada data yang telah ada. Algoritma ini dapat digunakan untuk klasifikasi dan regresi. Kali ini untuk nilai k tidak kita deklarasikan sehingga akan tetap pada nilai default. Untuk hyperparameter yang digunakan pada model ini hanya 1 yaitu :
* *n_neighbors* : Jumlah tetangga untuk yang diperlukan untuk menentukan letak data baru. Dalam fitting model yang kita gunakan, hyperparameter n_neigbors diberikan nilai 6 karena kita hanya ingin 6 titik yang digunakan untuk menentukan letak baru.

##### Kelebihan
* Dapat menerima data yang masih *noisy*
* Sangat efektif apabila jumlah datanya banyak
* Mudah diimplementasikan

##### Kekurangan
* Sensitif pada outlier
* Rentan pada fitur yang kurang informatif

### Gradient Boosting
Gradient Boosting adalah algoritma machine learning yang menggunakan teknik *ensembel learning* dari *decision tree* untuk memprediksi nilai. Gradient Boosting sangat mampu menangani pattern yang kompleks dan data ketika linear model tidak dapat menangani. Untuk hyperparameter yang digunakan pada model ini ada 3 yaitu :
* *learning_rate* : Hyperparameter training yang digunakan untuk menghitung nilai koreksi bobot padad waktu proses training. Umumnya nilai learning rate berkisar antara 0 hingga 1. Dalam fitting model yang kita gunakan, hyperparameter ini diberikan nilai 0.01.
* *n_estimators* : Jumlah tahapan boosting yang akan dilakukan. Dalam proses fitting model, kita menggunakan 1000 tahapan sehingga nilai dari n_estimators adalah 1000
* *criterion* : Hyperparameter yang digunakan untuk menemukan fitur dan ambang batas optimal dalam membagi data. Ada beberapa criterion yang dapat diaplikasikan, diantaranya adalah "friedman_mse" untuk kesalahan kuadrat rata-rata dengan skor perbaikan oleh Friedman, "squared_error" untuk kesalahan kuadrat rata-rata. Dalam proses fitting model, kita menggunakan criterion "squared_error".

##### Kelebihan
* Hasil pemodelan yang lebih akurat
* Model yang stabil dan lebih kuat (robust)
* Dapat digunakan untuk menangkap hubungan linear maupun non linear pada data

##### Kekurangan
* Pengurangan kemampuan interpretasi model
* Waktu komputasi dan desain tinggi
* Tingkat kesulitan yang tinggi dalam pemilihan model

Untuk proyek kali ini kita akan menggunakan model *K-Nearest Neighbors* karena memiliki error (*0.00001*) yang paling sedikit daripada model yang lain. Namun tidak bisa dipungkiri model dari Gradient Boosting juga memiliki error (*0.000011*) yang hampir seperti *KNN*.

# Evaluation
---

Untuk evaluasi pada machine learning model ini, metrik yang digunakan adalah *mean squared error (mse)*. Dimana metrik ini mengukur seberapa dekat garis pas dengan titik data. Model terbaik adalah model dengan nilai MSE paling sedikit

<br>
<image src='https://www.pythonpool.com/wp-content/uploads/2021/08/20210812_200937_0000-1024x270.png' width= 500/>

dimana :
n = jumlah titik data
Yi = nilai sesungguhnya
Yi_hat = nilai prediksi

Berikut adalah nilai MSE dari masing-masing model:
<br>

![mse](https://user-images.githubusercontent.com/79641595/189610928-04038024-04ba-4d91-a6d1-3933b6b49644.png)

<br>

![mse_plot](https://user-images.githubusercontent.com/79641595/189610978-64ce4457-4c81-473d-995a-cfe30387ccad.png)

<br>Untuk lebih jelasnya, kita akan menampilkan hasil akurasi dari beberapa model yang dipakai :

![model_accuracy](https://user-images.githubusercontent.com/79641595/189601673-e01997bb-c274-4f60-94fc-4a21e504a99c.png)

<br>
Untuk proyek kali ini terdapat 2 model yang dapat berjalan dengan performa optimal yaitu, Gradient Boosting model dan K-Nearest Neighbors. Terdapat selisih nilai yang sangat kecil. Tetapi pada perhitungan akurasi model terlihat model yang menggunakan K-Nearest Neighbors memiliki nilai lebih 0.02% daripada Gradient Boosting.

# Forecasting
---

Berdasarkan algoritma terbaik yang telah didapatkan, yaitu algoritma KNN. Algoritma KNN sendiri memiliki akurasi sebesar 99.944909% dan MSE sebesar 0.000274. Selanjutnya kita akan melakukan peramalan atau prediksi harga bensin selama satu minggu ke depan.
<br>

![forecasting](https://user-images.githubusercontent.com/79641595/189611054-13ac0f30-a1c3-42df-8d37-cbbe9b0c267c.png)

# Conclusion
---

Berdasarkan seluruh proses dalam proyek mulai dari penyiapan dataset hingga forecasting, akhirnya kita tiba pada kesimpulan dari keseluruhan jalannya proyek ini. Beberapa poin penting yang terdapat dalam proyek ini adalah sebagai berikut:
* Proses EDA (Exploratory Data Analysis) dilakukan dengan _handling missing value_ berupa pengisian data _null_ dengan bantuan SimpleImputer serta penghapusan data _outliers_ dengan IQR Method.
* Pengujian korelasi untuk menemukan variabel _dependent_ dan _independent_ dilakukan dengan menggunakan univariate analysis, multivariate analysis, dan visualisasi heatmap menggunakan bantuan library seaborn.
* Splitting data train dan test menggunakan perbandingan 80:20
* Normalisasi data menggunakan MinMaxScaler
* Berdasatkan tiga algoritma yang telah diuji yaitu SVR, Gradient Boosting, dan KNN menghasilkan kesimpulan bahwa algoritma KNN adalah yang paling optimal dengan akurasi sebesar 99.944909% dan MSE sebesar 0.000274.
* Berdasarkan pemilihan algoritma yang paling optimal, maka proses _time series forecasting_ berhasil dilakukan dengan menggunakan algoritma KNN.

Dari beberapa poin tersebut dapat ditarik sebuah kesimpulan di mana proyek yang telah kita buat berhasil memenuhi _goal_ atau tujuan yang kita rumuskan di awal.

# Referensi :
---

* Aliyev, V. (2020, October 7). Gradient boosting classification explained through python. Medium. Retrieved August 22, 2022, from https://towardsdatascience.com/gradient-boosting-classification-explained-through-python-60cc980eeb3d 
* Foreign Exchange turnover in April 2019. The Bank for International Settlements. (2019, September 16). Retrieved August 20, 2022, from https://www.bis.org/statistics/rpfx19_fx.htm 
* Hussein, S., &amp; About The AuthorSaddam HusseinTerlibat di pekerjaan dunia geospasial sejak 2011. Sekarang bekerja di sebuah NGO internasional yang bergerak di bidang konservasi satwa liar. (2022, February 2). Ensemble learning dalam machine learning: Bagging Dan Boosting. GEOSPASIALIS. Retrieved August 22, 2022, from https://geospasialis.com/ensemble-learning/ 
* Jaka, Nur dkk. (2007). Intisari Ekonomi untuk SMA. Bandung : CV Pustaka Mandiri
* Rosyidi, Suherman. (2009). Pengantar Teori Ekonomi : Pendekatan Kepada Teori
* Saputri, L. (2016). IMPLEMENTASI JARINGAN SARAF TIRUAN RADIAL BASIS FUNCTION (RBF) PADA PERAMALAN FOREIGN EXCHANGE (FOREX). 
* Wiagustini, Ni Luh Putu. (2010). Dasar-Dasar Manajemen Keuangan. Denpasar : Udayana University Press. 
