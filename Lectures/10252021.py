grades = {"PHY": "A+", "CIV": "A", "CSC": "A+", "ESC": "B+"}

del grades["PHY"]

def correct_transcript_bad(grades): #messes up because you are shrinking the list you are using as you work with it
    for course in grades:
        if grades[course] not in ["A", "A+"]:
            del grades[course]

def correct_transcript_fixed(grades): #list is based on keys rather than the list itself
    for course in list(grades.keys()):
        if grades[course] not in ["A", "A+"]:
            del grades[course]

def drop_everything_bad(grades):
    grades = {} # no effect outside function

def drop_everything_fixed(grades):
    grades.clear() #does have an effect outside the function


def make_csc_100(grades):
    grades["CSC"] = 100 #has an effect outside function

def drop_everything_fixed3(grades):
    while len(grades) > 0:
        del grades[list(grades.keys()[0])] #missing a paranthesis

if __name__ == "__main__":
    grades = {"PHY": "A+", "CIV": "A", "CSC": "A+", "ESC": "B+"}
    correct_transcript_fixed(grades)