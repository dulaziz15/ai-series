ANALISIS CONTAGION RISK PASAR SAHAM INDONESIA MENGGUNAKAN GRAPH NEURAL NETWORK DENGAN GRAF KORELASI DINAMIS ANTAR SAHAM BERBASIS DCC-GARCH 


SKRIPSI
Digunakan Sebagai Syarat Maju Ujian Diploma IV
Politeknik Negeri Malang

Oleh:
ABDUL AZIZ	NIM. 244107023009



 



PROGRAM STUDI TEKNIK INFORMATIKA
JURUSAN TEKNOLOGI INFORMASI
POLITEKNIK NEGERI MALANG
JULI 2021 

 
HALAMAN PENGESAHAN
ANALISIS CONTAGION RISK PASAR SAHAM INDONESIA MENGGUNAKAN GRAPH NEURAL NETWORK BERBASIS KORELASI DINAMIS ANTAR SAHAM

Disusun oleh: 
ABDDUL AZIZ 	NIM. 244107023009

Laporan Akhir ini telah diuji pada tanggal 21 Juni 2021

Disetujui oleh:

1.	Pembimbing Utama	:	Imam Fahrur Rozi, S.T., M.T.
NIP. 19840610 200812 1 004	
...........................
				
2.	Pembimbing Pendamping	:	Ir. Deddy Kusbianto P., M.MKom.
NIP. 19621128 198811 1 001	
...........................
				
3.	Penguji Utama	:	Budi Harijanto, S.T., M.MKom.
NIP. 19620105 199003 1 002	
...........................
				
4.	Penguji Pendamping	:	Hendra Pradibta, SE., M.Sc
NIP. 19830521 200604 1 003	
...........................



Mengetahui,

Ketua Jurusan
Teknologi Informasi	Ketua Program Studi
Teknik Informatika





Rudy Ariyanto, S.T., M.Cs.	




Imam Fahrur Rozi, S.T., M.T.
NIP. 19711110 199903 1 002	NIP. 19840610 200812 1 004

 
PERNYATAAN
Dengan ini saya menyatakan bahwa pada Skripsi ini tidak terdapat karya, baik seluruh maupun sebagian, yang sudah pernah diajukan untuk memperoleh gelar akademik di Perguruan Tinggi manapun, dan sepanjang pengetahuan saya juga tidak terdapat karya atau pendapat yang pernah ditulis atau diterbitkan oleh orang lain, kecuali yang secara tertulis disitasi dalam naskah ini serta disebutkan dalam daftar sitasi/pustaka.


	Malang, 21 Juni 2021

Anggi Kartika P.
 
ABSTRAK
Kartika P., Anggi. “Pengembangan Aplikasi Manajemen Stok UMKM dengan Fitur Prediksi Penjualan Harian Menggunakan Metode Jaringan Syaraf Tiruan”. Pembimbing: (1) Rudy Ariyanto, S.T., M.Cs., (2) Yan Watequlis S.T., M.MT.

Skripsi, Program Studi Teknik Informatika, Jurusan Teknologi Informasi, Politeknik Negeri Malang, 2020.

Pada proses bisnis UMKM di Indonesia, umumnya masih belum menerapkan manajemen stok berdasarkan prediksi data penjualan. Artinya dari segi pencatatan masih bersifat Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi.
Oleh karena itu, perlu adanya Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi.

Kata Kunci : Sistem Informasi, Jaringan Syaraf Tiruan, UMKM

 
ABSTRACT
Kartika P., Anggi. “The Development of Stock Management Application for Small Businesses with Selling Prediction Feature using Artificial Neural Network Methodology”. Supervisor: Rudy Ariyanto, S.T., M.Cs., Co–Supervisor: Yan Watequlis S.T., M.MT.

Thesis, Informatics Management Study Program, Department of Information Technology, State Polytechnic of Malang, 2020.

As we might already know, the business process of small business in Indonesia, in general, have not implement selling data prediction based stock management. It means that the data recording process still having Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi.
Due to the given fact, it undoubtedly needed a kind of Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi. Lorem ipsum dolor sit amet. A quick brown fox jumps over a lazy frog. Kerjakan segera apa yang bisa dikerjakan hari ini, termasuk skripsi.
 
