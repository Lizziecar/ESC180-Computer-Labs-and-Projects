def display_current_value():
    print("Current Value:", current_value)

def add(to_add):
    global current_value

    #track previous value
    global previous_value
    previous_value = current_value

    #opperation:
    current_value += to_add

def subtract(to_subtract):
    global current_value

    #track previous value
    global previous_value
    previous_value = current_value

    #opperation:
    current_value -= to_subtract

def multiply(to_multiply):
    global current_value

    #track previous value
    global previous_value
    previous_value = current_value

    #opperation:
    current_value *= to_multiply

def divide(to_divide):
    global current_value

    #track previous value
    global previous_value
    previous_value = current_value

    #opperation:
    current_value /= to_divide

def store_value_m():
    global current_value

    #track previous value
    global previous_value
    previous_value = current_value

    global stored_m
    stored_m = current_value

def recall_value_m():
    global current_value

    #track previous value
    global previous_value
    previous_value = current_value

    global stored_m
    current_value = stored_m

def undo():
    global current_value
    global previous_value

    current_value,previous_value = previous_value, current_value



if __name__ == "__main__":
#initialize the two important variables
    current_value = 0
    stored_m = 0
    previous_value = 0

#opening message
    print("Welcome to the calculator program")
    display_current_value()


    #Actual calculator
    #whatever code you want
