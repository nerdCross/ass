from pipelines import pipeline
import requests
import os
cmd = "python -m nltk.downloader punkt"
returned_value = os.system(cmd)
nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl")
def gen(resource_link):
    url = 'http://3.8.100.147/transpile/'
    myobj = {"resource_link": "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"}
    myobj["resource_link"] = resource_link

    print("Dictionary = ",myobj)

    #x = requests.post(url, json = myobj)
    # Inserting a key that already exists, updates only the values

    #print the response text (the content of the requested file):

    #questions_and_ans = nlp(transcribed_text)
    #print (questions_and_ans)
    #return questions_and_ans
link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample5.wav"
gen(link)