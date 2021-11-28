list=["a", "b", "c", "d", "e"]

print("tampilkan element ke 3:", list[2])
print("ambil element ke 2 sampai 4:", list[1:4])
print("ambil element terakhir:", list[-1])

# merubah element ke 4 dengan nilai lain
list[3] = "f"

print("merubah element ke 4 demgan nilai lain:", list)

# merubah ke 4 sampai terakhir
list[3:] = "f", "g"
print("merubah element ke 4 sampai element terakhir:", [list])




# tambah element list
a=[1,2,3,4,5]
b=[6,7,8,9,10]

# ambil 2 bagian list A ke list B
b.append(a[1:3])
print("2 bagian list A dijadikan list B:", b)

# tambah list B dengan string
b.append("saya")
print("tambah B dengan string:", b)

# tambah list B dengan 3 nilai
print("tambah list B dengan 3 nilai:", b+[11,12,13])

# gabungan list A dan B
c=b+a
print("gabungan list A dan B:", c)