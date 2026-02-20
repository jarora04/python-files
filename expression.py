import re
pattern=r"\n"
text='''
Written collaboratively by largely anonymous volunteers, known as Wikipedians, Wikipedia articles can be edited by anyone with Internet access (and who is not presently blocked), except in limited cases where editing is restricted to prevent disruption or vandalism. Since its creation on January 15, 2001, it has grown into the world's largest reference website,Fritten attracting over a billion visitors monthly. Wikipedia currently has more than sixty-two million articles in more than 300 languages, including 6,764,724 articles in English, with 115,413 active contributors in the past month
'''

# match =re.search(pattern,text)
# print(match)
#it is used to find the matches in the text

matches=re.finditer(pattern,text)
for match in matches:
    # print(text[match.span()[0]:match.span()[1]])
#used to print the text
    print(match)
#print he match of the  letters in the text
