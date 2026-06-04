import json

student = {
    "name": "Sarah",
    "course": "CSE",
    "city": "Coimbatore",
    "college": "XYZ College"
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("JSON file saved")
