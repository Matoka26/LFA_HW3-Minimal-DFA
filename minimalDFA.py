import random
def afisare(dic):
    for linie in dic:
        print(linie,dic[linie])
    print()

def afisarePatitie(part):
    for parti in part:
        print(part.index(parti))
        for stare in parti:
            print(stare,parti[stare])
    print()

def stariAproapeEgale(stare1,stare2):
    check = 1
    for litera in alfabet:
        if stare1[litera][1] != stare2[litera][1]:
            check = 0
    return check

def partitionare(listaPartitii):
    partitieNoua = []
    for partitie in listaPartitii:
        for stare in partitie:
            if len(partitieNoua) == 0 or len(partitie) == 1:
                partitieNoua.append({stare:partitie[stare]})
            else:
                for par in partitieNoua:
                    if stariAproapeEgale(partitie[stare] , par[random.choice(list(par.keys()))]):
                        par[stare] = partitie[stare]
                        break
                else:
                    partitieNoua.append({stare: partitie[stare]})
    return partitieNoua

def reFactor(partiii):
    for partitie in partitii:
        for stare in partitie:
            for litera in partitie[stare]:
                for partitie2 in partitii:
                    if partitie[stare][litera][0] in partitie2:
                        partitie[stare][litera][1] = partitii.index(partitie2)

with open("minimalDFA.in")as f:
    alfabet = f.readline().strip().split()
    finale = f.readline().strip().split()
    tranzitii = f.readline().strip().split()
    dicTranzitii = {}
    for stare in tranzitii:
        dicTranzitii[stare] = {}
    for linie in f:
        tranz = linie.strip().split()
        dicTranzitii[tranz[0]][tranz[1]] = [tranz[2],None]

partitii = []
A = {}
B = {}
for stare in dicTranzitii:
    if stare in finale:
        B[stare] = dicTranzitii[stare]
    else:
        A[stare] = dicTranzitii[stare]
partitii.append(A)
partitii.append(B)
reFactor(partitii)

parAux = partitionare(partitii)
reFactor(parAux)

###incepem sa partitionam
#print("FUNCTIA DE TRANZITIE")
#afisare(dicTranzitii)
#print("PARTITIA 1")
#afisarePatitie(partitii)
#i = 2
while parAux != partitii:
    partitii = partitionare(partitii)
    reFactor(partitii)
    #print("PARTITIA",i)
    #i += 1
    #afisarePatitie(partitii)
    parAux = partitionare(parAux)
    reFactor(parAux)
print("PARTITIILE FINALE DUPA MINIMIZARE")
afisarePatitie(partitii)
