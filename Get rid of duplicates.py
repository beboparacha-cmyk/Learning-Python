All_Students = {
    "ID#1": {"name": "Babar",  "Class": "VII",  "Favourite_Subjects":  "English, Urdu, Geography"},
    "ID#2": {"name": "Rayyan",  "Class": "VII",  "Favourite_Subjects":  "History, Maths, Islamiat"},
    "ID#3": {"name": "Hamza",  "Class": "VII",  "Favourite_Subjects":  "Geography, Science, Computer"},
    "ID#4": {"name": "Rayyan",  "Class": "VII",  "Favourite_Subjects":  "Islamiat, Maths, History"},
}

result = {}
seen_keys = []

for student_id, details in All_Students.items():
    unique_key = (details["name"], details["Class"], details["Favourite_Subjects"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, "i", v) 