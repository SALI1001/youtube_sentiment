from get_text import getText
from clean import cleanText
from video_stats import getTopWordCount, getSentiment
import sys

# prettify the text for output
def textFormatWordCount(wc_list):
	print("Word Count:")
	print()
	for word_tuple in wc_list:
		print(f"{word_tuple[0]} : {word_tuple[1]}")
	print()
	print()
	


def main(url):
	#test_url = "https://www.youtube.com/watch?v=xWL40q3DMoQ"
	text = getText(url)
	cleaned_text = cleanText(text)
	top_word_count = getTopWordCount(cleaned_text)
	textFormatWordCount(top_word_count)
	print("Sentiment:")
	print()
	print(getSentiment(cleaned_text))


if __name__ == "__main__":
    main(sys.argv[1])
