# Catatan validasi

Diuji dengan Django 5.2.17. `python manage.py check` lulus pada kedua versi. `python manage.py test` menemukan 13 tes: **13 gagal/error pada starter** tepat karena TODO 1–8 belum selesai; **13 lulus pada solusi pengajar**. Kegagalan starter terbagi menjadi 2 tes untuk TODO 1, 2 untuk TODO 2, 1 untuk TODO 3, 2 untuk TODO 4, 1 untuk TODO 5, 2 untuk TODO 6, 2 untuk TODO 7, dan 1 untuk TODO 8.

Tes memeriksa `.gitignore`, route dan template statis, struktur HTML, penggunaan ilustrasi serta alt, dan aturan CSS desktop/mobile. Jalur Django tidak membutuhkan model atau migrasi aplikasi. Pemeriksaan visual desktop/mobile tetap bagian dari penilaian karena tes statis tidak dapat mengukur seluruh kualitas tata letak.
