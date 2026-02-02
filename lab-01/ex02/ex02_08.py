def chiahetcho5(so_nhi_phan):
    sothapphan= int(so_nhi_phan,2)
    if sothapphan % 5==0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("nhap chuoi so nhi phan")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
sochiahetcho5 = [so for so in so_nhi_phan_list if chiahetcho5(so)]
if len(sochiahetcho5)>0:
    ketqua=','.join(sochiahetcho5)
    print("cac so nhi phan chia het cho 5 la ",ketqua)
else:
    print("khong co so nhi phan nao chia het cho 5")