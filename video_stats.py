from collections import Counter
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# gets top five most occuring word
def getTopWordCount(text_list):
	counter = Counter(text_list)
	word_count = counter.most_common()
	return word_count[0:5]


# gets sentiment of transcript text
def getSentiment(text_list):
	text = " ".join(text_list) # has to be joined as a string for NLTK sentimentAnalyzer to work
	sia = SentimentIntensityAnalyzer()
	return sia.polarity_scores(text)
