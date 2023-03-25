import sys


#tranformers is a package and pipeline is  a module in that package
from transformers import pipeline

from youtube_transcript_api import YouTubeTranscriptApi

#youtube_video = "https://www.youtube.com/watch?v=aOL7wzEIZSc"

print("Python program execution started.......................")
youtube_video_URL = sys.argv[1]
print("video_URL=" ,youtube_video_URL)

video_id = youtube_video_URL.split("=")[1]
print("video_id=" ,video_id)

lang_code = sys.argv[2]
print("lang_code=" ,lang_code)

lang_list = []
lang_list.append(lang_code)
print("lang_list =" ,lang_list)

print("checking......................." )

try:
    srt = YouTubeTranscriptApi.get_transcript(video_id)
except:
    print("This vidoe doesn't have a transcript")
    sys.exit("This vidoe doesn't have a transcript") 

print("Collecting transcript.......................")       
#gt_list = YouTubeTranscriptApi.get_transcript(video_id)
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

transcript = transcript_list.find_transcript(lang_list)

gt_list = transcript.fetch()


result = " "
for d in gt_list:
    result += ' ' + d['text']

print("Length of transcript =",len(result))
print("Transcript:")
print(result)
print("===========================================================")


summarizer = pipeline('summarization')

#num_iters = int(len(result)/1000)
num_iters = 2
summarized_text = [] 
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  out = summarizer(result[start:end])
  print("iteration i = " , i)
  print("start = " , start)
  print("end = " , end)
  print("out=",out)
  
  print("=============================================")
  out = out[0]
  out = out['summary_text']
  summarized_text.append(out)
print("sumary:")
print(summarized_text)

print("length of summarized text :",len(str(summarized_text)))


print("Python program execution completed......................." )

