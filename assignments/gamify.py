"""
ESC180 Assignment 1: Gamify
Lynn Tao
September 28, 2024
"""

def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health
    global cur_star, cur_star_activity
    global last_star_time, last_last_star_time

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    global tired
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = ""

    last_star_time = -200
    last_last_star_time = -400
    
    bored_with_stars = False
    tired = False
    
    last_activity = ""
    last_activity_duration = 0
    
    cur_time = 0
    last_finished = -1000
            

def star_can_be_taken(activity):
    '''
    finds whether or not a star can be taken for a current activity (can take if it's not bored)
    parameters: (str) activity is the activity to offer the star for
    return: boolean whether or not user is able to take the star 
    '''
    global bored_with_stars

    if (cur_time - last_last_star_time < 120):
        bored_with_stars = True

    return (not bored_with_stars)
        

def perform_activity(activity, duration):
    '''
    does a specified activity and updates hedons + health points for specified duration
    parameters: (str) activity is the activity to be performed, (int) duration is number of minutes to perform it for
    return: none; sets global variables
    '''

    global cur_health, cur_hedons, cur_star, cur_time, last_activity, last_finished, tired, last_activity_duration
    
    previous_time = 0 # time taken for the same activity immediately before

    if (last_activity == activity):
        previous_time = last_activity_duration

    if (activity == "running"):
        # more than 3 hours of running already -> 1 health point per additional minute
        if (previous_time > 180):
            cur_health += duration
            
        # reached 3 hours after running current amount -> full 180*3 health points plus 1 point per additional minute
        elif (duration + previous_time > 180):
            cur_health += 180 * 3 - previous_time * 3 + (duration + previous_time - 180) 
        
        # under 3 hours -> 3 health points per minute
        else:
            cur_health += duration*3

        # tired
        if (tired):
            cur_hedons += (-2)*duration

        # not tired (also means that user did NOT just finish running immediately before)
        else:
            # -2 hedons per min for every min after 10
            if (duration > 10):
                cur_hedons += 2 * 10
                cur_hedons += (-2) * (duration - 10)

            else:
                cur_hedons += 2*duration

        tired = True

        


    elif (activity == "textbooks"):
        # textbooks always gives 2 health points per minute
        cur_health += 2*duration

        if (tired):
            cur_hedons += (-2)*duration
        
        # not tired (also means the user did NOT just finish carrying textbooks immediately before)
        else:
            if (duration > 20):
                cur_hedons += 20 * 1 + (duration - 20) * (-1)

            else:
                cur_hedons += duration * 1

        tired = True

    elif (activity == "resting"):
        # resting for 120 mins or more in total means user is no longer tired
        if (duration + previous_time >= 120):
            tired = False

    # not running, textbooks, or resting
    else:
        return
        
    # using star
    if cur_star == activity:
        if duration + previous_time  <= 10:
            cur_hedons += 3*duration
        else:
            cur_hedons += 30

    cur_star = None
    cur_time += duration
    last_finished = cur_time
    last_activity_duration = duration + previous_time
    last_activity = activity

def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    '''
    offers a star for an activity
    parameters: (str) activity is the activity to be offered a star for
    return: none; sets global variables
    '''

    global cur_star, bored_with_stars, last_star_time, last_last_star_time

    if star_can_be_taken(activity):
        cur_star = activity
    else:
        cur_star = None

    last_last_star_time, last_star_time = last_star_time, cur_time


        
def most_fun_activity_minute():
    '''
    finds the activity that would give most hedons if user performed it for 1 minute right now
    parameters: none
    return: "running", "textbooks", or "resting"
    '''

    running_hedons = 0
    textbook_hedons = 0
    resting_hedons = 0


    # not tired also means user hasn't ran or carried textbooks in 2 hours (last activity must've been resting or just started simulation)
    if (not tired):
        running_hedons = 2
        textbook_hedons = 1    

    # tired (last activity was running/textbooks OR rested for less than 2 hours)
    else:
        running_hedons = -2
        textbook_hedons = -2

    # check stars
    if (cur_star == "running"):
        running_hedons += 3

    elif (cur_star == "textbooks"):
        textbook_hedons += 3


    # find max between running, textbook, and resting hedons
    if (running_hedons > textbook_hedons and running_hedons > resting_hedons):
        return "running"
    elif (textbook_hedons > running_hedons and textbook_hedons > resting_hedons):
        return "textbooks"
    else:
        return "resting"
    
    
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        

if __name__== "__main__":
    initialize()