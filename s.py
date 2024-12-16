list = [2,5]
list.append(30)
print(list)


list = [3,4]
list.extend([30,40])
print(list)


list = [3,4]
list.insert(3,5)
print(list)

list = [1,2,3]
list.remove(2)
print(list)


list = [1,2,3,4,5]
list.pop(4)
print(list)


list = ["soumya","pragya","divya","ashi","kajal"]
a= list.index("divya")
print(a)


list = [1,2,3,2,5,2,6,7,8]
a = list.count(2)
print(a)


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
print(list1 + list2)


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
print(list1*3)


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
print(list1[1:3], list2[2:4])


list = [1,2,3,4,5]
list.sort()
list.reverse()
print(list)