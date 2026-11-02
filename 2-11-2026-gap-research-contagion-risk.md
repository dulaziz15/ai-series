# ANALISIS CONTAGION RISK PASAR SAHAM INDONESIA MENGGUNAKAN GRAPH NEURAL NETWORK DENGAN GRAF KORELASI DINAMIS ANTAR SAHAM BERBASIS DCC-GARCH

## 4. CCC-GARCH (Constant Conditional Correlation)

Model ini adalah "tolok ukur dasar" (*baseline model*) di mana korelasi antar-aset dianggap konstan sepanjang waktu pengamatan.
- **Kenapa harus dibandingkan:** Untuk membuktikan secara empiris bahwa korelasi antar-negara atau pasar memang bersifat dinamis dan berubah karena guncangan krisis, bukan sesuatu yang stabil sejak awal.
- **Cara Membandingkannya:** Lakukan uji formal seperti *Engle and Sheppard Test for Dynamic Correlation*. Jika pengujian menolak hipotesis CCC-GARCH, maka penggunaan DCC-GARCH Anda terjustifikasi secara ilmiah bahwa korelasi di pasar tersebut memang bergerak dinamis.

[Link Referensi Google](https://www.google.com/goto?url=CAESfwHrOzAVO3T95AvSnNZV1IbAqXew7nSJDOWcD0eI0S_uRiQvaHvJyrq-Gcv6PzWvRfkNw4STmM8boOCiTAu5pAtoFBIxZ6yh74yzTpcMAOVxk2Ng0J42YaXBoUoh4Py8HjlcA-84_8rpJc4E3r_hnuUNYwyWtyXerncC-6Y5wFM)

---

## Terkait Judul

1. Menggunakan **GNN** atau langsung spesifik varian GNN seperti **DGCN** atau **T-GCN**?
2. Perubahan yang awal hanya *mention* korelasi dinamis diubah menjadi korelasi dinamis berbasis **DCC-GARCH**, lebih baik spesifik atau hanya korelasi dinamis?

---

## Struktur Direktori Proyek

```text
penelitian-gnn-saham/
│
├── README.md                  # Dokumentasi utama (cara menjalankan kode, dependensi)
├── requirements.txt           # Daftar library Python (PyG/DGL, PyTorch, Pandas, dll.)
│
├── data/                      # PUSAT DATASET (Jangan pernah diubah manual)
│   ├── raw/                   # Data mentah 25 tahun dari BEI (CSV/Excel per emiten)
│   ├── processed/             # Data bersih setelah handling missing value & alignment
│   └── graphs/                # Struktur matriks graf/adjacency per window yang sudah jadi
│
├── src/                       # SOURCE CODE UTAMA (Modular & Reusable)
│   ├── __init__.py
│   ├── data_loader.py         # Skrip untuk membaca data & memotong berdasarkan rolling window
│   ├── graph_builder.py       # Skrip membuat matriks korelasi/fundamental jadi objek graf
│   ├── models/                # Arsitektur Model GNN
│   │   ├── __init__.py
│   │   ├── gcn.py             # Baseline Model 1 (GCN)
│   │   └── gat.py             # Baseline Model 2 / Propose Model (GAT)
│   └── utils.py               # Fungsi pembantu (kalkulasi metrics: MSE, MAE, Sharpe Ratio)
│
├── experiments/               # RIWAYAT EKSPERIMEN & RUNNING CODE
│   ├── config/                # File konfigurasi parameter (YAML/JSON)
│   │   ├── config_w5_t1.yaml  # Konfigurasi misal: Window 5 thn, Test 1 thn
│   │   └── config_w3_t1.yaml
│   ├── train_rolling.py       # Skrip utama untuk menjalankan loop rolling window 25 tahun
│   └── evaluate.py            # Skrip untuk agregasi hasil seluruh window
│
└── output/                    # OUTPUT EKSPERIMEN (Automated Generation)
    ├── checkpoints/           # Bobot model (.pth) yang disimpan per window
    │   └── exp_run_01/
    │       ├── window_1_model.pth
    │       └── window_2_model.pth
    ├── logs/                  # Catatan training (Loss, Akurasi) per epoch & window
    │   └── exp_run_01_train.log
    └── results/               # Hasil akhir evaluasi untuk visualisasi / isi bab 4
        └── exp_run_01/
            ├── predictions_all_windows.csv  # Prediksi harga/return kumulatif 25 thn
            ├── metrics_summary.json         # Ringkasan MAE, RMSE, R-Square per window
            └── plots/                       # Grafik hasil backtesting (Return vs Aktual)
