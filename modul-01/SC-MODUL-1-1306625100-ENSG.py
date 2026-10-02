print("pemograman konvesi suhu")
print(" nama : Eni Naura Sari Girsang")
print(" nim :1306625100")
print()

x = int(input("suhu_awal :"))
y = int(input("suhu_akhir :"))
z = int(input("selang :"))
print()

print("TABEL KONVENSI")
print()
print ('-' * 57)
print("| {0:^5}|{1:^15}|{2:^15}|{3:^15}|".format('no','celcius','Fahrenhait','Reamur'))
print('-' * 57)

n=1
while (x<= y):
    c = round(x)
    R = round((4/5) * c)
    F = round((9/5) * c + 32)
    print("|{0:^5}|{1:^15}|{2:^15}|{3:^15}|".format(n,c,R,F))
    n=n+1
    x=x+z

print('-' * 57)

print()
print("selesai")