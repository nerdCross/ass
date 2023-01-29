inp = " Welcome to the second lesson of the course, Doing Presentations Like A Pro. This course is designed to help you elevate your presentation game. In the first lesson, we learnt about the rudiments of academic presentations. We saw that these presentations are important to promote knowledge, creation, as they facilitate cross-fortalization of ideas. We also identified poster and oral presentations as the two main types of presentation. In the second lesson, we shall focus on poster presentations. We will consider the format, content, organization, words, fonts, colors, and printing required for a good poster. To start with, a poster is a visual representation of an idea or research finding to be disseminated to an audience. One of the most common standard sizes of poster is the A zero paper size with dimension 841 by 1189 mm. Or, 33.1 by 46.8 inches. In doing a poster presentation, the presenter would usually take about 5 minutes to speak to the poster and then stand by for questions. The number of questions a poster presentation generates can be a deciding factor for its success. That is to say, you will know how successful your poster presentation is if it generates a lot of questions afterwards. This would be an indication that your poster is interesting to people and that people are interested in the thoughts you are trying to share in that poster. The choice of poster formats is usually left for the presenter. Of course, there are some events where you would be given a standard poster format, but in most cases you are allowed to choose what you like. All kinds of templates can be downloaded online and adapted for use as a property. You can feel free to get and tweak any format of interest you can find on the internet. So, you are just edit templates of format you find, you adjust them to your own taste. Next, the creation of a poster will usually include title, summary, brief introduction, in-s and objectives, methodology, result, discussion and conclusion. You have to ensure you do justice to each part. Inorganizing the content of a poster, headings, numbering, bullets, graphics and blank spaces should all be appropriately deployed for maximum impact. This can be a real game changer. Since the poster is mostly visual, words should only be used when necessary. Having too many words or words in unnecessary places in your poster can be a disaster. Wordy posters can be boring. So, they should be avoided by all means. In addition, font style and size should be carefully chosen for the desired impact. Color combination is another crucial factor in a poster. This is particularly important because the kinds of colors used can determine whether the poster will be good enough to attract attention after printing. Marova, good quality printing is important. If you think of how your poster will appear, after printing, right from the moment you set out to design the poster. So, this is all about keeping the end in view. You do not want to choose formats or design templates or color combinations that will not be good after you print as a recap. The poster presentation has a lot to do with a poster and as such, can you be taking to make good decisions about key features that I stated before, like format, content, organization and the printing. A masterful interplay of all these components will set your poster presentation apart. So, you want to show yourself as the master. You want to show yourself as a pro you are supposed to be. Now that you have these great ideas, you have to implement them. They must not remain in the realm of ideas in your head. You have to capitalize on the lessons you have learned, on the tips you have got from this lesson. So, that you can be an expert poster presenter. So, that you can be that poster presenter that people look up to. So, that you can be that person that people get ideas from. What you make presentations should be able to get ideas for making their own posters in the future. And that is why this lesson has been put across to you right now. And you want to definitely make the most of this opportunity you have to be a master poster designer, to be a master poster presenter, and to be an inspiring one while at it. Until I see you in the next lesson. Thank you very much for paying attention. Make sure you turn people's head the next time you present your poster. See you later."
li = inp.strip().split(" ")


page = []
sentences = []
character_len = 0
for idx, word in enumerate(li):
    character_len += len(word)
    
    if "," in word:
        pass
    else:
        sentences.append(word)
    if "." in word:
        character_len =0
        sentences.append(" \n ")
        page.append(sentences)
        sentences = []
    elif character_len>=150:
        character_len = 0
        sentences.append(" \n")
        page.append(sentences)
        sentences = []
s = ''
f = open("demo.txt", "w")

for p in page:
    w = ' '.join(p)
    f.write(w.strip())
    f.write("\\")
    f.write("\n")
    # s = s+" "+w.strip()

f.close()

f = open("demo.txt", "r")
var = f.read()
print(var)
