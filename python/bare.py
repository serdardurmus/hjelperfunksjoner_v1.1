N = int(input())
listem = []
for i in range(N):
    kode = (input("Tast inn din kode: ")).split()
    if kode[0] == "insert": 
        listem.insert(int(kode[1]), int(kode[2]))
    elif kode[0] == "print": 
        print(listem)
    elif kode[0] == "remove":
        listem.remove(int(kode[1]))
    elif kode[0] == "append":
        listem.append(int(kode[1]))
    elif kode[0] == "sort":
        listem.sort()
    elif kode[0] == "pop":
        listem.pop()
    elif kode[0] == "reverse":
        listem.reverse()

print(listem)