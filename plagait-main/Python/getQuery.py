from operator import indexOf
import re


def getQueries(text, n):

    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(text)
    sentencesplits = []
    for sentence in sentenceList:
        x = re.compile(r'\W+', re.UNICODE).split(sentence)
        print("\n \t -> ")
        print(x)
        x = [ele for ele in x if ele != '']
        sentencesplits.append(x)
    finalq = []
    for sentence in sentencesplits:
        l = len(sentence)
        l = l/n
        index = 0
        for i in range(0, int(l)):
            finalq.append(sentence[index:index+n])
            index = index + n-1
        if index != len(sentence):
            finalq.append(sentence[len(sentence)-index:len(sentence)])
    return finalq


def text_to_query(text):
    n = 23
    sentenceEnders = re.compile('[.!]')
    sentenceList = sentenceEnders.split(text)
    s = []
    for sentence in sentenceList:
        if sentence != "":
            if len(sentence) >= n:
                for i in split_by_n(n, sentence):
                  #  print("------->"+i)
                    s.append(i)
            else:
                s.append(sentence)
    return s


def split_by_n(n, sentence):
    list = sentence.split()
    j = 0
    r = ""
    res = []
    for word in list:

        if j >= n:
            res.append(r)
            r = ""
            j = 0
        r = r + word+" "
        j = j+1

    res.append(list_to_string(list[len(res)*n:len(list)]))
    return res


def list_to_string(list):
    s = ""
    for i in list:
        s = s + i+" "
    return s


#text = "Le marketing Business to Business (B to B) est le marketing des entreprises qui vendent des biens ou des services à d’autres professionnels. Le marketing B to B est parfois appelé en français marketing d’entreprise à entreprise, marketing industriel, marketing professionnel, ou encore marketing d’affaires. Le marketing B to B n’est, à priori, pas une matière que l’on pourrait imaginer passionnante, or en l’étudiant de plus près, on s e rend compte que l’on a beaucoup à apprendre et combien cela peut être enrichissant."


#print(split_by_n(5, "Le marketing Business to Business (B to B) est le marketing des entreprises qui vendent des biens ou des services à d’autres professionnels"))
# print(getQueries(text, 6))

# print(text_to_query(text))


# f = open("C:/wamp64/www/iliass/Plagiarism-Checker-master/scripts/sampleText.txt", "r")
# text = f.read()
# print(len(text.split()))
# print(len(getQueries(text, 8)))
