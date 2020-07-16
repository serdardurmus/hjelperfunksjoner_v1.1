en_liste = [["Anne", 95],["Tom", 89],["Jorunn", 85],["Oddny", 100]]
total = 0

for a in en_liste:
    total = total + a[1]
print(total/len(en_liste))

# Under gjennomsnittet
under_gjennomsnittet = []
for a,b in en_liste:
    if (b<(total/len(en_liste))) : under_gjennomsnittet.append([a,b])
print(under_gjennomsnittet)