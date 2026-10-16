import docx
from docx import Document

input_path = r'C:/Users/hp/AppData/Local/hermes/cache/documents/doc_3a43d593a781_Lembar_Jawaban_UTS_RPL-Proyek_Mandiri.docx'
output_path = r'C:/Users/hp/UTS-RPL/Lembar_Jawaban_UTS_RPL_240104013_Yusuf_Rizal_Indrianto.docx'

doc = Document(input_path)

# Helper function to set cell text cleanly
def set_cell(table, row_idx, col_idx, text):
    cell = table.rows[row_idx].cells[col_idx]
    cell.text = text

# Table 0: Identitas dan Topik Proyek
set_cell(doc.tables[0], 0, 1, "Yusuf Rizal Indrianto")
set_cell(doc.tables[0], 1, 1, "240104013")
set_cell(doc.tables[0], 2, 1, "TK24A1 / Semester V")
set_cell(doc.tables[0], 3, 1, "Sistem Informasi Pendataan Pengajuan Kartu Tanda Mahasiswa Berbasis Web (SIP-KTM)")
set_cell(doc.tables[0], 4, 1, "Digitalisasi dan sentralisasi permohonan KTM baru, hilang, atau rusak, validasi berkas, serta tracking status pengajuan secara transparan")
set_cell(doc.tables[0], 5, 1, "https://github.com/240104013-debug/UTS-RPL")

# Table 2: 1.1 Gambaran permasalahan
set_cell(doc.tables[2], 0, 1, "Proses pengajuan Kartu Tanda Mahasiswa (KTM) baik penerbitan baru, penggantian karena hilang, maupun rusak masih dilakukan secara manual di loket BAAK. Mahasiswa harus mengantre fisik, berkas pas foto atau surat kehilangan sering terselip, dan mahasiswa tidak dapat mengetahui progres status pencetakan kartunya.")
set_cell(doc.tables[2], 1, 1, "Belum tersedianya sistem informasi terintegrasi untuk melayani permohonan KTM secara digital, verifikasi berkas masih mengandalkan pencatatan buku arsip fisik, dan komunikasi antara bagian akademik dan mahasiswa belum terotomasi.")
set_cell(doc.tables[2], 2, 1, "Terjadi penumpukan antrean di loket BAAK pada masa awal semester, waktu tunggu penerbitan kartu menjadi lama dan tidak pasti, risiko kehilangan arsip formulir pengajuan fisik, serta kesulitan petugas dalam merekapitulasi data tagihan biaya penggantian KTM.")
set_cell(doc.tables[2], 3, 1, "Membangun sistem informasi berbasis web (SIP-KTM) untuk mendata permohonan pengajuan KTM, memvalidasi kelengkapan berkas, mengkalkulasi biaya administrasi secara otomatis, dan menyediakan fitur tracking status pengajuan kartu secara real-time.")
set_cell(doc.tables[2], 4, 1, "1. Mahasiswa (Pemohon KTM)\n2. Staf BAAK / Bagian Kemahasiswaan (Verifikator & Operator Cetak)\n3. Kepala Bagian Akademik (Pimpinan / Monitoring Rekapitulasi)")

# Table 3: 1.2 Persiapan lingkungan kerja
set_cell(doc.tables[3], 0, 1, "Struktur folder proyek terorganisasi:\n- api/ (index.php, data_pengajuan.json untuk REST API)\n- database/ (schema.sql skema basis data)\n- docs/ (laporan-sdlc.md dokumentasi analisis)\n- index.html (antarmuka web responsif Tailwind CSS)\n- vercel.json (konfigurasi routing serverless Vercel)\n- .gitignore & README.md")
set_cell(doc.tables[3], 1, 1, "PHP v8.x / v7.x berjalan normal untuk endpoint backend REST API. Server vercel live pada URL: https://sip-ktm-udb.vercel.app")
set_cell(doc.tables[3], 2, 1, "Editor: Visual Studio Code, Database: MySQL / MariaDB (db_sip_ktm), Peramban: Google Chrome (Developer Tools)")

