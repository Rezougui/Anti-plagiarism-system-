from similarity import *
from getQuery import *
# from htmlstrip import *
# from extractdocx import *
from googleSearch import *

# -----------------------

import codecs
import traceback
import sys
import operator
import urllib
import urllib.request
import urllib.parse
import json as simplejson
import numpy as np
import time
import random


def plagait(text):

    queries = text_to_query(text)
    # queries = [' '.join(i) for i in getQueries(text, 8)]
    # print(queries)
    count = 0
    result = []
    result_line = []
    for i in queries:

        """
            if count > 8:
                time.sleep(2+random.randint(0, 15))
                count = 0
        """

        count += 1
        if len(i) < 60:
            continue

        content = search_content(i)
        # print("\n ---------->"+content)
        content_query = text_to_query(content)

        max = 0
        for j in content_query:
            # r1.append(cosineSim(j, i))
            temp = cosineSim(j, i)
            if(temp > max):
                max = temp

        result_line.append(max)
        result_line.append(i)
        result_line.append(isPlagait(max))
        result.append(result_line)
        result_line = []

    # print(result)
    # print(queries_text)
    # plagait_percentage = np.average(result)

    return result


def isPlagait(data):
    if data > 0.75:
        return -1
    if data < 0.50:
        return 1
    else:
        return 0


# text2 = "Casablanca possède certaines des plus grandes mosquées de la planète, notamment la mosquée Hassan-II. Ville martyre, 440 ans après avoir été rasée par les ..."
"""
text = "La problématique de cet écrit sera de démontrer en quoi le marketing B to B est spécifique bien qu’il emprunte au marketing « classique » un certain  nombre de techniques, il les adapte intelligemment aux caractéristiques propres des " +\
    "marchés B to B en défi nissant des outils spécifiques pour atteindre ses objectifs. A travers, le marché du mobilier de bureau, avec l’exemple de « Steelcase » nous pourrions voir combien il est complexe d’adapter un produit B to B à une cible bien spécifique(secteur de l’offs hore) et face à une concurrence très rude"


text3 = "Le marketing Business to Business (B to B) est le marketing des entreprises qui vendent des "

print(plagait(str(text)))
"""

# plagia("J’ai travaillé comme un Freelancer sur un projet de création d'un site web vitrine à base de WordPress « https: : // cd sa com » qui représente les services d'une Agence en Arabie Saoudite s’appelle « Colors design" +
#       "advertising agency » Ce site satisfait tous les besoins de client un moderne design, supporte deux langue, sécurisé ")

# plagia(Casablanca possède certaines des plus grandes mosquées de la planète , notamment la mosquée Hassan-II. Ville martyre, 440 ans après avoir été rasée par les\xa0...)

# plagia("Pour utiliser ce vérificateur de plagiat, copiez puis collez votre contenu dans l’encadré ci-dessous. Cliquez ensuite sur le gros bouton rouge « Vérifier le Plagiat ! » et votre article sera scanné pour détecter tout contenu dupliqué.")

# plagia("Le marketing Business to Business (B to B) est le marketing des entreprises qui vendent des biens ou des services à d’autres professionnels. Le marketing B to B est parfois appelé en français marketing d’entreprise à entreprise, marketing industriel, marketing professionnel, ou encore marketing d’affaires. Le marketing B to B n’est, à priori, pas une matière que l’on pourrait imaginer passionnante, or en l’étudiant de plus près, on s e rend compte que l’on a beaucoup à apprendre et combien cela peut être enrichissant.")

# plagia("D’après les profils existants, on identifie quatre facteurs externes du système : locataire, administrateur, agence/propriétaire et visiteur. Ils peuvent tous s’identifier sauf le visiteur, comme ils peuvent accéder au panneau de gestion correspondant à leur rôle. Le visiteur peut aussi réserver une voiture et réclamer un problème.")
