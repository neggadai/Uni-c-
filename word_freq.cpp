"""Find a most frequently used words in a text"""

from os import remove
import re

def top_3_words(text):

    words = re.split('[,-.:_;!?/ \n]+', text.lower()) 
    words = list(filter(lambda x: x != '' and x != "'" and x != "'''",words))#create new list without',''','' symbols
    uniq_words = []
    [uniq_words.append(x) for x in words if x not in uniq_words]
    count_word_list =[]
    
    for word in uniq_words:
        count = words.count(word)
        count_word_list.append((count,word))
    
    count_word_list.sort(reverse=True)
    top = [x[1] for x in count_word_list]
    return top[0:3]
