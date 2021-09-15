# vclass-tracker

## deskripsi singkat

vclass tracker adalah sebuah aplikasi berbasis web scrapping dan otomatisasi untuk mendapatkan informasi dari website vclass , 
jika sebelumnya pengguna website vclass harus mengecek halaman matakuliah satu persatu untuk mendapatkan informasi mengenai tugas terbaru dengan aplikasi ini
masalah tersebut dapat diambil alih oleh aplikasi sehingga informasi dapat didapat dengan lebih cepat dan efisien, sehingga pekerjaan yang  sebelumnya perlu 
dilakukan berulang ulang dan manual dapat dihindari 
aplikasi ini menggunakan Command Line Interface (CLI) sebagai antarmukanya jadi pengguna akan membutuhkan keyboard untuk berinteraksi dengan aplikasi,
informasi yang didapat kemudian diolah dan diproses untuk kemudian ditampilkan ke command prompt pengguna, 
### menu-menu yang terdapat di aplikasi ini antara lain : 
#### 1. perbarui daftar matakuliah
#### 2. tampilkan daftar matakuliah
#### 3. cek halaman matakuliah
#### 4. tampilkan daftar tugas
#### 5. cek tugas terbaru
#### 6. tampilkan daftar tugas terbaru
#### 7. buka tautan
#### 8. keluar
semua informasi yang didapat bersifat realtime yang artinya sesuai dengan yang terdapat di website vclass

## penggunaan & instalasi
sebelum menjalankan aplikasi buka file ```get_course_page_content.py``` dan ```get_course_page_content.py``` di teks editor, lalu di masing-masing file 
ubah value dari properi ```username``` dan ```password``` dengan username dan password akun vclass anda pada dictionary ```payload```. 
Aplikasi tidak akan berjalan jika username dan password yang dimasukkan salah
### untuk menjalankan aplikasi dapat dilakukan dengan 2 cara, 
#### 1.mengeksekusi file main.py di command prompt 
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

## cara kerja
cara kerja aplikasi ini untuk mendeteksi apakah terdapat tugas baru atau tidak adalah dengan membandingkat 2 buah file json yg berisi list string dari  daftar tugas
matakuliah, apabila salah satu list yang terdapat didalam file json tersebut lebih panjang dari list di file json lainya maka dapat dipastikan terdapat tugas 
terbaru, maka dari itu aplikasi ini baru dapat mendeteksi tugas terbaru apabila setidaknya pengguna sudah mengecek halaman matakuliah sebanyak 2 kali dengan
menjalankan menu ```3. cek halaman matakuliah```, setelah itu pilih menu ```5. cek tugas terbaru``` untuk mengecek tugas terbaru, terakhir untuk menampilkan 
daftar tugas terbaru pilih menu ```6. tampilkan daftar tugas terbaru```, maka tugas terbaru akan ditampilkan ke command prompt.

## penjelasan menu
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


## note
