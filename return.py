def tanah(panjang,lebar):
    luas = panjang * lebar
    return luas

def harga(luas,hpm2):
    jual = luas * hpm2
    print ('harga jual tanah :',jual)
    print('-------------')

luas = tanah(4,6)
harga(luas,1000)
