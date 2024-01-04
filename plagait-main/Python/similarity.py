# module to check cosine similarity of two strings

from bs4 import BeautifulSoup
import requests
# ***************
from operator import index
import re
import math
from collections import Counter
from typing import Sized

import numpy as np

from getQuery import *


WORD = re.compile(r'\w+')

# returns cosine similarity of two vectors
# input: two vectors
# output: integer between 0 and 1.


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())

    # calculating numerator
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    # calculating denominator
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    # checking for divide by zero
    if denominator == 0:
        return 0.0
    else:
        return float(numerator) / denominator

# converts given text into a vector


def text_to_vector(text):
    # uses the Regular expression above and gets all words
    words = WORD.findall(text)
    # returns a counter of all the words (count of number of occurences)
    return Counter(words)

# returns cosine similarity of two words
# uses: text_to_vector(text) and get_cosine(v1,v2)


def cosineSim(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    # print vector1,vector2
    cosine = get_cosine(vector1, vector2)
    return cosine


def text_to_v(text):
    # uses the Regular expression above and gets all words
    words = WORD.findall(text)
    # returns a counter of all the words (count of number of occurences)
    return words


"""

def sim(a, b):
    a = text_to_v(a)
    b = text_to_v(b)
    if len(b) < len(a):
        w = b
        b = a
        a = w

    if len(a) < 1:
        return 0

    # print(a)
    indexes = []
    for i in a:
        try:
            c = b.index(i)
        except:
            c = -1
        indexes.append(c)
    # print(indexes)

    s = 1
    index = 0
    sizes = []
    for i in indexes:
        if i != -1:
            if (index+1) < len(indexes):
                if indexes[int(index)+1] == int(i) + 1:
                    s = int(s) + 1
                    # print(s)

                else:
                    sizes.append(s)
                    s = 1
                    # print(s)
            else:
                sizes.append(s)
        index = index + 1

    # print(sizes)
    r = []
    for i in sizes:
        if i != 1:
            r.append(i)
    r = sizes
    # print(r)
    #res = (2*(np.max(r)/len(a)) + np.sum(r)/len(a))/3
    res = np.max(r)/len(a)
    # print(res)

    return res

"""


"""
result = requests.get(
    "https://www.google.com/search?q=%22Pour+cela+nous+avons+r%C3%A9alis%C3%A9+une+plateforme+web+dynamique+pour+la+location+des+v%C3%A9hicules%22&hl=fr&ei=BWUQYfiXL5L2gAam1rK4Bg&oq=%22Pour+cela+nous+avons+r%C3%A9alis%C3%A9+une+plateforme+web+dynamique+pour+la+location+des+v%C3%A9hicules%22&gs_lcp=Cgdnd3Mtd2l6EAM6FwguEOoCELQCEIoDELcDENQDEOUCEJMCOhQILhDqAhC0AhCKAxC3AxDUAxDlAjoUCAAQ6gIQtAIQigMQtwMQ1AMQ5QJKBAhBGABQ9qNbWP-7W2Dcw1toAXAAeAOAAZoBiAGqA5IBAzAuM5gBBKABAaABArABCsABAQ&sclient=gws-wiz&ved=0ahUKEwi4ru3LxqLyAhUSO8AKHSarDGcQ4dUDCA0&uact=5")

src = result.content
# print(src)

soup = BeautifulSoup(src, 'html.parser')

# print(soup)
text = soup.get_text().split("Tous les résultatsMot à mot")[1]

# print(text)

t1 = text_to_query(text)


print(t1)

t2 = "Pour cela nous avons réalisé une plateforme web dynamique pour la location des véhicules"
t2 = text_to_query(t2)
print(t2)
r1 = []
result = []
for i in t2:
    for j in t1:
        r1.append(cosineSim(j, i))
   # print(r1)
    result.append(np.max(r1))
    r1 = []
print(result)


#print(cosineSim(t1, t2))

# sim(" m  a b", "x e c d a b")
#s = sim(t2, t1)
# print(s)




"""