Keywords:	Information System, Artificial Neural Network, Small Business

 
KATA PENGANTAR
Puji Syukur kami panjatkan kehadirat Allah SWT/Tuhan YME atas segala rahmat dan hidayah-Nya penulis dapat menyelesaikan skripsi dengan judul “PENGEMBANGAN APLIKASI MANAJEMEN STOK UMKM DENGAN FITUR PREDIKSI PENJUALAN HARIAN MENGGUNAKAN METODE JARINGAN SYARAF TIRUAN”. Skripsi ini penulis susun sebagai persyaratan untuk menyelesaikan studi program Diploma IV Program Studi Teknik Informatika, Jurusan Teknologi Informasi, Politeknik Negeri Malang.
Kami menyadari bahwasannya dengan tanpa adanya dukungan dan kerja sama dari berbagai pihak, kegiatan laporan akhir ini tidak akan dapat berjalan baik. Untuk itu, kami ingin menyampaikan rasa terima kasih kepada:
1.	Bapak Rudy Ariyanto, ST., M.Cs., selaku Ketua Jurusan Teknologi Informasi
2.	Bapak Imam Fahrur Rozi, ST., MT., selaku Ketua Program Studi DIV Teknik Informatika
3.	........
4.	Dan seluruh pihak yang telah membantu dan mendukung lancarnya  pembuatan Laporan Akhir dari awal hingga akhir yang tidak dapat kami sebutkan satu persatu.
Penulis menyadari bahwa dalam penyusunan laporan akhir ini, masih banyak terdapat kekurangan dan kelemahan yang dimiliki penulis baik itu sistematika penulisan maupun penggunaan bahasa. Untuk itu penulis mengharapkan saran dan kritik dari berbagai pihak yang bersifat membangun demi penyempurnaan laporan ini. Semoga laporan ini berguna bagi pembaca secara umum dan penulis secara khusus. Akhir kata, penulis ucapkan banyak terima kasih.

Malang, 21 Juni 2021


Penulis
 
DAFTAR ISI
Halaman
SAMPUL DEPAN	i
HALAMAN JUDUL	ii
HALAMAN PENGESAHAN	iii
HALAMAN PERNYATAAN	iv
ABSTRAK	vi
ABSTRACT	vii
KATA PENGANTAR	viii
DAFTAR ISI	ix
DAFTAR GAMBAR	xi
DAFTAR TABEL	xii
DAFTAR LAMPIRAN	xiii
BAB I.	PENDAHULUAN	1
1.1	.	1
1.2	.	2
1.3	.	3
1.4	.	3
1.5	.	4
BAB II.	LANDASAN TEORI	5
2.1		5
2.2		5
BAB III.	METODOLOGI PENELITIAN	6
3.1		8
3.2		10
BAB IV.	ANALISIS DAN PERANCANGAN SISTEM	13
4.1	.	20
4.2	.	23
4.3	.	24
4.4	.	25 
BAB V.	IMPLEMENTASI DAN PENGUJIAN	26
5.1	.	28
5.2	.	30 
5.3	.	34 
5.4	.	35
5.5	.	40
BAB VI.	HASIL DAN PEMBAHASAN	42
6.1		42
6.2		49
BAB VII.	KESIMPULAN DAN SARAN	50
7.1		58
7.2		58
DAFTAR PUSTAKA	63
LAMPIRAN-LAMPIRAN	35
 
DAFTAR GAMBAR
Halaman 
Gambar 2.1	Statistik Institusi	16 
Gambar 2.2	Struktur Organisasi	18 
Gambar 3.1	Waterfall Model	19 
Gambar 3.2	Desain Input	22 
Gambar 3.3	Desain Output	28 
Gambar 3.4	Antarmuka Utama	36 
Gambar 3.5	Laporan Data Pegawai	46

 
DAFTAR TABEL
Halaman 
Tabel 2.1	Data Penjualan Barang Selama Setahun	24
Tabel 2.2	Tugas dan Wewenang Tiap Unit Kerja	25
Tabel 3.3	Fungsi-fungsi/ Unit-unit Pada Delphi Yang Digunakan	35
Tabel 4.1	Peralatan Yang Diperlukan	49

 
DAFTAR LAMPIRAN
Lampiran 1	Menu Utama Aplikasi
Lampiran 2	Keluaran Sistem
Lampiran 3	Kuesioner Uji Pengguna
Lampiran 4	Listing Program
 
BAB I. PENDAHULUAN

