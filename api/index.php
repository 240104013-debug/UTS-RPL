<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

$storageFile = __DIR__ . '/data_pengajuan.json';

// Inisialisasi data default jika file belum ada
if (!file_exists($storageFile)) {
    $initialData = [
        [
            'id' => 'KTM-202610-101',
            'nim' => '240104013',
            'nama' => 'Yusuf Rizal Indrianto',
            'prodi' => 'D3 Teknik Komputer',
            'email' => '240104013@mhs.udb.ac.id',
            'no_hp' => '081234567890',
            'jenis' => 'baru',
            'alasan' => 'Penerbitan kartu mahasiswa baru TA 2026/2027',
            'biaya' => 0,
            'status' => 'siap_diambil',
            'tgl_pengajuan' => '2026-10-14 09:30:00'
        ],
        [
            'id' => 'KTM-202610-102',
            'nim' => '240104088',
            'nama' => 'Ahmad Fauzi',
            'prodi' => 'D3 Teknik Komputer',
            'email' => 'fauzi@mhs.udb.ac.id',
            'no_hp' => '085712345678',
            'jenis' => 'hilang',
            'alasan' => 'Dompet terjatuh di area parkir kampus',
            'biaya' => 50000,
            'status' => 'proses_cetak',
            'tgl_pengajuan' => '2026-10-15 11:15:00'
        ]
    ];
    file_put_contents($storageFile, json_encode($initialData, JSON_PRETTY_PRINT));
}

$action = $_GET['action'] ?? '';

if ($action === 'list') {
    header('Content-Type: application/json');
    $data = json_decode(file_get_contents($storageFile), true);
    echo json_encode($data);
    exit();
}

if ($action === 'tracking') {
    header('Content-Type: application/json');
    $nim = trim($_GET['nim'] ?? '');
    $data = json_decode(file_get_contents($storageFile), true);
    $result = array_values(array_filter($data, function($item) use ($nim) {
        return strtolower($item['nim']) === strtolower($nim) || strtolower($item['id']) === strtolower($nim);
    }));
    echo json_encode(['success' => true, 'data' => $result]);
    exit();
}

if ($action === 'submit' && $_SERVER['REQUEST_METHOD'] === 'POST') {
    header('Content-Type: application/json');
    $nim = trim($_POST['nim'] ?? '');
    $nama = trim($_POST['nama'] ?? '');
    $prodi = trim($_POST['prodi'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $no_hp = trim($_POST['no_hp'] ?? '');
    $jenis = trim($_POST['jenis'] ?? 'baru');
    $alasan = trim($_POST['alasan'] ?? '');

    if (!$nim || !$nama) {
        echo json_encode(['success' => false, 'message' => 'NIM dan Nama Lengkap wajib diisi']);
        exit();
    }

    // Kalkulasi biaya administrasi (Logika Bisnis)
    switch ($jenis) {
        case 'hilang':
            $biaya = 60000; // Penyesuaian tarif KTM hilang cabang sim-conflict
            break;
        case 'rusak':
            $biaya = 25000;
            break;
        case 'baru':
        default:
            $biaya = 0;
            break;
    }

    $noTiket = 'KTM-' . date('Ym') . '-' . rand(100, 999);
    $newEntry = [
        'id' => $noTiket,
        'nim' => $nim,
        'nama' => $nama,
        'prodi' => $prodi,
        'email' => $email,
        'no_hp' => $no_hp,
        'jenis' => $jenis,
        'alasan' => $alasan,
        'biaya' => $biaya,
        'status' => 'menunggu_verifikasi',
        'tgl_pengajuan' => date('Y-m-d H:i:s')
    ];

    $data = json_decode(file_get_contents($storageFile), true);
    array_unshift($data, $newEntry);
    file_put_contents($storageFile, json_encode($data, JSON_PRETTY_PRINT));

    echo json_encode(['success' => true, 'message' => 'Pengajuan berhasil dikirim', 'data' => $newEntry]);
    exit();
}

// Fallback: Tampilkan petunjuk API
header('Content-Type: application/json');
echo json_encode([
    'service' => 'SIP-KTM Backend API',
    'endpoints' => [
        'GET /api/index.php?action=list' => 'Mendapatkan semua daftar pengajuan',
        'GET /api/index.php?action=tracking&nim=...' => 'Melacak pengajuan mahasiswa berdasarkan NIM/Tiket',
        'POST /api/index.php?action=submit' => 'Menyimpan data pengajuan baru'
    ]
]);
exit();
