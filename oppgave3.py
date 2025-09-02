def gjennsomsnitt(liste):
    if len(liste) != 0:
        return sum(liste)/len(liste)
    return

liste1 = [1, 2, 3]
liste2 = [10, 20, 30, 40]

print(gjennsomsnitt(liste1))
print(gjennsomsnitt(liste2))
