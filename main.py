import functions

produits =["Prod1","Prod2","Prod3","Prod4","Prod5","Prod6","Prod7"]
Prix=[100,2000,450,663,21,1068,20]


functions.getdata("produits.txt",produits,"Prix.txt", Prix)

# #1
ConbinList= functions.ConbainList(produits,Prix)
print(ConbinList)
# print("---------------------------------------------------------------------------------------------")
#
# #2
# Filter30 = functions.Filter3(ConbinList)
# print(Filter30)
# print("---------------------------------------------------------------------------------------------")
#
# #3
# FilterPaires = functions.FilterPaire(ConbinList)
# print(FilterPaires)
# for x in FilterPaires:
#     print (f"{x[0]} Cout {x[1]} DH")
# print("---------------------------------------------------------------------------------------------")
#
#
# #4-5
# SortingList = functions.Sorting(ConbinList)
# print("SortingList :",SortingList)
# print("---------------------------------------------------------------------------------------------")
#
# #7-1
# PrixCher = functions.GetMax(ConbinList)
# print("Max Prod:",PrixCher[0][0], "Prix :",PrixCher[0][1])
# print("---------------------------------------------------------------------------------------------")
#
# #4
# ConbinList.sort(key=lambda x : x[1], reverse=False)
# print(ConbinList)
# print("---------------------------------------------------------------------------------------------")
#
# #7-2
# MinList=functions.GetMin2(ConbinList)
# print("Min Prod :",MinList[0][0], "Prix :",MinList[0][1])
# print("---------------------------------------------------------------------------------------------")
#
#
# #8
# Lux = list(map(lambda x : x[1] >= 1000, ConbinList))
# print(Lux)
# print("Lux :",len(Lux))
# for i in range(0,(len(Lux))):
#     if Lux[i] == True:
#         print(f"{ConbinList[i][0]} Cout {ConbinList[i][1]} DH (LUXE)")
#     elif Lux[i] == False:
#         print(f"{ConbinList[i][0]} Cout {ConbinList[i][1]} DH")
#
# print("---------------------------------------------------------------------------------------------")
#
# #plus
# Min = ConbinList[0]
# print("Min Prod:",Min[0], "Prix :",Min[1])
# Max = ConbinList[-1]
# print("Max Prod:",Max[0], "Prix :",Max[1])
# print("---------------------------------------------------------------------------------------------")
#
# Lux1 = list(map(lambda x : f"{x[0]} Cout {x[1]} DH (LUXE)" if x[1] >= 1000  else f"{x[0]} Cout {x[1]} DH" , ConbinList))
# print(Lux1)
# -----------------------------------------------------------------
# functions.AddProduct(produits,Prix)
functions.RemoveProduct(ConbinList,produits)
print(ConbinList)

