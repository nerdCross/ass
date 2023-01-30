from pipelines import pipeline
import requests
from pre_parse import parseWords
import os
# from files_return import returnthefiles


#########
cmd = "python -m nltk.downloader punkt"
returned_value = os.system(cmd)
#nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl")
def gen(resource_link,unique_id):
    myobj = {}
    url = 'http://18.168.3.70/transpile/'
    #myobj = {"resource_link": "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"}
    myobj["resource_link"] = resource_link
    #print("Dictionary = ",myobj)
    transcribed_text = requests.post(url, json = myobj)
    transcribed_text = transcribed_text.text
    #print(transcribed_text)
    path_to_directory = parseWords(transcribed_text,unique_id)
    return path_to_directory



def assesment(link,unique_id):
    #link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample5.wav"
    #link  = ""
    #ink = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample4.wav"
    #unique_id = "asdfjhagkerf-0enqrge=-j"
    #unique_id = ""
    path = gen(link,unique_id)
    # tab = returnthefiles(path)
    # getting length of list
    #length = len(tab)
    # print(tab)
    # result = []
    i = path+"/demo.txt"
    print(i)
    f = open(i, "r")
    var = f.read()
    nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl",qg_format="prepend")
    questions_and_ans = nlp(var)
    return questions_and_ans
    # for i in tab:
    #     #print (i)
    #     f = open(i, "r")
    #     var = f.read()
    #     print(var)
    #     questions_and_ans = nlp(var)
    #     print ("?????????"+i)
    #     print (questions_and_ans)
    #     print(type(questions_and_ans))
    #     result.append(questions_and_ans)
    # return(result)

#link = "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample4.wav"
#unique_id = "asd-victorious1"
#total = assesment(link,unique_id)
#print(" total type  Below")
#print(type(total))
#print(" total   Below")
#print(total)

