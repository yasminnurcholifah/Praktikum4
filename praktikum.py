data =[]
while True :
	Nama = input("Nama : ")
	NIM = input("NIM : ")
	Tugas = int(input("Nilai Tugas :"))
	UTS = int(input('Nilai UTS : '))
	UAS = int(input("Nilai UAS : "))
	Nilai_Akhir = float(Tugas)*30/100+(UTS)*35/100+(UAS)*35/100
	data.append([Nama, NIM, Tugas, UTS, UAS, Nilai_Akhir])
	lagi  = input("Tambah data (y/t?)")
	if lagi.lower() == "t":
		break

print("=====================================================================================")
print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |");
print("=====================================================================================");
i=0
for x in data:
    i+=1
    print("|  {6:2}  |  {0:10}  |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
          .format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
print("=====================================================================================");