#my list
my_list=[1,2,3,4,4,16,19,10]
print(my_list)
#append method
my_list.append(5)
print(my_list)

#extend method
my_list.extend([6,7,8])
print(my_list)
#insert method
my_list.insert(4,10)
print(my_list)
#remove method
my_list.remove(10)
print(my_list)
#pop method
popping=my_list.pop(7)
print(my_list,"removed element:",popping)
#index method
my_list.index(5)
print(my_list)
#count method
count=my_list.count(4)
print(count)
#sort method
my_list.sort()
print(my_list)
#reverse method
my_list.reverse()
print(my_list)
#length method
length=len(my_list)
print(length)
#maximum method
minimum=min(my_list)
print(minimum)
#checkin element
check=3 in my_list
print(check)

undo_delete=my_list.copy()

#clear method
my_list.clear()
print(my_list)


print(undo_delete)