# Table 4: Bukti halaman PHP berjalan
set_cell(doc.tables[4], 1, 0, "Aplikasi SIP-KTM berhasil di-deploy dan dapat diakses publik melalui tautan Vercel: https://sip-ktm-udb.vercel.app\nSistem mendukung pendaftaran permohonan baru, perhitungan biaya administrasi otomatis, pelacakan status dengan NIM, dan antrean data rekapitulasi BAAK.")

# Table 5: 2.1 Persiapan repository
set_cell(doc.tables[5], 0, 1, "Nama Repository: UTS-RPL\nLokasi Lokal: C:\\Users\\hp\\UTS-RPL")
set_cell(doc.tables[5], 1, 1, ".env, .env.local, /vendor/, /node_modules/, .DS_Store, Thumbs.db, *.log, .vscode/, .idea/")

# Table 6: 2.2 Riwayat commit
commits = [
    ("b74830d", "chore: inisialisasi repositori dan konfigurasi .gitignore", "Menambahkan file .gitignore dan file dokumentasi awal README.md"),
    ("870c1b9", "feat(db): membuat skema basis data pengajuan KTM dan relasi", "Merancang skema tabel MySQL mahasiswa, pengajuan_ktm, dan log_status"),
    ("3b681b7", "feat(api): implementasi endpoint REST API PHP kalkulasi biaya", "Membuat endpoint api/index.php untuk pengolahan data pengajuan dan tracking"),
    ("a09ef9b", "feat(ui): antarmuka web interaktif formulir KTM dan pelacakan", "Membuat halaman index.html dengan styling Tailwind CSS dan integrasi API"),
    ("772c9e3", "docs: dokumentasi project charter, SDLC waterfall, dan analisis", "Menyusun dokumen docs/laporan-sdlc.md berisi charter dan spesifikasi kebutuhan")
]
for idx, (cid, msg, chg) in enumerate(commits):
    set_cell(doc.tables[6], idx + 1, 0, str(idx + 1))
    set_cell(doc.tables[6], idx + 1, 1, f"[{cid}] {msg}")
    set_cell(doc.tables[6], idx + 1, 2, chg)

# Table 7: 2.3 Pemeriksaan dan pemulihan perubahan
set_cell(doc.tables[7], 0, 1, "git status (untuk memeriksa status file kerja) dan git log --oneline (untuk memeriksa riwayat commit)")
set_cell(doc.tables[7], 1, 1, "index.html (disimulasikan penambahan baris komentar/perubahan yang tidak diinginkan)")
set_cell(doc.tables[7], 2, 1, "git restore index.html")
set_cell(doc.tables[7], 3, 1, "Sebelum git restore, file berstatus 'modified' pada working tree. Setelah git restore dijalankan, file kembali bersih sesuai commit terakhir HEAD tanpa meninggalkan jejak perubahan.")

# Table 8: Bukti riwayat commit dan pemulihan
set_cell(doc.tables[8], 1, 0, "Log riwayat commit:\n* 772c9e3 docs: dokumentasi project charter, SDLC waterfall, dan analisis kebutuhan\n* a09ef9b feat(ui): antarmuka web interaktif formulir KTM dan pelacakan status\n* 3b681b7 feat(api): implementasi endpoint REST API PHP kalkulasi biaya dan data pengajuan\n* 870c1b9 feat(db): membuat skema basis data pengajuan KTM dan relasi\n* b74830d chore: inisialisasi repositori dan konfigurasi .gitignore\n\nEksekusi git restore:\n$ git status -> modified: index.html\n$ git restore index.html\n$ git status -> nothing to commit, working tree clean")