1.1	Latar Belakang
Pasar saham Indonesia (Bursa Efek Indonesia/BEI) merupakan salah satu pasar keuangan yang dinamis dan terus berkembang, dengan lebih dari 600 emiten yang terdaftar hingga tahun 2025. Dinamika pergerakan harga saham di BEI tidak hanya dipengaruhi oleh faktor fundamental masing-masing perusahaan, tetapi juga oleh interaksi kompleks antar saham yang membentuk jaringan ketergantungan. Interaksi ini menjadi semakin kritis ketika pasar mengalami guncangan (shock), di mana penurunan tajam pada satu saham dapat merambat ke saham-saham lain yang memiliki korelasi tinggi, menciptakan efek domino yang dikenal sebagai contagion risk (risiko penularan) (Diebold & Yilmaz, 2014).  
Fenomena contagion risk telah terbukti nyata dalam berbagai krisis keuangan. Krisis keuangan global 2008 dan pandemi COVID-19 pada awal 2020 menunjukkan bagaimana guncangan pada sektor tertentu, seperti perbankan pada 2008 atau sektor pariwisata dan transportasi pada 2020, dapat menyebar dengan cepat ke seluruh pasar. Di Indonesia, peristiwa seperti kenaikan suku bunga The Fed, fluktuasi harga komoditas global, dan kebijakan domestik telah berulang kali memicu aksi jual massal yang menyebar lintas sektor (Mantegna, 1999). Dalam konteks ini, pemahaman mendalam tentang bagaimana risiko menyebar antar saham menjadi sangat penting bagi investor, regulator, dan pengambil kebijakan.  
Pendekatan tradisional dalam mengukur risiko sistemik umumnya mengandalkan model ekonometrik seperti Vector Autoregression (VAR), GARCH, atau analisis korelasi statis. Namun, pendekatan ini memiliki keterbatasan fundamental: mereka tidak secara eksplisit memodelkan struktur jaringan ketergantungan antar aset dan tidak mampu menangkap perubahan dinamis dalam hubungan antar saham (Diebold & Yilmaz, 2014). Padahal, pasar saham secara inheren merupakan sistem yang saling terhubung, di mana perilaku satu entitas dipengaruhi oleh dan mempengaruhi entitas lain melalui jaringan yang kompleks.  
Korelasi statis, misalnya korelasi Pearson sepanjang periode, mengasumsikan hubungan antar saham konstan. Asumsi ini gagal saat krisis: korelasi justru melonjak ketika diversifikasi paling dibutuhkan. Model Constant Conditional Correlation (CCC) memang mengukur korelasi kondisional terhadap volatilitas, tetapi korelasinya masih dianggap statis sepanjang periode studi. Oleh karena itu, diperlukan pendekatan korelasi dinamis yang mampu menyesuaikan diri terhadap perubahan volatilitas dan rezim pasar. Dynamic Conditional Correlation (DCC-GARCH) yang diperkenalkan oleh Engle (2002) memodelkan korelasi kondisional dari residual terstandarisasi model GARCH univariat, sehingga korelasi dapat berubah setiap waktu dan menangkap lonjakan korelasi saat guncangan. Dengan demikian, DCC-GARCH lebih sesuai digunakan sebagai dasar konstruksi graf korelasi dinamis antar saham dibandingkan korelasi statis.  
Perkembangan terkini dalam bidang pembelajaran mesin, khususnya Graph Neural Network (GNN), membuka peluang baru untuk memodelkan data yang memiliki struktur graf. GNN telah menunjukkan kinerja yang luar biasa dalam berbagai aplikasi mulai dari sistem rekomendasi, analisis jejaring sosial, hingga prediksi properti molekuler (Veličković et al., 2018; Hamilton et al., 2017). Keunggulan utama GNN terletak pada kemampuannya untuk belajar representasi node dengan mempertimbangkan informasi dari tetangga-tetangganya dalam graf, sehingga memungkinkan penangkapan pola ketergantungan yang kompleks dan non-linear.  
Dalam konteks pasar saham, GNN dapat digunakan untuk memodelkan pasar sebagai graf dinamis di mana setiap saham direpresentasikan sebagai node dan korelasi dinamis antar saham sebagai edge dengan bobot tertentu. Korelasi dinamis tersebut diestimasi menggunakan DCC-GARCH, lalu digunakan untuk membangun graf pada setiap periode rolling window. Dengan pendekatan ini, GNN dapat mempelajari bagaimana guncangan pada satu node menyebar melalui jaringan, memungkinkan prediksi contagion risk yang lebih akurat dibandingkan metode konvensional (Sawhney et al., 2020). Kemampuan GNN untuk mengintegrasikan berbagai fitur node seperti return historis, volume perdagangan, kapitalisasi pasar, dan ukuran sentralitas menjadikannya alat yang powerful untuk analisis risiko sistemik.  
Penelitian ini bertujuan untuk membangun model analisis contagion risk di pasar saham Indonesia menggunakan Graph Neural Network dengan graf korelasi dinamis antar saham berbasis DCC-GARCH. Dengan memodelkan pasar sebagai graf dinamis yang diperbarui secara berkala menggunakan rolling window, penelitian ini berupaya menangkap perubahan struktur jaringan pada periode normal versus periode krisis. Lebih lanjut, penelitian ini akan mengidentifikasi saham-saham yang berperan sebagai "superspreader" risiko sistemik melalui analisis sentralitas jaringan dan attention weights dari model GNN.  
Kontribusi utama dari penelitian ini mencakup: (1) aplikasi dynamic graph dengan korelasi dinamis DCC-GARCH untuk memodelkan korelasi yang berubah sepanjang waktu di pasar Indonesia, yang belum banyak dilakukan dalam literatur yang ada; (2) identifikasi kuantitatif saham-saham dengan kepentingan sistemik tinggi menggunakan GNN. Hasil penelitian ini diharapkan dapat memberikan wawasan baru bagi investor dalam mengelola risiko portofolio, serta bagi regulator dalam memantau stabilitas sistem keuangan.
1.2	Rumusan Masalah
Berdasarkan latar belakang yang dijelaskan, maka rumusan masalah dalam penelitian ini adalah:
1.	Bagaimana membangun graf korelasi dinamis antar saham di BEI menggunakan DCC-GARCH dengan skema rolling window?
2.	Seberapa efektif Graph Neural Network (GraphSAGE dan GAT) dalam memprediksi penyebaran volatilitas (contagion) antar saham dibandingkan metode konvensional non-graf?
3.	aham mana yang berperan sebagai "superspreader" risiko sistemik di pasar Indonesia berdasarkan metrik sentralitas jaringan dan attention weights model GAT?
1.3	Batasan Masalah
Untuk menjaga fokus dan kelayakan penelitian, batasan masalah ditetapkan sebagai berikut: 
1.	Cakupan Data: Penelitian ini menggunakan data return harian saham yang terdaftar di Bursa Efek Indonesia (BEI) pada periode 2010–2025. Saham yang dianalisis dibatasi pada saham-saham yang aktif diperdagangkan secara konsisten.
2.	Metode Korelasi Dinamis: Korelasi dinamis antar saham diestimasi menggunakan DCC-GARCH. Matriks korelasi kondisional yang dihasilkan digunakan sebagai bobot edge graf. Threshold filtering, top-k correlation, dan/atau Minimum Spanning Tree (MST) digunakan sebagai mekanisme penyaringan graf, bukan sebagai metode korelasi alternatif.
3.	Arsitektur GNN: Model Graph Neural Network yang digunakan dibatasi pada GraphSAGE dan Graph Attention Network (GAT) dengan dua lapisan konvolusi graf.
4.	Target Prediksi: Fokus prediksi adalah klasifikasi biner untuk mendeteksi volatility spike (lonjakan volatilitas) dan perhitungan contagion score, bukan prediksi harga saham secara langsung. Volatility spike didefinisikan sebagai kondisi ketika volatilitas return harian melewati persentil tertentu (misalnya persentil 90) dalam rolling window tertentu. Contagion score dihitung dari probabilitas prediksi GNN dan/atau ukuran spillover berbasis korelasi dinamis, dan dirinci pada Bab III.
5.	Metode pembanding: metode konvensional yang digunakan sebagai pembanding dibatasi pada model klasifikasi non-graf yang relevan, seperti regresi logistik, SVM, atau Random Forest, dan dirinci pada Bab III.
6.	Definisi operasional superspreader: saham yang berperan sebagai superspreader diidentifikasi berdasarkan nilai sentralitas jaringan, yaitu degree centrality dan/atau betweenness centrality, serta attention weights dari model GAT.
7.	Analisis periode krisis: analisis perubahan topologi jaringan pada periode krisis COVID-19, yaitu Februari–Desember 2020, digunakan sebagai analisis pendukung untuk membaca dinamika penyebaran risiko, bukan sebagai rumusan masalah atau tujuan utama penelitian.
8.	Interpretabilitas: interpretasi model dibatasi pada attention weights dari GAT dan ukuran sentralitas jaringan.
1.4	Tujuan
Untuk menjaga fokus dan kelayakan penelitian, batasan masalah ditetapkan sebagai berikut: 
1.	Membangun graf korelasi dinamis antar saham BEI menggunakan DCC-GARCH dengan skema rolling window.
2.	Mengimplementasikan Graph Neural Network (GraphSAGE dan GAT) untuk prediksi contagion risk di pasar saham Indonesia dan membandingkan kinerjanya dengan metode konvensional.
3.	Mengidentifikasi saham-saham dengan sentralitas tinggi (systemic importance) yang berpotensi menjadi "superspreader" risiko sistemik melalui analisis metrik sentralitas jaringan.
1.5	Manfaat
•	Manfaat akademis: memperkaya literatur penerapan GNN dan dynamic graph untuk analisis contagion risk di pasar saham Indonesia.
•	Manfaat praktis bagi investor: membantu memahami pola penyebaran risiko antar saham sehingga dapat digunakan sebagai pertimbangan dalam pengelolaan risiko portofolio.
•	Manfaat bagi regulator: memberikan alternatif alat analisis untuk memantau saham-saham dengan kepentingan sistemik tinggi yang berpotensi menjadi superspreader.
•	Manfaat metodologis: menunjukkan bagaimana korelasi dinamis dan struktur jaringan dapat diintegrasikan dalam model pembelajaran mesin berbasis graf untuk analisis risiko sistemik.






