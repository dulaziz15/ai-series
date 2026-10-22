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