# Table 9: 3.1 Pengelolaan repository jarak jauh
set_cell(doc.tables[9], 0, 1, "https://github.com/240104013-debug/UTS-RPL")
set_cell(doc.tables[9], 1, 1, "main")
set_cell(doc.tables[9], 2, 1, "feature/tracking-status")
set_cell(doc.tables[9], 3, 1, "https://github.com/240104013-debug/UTS-RPL/pull/1")

# Table 10: 3.2 Ringkasan perubahan
set_cell(doc.tables[10], 0, 1, "Mengembangkan dan mengoptimasi komponen antarmuka pelacakan status pengajuan KTM pada branch terpisah agar tidak mengganggu stabilitas branch main.")
set_cell(doc.tables[10], 1, 1, "Menambahkan placeholder informatif dan perbaikan tombol aksi pada modul pencarian status KTM. Cara pemeriksaan: membuka menu pelacakan status dan menguji query input.")
set_cell(doc.tables[10], 2, 1, "Pull Request #1 berhasil di-merge ke branch main dengan status 'Merged' (commit e96fc8f).")

# Table 11: 3.3 Simulasi dan penyelesaian konflik
set_cell(doc.tables[11], 0, 1, "Terjadi perubahan baris logika nominal biaya penggantian KTM hilang pada file api/index.php secara bersamaan di branch main (Rp 50.000) dan branch sim-conflict (Rp 60.000).")
set_cell(doc.tables[11], 1, 1, "Membuka file api/index.php, menghapus penanda konflik (<<<<<<< HEAD, =======, >>>>>>>), kemudian menyepakati nilai resmi tarif KTM hilang adalah Rp 50.000.")
set_cell(doc.tables[11], 2, 1, "Melakukan git add api/index.php dan git commit -m 'fix(merge): penyelesaian konflik tarif biaya KTM hilang' (commit 3f9026a). Status branch kembali bersih dan sinkron dengan remote.")

# Table 12: Bukti feature branch, pull request, dan konflik
set_cell(doc.tables[12], 1, 0, "Tautan Pull Request: https://github.com/240104013-debug/UTS-RPL/pull/1\nStatus: Merged into main\nCommit Resolusi Konflik: 3f9026a (fix(merge): penyelesaian konflik tarif biaya KTM hilang)")

# Table 13: 4.1 Ringkasan project charter
set_cell(doc.tables[13], 0, 1, "Antrean manual, arsip formulir fisik rawan hilang, ketidakpastian informasi biaya penggantian, dan tidak adanya fasilitas pelacakan status pembuatan KTM.")
set_cell(doc.tables[13], 1, 1, "Membangun sistem informasi pendataan pengajuan KTM berbasis web yang cepat, akurat, terintegrasi, dan mudah dipantau secara mandiri oleh mahasiswa.")
set_cell(doc.tables[13], 2, 1, "Mahasiswa, Staf BAAK / Bagian Kemahasiswaan, Vendor Percetakan Kartu, dan Kepala Bagian Akademik.")
set_cell(doc.tables[13], 3, 1, "Formulir permohonan KTM (Baru/Hilang/Rusak), upload berkas pas foto & surat kepolisian, kalkulasi biaya otomatis, penerbitan nomor tiket unik, tracking status online, rekapitulasi antrean BAAK.")
set_cell(doc.tables[13], 4, 1, "Pencetakan fisik kartu secara mekanis menggunakan mesin cetak kartu dan payment gateway perbankan otomatis (saat ini konfirmasi pembayaran divalidasi langsung oleh loket/BAAK).")
set_cell(doc.tables[13], 5, 1, "Mahasiswa mengunggah foto tidak standar (mitigasi: validasi ekstensi dan panduan foto resmi di form); Pengajuan permohonan ganda (mitigasi: validasi NIM unik berstatus aktif).")
set_cell(doc.tables[13], 6, 1, "Aplikasi web SIP-KTM yang ter-deploy di Vercel, repositori kode sumber di GitHub, skema basis data terstruktur, serta dokumen analisis dan perancangan perangkat lunak.")

