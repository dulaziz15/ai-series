# 📌 Makalah Utama (Main Benchmark)

### [Contagion risk prediction with Chart Graph Convolutional Network: Evidence from Chinese stock market](https://sciencedirect.com)
*   **Penjelasan Singkat:** Artikel ini memperkenalkan kerangka kerja *Chart GCN* untuk memprediksi risiko penularan finansial jangka pendek di 28 sektor pasar saham China. Model ini mengubah grafik runtun waktu harga saham (*technical charts*) menjadi bentuk graf statis berdasarkan kemiripan pola grafik (*chart similarity*) dan indikator teknikal.
*   **Keterbatasan (Gap):** Pembentukan grafnya cenderung statis atau hanya berbasis representasi pola visual chart, serta diuji pada pasar maju/besar (China).

***

# 📊 Klaster 1: Pembentukan Graf & Volatilitas Dinamis (Core Methodology)
*Makalah-makalah ini mendukung argumen Anda untuk mengganti "Chart GCN" yang kaku menjadi graf interkoneksi pasar keuangan yang adaptif secara harian menggunakan model ekonometrika.*

### [Dynamic equicorrelation stochastic volatility](https://semanticscholar.org)
*   **Penjelasan Singkat:** Jurnal ini mengusulkan model volatilitas stokastik (*stochastic volatility*) multivariat yang digabungkan dengan estimasi *Dynamic Equicorrelation* (DECO) dan efek keungkitan silang (*cross leverage*). Menggunakan pendekatan Bayesian (MCMC), model ini terbukti sangat efisien untuk menangkap fluktuasi risiko laten harian dari data indeks harga saham multidimensi.

### [Volatility equicorrelation: A cross-market perspective](https://sciencedirect.com)
*   **Penjelasan Singkat:** Artikel pertama yang menerapkan model DECO milik Engle dan Kelly pada data lintas pasar (saham, obligasi, valas, komoditas). Studi ini membuktikan bahwa *equicorrelation* (korelasi rata-rata instan) bersifat dinamis (*time-varying*) dan sangat ampuh menyederhanakan perhitungan matriks kovarians berskala besar tanpa beban komputasi yang berat.

### [Multivariate GARCH models: a survey](https://sciencedirect.com)
*   **Penjelasan Singkat:** Sebuah studi komprehensif yang memetakan evolusi model GARCH multidimensi (VEC, BEKK, DCC). Literatur ini menjadi fondasi teoretis Anda dalam menjelaskan mengapa korelasi bersyarat dinamis penting untuk memodelkan interaksi volatilitas aset keuangan.

***

# 📈 Klaster 2: Analisis Risiko Penularan Keuangan (Contagion & Tail Risk)
*Makalah-makalah empiris ini memperkuat justifikasi teoretis mengenai mekanisme jalar krisis (*spillover*) dan perilaku pasar saham di negara berkembang (*emerging market*).*

### [Dynamic interactions between sectoral tail risk and market integration: Evidence from Borsa Istanbul using PELVE and DCC-GARCH](https://researchgate.net)
*   **Penjelasan Singkat:** Jurnal ini mengkaji bagaimana risiko ekstrim (*tail risk*) dan integrasi pasar sektoral ber-evolusi bersama dari waktu ke waktu pada konteks *emerging market* (Pasar Saham Turki). Menggunakan DCC-GARCH, penelitian ini melacak bagaimana konektivitas antar-sektor dapat memicu penularan risiko sistemik saat terjadi guncangan pasar.

### [Contagion and tail risk in complex financial networks](https://sciencedirect.com)
*   **Penjelasan Singkat:** Mengembangkan kerangka kerja jaringan keuangan kompleks untuk mengukur bagaimana guncangan pada satu institusi menyebar secara sistemik. Jurnal ini memberikan landasan teori struktural tentang bagaimana *tail risk* (risiko kerugian ekstrim) mengalir di dalam interkoneksi pasar.

### [Risk contagion in the banking network: New evidence from China](https://sciencedirect.com)
*   **Penjelasan Singkat:** Menyajikan bukti empiris mengenai struktur penularan risiko pada jaringan perbankan di pasar Asia, berfokus pada bagaimana keterkaitan aset antar lembaga mempercepat transmisi krisis sistemik.

### [Detecting contagion in Asian exchange rate markets using asymmetric DCC-GARCH and R-vine copulas](https://sciencedirect.com)
*   **Penjelasan Singkat:** Memanfaatkan variasi model DCC-GARCH asimetris untuk mendeteksi penularan krisis mata uang di kawasan Asia. Jurnal ini memvalidasi keandalan rumpun model DCC-GARCH dalam menangkap pergeseran struktur korelasi secara instan saat krisis melanda wilayah Asia.

***

# 🤖 Klaster 3: Pemodelan AI Data Runtun Waktu (Machine Learning Framework)
*Mendukung implementasi teknis algoritma kecerdasan buatan berbasis graf (GNN) dan validasi runtun waktu (*time-series validation*).*

### [Exploring Graph Neural Networks for Stock Market Predictions with Rolling Window Analysis](https://springer.com)
*   **Penjelasan Singkat:** Makalah ini mendemonstrasikan bagaimana arsitektur GNN dapat dioptimalkan untuk ranah prediksi finansial dengan mengintegrasikan teknik evaluasi *Rolling Window*. Pengujian berkala ini memastikan model AI tetap andal meski karakteristik data pasar saham terus bergeser.

### [On the use of flexible rolling-window estimation for macroeconomic forecasting](https://sciencedirect.com)
*   **Penjelasan Singkat:** Jurnal ini memberikan fondasi ekonometrika mengenai pentingnya ukuran jendela bergerak (*rolling window*) yang fleksibel untuk peramalan runtun waktu, yang berguna untuk membantu model machine learning beradaptasi terhadap perubahan rezim pasar (misal dari kondisi ekonomi normal ke kondisi krisis).


https://www.gc.cuny.edu/sites/default/files/2021-07/dieboldandyilmaz_CUNY.pdf
