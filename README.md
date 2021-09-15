# VClass-Tracker

## Deskripsi Singkat

VClass Tracker adalah sebuah aplikasi berbasis web scrapping dan otomatisasi untuk mendapatkan informasi dari website vclass , 
jika sebelumnya pengguna website vclass harus mengecek halaman matakuliah satu persatu untuk mendapatkan informasi mengenai tugas terbaru dengan aplikasi ini
masalah tersebut dapat diambil alih oleh aplikasi sehingga informasi dapat didapat dengan lebih cepat dan efisien, sehingga pekerjaan yang  sebelumnya perlu 
dilakukan berulang ulang dan manual dapat dihindari. 
Aplikasi ini menggunakan Command Line Interface (CLI) sebagai antarmukanya jadi pengguna akan membutuhkan keyboard untuk berinteraksi dengan aplikasi,
informasi yang didapat kemudian diolah dan diproses untuk kemudian ditampilkan ke command prompt pengguna.
Aplikasi ini membutuhkan koneksi internet untuk dijalankan, pastikan perangkat sudah terkoneksi ke internet yang stabil sebelum menggunakan aplikasi
### menu-menu yang terdapat di aplikasi ini antara lain : 
#### 1. perbarui daftar matakuliah
#### 2. tampilkan daftar matakuliah
#### 3. cek halaman matakuliah
#### 4. tampilkan daftar tugas
#### 5. cek tugas terbaru
#### 6. tampilkan daftar tugas terbaru
#### 7. buka tautan
#### 8. keluar
semua informasi yang didapat bersifat realtime pada saat di track yang artinya sesuai dengan yang terdapat di website vclass

## Penggunaan & Instalasi
Sebelum menjalankan aplikasi buka file ```get_course_page_content.py``` dan ```get_home_page_content.py``` di teks editor, 
lalu di file ```get_course_page_content.py``` dan ```get_home_page_content.py``` 
ubah value dari properti ```username``` dan ```password``` dengan username dan password akun vclass anda pada dictionary ```payload```. 
Aplikasi tidak akan berjalan jika username dan password yang dimasukkan salah.
selanjutnya install library beautifulsoup dengan menjalankan perintah berikut di command prompt :
```bash
pip install bs4
```
### untuk menjalankan aplikasi dapat dilakukan dengan 2 cara :
### 1.mengeksekusi file main.py di command prompt 
untuk menjalankan file main.py di command prompt, pertama buka command prompt di direktori aplikasi lalu ketikkan perintah sebagai berikut :
```bash
python main.py
```
maka aplikasi akan dieksekusi dan berjalan di command prompt
### 2.menjalankan file main.exe
untuk penggunaan menggunakan file .exe, file main.exe perlu di generate terlebih dahulu , untuk melakukanya pastikan di sistem sudah terinstal python versi terbaru
agar perintah ```pip``` dapat digunakan.
pertama jalankan perintah berikut untuk menjalankan library python pyinstaller :
```bash
pip install pyinstaller
```
setelah pyinstaller terinstal, jalankan perintah berikut untuk men-generate file main.exe :
```bash
pyinstaller --onefile main.py
```
jika perintah selesai dijalankan di direktori aplikasi akan muncul file dan direktori baru yaitu  direktori  build, direktori dist, dan file main.spec.
setelah itu buka direktori dist dan copy file main.exe ke main root, kemudian hapus direktori build, dist dan file main.spec karena sudah tidak dibutuhkan lagi.
Double click di file main.exe untuk menjalankan aplikasi

## Cara Kerja
cara kerja aplikasi ini untuk mendeteksi apakah terdapat tugas baru atau tidak adalah dengan membandingkan 2 buah file json yg berisi list string dari  daftar tugas
matakuliah, apabila list yang terdapat didalam salah satu file json tersebut lebih panjang dari list di file json lainya maka dapat dipastikan terdapat tugas 
terbaru, maka dari itu aplikasi ini baru dapat mendeteksi tugas terbaru apabila setidaknya pengguna sudah mengecek halaman matakuliah sebanyak 2 kali dengan
menjalankan menu ```3. cek halaman matakuliah```, setelah itu pilih menu ```5. cek tugas terbaru``` untuk mengecek tugas terbaru, terakhir untuk menampilkan 
daftar tugas terbaru pilih menu ```6. tampilkan daftar tugas terbaru```, maka tugas terbaru akan ditampilkan ke command prompt.

## Penjelasan Menu
#### 1. perbarui daftar matakuliah
meperbarui daftar matakuliah yang diikuti sesuai dengan yang terdapat di website vclass
#### 2. tampilkan daftar matakuliah
menampilkan daftar matakuliah yang diikuti sesuai dengan yang terdapat di website vclass
#### 3. cek halaman matakuliah
mengecek halaman setiap matakuliah dan mengambil skip html dan mengekstrak daftar tugasnya,
untuk kemudian ditulis ke file json 
#### 4. tampilkan daftar tugas
menampilkan daftar tugas dari matakuliah yang dipilih sesuai dengan yang terdapat di website vclass
#### 5. cek tugas terbaru
mengecek dan membandingkan 2 file json di direkotori matakuliah apakah ada tugas terbaru atau tidak sesuai dengan yang terdapat di website vclass
#### 6. tampilkan daftar tugas terbaru
menampilkan daftar tugas terbaru
#### 7. buka tautan
membuka tautan di browser secara cepat dan otomatis
#### 8. keluar
keluar dari aplikasi


## Note
Untuk mengsimulasikan seolah olah ada dosen yg mengupload tugas, setelah minimal 2 kali mengecek halaman matakuliah menggunakan menu ```3. cek halaman matakuliah```, 
tambahkan objek baru ke list yg ada file dengan nama yang berakhiran ```latest.json``` di salah satu subfolder direktori ```course-list```, 
cara menambahkan objeknya dapat dengan mengcopy sembarang objek yg sudah terdapat di dalam list di file json dengan nama barakhiran ```latest.json```,
setelah itu cek tugas terbaru menggunakan menu ```5. cek tugas terbaru```, kemudian tampilkan tugas terbaru menggunakan menu  ```6. tampilkan daftar tugas terbaru```.
maka seharusnya sekarang sudah muncul tugas baru di daftar tugas baru pada saat menu ```6. tampilkan daftar tugas terbaru``` dipilih.
