student = {
"name": "Ali",
"age": 17,
"grade": "B"
}
updatedGrade=student.update()
print(student)

#get value of any key
get_item=student.get("age")
print(get_item)

#view of all keys
key1=student.fromkeys("keys","values")
print(key1)



