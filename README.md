# Praktikum4
## Membuat Program Sederhana Menambah Data ke Dalam Sebuah List
1. Program meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
2. Tampilkan pertanyan untuk menambah data (y/t?), apabila menjawab tidak maka menampilkan daftar datanya
3. Nilai akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, dan uas: 35%)
4. Buat flowchart dan penjelasannya pada README.md
5. Commit dan push repository ke github
## Step by Step
1. Pastikan kita mempunya software pycharm atau vscode, jika belum anda bisa download Pycharm atau VSCode
2. Instalasi salah satu software tersebut hingga selesai, lalu buka
3. Jika sudah semua masukan kodingan seperti dibawah ini

``` bash
print("Masukan Data Mahasiswa")
data =[]
while True :
   nama       = input    ("Nama        : ")
   nim        = input    ("NIM         : ")
   tugas      = int(input("Nilai Tugas : "))
   uts        = int(input("Nilai UTS   : "))
   uas        = int(input("Nilai UAS   : "))
   nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
   data.append([nama,nim,tugas,uts,uas,nilaiakhir])

   lagi= input("Tambah data (y/t)? ")
   if lagi.lower() =="t":
       break


print("=====================================================================================")
print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |")
print("=====================================================================================")
i=0
for x in data:
   i+=1
   print("|  {6:2}  |  {0:10}  |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
         .format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
print("=====================================================================================")
```
![gambar1](Screenshot/gambar%20(2).png)

4. Lalu save dan Run program tersebut, maka akan keluar hasil
5. Input data list tersebut terserah yang kita mau, maka akan keluar hasil seperti dibawah ini
![gambar2](Screenshot/gambar%20(1).png)

## Latihan Membuat, Mengubah dan Menambah List
![gambar4](Screenshot/gambar%20(4).png)
# Step by step membuat list sebanyak 5 elemen dengan nilai bebas

1. Menampilkan semua elemen pada variabel a
2. Menampilkan elemen ketiga pada variabel a
3. Menampilkan elemen ke 2 sampai dengan 4 pada variabel a
4. Menampilkan elemen terakhir pada variabel a
# Step by step mengubah list dengan nilai bebas

1. Mengubah elemen ke 4 pada variabel a
2. Menampilkan elemen ke 4 yang sudah diubah nilainya
3. Mengubah elemen ke 4 sampai ke elemen terakhir
4. Menampilkan elemen ke 4 sampai elemen terakhir
# Step by step tambah elemen list

1. Mengambil 2 bagian dari list pertama (a) dan list kedua (b)
2. Menambah list dengan nilai string dengan append
3. Menambah list (b) dengan 3 nilai dengan extend
4. Menggabungkan nilai list (a) dan list (b) dan menampilkan hasil list (c)
![gambar3](Screenshot/gambar%20(3).png)