def select_gifts(good_ratings, want_ratings):
    max_value = 0
    combined_ratings = {}
    res = []

    for key, val in good_ratings.items():
        combined_ratings[key] = val

    for key, val in want_ratings.items():
        if key in combined_ratings.keys():
            combined_ratings[key] += val

        else:
            combined_ratings[key] = val

        if combined_ratings[key] > max_value:
            res = [key]
            max_value = combined_ratings[key]

        elif combined_ratings[key] == max_value:
            res.append(key)

    return sorted(res)

good_ratings = {"Calc textbook": 5, "iPhone": 1, "Alarm clock": 4, "Notebooks": 4}
want_ratings = {"iPhone": 4, "A+ in CSC": 5, "Calc textbook": 4, "Notebooks": 5}

print(select_gifts(good_ratings, want_ratings))