def linearSearch(item):
    for i in range(0,len(arrayData)):
        if arrayData[i]==item:
            return True
    return False

arrayData = [10,5,6,7,1,12,13,15,21,8]
item = int(input("Input integer to be searched: "))

result = linearSearch(item)

if result == True:
    print("Value is found")
else:
    print("Value is not found")

def bubbleSort():
    for x in range(0,10):
        for y in range(0,9):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

bubbleSort()
print(str(arrayData))

