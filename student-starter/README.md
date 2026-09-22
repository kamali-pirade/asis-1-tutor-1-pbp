# BookShelf · Programming Quiz PBP (Tutorial 00–01, Tugas 01)

Ini adalah **starter kuis**, bukan aplikasi yang sudah selesai. Proyek Django dan aset visual dasar tersedia. Lengkapi delapan TODO untuk membuat satu halaman statis klub baca. Data pada halaman ditulis langsung dalam HTML; kuis ini belum memakai model, database aplikasi, form, atau JSON.

| TODO | Materi | Berkas |
|------|--------|--------|
| 1 | Kebersihan repositori dari Tutorial 00 | `.gitignore` |
| 2 | Sambungan view, URL, dan template dari Tutorial 01 | `bookquiz/views.py`, `bookquiz/urls.py` |
| 3 | Navigasi HTML semantik | `templates/index.html` |
| 4 | Intro, teks, aset statis, dan alt gambar | `templates/index.html` |
| 5 | Tata letak intro dengan Flexbox/Grid | `static/css/style.css` |
| 6 | Section tambahan dengan minimal tiga item (Tugas 01) | `templates/index.html` |
| 7 | CSS khusus section tambahan | `static/css/style.css` |
| 8 | Tampilan responsif desktop dan mobile | `static/css/style.css` |

## Menjalankan

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py runserver
```

Di Windows, aktifkan environment sesuai shell yang dipakai. Setelah mengerjakan TODO, buka `http://localhost:8000/` lalu jalankan `python manage.py test`. Tes starter memang gagal sebelum bagian terkait dilengkapi. Periksa juga halaman pada lebar desktop dan ponsel; tes CSS hanya memeriksa struktur aturan, sedangkan kerapian visual tetap perlu dilihat langsung.

Jangan ubah tes untuk menyembunyikan kegagalan. Kuis ini tidak meminta akun GitHub, deployment PWS, commit, atau push.