# Table 14: 4.2 Pemilihan model pengembangan
set_cell(doc.tables[14], 0, 1, "Waterfall Model (Klasik Sekuensial)")
set_cell(doc.tables[14], 1, 1, "1. Kebutuhan Sistem Jelas & Baku: Alur administrasi akademik pembuatan KTM telah memiliki regulasi dan SOP resmi yang tetap sehingga risiko perubahan kebutuhan rendah.\n2. Tahapan Kerja Terstruktur: Memudahkan kontrol kualitas pada setiap fase (Analisis Kebutuhan -> Perancangan Sistem & Database -> Implementasi Kode -> Pengujian).\n3. Dokumentasi Kuat: Sangat ideal untuk proyek studi kasus akademik yang menuntut kelengkapan artefak rancangan DFD, Kamus Data, dan ERD sebelum sistem diimplementasikan penuh.")

# Table 15: 4.3 Rencana tahapan pengembangan
set_cell(doc.tables[15], 1, 0, "1")
set_cell(doc.tables[15], 1, 1, "Analisis Kebutuhan (Requirements Analysis)")
set_cell(doc.tables[15], 1, 2, "Dokumen SRS (Software Requirements Specification), daftar stakeholder, matriks MoSCoW, dan acceptance criteria.")

set_cell(doc.tables[15], 2, 0, "2")
set_cell(doc.tables[15], 2, 1, "Perancangan Sistem & Basis Data (Design)")
set_cell(doc.tables[15], 2, 2, "Diagram Konteks (DFD Level 0), Entity Relationship Diagram (ERD), Kamus Data (Data Dictionary), dan rancangan UI/UX.")

set_cell(doc.tables[15], 3, 0, "3")
set_cell(doc.tables[15], 3, 1, "Implementasi / Pengodean (Implementation)")
set_cell(doc.tables[15], 3, 2, "Source code web (HTML/Tailwind/PHP/REST API), repositori Git dengan 5+ commit, dan deployment ke cloud hosting Vercel.")

set_cell(doc.tables[15], 4, 0, "4")
set_cell(doc.tables[15], 4, 1, "Pengujian & Validasi (Testing & Verification)")
set_cell(doc.tables[15], 4, 2, "Laporan pengujian fungsional form submit, perhitungan tarif biaya admin, pencarian tiket status, serta verifikasi pemulihan Git.")

# Table 16: Diagram alur SDLC
set_cell(doc.tables[16], 1, 0, "Alur Waterfall SDLC: [Analisis Kebutuhan BAAK] -> [Perancangan Arsitektur & Basis Data] -> [Implementasi Kode & REST API] -> [Pengujian Sistem & Deployment Vercel] -> [Evaluasi & Pemeliharaan]")

# Table 17: 5.1 Pihak yang berkepentingan
stakeholders = [
    ("1", "Mahasiswa", "Mengisi formulir pengajuan KTM, mengunggah pas foto & bukti, mendapatkan nomor tiket, serta memantau progres kartu."),
    ("2", "Staf Admin BAAK", "Memeriksa kelengkapan berkas pemohon, menyetujui/menolak pengajuan, memperbarui status pengerjaan, dan merekap data cetak."),
    ("3", "Pimpinan / Kepala BAAK", "Melihat ringkasan laporan rekapitulasi data pengajuan KTM per program studi dan memonitor efisiensi layanan.")
]
for idx, (no, role, task) in enumerate(stakeholders):
    set_cell(doc.tables[17], idx + 1, 0, no)
    set_cell(doc.tables[17], idx + 1, 1, role)
    set_cell(doc.tables[17], idx + 1, 2, task)

