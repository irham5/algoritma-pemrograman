print('HASIL REMIDI')
nilai = int(input('Masukkan nilai : '))

if nilai > 80 :
    transkip = 'A'
elif nilai > 60 :
    trnskip = 'B'
elif nilai > 40 :
    transkip = 'C'
elif nilai > 20 :
    transkip = 'D'
else :
    transkip = 'E'

print('Nilai transkip :',transkip)