Tentu! Sesuai permintaan Anda, kita akan membedah setiap elemen judul ini secara mendalam dengan format **apa itu** dan **mengapa dipilih (disertai alasannya dibanding pendekatan alternatif)**, persis seperti analogi DCC-GARCH dan GNN yang Anda sebutkan.

Berikut adalah detail lengkap per variabel dan kata dalam judul penelitian Anda:

---

### 1. CONTAGION RISK (Risiko Penularan)

* **Penjelasan:** Fenomena di mana guncangan, kepanikan, atau penurunan harga yang terjadi pada satu emiten/sektor dengan cepat menjalar dan menularkan tekanan ke emiten/sektor lainnya di pasar keuangan.
* **Kenapa menggunakan ini?** Karena krisis di pasar keuangan modern tidak pernah terjadi secara terisolasi. Dengan fokus pada *contagion risk*, penelitian Anda tidak hanya melihat "seberapa besar risiko suatu saham", tetapi **"bagaimana risiko itu menular dan memicu efek domino"**. Ini sangat krusial untuk mitigasi risiko sistemik.
* **Pembandingnya:** Analisis risiko individual (seperti *Value at Risk* / VaR atau GARCH univariat standar) yang hanya menghitung risiko masing-masing saham secara terpisah tanpa peduli apakah saham tersebut menularkan masalah ke saham lain atau tidak.

