'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):

    #denominator as a whole
    denominator = norm(vec1)*norm(vec2)

    #Numerator
    numerator = 0
    for i in vec1:
        for j in vec2:
            if i == j:
                numerator += vec1[i] * vec2[j]


    #final value
    return numerator/denominator

def build_semantic_descriptors(sentences):
    d = {}
    for sentence in range(len(sentences)):
        unique_words = []
        for word in range(len(sentences[sentence])):
            if sentences[sentence][word] not in unique_words:
                unique_words.append(sentences[sentence][word])

        for keyword in unique_words:
            if keyword not in d:
                d[keyword] = {}
            for compare_word in unique_words:
                if keyword != compare_word:
                    if compare_word in d[keyword]:
                        d[keyword][compare_word] += 1
                    else:
                        d[keyword][compare_word] = 1

    return d





def build_semantic_descriptors_from_files(filenames):
    f = ""
    for i in range(len(filenames)):
        k = open(filenames[i], "r", encoding="latin1").read()
        f += k

    #remove punctuation
    f = f.lower()
    f = f.replace(","," ")
    f = f.replace("-"," ")
    f = f.replace(";"," ")
    f = f.replace(":"," ")
    f = f.replace("\n"," ")

    #Form Sentences
    f = f.replace("!", ".")
    f = f.replace("?", ".")

    #split into sentences
    no_punc_file = f.split(".")
    sentence_list = []
    #split sentences into words
    for i in range(len(no_punc_file)):
        sentence_list.append(no_punc_file[i].split())

    d = build_semantic_descriptors(sentence_list)
    return d


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similarities = []
    for i in range(len(choices)):
        if word in semantic_descriptors and choices[i] in semantic_descriptors:
            similarities.append(similarity_fn(semantic_descriptors[word],semantic_descriptors[choices[i]]))
        else:
            similarities.append(-1)

    most_similar = 0
    similar_index = 0
    for i in range(len(similarities)):
        if similarities[i] > most_similar:
            most_similar = similarities[i]
            similar_index = i

    return choices[similar_index]



def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    #read the file
    f = open(filename, "r", encoding="latin1").read()
    file_lines = f.split("\n")
    similarity_sets = []

    #split sentences into words
    for i in range(len(file_lines)-1):
        similarity_sets.append(file_lines[i].split())

    #create lists for words
    words = []
    answers =[]
    choices = [[]] * len(similarity_sets)
    for i in range(len(similarity_sets)):
        words.append(similarity_sets[i][0])
        answers.append(similarity_sets[i][1])
        choices[i] = []
        for j in range(2, len(similarity_sets[i])):
            choices[i].append(similarity_sets[i][j])

    #find synonyms
    amount_correct = 0
    for i in range(len(similarity_sets)):
        if most_similar_word(words[i], choices[i], semantic_descriptors, similarity_fn) == answers[i]:
            amount_correct += 1

    return (amount_correct/len(similarity_sets))*100





if __name__ == "__main__":
    sentences = [["i", "am", "a", "sick", "man"],
    ["i", "am", "a", "spiteful", "man"],
    ["i", "am", "an", "unattractive", "man"],
    ["i", "believe", "my", "liver", "is", "diseased"],
    ["however", "i", "know", "nothing", "at", "all", "about", "my",
    "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    filenames = ["WarAndPeace.txt"]

    sem_descriptions = build_semantic_descriptors_from_files(filenames)
    res = run_similarity_test("test.txt", sem_descriptions, cosine_similarity)
    print(res, "% correct")


