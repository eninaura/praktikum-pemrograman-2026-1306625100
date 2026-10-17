# Modul [04] - [Grading]

**Nama:** [Eni Naura Sari Girsang]  
**NIM:** [1306625100]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Membuat program untuk menghitung nilai akhir dan menentukan grade mahasiswa berdasarkan sekumpulan data nilai mahasiswa yang terdapat pada file Excel DataNilai.xlsx.

## 2. Mathematical Equation
> NA = (0,30 × NL) + (0,35 × UTS) + (0,35 × UAS)

## 3. Algorithm
> 1. Mulai.

2. Inisialisasi variabel dan counter.

3. Deklarasi variabel:
   N, NIM, NBP, NB, NBP = 0, N = 0.

4. Baca data nilai mahasiswa, yaitu nama, NIM, dan nilai:
   Nama[], NIM[], dan NA[] (NA = numerik).

5. Print judul "LAPORAN GRADING MAHASISWA" dan header tabel
   (No, Nama Mahasiswa, NIM, Nilai Angka, Grade).

6. Menampilkan data mahasiswa yang telah dimasukkan.

7. Hitung NA = 0,30 × N + 0,70 × UAS.

8. Tentukan grade berdasarkan nilai akhir:
   a. Jika NA >= 86, Grade = "A".
   b. Jika tidak dan NA >= 81, Grade = "A-".
   c. Jika tidak dan NA >= 76, Grade = "B+".
   d. Jika tidak dan NA >= 71, Grade = "B".

9. Print semua data mahasiswa.

10. Print total mahasiswa = N.

11. Print "Selesai".

12. Selesai.
