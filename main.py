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
print("SortingList :",SortingList)

#7-1
PrixCher = functions.GetMax(ConbinList)
print("Max Prod:",PrixCher[0][0], "Prix :",PrixCher[0][1])

#4
ConbinList.sort(key=lambda x : x[1], reverse=False)
print(ConbinList)

#7-2
MinList=functions.GetMin2(ConbinList)
print("Min Prod :",MinList[0][0], "Prix :",MinList[0][1])


#8




#plus
Min = ConbinList[0]
print("Min Prod:",Min[0], "Prix :",Min[1])
Max = ConbinList[-1]
print("Max Prod:",Max[0], "Prix :",Max[1])



