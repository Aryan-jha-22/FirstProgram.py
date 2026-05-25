info = {
    "name" : "AJ",
    "subjects" : ["sst", "python"],
    "learning" : "python",
    "age" : 20,
    "is_adult" : True,
    "marks" : 98.9
}
null_dict = {}
info["age"] = 99
print(info["name"])
print(info)
null_dict["age"] = 20
print(null_dict)
# nested dictionary
student = {
    "name" : "AJ",
    "subjects" : {
        "sst" : 66,
        "python" : 98.9
    }
}

print(student["subjects"]["python"])
print(list(student.keys()))
print(len(list(student.keys())))
print(list(student.values()))
print(student.items())
pair = list(student.items())
print(pair[0])
print(student.get("name"))
print(student["name"])
student.update({"city" : "delhi"})
print(student)

# SET in PYTHON :-
collection = {1, 2, 3, 4, "Hello world"}
print(type(collection))
print(collection)
print(len(collection))
null_set = set()
print(null_set)
material = {1, 2, 3, "Hello aryan"}
material.add(4)
print(material)
material.remove(2)
print(material)
material.clear()
print(len(material))
m = {"hello", "world", "hello"}
print(m.pop())
print(m.pop())
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))
info = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(info)
subjects = {
    "python", "java", "python", "javascript", "java", "python", "java", "c++", "c"
}
print(len(subjects))
student = {}
x = int(input("enter physics"))
student.update({"physics" : x})
x = int(input("enter maths"))
student.update({"maths" : x})
x = int(input("enter chm"))
student.update({"chm" : x})
print(student)
val = {9, "9.0"}
print(val)
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)