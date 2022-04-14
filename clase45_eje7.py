lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []

for i in (lista_1):
    if i in lista_2:
        if i in lista_3:
            pass
        else:
            lista_3.append(i)

print("FINAL:",lista_3)
