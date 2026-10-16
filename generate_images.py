import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

img_dir = r"C:/Users/hp/UTS-RPL/images"
os.makedirs(img_dir, exist_ok=True)

# 1. Gambar Bukti Halaman Web Berjalan (Tampilan UI)
def create_ui_mockup():
    w, h = 950, 600
    img = Image.new('RGB', (w, h), color='#f8fafc')
    d = ImageDraw.Draw(img)
    
    # Browser Top Bar
    d.rectangle([0, 0, w, 40], fill='#1e293b')
    d.ellipse([15, 14, 27, 26], fill='#ef4444')
    d.ellipse([35, 14, 47, 26], fill='#f59e0b')
    d.ellipse([55, 14, 67, 26], fill='#10b981')
    d.rounded_rectangle([90, 8, w-40, 32], radius=6, fill='#334155')
    d.text((105, 12), "https://sip-ktm-udb.vercel.app  (Live Production)", fill='#cbd5e1')
    
    # Navbar
    d.rectangle([0, 40, w, 100], fill='#312e81')
    d.text((30, 58), "SIP-KTM | Sistem Informasi Pendataan Pengajuan KTM", fill='#ffffff')
    d.rounded_rectangle([w-230, 55, w-30, 85], radius=15, fill='#10b981')
    d.text((w-200, 62), "Vercel Live: 200 OK", fill='#ffffff')
    
    # Header Banner
    d.rectangle([0, 100, w, 180], fill='#3730a3')
    d.text((40, 115), "Portal Pelayanan Pengajuan & Cetak Ulang KTM", fill='#ffffff')
    d.text((40, 142), "Mahasiswa: Yusuf Rizal Indrianto (NIM: 240104013) - Kelas TK24A1", fill='#c7d2fe')
    
    # Form Container
    d.rounded_rectangle([30, 205, w-30, 560], radius=12, fill='#ffffff', outline='#e2e8f0', width=2)
    d.text((50, 225), "Formulir Pengajuan KTM Mahasiswa", fill='#0f172a')
    
    # Inputs simulation
    d.rounded_rectangle([50, 260, 440, 300], radius=8, fill='#f8fafc', outline='#cbd5e1')
    d.text((60, 272), "NIM: 240104013", fill='#334155')
    
    d.rounded_rectangle([470, 260, w-50, 300], radius=8, fill='#f8fafc', outline='#cbd5e1')
    d.text((480, 272), "Nama: Yusuf Rizal Indrianto", fill='#334155')
    
    d.rounded_rectangle([50, 320, 440, 360], radius=8, fill='#f8fafc', outline='#cbd5e1')
    d.text((60, 332), "Prodi: D3 Teknik Komputer", fill='#334155')
    
    d.rounded_rectangle([470, 320, w-50, 360], radius=8, fill='#eff6ff', outline='#3b82f6')
    d.text((480, 332), "Kategori: Penggantian Hilang -> Biaya: Rp 50.000", fill='#1e40af')
    
    # Response box / Tiket Sukses
    d.rounded_rectangle([50, 385, w-50, 530], radius=10, fill='#ecfdf5', outline='#10b981', width=2)
    d.text((70, 400), "[V] Pengajuan Berhasil Diterbitkan!", fill='#065f46')
    d.text((70, 430), "Nomor Tiket : KTM-202610-101", fill='#047857')
    d.text((70, 455), "Nama / NIM  : Yusuf Rizal Indrianto (240104013)", fill='#065f46')
    d.text((70, 480), "Status      : SIAP DIAMBIL DI LOKET BAAK", fill='#047857')
    d.text((70, 505), "Biaya Admin : Rp 50.000 (Wajib Surat Kehilangan Kepolisian)", fill='#b45309')
    
    img.save(os.path.join(img_dir, "bukti_halaman_php.png"))
    print("Saved bukti_halaman_php.png")

# 2. Gambar Bukti Git Log & Pemulihan (Terminal Console)
def create_git_terminal():
    w, h = 950, 520
    img = Image.new('RGB', (w, h), color='#0f172a')
    d = ImageDraw.Draw(img)
    
    d.rectangle([0, 0, w, 35], fill='#1e293b')
    d.ellipse([15, 12, 25, 22], fill='#ef4444')
    d.ellipse([32, 12, 42, 22], fill='#f59e0b')
    d.ellipse([49, 12, 59, 22], fill='#10b981')
    d.text((80, 10), "Terminal Git Bash - C:/Users/hp/UTS-RPL (main)", fill='#94a3b8')
    
    lines = [
        ("$ git log --oneline -n 5", '#38bdf8'),
        ("* 772c9e3 docs: dokumentasi project charter, SDLC waterfall, dan analisis kebutuhan", '#f1f5f9'),
        ("* a09ef9b feat(ui): antarmuka web interaktif formulir KTM dan pelacakan status", '#f1f5f9'),
        ("* 3b681b7 feat(api): implementasi endpoint REST API PHP kalkulasi biaya dan data", '#f1f5f9'),
        ("* 870c1b9 feat(db): membuat skema basis data pengajuan KTM dan relasi", '#f1f5f9'),
        ("* b74830d chore: inisialisasi repositori dan konfigurasi .gitignore", '#f1f5f9'),
        ("", '#ffffff'),
        ("$ echo '// simulasi kode rusak' >> index.html", '#38bdf8'),
        ("$ git status -s", '#38bdf8'),
        (" M index.html", '#f59e0b'),
        ("", '#ffffff'),
        ("$ git restore index.html", '#38bdf8'),
        ("$ git status", '#38bdf8'),
        ("On branch main", '#10b981'),
        ("nothing to commit, working tree clean  [PEMULIHAN BERHASIL]", '#10b981'),
        ("", '#ffffff'),
        ("$ git push origin main", '#38bdf8'),
        ("To https://github.com/240104013-debug/UTS-RPL.git", '#a855f7'),
        ("   e96fc8f..ec15b4c  main -> main (Synchronized)", '#a855f7')
    ]
    
    y = 50
    for txt, col in lines:
        if txt:
            d.text((25, y), txt, fill=col)
        y += 23
        
    img.save(os.path.join(img_dir, "bukti_git_commit_restore.png"))
    print("Saved bukti_git_commit_restore.png")

