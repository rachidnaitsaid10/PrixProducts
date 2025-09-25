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
ConbinList =list(zip(produits,Prix))
print(ConbinList)

#2
Filter30 = list(filter(lambda x : x[1] >= 30, ConbinList))
print(Filter30)

testfilter = functions.Filter3(ConbinList)
print(testfilter)

#3
FilterPaires = list(filter(lambda p : p[1]%2==0, ConbinList))
print(FilterPaires)
for x in FilterPaires:
    print (f"{x[0]} Cout {x[1]} DH")

#4-5
ConbinList.sort(key=lambda x : x[1])
print(ConbinList)






