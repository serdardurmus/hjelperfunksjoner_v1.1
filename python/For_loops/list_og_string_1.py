et_ord = input("skriv et ord: ")
hvor_mange_a = 0
hvor_mange_e = 0
for ord in et_ord:
    if (ord == "e") : hvor_mange_e += 1
    elif (ord == "a") : hvor_mange_a += 1
print(f"det er {hvor_mange_a} a og {hvor_mange_e} e i ordet.")