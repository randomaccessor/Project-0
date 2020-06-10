# read docs in github by using requests to get url n go through it
#remove stopwords,lemma,stems,normalize...in order
# tokenize text and use gensim n find out the percentage of similartyusing some model

from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer

#file open n read
filename = "xyz.txt"
file  = open(filename, "rt")
text = file.read()
file.close()
#splitting to sentences
sentences = sent_tokenize(text)
#filtering punctuation
tokenizer = RegexpTokenizer(r'\w+')