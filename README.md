# Ecoist

## Link Heroku
https://ecoist.herokuapp.com/

## Anggota
Azmi Rahmadisha

Bryan Tjandra

Mazaya Nur Labiba

Roy Maruli Tua Nababan

Son Sulung Suryahatta Asnan

## Main Idea

Donasi pohon

## Deskripsi / Manfaat

Situs Ecoist adalah situs yang bertujuan untuk menyebarkan kesadaran tentang pentingnya penghijauan hutan di Indonesia. Situs Ecoist memberikan ruang bagi 
masyarakat untuk berpartisipasi dalam kegiatan donasi pohon dan menyebarluaskan campaign-campaign terkait penghijauan hutan yang tersedia. Melalui aplikasi ini, masyarakat dapat sadar dan turut prihatin tentang isu penghijauan hutan di Indonesia.


## Modul / Pages
1. Register - Bryan - [mockup](https://drive.google.com/file/d/1QrvJXd9M2hszYsHtALVTOHyF303DAxBg/view?usp=sharing)

    Register berisi form untuk membuat akun agar user dapat melakukan kegiatan dalam website. 
Log In & Log Out - Bryan - login
Login dan logout berisi form untuk mengautentikasi dan membedakan antara user dan admin. Menggunakan modal untuk regist , kemudian menggunakan AJAX  POST & GET. 

2. Welcome Page (include deskripsi / about us) - Roy - [mockup](https://drive.google.com/file/d/1mrvJIjw1WbOiHeVV3QTALwAZ0OA1cZro/view?usp=sharing)


    Merupakan page yang akan ditampilkan saat awal orang memasuki website. Melalui page ini orang dapat di-redirect menuju page lainnya sesuai kebutuhan. Dalam page ini berisi deskripsi website, perkenalan tim pembuat web, serta form FAQ (menggunakan AJAX POST) jika pengunjung ingin memberikan masukan. Dalam laman ini, akan ditampilkan jumlah kampanye yang telah dibuat, bagian ini akan menggunakan AJAX GET.

3. Create Campaign - Hatta - [mockup](https://drive.google.com/file/d/1XR0QKDe9LzH_W-Qa8SJI-p_sXLBTzHoA/view?usp=sharing)


    Sebuah modal yang berisi form untuk mendaftarkan campaign. Di sini akan dilakukan implementasi AJAX GET

4. Campaign list - Hatta - [mockup](https://drive.google.com/file/d/1tMhTHTrt7l8UfNvdADdpZEFhNP8QegjO/view?usp=sharing)

    Berisi campaign-campaign yang dibuat oleh user. Di sini akan dilakukan implementasi AJAX POST dan AJAX GET

5. Join Campaign - Adish - [mockup](https://drive.google.com/file/d/1Xo3BjSqzE94hPkHAxygOuDa3Am53hfeL/view?usp=sharing)

    Fitur ini digunakan untuk user yang ingin mengikuti kampanye. User dapat mengisi form yang terdaftar untuk join campaign menanam/membersihkan hutan. Ketika user submit, akan dilakukan AJAX post berupa kampanye berhasil diikuti dan detail kampanye.

6. Donate - Maza - [mockup](https://drive.google.com/file/d/19YjNYBXmJI4caCt5EXVwktfI4xq4Bk2o/view?usp=sharing)

    Ini adalah fitur donasi untuk memfasilitasi user yang sudah login untuk berdonasi. Terdapat form untuk memasukkan input nominal donasi, jumlah pohon yang ingin didonasikan, dan catatan/pesan untuk kami serta tombol submit untuk menginput donasi. Ketika user ingin men-submit donasi, maka tombol submit tersebut akan menggunakan AJAX POST untuk menginput data yang dimasukkan user ke dalam database. Jika user belum login, maka akan di redirect ke halaman login terlebih dahulu.

7. Admin features - Bryan - [mockup](https://drive.google.com/file/d/1DR8PoU3aM14jDIiGi_2hjyNMaaWb7sID/view?usp=sharing)

    Merupakan fitur / web yang khusus bisa diakses oleh admin. Fitur yang khusus ini dapat digunakan untuk melihat data tentang user. Misalnya, melihat dashboard pageview dan click, total donasi yang ada, dan total campaign yang telah diikuti.



## Role Peran Pengguna
1. User

    User memiliki otoritas untuk mengakses welcome page, membuat dan berpartisipasi dalam campaign, serta melakukan donasi. 

2. Admin

    Admin atau administrator berperan sebagai pemegang kendali website dan memiliki akses penuh untuk melihat user database melalui dashboard admin. 


