#write a function named login
#the function takes in a user name and a password

#return "OK" if the username matches the password, unless they're three successive failed loigns.
#return "Refuse" otherwise

def login(username, password):
    global failed_logins
    if failed_logins >= 3:
        return "Refused"

    if username == "guerzhoy" and password == "ilovepython":
        failed_logins = 0
        return "OK"

    if username == "stageby" and password == "rigorous":
        failed_logins = 0
        return "OK"

    if username == "cluett" and password == "matrix":
        failed_logins=0
        return "OK"

    failed_logins += 1
    return "Refused"

def initialize():
    global failed_logins
    failed_logins = 0

initialize()

if __name__ == "__main__":

    print(login("guerzhoy", "ilovepython"))
    print(login("burh", "failed once"))
    print(login("stageby", "rigorous"))
    print(login("bruhuhuh", "hello"))
    print(login("hei", "dwad"))
    print(login("stageby", "rigorous"))
