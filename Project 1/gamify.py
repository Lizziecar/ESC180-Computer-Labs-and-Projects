def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global cur_star, cur_star_activity, time_since_star_offered, star_times
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars, total_stars

    global is_tired, tired_time
    global time_running_consecutively

    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None

    bored_with_stars = False
    total_stars = 0
    star_times = [0,0,0]

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000

    is_tired = False
    tired_time = 0
    time_running_consecutively = 0


def shift_star_times():
    global star_times
    star_times[0] = star_times[1]
    star_times[1] = star_times[2]
    star_times[2] = 0

def star_can_be_taken(activity):
    global cur_time #retrieve variable for time
    global cur_star, cur_star_activity, time_since_star_offered #retrieve variables for the star features
    if cur_star == 1 and cur_star_activity == activity and bored_with_stars == False and cur_time == time_since_star_offered:
    #checks for if star exists, if the star is for the right activity, if the user is not bored with stars, and if no time has passed since the star was offered
        return True
    else:
        return False


def perform_activity(activity, duration):
    global cur_hedons, cur_health #retrieve varialbe information for health and hedons
    global cur_time #retrieve variable information for time
    global is_tired, tired_time #retirieve variable information for tiredness
    global cur_star, time_since_star_offered

    #running
    if activity == "running":
        global time_running_consecutively

        #health
        if duration + time_running_consecutively > 180: #time will go over 180 minutes
            time_for_3hp = 180 - time_running_consecutively
            time_for_1hp = duration - time_for_3hp

            #adds health
            cur_health += 3 * time_for_3hp + 1 * time_for_1hp

        else: #time is under 180 minutes
            #adds health
            cur_health += 3 * duration

        #increases the running time counter
        time_running_consecutively += duration


        #hedons
        if star_can_be_taken("running") == True: #Has a star for this activity
            if is_tired == False: #not tired case
                if duration > 10: #will become tired case
                    time_for_negative_2_hedons = duration - 10
                    cur_hedons += (2 + 3) * 10 + -2 * time_for_negative_2_hedons #time with star and positive hedons, and then time without star and negative hedons
                else: #won't become tired case
                    cur_hedons += (2 + 3) * duration
                is_tired = True
                tired_time = cur_time + duration #this is to get the finish time

            else: #is tired case
                time_without_star = duration - 10
                if time_without_star < 0:
                    cur_hedons += (-2 + 3) * duration
                else:
                    cur_hedons += (-2 + 3) * 10 + -2 * time_without_star #time with star and then time without star

        else: #no star
            if is_tired == False: #not tired case
                if duration > 10: #will become tired case
                    time_for_negative_2_hedons = duration - 10
                    cur_hedons += 2 * 10 + -2 * time_for_negative_2_hedons
                else: #won't become tired case
                    cur_hedons += 2 * duration
                is_tired = True

            else: #is tired case
                cur_hedons += -2 * duration


    elif activity == "textbooks":
        #health
        cur_health += 2 * duration

        #hedons
        if star_can_be_taken("textbooks") == True: #Has a star for the activity
            if is_tired == False: #not tired case
                if duration > 20: #will become tired case
                    time_for_negative_2_hedons = duration - 20
                    cur_hedons += (1+3) * 10 + 1 * 10 + -1 * time_for_negative_2_hedons #10 minutes with star, 10 minutes without star, and then the time with negative hedons
                else: #won't become tired case
                    time_without_star = duration - 10
                    if time_without_star < 0:
                        cur_hedons += (1+3) * duration
                    else:
                        cur_hedons += (1 + 3) * 10 + 1 * time_without_star

                is_tired = True

            else: #is tired case
                time_without_star = duration - 10
                cur_hedons += (-2+ 3) * 10 + -2 * time_without_star

        else: #no star
            if is_tired == False: #not tired case
                if duration > 20: #will become tired case
                    time_for_negative_2_hedons = duration - 20
                    cur_hedons += 1 * 20 + -1 * time_for_negative_2_hedons
                else: #won't become tired case
                    cur_hedons += 1 * duration
                is_tired = True

            else: #is tired case
                cur_hedons += -2 * duration

    elif activity == "resting":
        #do nothing
        pass

    else:
        #do nothing
        pass

    #if activity wasn't running
    if activity != "running":
        #reset the time_running counter
        time_running_consecutively = 0

    #changes current time
    cur_time += duration

    #checks tiredness
    if is_tired == True and activity == "resting" and cur_time >= tired_time + 120: #resets tiredness
        tired_time = 0
        is_tired = False
    elif is_tired == True and activity == "resting": #tiredness continues without change
        pass
    else: #a new tiredness begins
        tired_time = cur_time #this is to ge the finish time

    #resets star
    if cur_star == 1:
        cur_star = 0
        time_since_star_offered = 0



def get_cur_hedons(): #returns the amount of hedons the user has accumilated
    return cur_hedons

def get_cur_health(): #returns the amount of health points the user has accumilated
    return cur_health

def offer_star(activity): #gives the user a star opportunity for a specific activity, by setting the global variable
    global cur_time
    global cur_star, cur_star_activity, time_since_star_offered, time_since_first_star, total_stars, star_times, bored_with_stars

    #checks if the activity is actually one of the three activities
    if activity == "running":
        cur_star_activity = activity
    elif activity == "textbooks":
        cur_star_activity = activity
    elif activity == "resting":
        cur_star_activity = None #you can't get a star for resting
    else: #error state, so it just returns nothing
        cur_star_activity = None

    #adjust star variables
    cur_star = 1
    time_since_star_offered = cur_time


    #adjust the star times tracking
    if cur_star_activity != None:
        total_stars += 1

        if total_stars > 3: #Only have to keep track of 3 stars
            total_stars = 3
        if total_stars == 3:
            if cur_time < star_times[0] + 120:
                bored_with_stars = True
            else:
                shift_star_times()
                star_times[2] = cur_time

        elif total_stars != 3:
            star_times[total_stars-1] = cur_time

def most_fun_activity_minute():
    global cur_time #retrieve variable information for time
    global is_tired, tired_time #retirieve variable information for tiredness
    global time_running_consecutively

    #running
    if star_can_be_taken("running") == True: #Has a star for this activity
        if is_tired == False: #not tired case
            hedons_for_running = 2 + 3
        else: #is tired case
            hedons_for_running = -2 + 3

    else: #no star
        if is_tired == False: #not tired case
            hedons_for_running = 2

        else: #is tired case
            hedons_for_running = -2

    #textbooks
    if star_can_be_taken("textbooks") == True: #Has a star for this activity
        if is_tired == False: #not tired case
            hedons_for_textbooks = 1 + 3
        else: #is tired case
            hedons_for_textbooks = -2 + 3

    else: #no star
        if is_tired == False: #not tired case
            hedons_for_textbooks = 1

        else: #is tired case
            hedons_for_textbooks = -2

    #resting
    hedons_for_resting = 0

    if  hedons_for_running > hedons_for_textbooks and hedons_for_running > hedons_for_resting:
        return "running"
    elif hedons_for_textbooks > hedons_for_running and hedons_for_textbooks > hedons_for_resting:
        return "textbooks"
    elif hedons_for_resting > hedons_for_running and hedons_for_resting > hedons_for_textbooks:
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

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10

    initialize()
    offer_star("textbooks")
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("textbooks", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())