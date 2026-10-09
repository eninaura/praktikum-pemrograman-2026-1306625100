print('program faktor bilangan')
print(' nama:Eni Naura Sari Girsang')
print(' nim: 1306625100')
print('\n')

while True:
    hasil = [18]
    n = int(input('masukkan bilangan <100 (selesai)=0 '))
    if n ==0:
        break
    for i in range (1, n+1):
        if n % i == 0:
            hasil.append(i)
    print('faktor bilangan', n, 'adalah', hasil)
    print('selesai')