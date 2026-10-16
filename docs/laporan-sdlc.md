# DOKUMENTASI PROYEK SIP-KTM

## 1. Identifikasi Masalah & Analisis Kebutuhan
- **Masalah:** Proses manual permohonan Kartu Tanda Mahasiswa di BAAK memicu antrean fisik, arsip hilang, dan tidak adanya transparansi progres cetak.
- **Tujuan:** Pendataan pengajuan KTM terpusat dan pelacakan status secara mandiri oleh mahasiswa.
- **Model SDLC:** Waterfall Model (Analisis Kebutuhan -> Desain Sistem -> Implementasi -> Pengujian -> Pemeliharaan).

## 2. Kebutuhan Fungsional (FR)
- **FR-01 (Must):** Pengisian formulir biodata (NIM, Nama, Prodi, No HP).
- **FR-02 (Must):** Penerbitan Nomor Tiket Pengajuan otomatis.
- **FR-03 (Must):** Kalkulasi otomatis biaya administrasi (Baru: Rp 0, Rusak: Rp 25.000, Hilang: Rp 50.000).
- **FR-04 (Must):** Pelacakan status pengajuan real-time menggunakan NIM/Tiket.
- **FR-05 (Should):** Daftar rekapitulasi antrean pengajuan untuk petugas BAAK.

## 3. Deployment & Tautan
- **GitHub Repository:** https://github.com/240104013-debug/UTS-RPL
- **Vercel Live URL:** https://sip-ktm-udb.vercel.app