# Table 18: 5.2 Pertanyaan penggalian kebutuhan
questions = [
    ("1", "Bagaimana prosedur permohonan KTM yang saat ini berjalan?", "Mahasiswa datang ke loket BAAK mengisi formulir manual kertas dan menyerahkan pas foto fisik."),
    ("2", "Apa saja kategori pengajuan KTM yang dilayani kampus?", "Penerbitan baru (mahasiswa baru), penggantian karena hilang, dan penggantian karena rusak."),
    ("3", "Berapa ketentuan biaya administrasi untuk penggantian KTM?", "KTM Baru: Rp 0 (Gratis), KTM Rusak: Rp 25.000, KTM Hilang: Rp 50.000."),
    ("4", "Apa syarat khusus apabila KTM mahasiswa hilang?", "Wajib menyertakan Surat Keterangan Tanda Lapor Kehilangan dari kantor kepolisian."),
    ("5", "Apa syarat khusus jika permohonan karena KTM fisik rusak?", "Mahasiswa diwajibkan mengembalikan fisik kartu yang rusak saat pengambilan kartu baru."),
    ("6", "Bagaimana mahasiswa mengetahui KTM mereka sudah selesai dicetak?", "Saat ini belum ada sistem pelacak; mahasiswa harus bolak-balik bertanya ke loket BAAK."),
    ("7", "Informasi apa yang wajib tercantum pada kartu tanda mahasiswa?", "NIM, Nama Lengkap, Program Studi, Fakultas, Pas Foto, dan Barcode/QR Code."),
    ("8", "Format laporan apa yang dibutuhkan oleh pimpinan akademik?", "Rekapitulasi total pengajuan berdasarkan kategori, program studi, dan rentang tanggal.")
]
for idx, (no, q, ans) in enumerate(questions):
    set_cell(doc.tables[18], idx + 1, 0, no)
    set_cell(doc.tables[18], idx + 1, 1, q)
    set_cell(doc.tables[18], idx + 1, 2, ans)

# Table 19: 5.3 Kebutuhan fungsional (FR)
frs = [
    ("FR-01", "Sistem harus menyediakan formulir permohonan pengajuan KTM (input NIM, Nama, Prodi, Email, No HP, Kategori, Alasan).", "Must"),
    ("FR-02", "Sistem harus mampu mengkalkulasi besaran biaya administrasi secara otomatis berdasarkan kategori pengajuan yang dipilih.", "Must"),
    ("FR-03", "Sistem harus menerbitkan Nomor Tiket Pengajuan unik (format: KTM-YYYYMM-XXX) setelah data berhasil dikirimkan.", "Must"),
    ("FR-04", "Sistem harus menyediakan modul pelacakan status pengajuan secara real-time berdasarkan input NIM atau Nomor Tiket.", "Must"),
    ("FR-05", "Sistem harus menyediakan tabel antrean dan rekapitulasi pengajuan untuk keperluan verifikasi staf BAAK.", "Should"),
    ("FR-06", "Sistem harus memvalidasi agar NIM yang masih memiliki pengajuan aktif tidak dapat mengajukan permohonan ganda.", "Should")
]
for idx, (code, req, prio) in enumerate(frs):
    set_cell(doc.tables[19], idx + 1, 0, code)
    set_cell(doc.tables[19], idx + 1, 1, req)
    set_cell(doc.tables[19], idx + 1, 2, prio)

# Table 20: 5.4 Kebutuhan nonfungsional (NFR)
nfrs = [
    ("NFR-01", "Waktu Tanggap (Performance): Waktu respon pencarian status dan pemrosesan form submit tidak lebih dari 2 detik.", "Pengujian beban response time menggunakan Chrome DevTools Network Tab."),
    ("NFR-02", "Ketersediaan & Aksesibilitas (Availability): Sistem dapat diakses 24/7 melalui jaringan internet dengan arsitektur serverless.", "Pemeriksaan uptime status pada dashboard cloud hosting Vercel."),
    ("NFR-03", "Kompatibilitas Tampilan (Usability & Responsiveness): Antarmuka web responsif dan dapat diakses dengan baik di perangkat desktop maupun smartphone.", "Pengujian responsivitas pada peramban Chrome, Firefox, dan Safari mobile.")
]
for idx, (code, spec, test) in enumerate(nfrs):
    set_cell(doc.tables[20], idx + 1, 0, code)
    set_cell(doc.tables[20], idx + 1, 1, spec)
    set_cell(doc.tables[20], idx + 1, 2, test)

