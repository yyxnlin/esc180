# ESC180 Lab 3
# September 25, 2024

# question 3

# def display_current_value():
#     global current_value
#     print(current_value)


# def add(to_add):
#     global current_value
#     update_last_value()
#     current_value += to_add

# def mult(to_mult):
#     global current_value
#     update_last_value()
#     current_value *= to_mult

# # zero doesn't work
# def div(to_div): 
#     global current_value
#     update_last_value()
#     current_value /= to_div

# def update_memory():
#     global recall
#     recall = current_value

# def get_recall():
#     return recall

# def update_last_value():
#     global last_value
#     global last_last_value
#     temp = last_value
#     last_value = current_value
#     last_last_value = temp

# def undo():
#     global current_value
#     global last_value

#     current_value, last_value = last_value, current_value

# def undo2():
#     global current_value
#     global last_value
#     global last_last_value

#     temp = last_value
#     last_value = current_value
#     current_value = last_last_value
#     last_last_value = temp

# if __name__ == "__main__":
#     current_value = 0
#     last_value = 0
#     last_last_value = 0

#     operation = " "

#     add(5)
#     display_current_value()
#     mult(5)
#     display_current_value()
#     add(-3)
#     display_current_value()
#     undo2()
#     display_current_value()




# question 4
def drink_coffee():
    global last_coffee_time, last_coffee_time2, too_much_coffee

    

    if (current_time-last_coffee_time2 < 120):
        too_much_coffee = True

    last_coffee_time2 = last_coffee_time
    last_coffee_time = current_time

    

def study(minutes):
    global knols
    global current_time
    global too_much_coffee

    

    if (too_much_coffee == False and last_coffee_time == current_time):
        knols += 10*minutes
    elif (too_much_coffee == False or last_coffee_time2 == -100):
        knols += 5*minutes
    
    current_time += minutes


def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -1000

initialize()
if __name__ == '__main__':
    initialize() # start the simulation
    study(60) # knols = 300
    print(knols)
    study(20) # knols = 400
    print(knols)

    drink_coffee() # knols = 400

    study(10) # knols = 500
    print(knols)

    drink_coffee() # knols = 500

    study(10) # knols = 600
    print(knols)
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes

    study(10) # knols = 600
    print(knols)



