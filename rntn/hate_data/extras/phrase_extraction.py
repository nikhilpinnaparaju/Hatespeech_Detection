import pandas
import csv
import itertools
from rake_nltk import Rake
import random

rake = Rake()

col_names = ["sentence"]
data = pandas.read_csv('datasetSentences.txt', names=col_names, sep="\t", quoting=csv.QUOTE_NONE, encoding='utf-8')

tweets = data.sentence.tolist()

tweet_label = open('hatespeech_labels.csv')
dictionary_file = open("dictionary.txt","w")
label_file = open("sentiment_labels.txt","w")

tlab = csv.reader(tweet_label)

def random_number(label):
	if label == "normal":
		return round(random.uniform(0,0.25),2)
	elif label == "spam":
		return round(random.uniform(0.25,0.5),2)
	elif label == "abusive":
		return round(random.uniform(0.5,0.75),2)
	elif label == "hateful":
		return round(random.uniform(0.5,1),2)

count = -1
c = 1
for row1,tweet in itertools.izip(tlab,tweets):
	rake.extract_keywords_from_text(tweet)
	all_phrases = rake.get_ranked_phrases()
	for phrase in all_phrases:
		dictionary_file.write(phrase.encode('utf-8')+"|"+str(count)+"\n")
		label_file.write(str(count)+"|"+str(random_number(row1[1]))+"\n")
		count += 1

	print str(c)+" tweets processed."
	c += 1