### 2. PASAR SAHAM INDONESIA

* **Penjelasan:** Objek empiris penelitian yang mencakup emiten-emiten yang terdaftar di Bursa Efek Indonesia (BEI), misalnya saham-saham likuid seperti LQ45 atau IDX80.
* **Kenapa menggunakan ini?** Pasar saham Indonesia (*emerging market*) memiliki karakteristik unik: sangat sensitif terhadap sentimen global, aliran modal asing (*capital flows*), serta didominasi oleh beberapa saham penggerak (*heavyweights*). Dinamika penularan krisis di pasar berkembang sering kali jauh lebih liar dan cepat dibanding pasar maju.
* **Pembandingnya:** Pasar saham negara maju (seperti S&P 500 di AS atau bursa Eropa) yang memiliki likuiditas lebih dalam, struktur pasar lebih matang, dan pola penularan yang berbeda.

### 3. DCC-GARCH *(Dynamic Conditional Correlation - Generalized Autoregressive Conditional Heteroskedasticity)*

* **Penjelasan:** Model ekonometrika keuangan multivariat yang digunakan untuk mengestimasi volatilitas sekaligus korelasi antar aset yang berubah-ubah seiring waktu (*time-varying*).
* **Kenapa menggunakan ini?** Karena di dunia nyata, hubungan (korelasi) antar saham **tidak pernah konstan**. Saat pasar normal, korelasi antar saham mungkin rendah; namun saat terjadi krisis, korelasi mendadak melonjak drastis (kepanikan massal). DCC-GARCH mampu menangkap dinamika perubahan korelasi real-time ini secara akurat.
* **Pembandingnya:** Korelasi statis konvensional (seperti korelasi Pearson atau Spearman sepanjang periode penelitian). Korelasi statis menganggap hubungan antar saham dari awal tahun hingga akhir tahun adalah angka yang sama, yang mana sangat tidak realistis dan gagal menangkap kepanikan pasar saat krisis terjadi.

### 4. GRAF KORELASI DINAMIS ANTAR SAHAM

* **Penjelasan:** Bentuk representasi data di mana setiap saham direpresentasikan sebagai titik (*node*) dan kekuatan korelasi antar saham (hasil hitungan DCC-GARCH) direpresentasikan sebagai garis penghubung (*edge*) yang bentuk serta bobotnya berubah setiap periode waktu.
* **Kenapa menggunakan ini?** Karena angka-angka matriks korelasi yang dihasilkan DCC-GARCH jika dibiarkan berbentuk tabel mentah akan sangat sulit dianalisis. Mengubahnya menjadi "Graf Dinamis" memungkinkan kita melihat peta jaringan pasar yang hidup—menunjukkan emiten mana yang sedang menjadi pusat penularan (*hub*) dari waktu ke waktu.
* **Pembandingnya:** Matriks tabel angka konvensional (seperti *matrix correlation table* di Excel) yang statis, tidak bisa divisualisasikan sebagai jaringan, dan menyulitkan pembacaan pola interaksi antar banyak emiten sekaligus.

### 5. GRAPH NEURAL NETWORK / GNN

