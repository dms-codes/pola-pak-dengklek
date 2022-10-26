n = int(input('Masukkan n: '))
awal = 0
akhir = 0
index = []
row_index = []
for baris in range(1,n+1):
    awal = akhir 
    akhir = baris + awal
    for i in range(awal,akhir):
        index.append(i)
    row_index.append([i for i in range(awal,akhir)])

banyak_angka = len(index)
hasil = banyak_angka//10
sisa = banyak_angka%10
result = hasil * '0123456789'
sisa_result = '0123456789'[:sisa+1]    
res = result + sisa_result

for row in row_index:
    for r in row:
        print(res[r],sep=' ', end='')
    print()
