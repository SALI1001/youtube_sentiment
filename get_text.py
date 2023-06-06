import sys
from youtube_transcript_api import YouTubeTranscriptApi

# gets videoID from URL
# this is needed for youtube_transcript_api
def getID(url):
	return url.partition("?v=")[2]
	

# checks if video has transcript
# Pulls transcript if so
def getTranscript(id):
	try:
		srt = YouTubeTranscriptApi.get_transcript(id,languages=['en'])
		return srt
	except:
		print("It seems this video has no transcript..")
		exit()


# pulls only relevant text data from transcript
def getText(url):
	id = getID(url)
	transcript = getTranscript(id)

	video_text = ""
	for video_dict in transcript:
		if "text" in video_dict:
			video_text+= video_dict["text"]
	return video_text

