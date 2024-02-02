def finddob(listofNums):
    dob = 1
    for num in listofNums:
        dob *= num
    return dob
def findMax(*args):
    max = 0  
    for num in args:
        if max<num:
            max = num
    return max
def lists(list1,list2):
    combined = list1 + list2
    return combined
def findcount(listofNums):
    count = 0
    for num in listofNums:
        for i in range(2,num):
            if num%i == 0:
                break
            else:
                count +=1
    return count
def delnum(listofNums,num):
    count = 0
    for i in listofNums:
        if i == num:
            count += 1
    for i in range(0,count):
        listofNums.remove(num)
    return count
def stepnum(listofNums,num):
    list45 = []
    for i in listofNums:
        num1 = i
        for j in range(1,num):
            num1 *= i
        list45.append(num1)
    return list45








list1 = [1,2,3]
list2 = [4,5,6]
listNums = [1,2,3,4,5]
print(finddob(listNums))
print(findMax(3,4,5,6,7,8))
combList = (list1,list2)
print(combList)
print(findcount(listNums))
print(listNums)
num = int(input("Enter num to del: "))
print(delnum(listNums,num))
print(listNums)
step = int(input("enter your step: "))
print(stepnum(listNums,step))