* **Penjelasan:** Cabang dari *Deep Learning* yang dirancang khusus untuk memproses data yang terstruktur dalam bentuk jaringan atau graf (*nodes* dan *edges*).
* **Kenapa menggunakan ini?** Seperti yang Anda katakan: **kita tidak fokus untuk menganalisis satu entitas secara terisolasi, melainkan fokus pada persebaran/penjalaran (spread/propagation), dan GNN memiliki kerangka kerja yang memang diciptakan untuk itu**. GNN dapat membaca bagaimana sebuah guncangan mengalir dari satu *node* ke *node* tetangga melalui *edges* (korelasi dinamis), sesuatu yang tidak bisa dilakukan oleh AI biasa.
* **Pembandingnya:** *Deep Learning* sekuensial standar seperti LSTM, GRU, atau *Transformer* univariat. Model-model tersebut hanya memproses data historis harga saham secara terpisah per emiten (menganggap saham A dan saham B tidak saling terhubung secara spasial), sehingga gagal mendeteksi efek penularan jaringan (*contagion path*).

---

Dengan penjelasan detail di atas, narasi latar belakang (*background*) untuk proposal atau tesis Anda akan menjadi sangat kuat karena setiap kata dalam judul Anda memiliki alasan metodologis yang saling mengunci secara logis!






Untuk memperkuat landasan teoretis dan metodologis proposal atau tesis Anda, daftar pustaka perlu dibagi menjadi beberapa klaster utama. Klaster ini merentang dari **ekonometrika keuangan klasik** (dasar DCC-GARCH), **teori jejaring risiko sistemik**, hingga **penerapan AI modern (*Graph Neural Network*)** pada analisis pasar keuangan.

Berikut adalah rujukan literatur wajib dan peta pustaka yang dapat Anda jadikan acuan utama:

---

### 1. Klaster Fondasi Ekonometrika & Volatilitas (DCC-GARCH)

Klaster ini digunakan untuk memperkuat bab metodologi terkait bagaimana korelasi dan volatilitas antar saham dihitung secara dinamis.

* **Engle, R. (2002).** *Dynamic Conditional Correlation: A Simple Class of Multivariate Generalized Autoregressive Conditional Heteroskedasticity Models*. **Journal of Business & Economic Statistics**, 20(3), 339-350.
* *Fungsi untuk Tesis Anda:* Ini adalah **paper wajib utama (foundational paper)** penemu metode DCC-GARCH. Menjadi rujukan utama ketika Anda menjelaskan rumus matematika pembentukan matriks korelasi kondisional yang berubah seiring waktu.


* **Bollerslev, T. (1986).** *Generalized Autoregressive Conditional Heteroskedasticity*. **Journal of Econometrics**, 31(3), 307-327.
* *Fungsi untuk Tesis Anda:* Landasan historis model GARCH univariat yang menjadi akar pengembangan model-model multivariat di bawahnya.



---

### 2. Klaster Teori Risiko Penularan (*Contagion Risk* & *Financial Networks*)

Klaster ini digunakan untuk membangun argumen di bab Pendahuluan/Tinjauan Pustaka mengenai mengapa guncangan pasar dapat menular dan bagaimana struktur jaringan finansial terbentuk.

* **Diebold, F. X., & Yilmaz, K. (2014).** *On the Network Topology of Variance Decompositions: Measuring the Connectedness of Financial Firms*. **Journal of Econometrics**, 182(1), 119-134.
* *Fungsi untuk Tesis Anda:* Literatur klasik yang mempopulerkan pendekatan berbasis jaringan (*network topology*) dalam melihat limpahan risiko (*spillover*) di pasar keuangan. Sangat bagus dijadikan pembanding atau landasan konseptual graf.


* **Allen, F., & Gale, D. (2000).** *Financial Contagion*. **Journal of Political Economy**, 108(1), 1-33.
* *Fungsi untuk Tesis Anda:* Landasan teoretis fundamental mengenai bagaimana kepanikan atau guncangan pada satu titik institusi/aset dapat memicu efek domino (*contagion*) ke seluruh sistem ekonomi.



---

### 3. Klaster *Graph Neural Network* (GNN) & AI dalam Keuangan

Klaster ini mendukung bagian metode *Deep Learning* Anda, menjelaskan mengapa GNN dipilih untuk membaca struktur graf dinamis daripada model AI konvensional.

* **Kipf, T. N., & Welling, M. (2017).** *Semi-Supervised Classification with Graph Convolutional Networks*. **Proceedings of International Conference on Learning Representations (ICLR)**.
* *Fungsi untuk Tesis Anda:* Paper rujukan utama untuk arsitektur *Graph Convolutional Networks* (GCN) yang sering menjadi fondasi dasar pemrosesan data spasial berbasis graf.


