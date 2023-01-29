from pipelines import pipeline
import requests
nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl")

def gen():
    url = 'http://3.8.100.147/transpile'
    #data = {"https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"}
    #data.update["string"] = resource_link
    transcribed_text = requests.post(url, data= "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav")
   # print (transcribed_text)
   # questions_and_ans = nlp(transcribed_text)
  #  print (questions_and_ans)
    return transcribed_text

#resource_link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"
gen()

