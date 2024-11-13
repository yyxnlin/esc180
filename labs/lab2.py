# ESC180 Lab 2
# September 18, 2024

# question 1
# def my_sqrt(x):
#     sqr = x**.5
#     return sqr

# def my_print_square(x):
#     print(x**.5)

# if __name__ == "__main__":
#     # (a)
#     # res = my_sqrt(25) # only stores the value into res, but doesn't display anything
#     # print(res)

#     # (b)
#     # sqr is a local variable only accessible inside the my_sqrt function, not outside
#     # can modify by making sqr global

#     # (c)
#     res = my_print_square(25)
#     print(res)


# question 2

# question 3
# if __name__ == "__main__":
#     current_value = 0
#     print ("Welcome to the calculator program")
#     print ("Current value: " + current_value)

# question 4
def display_current_value():
    global current_value
    print(current_value)

# if __name__ == "__main__":
#     current_value = 0
#     display_current_value()

# question 5
def add(to_add):
    global current_value
    update_last_value()
    current_value += to_add

# question 6
def mult(to_mult):
    global current_value
    update_last_value()
    current_value *= to_mult

# question 7
# zero doesn't work
def div(to_div): 
    global current_value
    update_last_value()
    current_value /= to_div

# question 8
def update_memory():
    global recall
    recall = current_value

def get_recall():
    return recall

# question 9
def update_last_value():
    global last_value
    last_value = current_value

def undo():
    global current_value
    global last_value
    temp = current_value
    current_value = last_value
    last_value = temp

if __name__ == "__main__":
    current_value = 0
    add(10)
    mult(20)
    update_memory()
    div(-10)
    display_current_value()
    # print(get_recall())
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
