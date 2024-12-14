#    Problem 2 (20 pts)
#
#    This problem will be auto-graded.
#
#
#    Recall that links in an html file are given in the format
#    <a href = "http://engsci.utoronto.ca">EngSci homepage</a>
#    Write a function that takes in the text of an html file, and returns a dictionary
#    whose keys are the link texts (e.g. "EngSci homepage") and whose values are
#    the corresponding URLs (e.g., "http://engsci.utoronto.ca"). You can assume
#    that link texts do not repeat.
#    Sample call:
#     get_links('<a href = "http://engsci.utoronto.ca">EngSci homepage</a>')
#    should return {"EngSci homepage": "http://engsci.utoronto.ca"}

def get_links(html_text):
    dict = {}
    temp1 = html_text.split("<a href  = \"")
    for e in temp1:
        link = e.split(">")[0][9:]
        text = e.split("\">")[1].split("</a>")[0]

        dict[text] = link

    return dict

print(get_links('<a href = \"http://engsci.utoronto.ca\">EngSci homepage</a>'))