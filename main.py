
def findFactors(arr, index):
    res = []
    num = abs(int(arr[index]))
    for x in range(1,num+1):
        if num % x == 0:
            res.append(x)
    return res

def findPQ(pArr, qArr):
    pq = []
    for q in qArr:
        for p in pArr:
            pq.append(p/q)
            pq.append(-p/q)
    return pq

def printFixedLen(item):
    if item >= 0:
        print(f" {item} ",end="")
    else:
        print(f"{item} ",end="")

def calculate(memArr, pqArr, maxIndex, pqUsedArr):
    for pq in pqArr:
        resFromPrevCol=0
        tempRes=[]
        for member in memArr:
            temp = pq * resFromPrevCol + int(member)
            resFromPrevCol = temp
            tempRes.append(temp)
        if tempRes[maxIndex]==0:
            printFixedLen(pq)
            print(f"|",end="")
            printArr(tempRes)
            pqUsedArr.append(pq)
            if maxIndex == 1:
                #pqUsedArr.append(-tempRes[0])
                return pqUsedArr
            return calculate(tempRes, pqArr, maxIndex-1, pqUsedArr)

def getBracket(pqUsed):
    if pqUsed >= 0:
        return f"(x+{pqUsed})"
    return f"(x{pqUsed})"

def printRes():
    for pqUsed in pqUsedArr:
        print(getBracket(-pqUsed),end="")
    print()

def printArr(arr):
    for x in arr:
        printFixedLen(float(x))
    print()

members = input("Enter absolute members of polynom (divided by spaces): ")
print()
memArr = members.split(" ")

pqUsedArr = []
maxIndex = len(memArr)-1
pArr = findFactors(memArr,maxIndex)
qArr = findFactors(memArr,0)
pqArr = findPQ(pArr,qArr)
print(f"  –  |",end="")
printArr(memArr)
pqUsedArr = calculate(memArr, pqArr, maxIndex, pqUsedArr)
if pqUsedArr:
    string = ""
    for x in range(0,len(memArr)*6+5):
        string += "–"
    print(string)
    printRes()
print()
input("Press ENTER to exit")

