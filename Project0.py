# read docs in github by using requests to get url n go through it
#remove stopwords,lemma,stems,normalize...in order
# tokenize text and use gensim n find out the percentage of similartyusing some model

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
#from nltk.tokenize import RegexpTokenizer
#from nltk.tokenize import word_tokenize
def Processed_Words():
	#file open n read
	filename = "list1.py"
	file  = open(filename, "rt")
	text = file.read()
	#new_code = open('filtered_file.txt')
	#removing comments from code
	'''for line in filename:
		if not line.startswith('#'):
			new_code.write(line)'''
	#removing noise
	text = re.sub("(<.*?>)"," ",text)	
	text = re.sub("(\\W|\\d)"," ",text)
	text = text.strip()	
		
	#splitting to words/tokens
	tokens = word_tokenize(text)
	#lemmization
	'''for words in tokens:
		terms = words.lemmatize(w)'''
	lemmatizer = WordNetLemmatizer()	
	lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in tokens])	
	#remove stop words for docs
	# remove punctuation marks
	#Normalizing case
	words = [words.lower() for words in tokens]
	#print(words)
	#file.close()	

	return words 

#Substring to compare	
def make_kgrams(s, k):
	grams = []
	start, end = 0, k
	while start < len(s) - k + 1:
		grams.append(s[start:end])
		start += 1
		end += 1
	return grams



