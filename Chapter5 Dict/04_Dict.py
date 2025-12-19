student = {"name": "Rahul", "age": 20}
print(student["name"])

#📌 4. Adding & Updating Items
student["city"] = "Delhi"      # Add
student["age"] = 21            # Update
print(student)

#📌 5. Removing Items
student.pop("age")
student.clear()

student = {"name": "Rahul", "age": 20}
for key, value in student.items():
    print(key, value)
