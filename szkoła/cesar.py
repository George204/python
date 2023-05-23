import string
duże = string.ascii_uppercase
małe = string.ascii_lowercase
while True:
    tekst = str(input("tekst jawny:"))
    przesunięcie = int(input("przesunięcie:"))
    szyfr = ""
    for i in tekst:
        if i in małe:
            index = małe.index(i) + przesunięcie
            if index > len(małe):
                index -= len(małe)
            szyfr += (małe[index])
        elif i in duże:
            index = duże.index(i) + przesunięcie
            if index > len(duże):
                index -= len(duże)
            szyfr += (duże[index])
    print(szyfr)
 