* **Studi Literatur Terkini (Recent Studies on GNN for Systemic Risk & Shock Propagation):**
* Cari jurnal-jurnal bereputasi (seperti *Expert Systems with Applications*, *Journal of Financial Stability*, atau *IEEE Transactions on Neural Networks and Learning Systems*) dengan kata kunci: **"Graph Neural Network for Systeming Risk Forecasting"** atau **"Dynamic Graph Neural Networks for Stock Market Shock Propagation"**.
* *Fungsi untuk Tesis Anda:* Menunjukkan bahwa penggunaan GNN dengan *dynamic edges* untuk pemodelan penjalaran krisis (*contagion*) adalah pendekatan *state-of-the-art* (mutakhir) di literatur riset keuangan global saat ini.



---

### 4. Klaster Kontekstual Pasar Saham Indonesia & *Emerging Markets*

Klaster ini digunakan untuk memperkuat bagian objek penelitian (*empirical setting*) di Bab Pendahuluan atau Metodologi.

* **Jurnal-jurnal Nasional Terakreditasi SINTA 1 / SINTA 2** atau **Jurnal Internasional Bereputasi (Scopus)** yang spesifik meneliti tentang:
* *Volatilitas Pasar Saham Indonesia* (misalnya dinamika indeks LQ45 atau IDX80).
* *Integration and Contagion in ASEAN / Emerging Equity Markets*.
* *Fungsi untuk Tesis Anda:* Memberikan justifikasi empiris mengenai karakteristik unik pasar saham Indonesia yang rentan terhadap guncangan eksternal maupun internal, sehingga analisis risiko penularan (*contagion risk*) menjadi sangat urgen untuk dilakukan.



---

### Tips Menyusun di Daftar Pustaka:

1. Pastikan proporsi literatur seimbang: **30% teori dasar ekonometrika (DCC-GARCH)**, **30% konsep risiko penularan/jaringan**, dan **40% penerapan teknologi terbaru (GNN dalam *finance*)**.
2. Usahakan mencari beberapa jurnal pendukung tambahan dari 3–5 tahun terakhir (2021–2026) untuk menunjukkan bahwa topik penggabungan DCC-GARCH dan GNN ini memang sedang menjadi tren riset global yang mutakhir.


Berikut adalah penjelasan rinci mengenai **fungsi spesifik** dari masing-masing 20 jurnal/literatur tersebut jika diaplikasikan ke dalam bab-bab tesis Anda (terutama pada Bab 1 Pendahuluan, Bab 2 Tinjauan Pustaka, dan Bab 3 Metodologi Penelitian):

---

### Klaster 1: Fondasi Ekonometrika & Model Volatilitas Multivariat (DCC-GARCH)

*Fungsi Utama: Digunakan di Bab Metodologi untuk membangun model matematis penghitungan korelasi dinamis antar saham.*

1. **Engle (2002) – *Dynamic Conditional Correlation***
* **Fungsi di Tesis:** Menjadi **rujukan utama (primary baseline)** untuk rumus matematika DCC-GARCH yang Anda gunakan untuk mengekstrak matriks korelasi waktu nyata (*time-varying*) antar saham di BEI.


2. **Bollerslev (1986) – *Generalized Autoregressive Conditional Heteroskedasticity***
* **Fungsi di Tesis:** Landasan teoretis awal untuk menjelaskan konsep volatilitas bersyarat (*conditional volatility*) univariat yang menjadi fondasi dasar sebelum dikembangkan ke model multivariat.


3. **Nelson (1991) – *EGARCH***
* **Fungsi di Tesis:** Digunakan untuk menjelaskan fenomena *asymmetry* atau efek *leverage* (pasar merespons berita buruk berbeda dengan berita baik) jika Anda ingin memperkaya spesifikasi model GARCH sebelum dimasukkan ke matriks korelasi.


4. **Engle & Kroner (1995) – *Multivariate Simultaneous GARCH***
* **Fungsi di Tesis:** Memberikan pembanding teoretis mengapa model multivariat kompleks seperti BEKK digunakan atau mengapa Anda memilih DCC-GARCH sebagai alternatif yang lebih efisien untuk jumlah saham yang banyak.


5. **Tse & Tsui (2002) – *Time-Varying Correlations***
* **Fungsi di Tesis:** Sebagai rujukan alternatif model korelasi dinamis berbasis bobot bergerak (*moving average*) untuk memperkuat argumen pemilihan spesifikasi DCC Anda.


6. **Baillie, Bollerslev, & Mikkelsen (1996) – *FIGARCH***
* **Fungsi di Tesis:** Mendukung argumen literatur mengenai memori jangka panjang (*long memory*) pada volatilitas aset keuangan.



---

### Klaster 2: Teori Risiko Penularan (*Contagion Risk*) & Topologi Jaringan Keuangan

*Fungsi Utama: Digunakan di Bab Pendahuluan & Tinjauan Pustaka untuk membangun argumen mengapa penjalaran krisis itu penting dan bagaimana struktur jaringan terbentuk.*

