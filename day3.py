#dictionaries in python
# rules 
# unordered items do not have a specific order and access them by their kes
# mutable you can add  remove nad modify key value pairs
# keys are unique:each ke in a dictionary is unique
my_dict={"name":"kyalo","age":22,"tribe":"Kamba"}
print(my_dict)
# #mehod clear
# my_dict.clear()
# print(my_dict)
#mthod copy
backup=my_dict.copy()
print(backup)

#fromkeys
keys=["name","age","city"]
values="unknown"
default=dict.fromkeys(keys,values)
print(default)
#get method
getting=backup.get("age")
print(getting)

key1=backup.keys()
print(key1)

value1=my_dict.values()
print(value1)

all_items=backup.items()
print(all_items)

popping=backup.pop("tribe")
print(popping)

print(backup)

#pop item
pop_item=my_dict.popitem()
print(pop_item)
print(my_dict)

new_dict={"name":"lenox","country":"kenya"}
setdefault=new_dict.setdefault("name","Mjaka")#ignored as name key already has a value
print(setdefault)

#update
updating=my_dict.update(new_dict)#we updated the old dict here
print(my_dict)

# merging the keys with values
new_keys=["school","gender","class"]
new_values=["Barani","Male",8]
complete_dict=dict(zip(new_keys,new_values))
print(complete_dict)

#