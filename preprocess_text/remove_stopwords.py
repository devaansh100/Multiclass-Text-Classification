import numpy as np
from tqdm import tqdm
import random
import re
import spacy
from spacy.lang.en import STOP_WORDS
from spacy.lang.en import English
nlp = spacy.load('en_core_web_sm')
stops = STOP_WORDS

def remove_stopwords(product_detail:str):
    '''
            This function removes stopwords
            Arguemts:
            product_detail: String contating product details and labels. 
            It assumes that the input is according to fasttext format.

            Output:
            cleaned string in fasttext format
    '''
    # tokenising the text 
    tokenizer = nlp.tokenizer
    tokens = nlp(product_detail)
    words = list()

    # removing stopwords 
    for word in tokens:
        if word not in stops:
            words.append(word)

    #converting list back to string
    return " ".join(words)