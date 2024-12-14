def merge_dict(A, B):
    merged = {}

    for key, val in dict1.items():
        merged[key] = val

    for key, val in dict2.items():
        if key in merged.keys():
            merged[key] = [merged[key], val]
        else:
            merged[key] = val
    return merged

dict1 = {10: "exams", 20: "holidays", "winter": "break"}
dict2 = {30: "lights", "winter": "snow"}
print(merge_dict(dict1, dict2))
# {10: "exams", 20: "holidays", 30: "lights", "winter": ["break", "snow"]}