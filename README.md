# 🎮 Game Quiz Matematika Interaktif – Edukasi Anak SD dengan Pygame

**Game Matematika** adalah aplikasi edukasi interaktif berbasis **Pygame** yang dirancang untuk melatih kemampuan berhitung anak-anak Sekolah Dasar. Pemain akan mengerjakan soal matematika sesuai tingkat kesulitan, dengan sistem skor dan leaderboard untuk meningkatkan motivasi belajar.

## 📌 Fitur Utama

* ✅ **Tiga tingkat kesulitan**: Mudah, Sedang, dan Sulit
* ✅ **Soal interaktif**: Penjumlahan, Pengurangan, Perkalian, dan Pembagian
* ✅ **Tampilan fullscreen** yang ramah anak
* ✅ **Input nama pemain dan penyimpanan skor terbaik**
* ✅ **Leaderboard lokal (Top 3) per level**
* ✅ **Penyimpanan skor lokal dalam file `JSON`**

## 🖼️ Tampilan Antarmuka

* Layar sambutan dengan tombol **"Mulai"**
* Menu pemilihan level permainan
* Tampilan soal dan input jawaban langsung
* Indikator skor, soal ke-, dan status jawaban
* Leaderboard real-time di sisi kiri layar

## 📸 Cuplikan Tampilan

![Screenshot Game](assets/Screenshot%202025-07-01%20205758.png)

## 🧮 Contoh Soal Berdasarkan Level

| Level  | Operasi                      | Rentang Angka |
| ------ | ---------------------------- | ------------- |
| Mudah  | Penjumlahan, Pengurangan     | 1 – 10        |
| Sedang | +, -, ×                      | 2 – 10        |
| Sulit  | +, -, ×, ÷ (pembagian tepat) | 1 – 20        |

## 🗂️ Struktur File

```
.
├── main.py           # File utama program
├── history.json      # File riwayat skor (otomatis dibuat)
└── README.md         # Dokumentasi proyek
```

## 🚀 Cara Menjalankan

### 1. Pastikan Python dan Pygame sudah terpasang:

```bash
pip install pygame
```

### 2. Jalankan program:

```bash
python main.py
```

Program akan berjalan dalam mode **fullscreen**.

## 💾 Penyimpanan Skor

* Setiap skor akan disimpan ke dalam file `history.json`.
* Jika pemain menggunakan **nama dan level yang sama**, hanya **skor tertinggi** yang akan disimpan.

## 🏆 Leaderboard

* Ditampilkan selama permainan di sisi kiri layar.
* Warna peringkat:

  * 🥇 Emas – Peringkat 1
  * 🥈 Perak – Peringkat 2
  * 🥉 Perunggu – Peringkat 3

## 👦 Untuk Siapa Game Ini?

Cocok digunakan oleh:

* Anak-anak usia Sekolah Dasar
* Guru atau orang tua sebagai media latihan menyenangkan
* Siapa pun yang ingin bermain sambil mengasah matematika dasar

## 🛑 Keluar dari Game

* Tekan tombol **ESC** kapan saja untuk keluar dari permainan.
* Tersedia juga tombol **Kembali** dan **Keluar** di antarmuka.

## 📌 Catatan Tambahan

* Aplikasi berjalan dalam mode fullscreen. Gunakan `Alt + Tab` jika ingin berpindah aplikasi.
* Semua data disimpan secara **lokal** — **tidak ada koneksi internet** yang digunakan.
