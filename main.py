import functions

produits =[]
Prix=[]

functions.getdata("produits.txt",produits,"Prix.txt", Prix)



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

#7
PrixCher = functions.GetMax(ConbinList)
print("Max :",PrixCher)







