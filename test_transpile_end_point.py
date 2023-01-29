import requests

url = 'http://3.8.100.147/transpile/'
myobj = {"resource_link": "https://relen.s3.us-east-2.amazonaws.com/audio/samples/sample3.wav"}

x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

print(x.text)