# Table 21: 5.5 Kriteria penerimaan (acceptance criteria)
acs = [
    ("AC-01", "Mahasiswa memilih kategori 'Penggantian karena Hilang' pada formulir pengajuan.", "Sistem otomatis menampilkan estimasi biaya Rp 50.000 dan mewajibkan catatan surat kehilangan kepolisian."),
    ("AC-02", "Mahasiswa menekan tombol 'Kirim Permohonan' dengan data yang valid dan lengkap.", "Sistem menyimpan data, menerbitkan nomor tiket unik (KTM-XXXXXX), dan menampilkan kotak bukti pendaftaran."),
    ("AC-03", "Pengguna memasukkan NIM yang valid pada menu 'Cek & Lacak Status' lalu klik Lacak.", "Sistem menampilkan kartu rincian progres pengajuan lengkap dengan badge status pengerjaan saat ini.")
]
for idx, (code, cond, exp) in enumerate(acs):
    set_cell(doc.tables[21], idx + 1, 0, code)
    set_cell(doc.tables[21], idx + 1, 1, cond)
    set_cell(doc.tables[21], idx + 1, 2, exp)

# Table 22: 5.6 Batasan dan prioritas pelaksanaan
set_cell(doc.tables[22], 0, 1, "Formulir input biodata mahasiswa, kalkulasi otomatis tarif biaya admin, generate nomor tiket unik, tracking status pengajuan, serta tabel antrean verifikasi BAAK.")
set_cell(doc.tables[22], 1, 1, "Integrasi notifikasi WhatsApp otomatis saat kartu selesai dicetak, modul login multi-level RBAC (Role-Based Access Control), dan fitur export data ke file PDF/Excel.")
set_cell(doc.tables[22], 2, 1, "Sistem ini difokuskan pada pendataan dan pemantauan permohonan KTM; sistem tidak mengendalikan perangkat keras mesin cetak fisik kartu secara langsung dan pembayaran biaya admin dilakukan manual di loket/bank.")

# Table 23: 6.1 Alur proses bisnis
flows = [
    ("1", "Mahasiswa mengakses portal web SIP-KTM dan mengisi formulir pengajuan permohonan KTM.", "Data tersimpan di sistem dan sistem menerbitkan Nomor Tiket Pengajuan unik."),
    ("2", "Sistem memeriksa kategori pengajuan yang dipilih mahasiswa (Baru, Hilang, atau Rusak).", "Kalkulasi otomatis besaran biaya administrasi (Rp 0 / Rp 25.000 / Rp 50.000)."),
    ("3", "Staf BAAK memeriksa dan memverifikasi kelengkapan berkas permohonan melalui daftar antrean.", "Status pengajuan diubah menjadi 'Diverifikasi' lalu diteruskan ke status 'Proses Cetak'."),
    ("4", "KTM fisik telah selesai diproduksi oleh vendor/operator cetak kartu.", "Staf BAAK memperbarui status menjadi 'Siap Diambil' sehingga mahasiswa dapat datang mengambil kartu.")
]
for idx, (step, act, out) in enumerate(flows):
    set_cell(doc.tables[23], idx + 1, 0, step)
    set_cell(doc.tables[23], idx + 1, 1, act)
    set_cell(doc.tables[23], idx + 1, 2, out)

