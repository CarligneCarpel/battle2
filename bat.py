def kalkile_total(s):
    chif = s.split()  
    total = 1

    for chif in chif :
        total_chif = sum(int(chif) for chif in chif) 
        total *= total_chif

    return total

chenn_karaktè = "5 45 123 12"
rezilta = kalkile_total(chenn_karaktè)
print(rezilta)
