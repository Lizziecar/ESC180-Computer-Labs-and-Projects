f = open("versedog.txt", encoding = "latin1")
s = f.read()
print(s)

s.split("\n")

"Engineers rule the world".split(" ")

s.split("\n")[11]

def num_words(text):
    return len(text.split(" "))

def num_words_file(filename):
    f = open(filename, encoding = "latin1")
    s = f.read()
    return len(s.split(" "))

def num_sentences(text):
    #assume that sentences are separated
    #by "!"s and "."s and "?"s
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    return len(text.split("."))

#something about translation who knows