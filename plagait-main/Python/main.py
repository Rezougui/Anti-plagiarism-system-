#!/usr/bin/env python
import json
import sys


from plagiat import *
from docx_to_txt import *


def main():

    if len(sys.argv) < 3:
        print("Usage: python main.py <input-filename>.txt <output-filename>.txt")
        sys.exit()
    if sys.argv[1].endswith(".docx"):
        text = docx_to_txt(sys.argv[1])
    else:
        text = open(sys.argv[1], 'r', encoding='utf-8')
        if not text:
            print("Invalid Filename")
            print("Usage: python main.py <input-filename>.txt <output-filename>.txt")
            sys.exit()
        text = text.read()

    output = plagait(str(text))

    with open(sys.argv[2]+".json", 'w', encoding='utf-8') as outfile:

        json.dump(output, outfile)


main()


#text = "Thanks for the answers above. Here's how I did it, I hope it helps those who follow. I'm looking to pass a registration number from one page to another, hence regName and regValue: Create your first page, call it set_reg.php: "

# print(plagait(str(text)))
