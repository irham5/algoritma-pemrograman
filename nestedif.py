print('HASIL REMIDI')
nilai = int(input('Masukkan nilai : '))

#proses
if nilai >= 75 :
    status = 'remidi'
    if nilai >= 85 :
        predikat = 'lulus'
    else :
        predikat = 'Cukup'
else :
    status = 'Gagal'
    predikat = 'Kurang'

# output
print('status :',status)
print('predikat :',predikat)
