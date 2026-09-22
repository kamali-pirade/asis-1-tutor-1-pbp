# BookShelf · Solusi dan Panduan Pengajar

Folder ini adalah **solusi privat** untuk kuis yang hanya mencakup Tutorial 00, Tutorial 01, dan Tugas 01 PBP. Bagikan hanya paket `student-starter/` kepada mahasiswa. Kuis ini menguji kebersihan repositori, hubungan view–URL–template statis, HTML semantik, aset statis, Flexbox/Grid, section tambahan, dan media query.

Untuk menjalankan secara lokal, pasang `requirements.txt`, jalankan `python manage.py migrate` untuk aplikasi bawaan Django, lalu `python manage.py runserver`.

## Pemetaan tes

| TODO | Materi | Kelas tes |
|------|--------|-----------|
| 1 | `.gitignore` dan berkas lokal | `GitHygieneTests` |
| 2 | View, root URL, dan template | `PageRoutingTests` |
| 3 | Navigasi semantik | `NavigationTests` |
| 4 | Intro dan aset statis | `IntroTests` |
| 5 | Layout desktop | `IntroStyleTests` |
| 6 | Section baru dan tiga item | `PicksTests` |
| 7 | CSS khusus section baru | `PicksStyleTests` |
| 8 | Layout mobile | `ResponsiveTests` |

## Rubrik internal

Nilai inti maksimum 100 poin. Nilai akhir: **1** jika aplikasi gagal berjalan atau materi inti hampir tidak ada; **2** jika berjalan sebagian tetapi banyak bagian gagal; **3** jika sebagian besar berjalan dengan kekurangan kecil; **3.5** jika semua syarat inti benar; **4** jika syarat inti benar ditambah peningkatan UI/interaksi yang relevan. Poin membantu konsistensi antarpemeriksa; polesan visual tidak mengganti fungsi inti yang hilang.

| TODO | Poin | Penuh | Sebagian | Nol |
|------|------|-------|----------|-----|
| 1 | 10 | Semua pola lokal penting diabaikan | Sebagian pola ada | Berkas lokal sensitif tidak diabaikan |
| 2 | 14 | Route bernama dan view merender template | Salah satu sambungan benar | Halaman utama tidak bekerja |
| 3 | 10 | Navigasi semantik ke kedua section | Navigasi ada tetapi tautan kurang | Tidak ada navigasi |
| 4 | 16 | Intro semantik, teks jelas, gambar dan alt | Isi atau aksesibilitas kurang | Intro tidak ada |
| 5 | 12 | Layout desktop Flexbox/Grid jelas | Layout ada tetapi belum rapi | Tidak ada layout khusus |
| 6 | 16 | Section baru dengan tiga artikel bermakna | Section/item belum lengkap | Section tidak ada |
| 7 | 12 | Grid/Flex dan gaya kartu khusus | Hanya layout atau gaya kartu | Tidak ada CSS khusus |
| 8 | 10 | Media query mengadaptasi kedua layout | Hanya satu layout diadaptasi | Tidak responsif |

Untuk nilai sebagian, gunakan 25–75% poin TODO sesuai bukti yang berfungsi. Tinjau hasil pada lebar desktop dan ponsel selain menjalankan tes; tes CSS memeriksa keberadaan aturan, bukan kualitas visual sepenuhnya.
