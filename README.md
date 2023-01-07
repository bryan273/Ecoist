# Ecoist-Web

## Link Heroku
https://ecoist.herokuapp.com/

Our app : https://github.com/bryan273/Ecoist-Web

## Anggota

* Azmi Rahmadisha
* Bryan Tjandra
* Mazaya Nur Labiba
* Roy Maruli Tua Nababan
* Son Sulung Suryahatta Asnan

## Main Idea

Donasi dan kampanye penanaman pohon

## Deskripsi / Manfaat

Situs Ecoist adalah situs yang bertujuan untuk menyebarkan kesadaran kepada masyarakat tentang pentingnya penghijauan hutan di Indonesia. Situs Ecoist memberikan ruang bagi masyarakat untuk berpartisipasi dalam kegiatan donasi pohon dan menyebarluaskan campaign-campaign terkait penghijauan hutan yang tersedia. Melalui aplikasi ini, masyarakat dapat sadar dan turut prihatin tentang isu penghijauan hutan di Indonesia.

## Pages
1. Register

    <img src="https://user-images.githubusercontent.com/88226713/210933679-355abfaf-1c2d-4179-bb43-538ebbaea0e0.png" width="400" height="190"/>

2. Log In & Log Out

    <img src="https://user-images.githubusercontent.com/88226713/210933105-a2539295-263a-4fad-8557-7880a482872c.png" width="400" height="190"/>

3. Home Page
   
    <img src="https://user-images.githubusercontent.com/88226713/210932777-759e5f2c-1595-4a80-aa04-78c2f79fdbb0.jpg" width="400" height="661"/>
    
4. Create Campaign

    <img src="https://user-images.githubusercontent.com/88226713/210934143-5dd4f3f7-b90c-4cf1-9bd9-0244bf638157.png" width="400" height="200"/>

5. Campaign List

    <img src="https://user-images.githubusercontent.com/88226713/210934102-7dd01b23-093f-4e83-a6dd-3eb17ece5ca5.png" width="400" height="190"/>

6. Join Campaign

    <img width="400" height="383" src="https://user-images.githubusercontent.com/88226713/210934840-7f45ac62-392a-45ef-9881-503b49897a2f.jpg">

7. Donate

    <img width="400" height="277" src="https://user-images.githubusercontent.com/88226713/210934942-808e8e94-55fe-4698-8a06-8872f25f58eb.png">

8. Admin Features

    <img width="400" height="300" src="https://user-images.githubusercontent.com/88226713/210935787-b3da5815-5f10-4776-b988-64ebfce8a4c6.jpg">

## Deskripsi Modul
1. Register
    
    Register berisi form untuk membuat akun agar user dapat melakukan kegiatan dalam website. 

2. Log In & Log Out
    
    Login dan logout berisi form untuk mengautentikasi dan membedakan antara user dan admin. Menggunakan modal untuk regist , kemudian menggunakan AJAX  POST & GET. 

3. Home Page
   
    Merupakan page yang akan ditampilkan saat awal orang memasuki website. Melalui page ini orang dapat di-redirect menuju page lainnya sesuai kebutuhan. Dalam page ini berisi deskripsi website, perkenalan tim pembuat web, serta form FAQ (menggunakan AJAX POST) jika pengunjung ingin memberikan masukan. Dalam laman ini, akan ditampilkan jumlah kampanye yang telah dibuat, bagian ini akan menggunakan AJAX GET.

4. Create Campaign

    Sebuah modal yang berisi form untuk mendaftarkan campaign. Di sini akan dilakukan implementasi AJAX GET

5. Campaign List

    Berisi campaign-campaign yang dibuat oleh user. Di sini akan dilakukan implementasi AJAX POST dan AJAX GET

6. Join Campaign

    Fitur ini digunakan untuk user yang ingin mengikuti kampanye. User dapat mengisi form yang terdaftar untuk join campaign menanam/membersihkan hutan. Ketika user submit, akan dilakukan AJAX post berupa kampanye berhasil diikuti dan detail kampanye.

7. Donate

    Ini adalah fitur donasi untuk memfasilitasi user yang sudah login untuk berdonasi. Terdapat form untuk memasukkan input nominal donasi, jumlah pohon yang ingin didonasikan, dan catatan/pesan untuk kami serta tombol submit untuk menginput donasi. Ketika user ingin men-submit donasi, maka tombol submit tersebut akan menggunakan AJAX POST untuk menginput data yang dimasukkan user ke dalam database. Jika user belum login, maka akan di redirect ke halaman login terlebih dahulu.

8. Admin Features

    Merupakan fitur / web yang khusus bisa diakses oleh admin. Fitur yang khusus ini dapat digunakan untuk melihat data tentang user. Misalnya, melihat dashboard pageview dan click, total donasi yang ada, dan total campaign yang telah diikuti.

## Role Peran Pengguna
1. User

    User memiliki otoritas untuk mengakses welcome page, membuat dan berpartisipasi dalam campaign, serta melakukan donasi. 

2. Admin

    Admin atau administrator berperan sebagai pemegang kendali website dan memiliki akses penuh untuk melihat user database melalui dashboard admin. 


