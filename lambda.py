def hitung (j,h):
    bayar = j*h
    return bayar

print ('jumlah yang harus dibayar func :',hitung(4,20000))


bayar = lambda h,j : h*j
print('jumlah yang harus dibayar lamb1 :',bayar(2,40000))

print('jumlah yang harus dibayar lamb2 :',(lambda j,h : j*h)(3,30000))
