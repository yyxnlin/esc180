def get_dict_by_date(movies):
    dict = {}

    for key, val in movies.items():
        if val[0:15] == "a long time ago":
            if 0 in dict.keys():
                dict[0].append(key)
            else:
                dict[0] = [key]
        else:
            year = int(val[0:4])
            if year in dict.keys():
                dict[year].append(key)
            else:
                dict[year] = [key]
    return dict


def movies_by_release_year(movies):
    res = []
    dict = get_dict_by_date(movies)
    for val in sorted(dict.items(), reverse=True):
        res.extend(val[1])

    return res

movies = {"Dude, Where’s My Death Star": "a long time ago, in a galaxy far far away",
"Star Wars: The Force Awakens": "2015, in Los Angeles",
"Star Wars": "1977, in Los Angeles",
"Sleepless in Aldera": "a long time ago, in Alderaan City",
"Jurassic World": "2015, in New York"}

print(movies_by_release_year(movies))