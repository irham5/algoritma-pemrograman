print('HASIL REMIDI')
nilai = int(input('Masukkan nilai : '))

#proses
if nilai >= 75 :
    status = 'Lulus'
    if nilai >= 85 :
        predikat = 'Memuaskan'
    else :
        predikat = 'Cukup'
else :
    status = 'Gagal'
    predikat = 'Kurang'

# output
print('status :',status)
print('predikat :',predikat)
