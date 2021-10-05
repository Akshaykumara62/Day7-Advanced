list1=[10,20,30,40,50]
list2=[5,15,25,35,45,60]
size_1 = len(list1)
size_2 = len(list2)
list3 = []
i,j = 0,0

while i < size_1 and j < size_2:
    if list1[i] < list2[j]:
        list3.append(list1[i])
        i+=1
    else:
        list3.append(list2[j])
        j+=1
list3 = list3+list1[i:] +list2[j:]
print("The Merged sorted list is: " +str(list3))