# Table 24: 6.2 Rancangan Basis Data - Daftar entitas
tables_meta = [
    ("mahasiswa", "nim", "-", "Menyimpan data induk mahasiswa yang terdaftar di universitas"),
    ("pengajuan_ktm", "id_pengajuan", "nim", "Menyimpan data transaksi permohonan kartu tanda mahasiswa"),
    ("log_status_pengajuan", "id_log", "no_tiket", "Merekam riwayat perubahan status pengerjaan KTM untuk audit trail"),
    ("admin_baak", "id_admin", "-", "Menyimpan data akun petugas akademik yang memiliki wewenang verifikasi"),
    ("kategori_biaya", "id_kategori", "-", "Menyimpan parameter konfigurasi tarif biaya per jenis pengajuan")
]
for idx, (tname, pk, fk, desc) in enumerate(tables_meta):
    set_cell(doc.tables[24], idx + 1, 0, tname)
    set_cell(doc.tables[24], idx + 1, 1, pk)
    set_cell(doc.tables[24], idx + 1, 2, fk)
    set_cell(doc.tables[24], idx + 1, 3, desc)

# Table 25: Relasi antarentitas
rels = [
    ("mahasiswa - pengajuan_ktm", "1 : N (One-to-Many)", "Satu mahasiswa dapat mengajukan permohonan KTM lebih dari satu kali dalam rentang waktu perkuliahan (misal pengajuan baru, kemudian rusak)."),
    ("pengajuan_ktm - log_status_pengajuan", "1 : N (One-to-Many)", "Satu berkas pengajuan memiliki banyak riwayat perubahan status (diajukan -> diverifikasi -> dicetak -> siap diambil)."),
    ("admin_baak - log_status_pengajuan", "1 : N (One-to-Many)", "Satu petugas admin BAAK dapat memvalidasi dan memperbarui banyak riwayat status pengajuan mahasiswa."),
    ("kategori_biaya - pengajuan_ktm", "1 : N (One-to-Many)", "Satu kategori aturan biaya dapat dirujuk oleh banyak transaksi permohonan pengajuan KTM.")
]
for idx, (pair, card, exp) in enumerate(rels):
    set_cell(doc.tables[25], idx + 1, 0, pair)
    set_cell(doc.tables[25], idx + 1, 1, card)
    set_cell(doc.tables[25], idx + 1, 2, exp)

# Table 26: 6.3 Kamus data (data dictionary)
dict_entries = [
    ("mahasiswa", "nim", "VARCHAR(15)", "Nomor Induk Mahasiswa sebagai kunci utama (Primary Key)"),
    ("mahasiswa", "nama_lengkap", "VARCHAR(100)", "Nama lengkap mahasiswa pemohon sesuai kartu identitas"),
    ("mahasiswa", "prodi", "VARCHAR(50)", "Program studi / jurusan mahasiswa"),
    ("pengajuan_ktm", "no_tiket", "VARCHAR(20)", "Nomor identifikasi unik pengajuan (format: KTM-YYYYMM-XXX)"),
    ("pengajuan_ktm", "jenis_pengajuan", "ENUM('baru','hilang','rusak')", "Kategori permohonan KTM yang menentukan syarat dan tarif"),
    ("pengajuan_ktm", "biaya_admin", "DECIMAL(10,2)", "Biaya penggantian kartu hasil kalkulasi logika bisnis"),
    ("pengajuan_ktm", "status_pengajuan", "ENUM", "Status tahapan (menunggu_verifikasi, disetujui, proses_cetak, siap_diambil)"),
]
for idx, (tname, attr, dtype, note) in enumerate(dict_entries):
    set_cell(doc.tables[26], idx + 1, 0, tname)
    set_cell(doc.tables[26], idx + 1, 1, attr)
    set_cell(doc.tables[26], idx + 1, 2, dtype)
    set_cell(doc.tables[26], idx + 1, 3, note)

# Table 27: 7.1 Berkas rancangan yang dilampirkan
set_cell(doc.tables[27], 1, 1, "https://github.com/240104013-debug/UTS-RPL")
set_cell(doc.tables[27], 2, 1, "https://sip-ktm-udb.vercel.app")

doc.save(output_path)
print(f"File berhasil diisi dan disimpan di: {output_path}")
