import functions

produits =[]
Prix=[]

with open("Produits.txt","r") as file:
    for line in file:
        produits.append(line.strip())
print(produits)

with open("Prix.txt","r") as file:
    for line in file:
        Prix.append(int(line.strip()))
print(Prix)

#1
ConbinList= functions.ConbainList(produits,Prix)
print(ConbinList)

#2
Filter30 = functions.Filter3(ConbinList)
print(Filter30)

#3
FilterPaires = functions.FilterPaire(ConbinList)
print(FilterPaires)
for x in FilterPaires:
    print (f"{x[0]} Cout {x[1]} DH")

#4-5
SortingList = functions.Sorting(ConbinList)
print(SortingList)






