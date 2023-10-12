# bunga = {
#     "nama" : "tulip",
#     "harga": 10000,
#     "jumlah": 12
# }
# # print(bunga)

# #mengambil value dalam dictionary
# tampilnama = (bunga["nama"])
# tampilharga = (bunga["harga"])
#0
#  tampiljumlah = bunga.get("jumlah")

# print(f"Bunga {tampilnama} dengan harga {tampilharga} jumlah {tampiljumlah}")

laptop = {
    "nama" :["asus","hp","lenovo"],
    "harga":[20, 30, 40],
    "jumlah":[1, 2, 3]
}

#nambah data
laptop.get("nama").append("msi")
print(laptop["nama"])

#menghapus data
laptop.get("harga").pop() #menghapus langsung yang belakang
laptop.get("harga").remove(20) #menghapus sesuai dengan nilai yang diinginkan
print(laptop["harga"])
print(laptop["jumlah"])

#update data
idx = int(input("Masukkan index data yang ingin diubah: "))
jumlahBaru = int(input("Jumlah Baru: "))
idx -= 1 #mengubah index dari 0 jadi 1

laptop.get("jumlah")[idx] = jumlahBaru
print(laptop.get("jumlah"))