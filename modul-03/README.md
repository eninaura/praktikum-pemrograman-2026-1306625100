# Modul [03] - [TRIGONOMETRIC WITH FUNCTION]

**Nama:** [ENI NAURA SARI GIRSANG]  
**NIM:** [1306625100]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Membuat program untuk menghitung nilai sinus dan cosinus dengan menggunakan pendekatan deret MC Laurin
## 2. Mathematical Equation
> PERSAMAAN MATEMATIS
a. Deret Maclaurin untuk Sinus

sin x = Σ (n=0 sampai ∞) [(-1)^n × x^(2n+1) / (2n+1)!]

sin x = x - x^3/3! + x^5/5! - x^7/7! + ...

b. Deret Maclaurin untuk Cosinus

cos x = Σ (n=0 sampai ∞) [(-1)^n × x^(2n) / (2n)!]

cos x = 1 - x^2/2! + x^4/4! - x^6/6! + ...

c. Galat Relatif (Relative Error)

Er = |(Av - Tv) / Tv| × 100%

Keterangan: Er = Galat relatif (Relative Error) Av = Nilai hampiran (Approximate Value) Tv = Nilai sebenarnya (True Value)




## 3. Algorithm
>
1.Mulai
2.import library math
3.Masukkan nilai sudut dalam derajat
4.konversikan sudutdari derajat keradian
5.hitung nilai sin menggunakan deret MC laurin :sin (x)=x-(x^3/3!)+(x15/5!)-(x^7/7!)+....
6.Hitung nIlai COS manggunakan deret Mc larin: cos(x)=1-(x^1 2/2!)+(x^4/4!) -(x^7/7!)+...
7.Hitung nilai sin dan cos menggunaKan fungsi math sebagai true value (Tv)
8.Hitung RelatiVe error menggunakan rumus = ER= 1(AV-TV/TV) X1 00%
9.PeriKsa apakah Relative Error sudah kurang dari 5%
10.jika Er belum kurang dari 5% tambankan jumlah suatu deret dan ulangi perhitungan 
11.jika Er sudah kurang dari 5% tampilkan hasil  nilai sin,cos,dan Relative eror
12.selesai

