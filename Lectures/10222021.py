'''#Trying to pay attention this time LOL

#Tuples
#Like lists but immutable

t = (2, 3, 4)
t[0]
t[1:]

#t[0] = 5

t = ([1,2], 3)
t[0][0] = 5
#t[0] = 6

print(t[1:])

#unpacking
t = ("a", "b", "c")
x , y, z = t

print(x)
print(y)
print(z)

#error
#x, y = t


#return a tupple

def f():
    return 42, 43'''




'''#dictionaries
# a set of key, value pairs
# keys are unique, values can repeat

grades = {"PHY": 90, "MAT": 80, "CSC": 90}
grades["MAT"]

kids = ["Bob", "Dorothy", "Alice"]
faves = ["candy", "costumes", "midterms"]
#kids[i] -> faves[i]

#rewrite as a dictionary
faves_dict = {"Bob": "candy", "Dorothy": "costumes", "Alice": "midterms"}

#Recall: grades = {"PHY": 90, "MAT": 80, "CSC": 90}
#adding something to the list
grades["CIV"] = 95


#data on the UofT endowment
endowment = {2012: 1518, 2014: 1881, 2015:2142, 2021: 3150}

#error
#endowment[[1,2]] = 5

#tupple works though
endowment[(1,2)] = 5

#return keys
grades.keys()

#return values
grades.values()

for subj in grades: #may not always give a list in the order entered
    print(f" I got {grades[subj]} in {subj}")

grades.items()

for subj, grade in grades.items():
    print(f"I got {grade} in {subj}")'''


#examples and functions

grades = {"PHY": 90, "MAT": 80, "CIV": 95, "CSC": 90}

#get all the subjects in which I got a partciular grade

def get_subj_by_grade(grade):
    res = []
    for subj, gr in grades.items():
        if gr == grade:
            res.append(subj)

    return res

#want to invert the dictionary grades:
#keys will be the grades, values will be the subjects
{90: ["PHY", "CSC"], 80: ["MAT"], 95: ["CIV"]}

def get_inv_grades(grades):
    res = {}
    for subj, grade in grades.items():
        #grade already exists in new dictionary
        if grade in res: #same as grade in grades.keys()
            res[grade].append(subj)
        #grade doesn't already exist in the new dictionary and needs a new key
        else:
            res[grade] = [subj]

    return res

#lists and dictionary stuff
L = [3, 4, 2, 1, 2, 4, 5, 6, 4, 4, 4, 7, 8]

#doesn't work
'''for i in range(len(L)):
    if L[i] == 4.0:
        del L[i]'''

i = 0
while i < len(L):
    if L[i] == 4.0: #if the value gets deleted, then the list doesn't need to increment
        del L[i]
    else:
        i += 1 #increment due to no shift