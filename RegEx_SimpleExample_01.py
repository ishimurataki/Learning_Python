import re
# import RegEx module

print(re.split(r'\s*', 'here are some words'))
# returns: ['here', 'are', 'some', 'words']
# r denotes a special form of python string evaluation. r'\s*' is identical to r' '.
# '\s' signifies space character. Code splits the string by space character

print(re.split(r'(\s*)', 'here are some words'))
# returns: ['here', ' ', 'are', ' ', 'some', ' ', 'words']
# () signifies to include the split-character in the returned list

print(re.split(r'[a-f]', 'lKJdlfAjsd;klfjas;'))
# returns: ['lKJ', 'l', 'Ajs', ';kl', 'j', 's;']
# [a-f] tells string to break every time a character from 'a' through 'f' is detected

print(re.split(r'[a-fA-F]', 'lKJdlfAjsd;klfjas;', re.I|re.M))
# returns: ['lKJ', 'l', '', 'js', ';kl', 'j', 's;']
# parameters in the brackets are denote ranges. Both 'a-f' and 'A-F' are included.

print(re.split(r'[a-f][a-f]', 'lKJdlfabjsd;klfjabs;', re.I|re.M))
# returns: ['lKJdl', 'bjsd;klfj', 's;']
# specific string breakers can be constructed by adding [] ranges with more [] ranges.

print(re.findall(r'\d{1,5}\s\w+\s\w+\.', 'ocinwe324 main st.asdvce'))
# returns: ['324 main st.']
# finding hidden address in a string
# '\d' denotes digits and the {} is a range of digits allowed.
# '\w' denotes words surrounded by spaces. '+' means at least one.
# '\.' denotes the period character.