7. **Diebold & Yilmaz (2014) – *Network Topology of Variance Decompositions***
* **Fungsi di Tesis:** Sebagai pembanding metode jaringan konvensional berbasis *variance decomposition* (VAR) untuk menunjukkan bahwa pendekatan Anda (DCC-GARCH + GNN) menawarkan perspektif yang lebih mendalam secara non-linear.


8. **Diebold & Yilmaz (2009) – *Measuring Financial Asset Return and Volatility Spillovers***
* **Fungsi di Tesis:** Membangun definisi operasional mengenai *spillover* (limpahan risiko) antaraset yang menjadi indikator awal sebelum risiko berubah menjadi *contagion*.


9. **Allen & Gale (2000) – *Financial Contagion***
* **Fungsi di Tesis:** Landasan teoretis fundamental ekonomi makro/keuangan mengenai bagaimana guncangan di satu titik dapat memicu efek domino sistemik akibat keterhubungan jaringan.


10. **Forbes & Rigobon (2002) – *No Contagion, Only Interdependence***
* **Fungsi di Tesis:** Digunakan untuk membedakan secara akademis antara fenomena *interdependence* (ketergantungan normal) dan *contagion* (penularan krisis sejati yang ditandai lonjakan korelasi ekstrem).


11. **Billio et al. (2012) – *Systemic Risk and Connectedness***
* **Fungsi di Tesis:** Mendukung argumen pengukuran risiko sistemik menggunakan matriks keterhubungan (*connectedness measures*) antarlembaga atau aset keuangan.


12. **Corsetti, Pericoli, & Sbracia (2005) – *Pitfalls in Tests of Financial Contagion***
* **Fungsi di Tesis:** Digunakan sebagai tinjauan kritis dalam mendesain metodologi agar pengujian *contagion risk* Anda bebas dari bias kesalahan statistik akibat volatilitas pasar yang tinggi.



---

### Klaster 3: Graph Neural Networks (GNN) & Deep Learning dalam Keuangan

*Fungsi Utama: Digunakan di Bab Metodologi untuk menjustifikasi mengapa AI berbasis graf dipilih untuk membaca hubungan antar saham.*

13. **Kipf & Welling (2017) – *Graph Convolutional Networks (GCN)***

* **Fungsi di Tesis:** Menjadi **fondasi arsitektur AI utama** Anda dalam menjelaskan bagaimana lapisan konvolusi pada graf bekerja untuk menggabungkan informasi fitur saham dan tetangganya (*node embeddings*).

14. **Velickovic et al. (2018) – *Graph Attention Networks (GAT)***

* **Fungsi di Tesis:** Memberikan justifikasi jika Anda ingin menggunakan mekanisme perhatian (*attention mechanism*) untuk menentukan bobot korelasi mana yang paling krusial dalam penularan risiko.

15. **Wu et al. (2020) – *A Comprehensive Survey on Graph Neural Networks***

* **Fungsi di Tesis:** Digunakan dalam tinjauan pustaka untuk memetakan perkembangan GNN secara komprehensif dan memposisikan riset Anda pada ranah *financial network forecasting*.

16. **Hamilton, Ying, & Leskovec (2017) – *Inductive Representation Learning (GraphSAGE)***

* **Fungsi di Tesis:** Mendukung fleksibilitas model GNN Anda jika diterapkan untuk memprediksi struktur graf baru yang dinamis dari waktu ke waktu (*inductive learning*).

---

### Klaster 4: Dinamika Pasar Saham, Integrasi, & *Emerging Markets*

*Fungsi Utama: Digunakan di Bab Pendahuluan untuk memperkuat alasan mengapa objek penelitian adalah Pasar Saham Indonesia.*

17. **Bekaert & Harvey (1997) – *Emerging Equity Market Volatility***

* **Fungsi di Tesis:** Menjelaskan karakteristik khusus pasar berkembang (*emerging markets*), seperti volatilitas yang lebih tinggi dan sensitivitas terhadap guncangan eksternal.

18. **Claessens & Forbes (2001) – *International Financial Contagion***

* **Fungsi di Tesis:** Buku rujukan untuk memperkuat pemahaman mengenai bagaimana penularan keuangan menyebar lintas batas dan domestik.

19. **Levine & Zervos (1998) – *Stock Markets and Economic Growth***

* **Fungsi di Tesis:** Menjelaskan pentingnya likuiditas dan peran strategis pasar saham dalam perekonomian nasional.

20. **Phylaktis & Ravazzolo (2002) – *Financial and Monetary Integration***

* **Fungsi di Tesis:** Mendukung argumen mengenai bagaimana keterkaitan pasar keuangan domestik dengan dinamika global membentuk pola korelasi aset.



