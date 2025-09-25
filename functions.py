def Filter3(List):
    filter30 = list(filter(lambda x : x[1] >= 30, List))
    return filter30

def ConbainList(List1, List2):
    Conbin = list(zip(List1, List2))
    return Conbin;

def FilterPaire(list2):
    Filter = list(filter(lambda x : x[1]%2==0, list2))
    return Filter;

def Sorting(list3):
    return list3.sort(key=lambda x : x[1])

def getdata(filename1, mylist1, filename2, mylist2):
    with open(filename1,"r") as file:
        for line in file:
            mylist1.append(line.strip())
    with open(filename2,"r") as file:
        for line in file:
            mylist2.append(int(line.strip()))
    return mylist1, mylist2;

def GetMax(List0):
    MaxPrix = max(map((lambda x : x[1]), List0))
    ProductMax = list(filter(lambda x : x[1] == MaxPrix, List0))
    return ProductMax;

def GetMax2(List3):
    MaxPrix = max(map((lambda x : x[1]), List3))
    ProductMax = list(filter(lambda x : x[1] == MaxPrix, List3))
    return ProductMax;