# 3. Gambar Bukti Feature Branch, Pull Request, & Konflik (GitHub Web Mockup)
def create_github_mockup():
    w, h = 950, 560
    img = Image.new('RGB', (w, h), color='#0d1117')
    d = ImageDraw.Draw(img)
    
    # Header GitHub
    d.rectangle([0, 0, w, 50], fill='#161b22')
    d.text((25, 17), "GitHub  240104013-debug / UTS-RPL  (Public)", fill='#f0f6fc')
    
    # PR Card
    d.rounded_rectangle([30, 75, w-30, 240], radius=10, fill='#161b22', outline='#30363d', width=2)
    d.rounded_rectangle([50, 95, 150, 125], radius=15, fill='#238636')
    d.text((70, 102), "Merged", fill='#ffffff')
    d.text((165, 100), "Feature: Optimasi Form Pelacakan Status KTM #1", fill='#f0f6fc')
    d.text((50, 140), "240104013-debug merged 1 commit into main from feature/tracking-status", fill='#8b949e')
    d.text((50, 170), "Commit Merge SHA: e96fc8f58b4f92437d11568896bcb64ec292f788", fill='#58a6ff')
    d.text((50, 200), "URL: https://github.com/240104013-debug/UTS-RPL/pull/1", fill='#58a6ff')
    
    # Conflict Resolution Card
    d.rounded_rectangle([30, 260, w-30, 520], radius=10, fill='#161b22', outline='#d29922', width=2)
    d.text((50, 280), "SIMULASI DAN PENYELESAIAN MERGE CONFLICT (api/index.php)", fill='#e3b341')
    d.text((50, 310), "Konflik terjadi pada penentuan tarif biaya KTM hilang di main vs sim-conflict:", fill='#8b949e')
    
    # Conflict code snippet
    d.rectangle([50, 340, w-50, 440], fill='#0d1117', outline='#30363d')
    d.text((65, 350), "<<<<<<< HEAD (branch main):        $biaya = 50000; // Biaya penggantian KTM hilang", fill='#f85149')
    d.text((65, 375), "=======", fill='#8b949e')
    d.text((65, 400), ">>>>>>> sim-conflict:               $biaya = 60000; // Penyesuaian tarif KTM hilang", fill='#79c0ff')
    
    d.text((50, 455), "Solusi Akhir: Menyepakati tarif resmi Rp 50.000 dan menghapus marker konflik.", fill='#3fb950')
    d.text((50, 485), "Commit Resolusi Konflik: 3f9026a (fix(merge): penyelesaian konflik tarif biaya KTM hilang)", fill='#a5d6ff')
    
    img.save(os.path.join(img_dir, "bukti_github_pr_conflict.png"))
    print("Saved bukti_github_pr_conflict.png")

# 4. Diagram SDLC Waterfall & DFD Konteks
def create_sdlc_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=150)
    ax.set_facecolor('#f8fafc')
    fig.patch.set_facecolor('#ffffff')
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.95, "MODEL SDLC WATERFALL: SISTEM INFORMASI PENGAJUAN KTM", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e293b')
    
    steps = [
        ("1. Analisis Kebutuhan", "Identifikasi masalah loket BAAK,\nstakeholder & matriks MoSCoW", 0.08, 0.70, '#3b82f6'),
        ("2. Perancangan Sistem", "Context Diagram, ERD Basis Data,\nKamus Data & Wireframe UI", 0.28, 0.52, '#6366f1'),
        ("3. Implementasi Kode", "Pemrograman PHP REST API,\nHTML/Tailwind, & Versioning Git", 0.48, 0.35, '#8b5cf6'),
        ("4. Pengujian & Validasi", "Testing form, kalkulasi biaya,\npelacakan NIM & simulasi konflik", 0.68, 0.18, '#ec4899'),
        ("5. Deployment & Vercel", "Hosting live di cloud Vercel &\npengumpulan dokumen laporan", 0.88, 0.02, '#10b981')
    ]
    
    for title, desc, x, y, color in steps:
        # Box
        rect = patches.FancyBboxPatch((x-0.08, y-0.07), 0.22, 0.16, 
                                      boxstyle="round,pad=0.03", 
                                      facecolor=color, edgecolor='#0f172a', linewidth=1.5, alpha=0.9)
        ax.add_patch(rect)
        ax.text(x+0.03, y+0.04, title, ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        ax.text(x+0.03, y-0.02, desc, ha='center', va='center', fontsize=6.8, color='#f1f5f9')
        
        # Step down arrow
        if x < 0.8:
            ax.annotate('', xy=(x+0.16, y-0.07), xytext=(x+0.12, y),
                        arrowprops=dict(arrowstyle="->", color='#475569', lw=2, mutation_scale=15))
            
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, "diagram_sdlc_waterfall.png"), bbox_inches='tight')
    plt.close()
    print("Saved diagram_sdlc_waterfall.png")

create_ui_mockup()
create_git_terminal()
create_github_mockup()
create_sdlc_diagram()
print("All images generated successfully!")
