from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from konlpy.tag import Okt
from konlpy.tag import Hannanum

with open('blog_irum.txt') as f :
    file_text = f.read().replace('\u200b','')

han = Hannanum()
tokens_ko = han.nouns(file_text)

#빈도수 처리
ko = nltk.Text(tokens_ko)

# stopwords 불용어 : 의미없는 단어 제외
stopwords = ['것','8','때','+','등','후','이','수', '중', '들']
ko = [each_word for each_word in ko if each_word not in stopwords]

#빈도수 처리
ko = nltk.Text(ko)

data = ko.vocab()

wc = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumGothicEco.ttf', \
               background_color = 'white', \
               width=500, \
               height=500, \
               max_words=5000, \
               max_font_size=200)

wc = wc.generate_from_frequencies(dict(data))

plt.figure(figsize=(8,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()