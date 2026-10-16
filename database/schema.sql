-- ==========================================================
-- SKEMA BASIS DATA: SIP-KTM (Sistem Informasi Pendataan KTM)
-- Mata Kuliah : Rekayasa Perangkat Lunak (D3 Teknik Komputer)
-- Penyusun    : Yusuf Rizal Indrianto (240104013)
-- ==========================================================

CREATE DATABASE IF NOT EXISTS db_sip_ktm;
USE db_sip_ktm;

-- 1. Tabel Mahasiswa
CREATE TABLE IF NOT EXISTS mahasiswa (
    nim VARCHAR(15) PRIMARY KEY,
    nama_lengkap VARCHAR(100) NOT NULL,
    prodi VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    no_hp VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabel Pengajuan KTM
CREATE TABLE IF NOT EXISTS pengajuan_ktm (
    id_pengajuan INT AUTO_INCREMENT PRIMARY KEY,
    no_tiket VARCHAR(20) NOT NULL UNIQUE,
    nim VARCHAR(15) NOT NULL,
    jenis_pengajuan ENUM('baru', 'hilang', 'rusak') NOT NULL,
    alasan TEXT,
    file_foto VARCHAR(255) NOT NULL,
    file_surat_kehilangan VARCHAR(255) NULL,
    biaya_admin DECIMAL(10,2) DEFAULT 0.00,
    status_pengajuan ENUM('menunggu_verifikasi', 'disetujui', 'proses_cetak', 'siap_diambil', 'selesai', 'ditolak') DEFAULT 'menunggu_verifikasi',
    tgl_pengajuan TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tgl_selesai TIMESTAMP NULL,
    catatan_admin TEXT NULL,
    CONSTRAINT fk_mahasiswa_pengajuan FOREIGN KEY (nim) REFERENCES mahasiswa(nim) ON DELETE CASCADE
);

-- 3. Tabel Riwayat Status (Log Tracking)
CREATE TABLE IF NOT EXISTS log_status_pengajuan (
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    no_tiket VARCHAR(20) NOT NULL,
    status_sebelumnya VARCHAR(30),
    status_terbaru VARCHAR(30) NOT NULL,
    keterangan TEXT,
    diubah_oleh VARCHAR(50) DEFAULT 'Petugas BAAK',
    waktu_perubahan TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_pengajuan_log FOREIGN KEY (no_tiket) REFERENCES pengajuan_ktm(no_tiket) ON DELETE CASCADE
);

-- Insert Sample Data
INSERT INTO mahasiswa (nim, nama_lengkap, prodi, email, no_hp)
VALUES 
('240104013', 'Yusuf Rizal Indrianto', 'D3 Teknik Komputer', '240104013@mhs.udb.ac.id', '081234567890'),
('240104088', 'Ahmad Fauzi', 'D3 Teknik Komputer', 'fauzi@mhs.udb.ac.id', '085712345678')
ON DUPLICATE KEY UPDATE nama_lengkap=VALUES(nama_lengkap);

INSERT INTO pengajuan_ktm (no_tiket, nim, jenis_pengajuan, alasan, file_foto, biaya_admin, status_pengajuan)
VALUES 
('KTM-202610-101', '240104013', 'baru', 'Penerbitan kartu mahasiswa baru TA 2026/2027', 'uploads/foto_240104013.jpg', 0.00, 'siap_diambil'),
('KTM-202610-102', '240104088', 'hilang', 'Dompet hilang di area parkir', 'uploads/foto_240104088.jpg', 50000.00, 'proses_cetak')
ON DUPLICATE KEY UPDATE no_tiket=VALUES(no_tiket);
