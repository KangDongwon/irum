from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from konlpy.tag import Okt
from konlpy.tag import Hannanum

file_text = open('test.txt').read()

#okt = Okt()
#tokens_ko = okt.nouns(file_text)
han = Hannanum()
tokens_ko = han.nouns(file_text)

#빈도수 처리
ko = nltk.Text(tokens_ko)
#print(f'빈도 수 처리 타입 : {type(ko)}')

# stopwords 불용어 : 의미없는 단어 제외
#stopwords = ['수','음','잔','함','분'] # Okt 불용어
stopwords = ['수','한','잔','분'] # 한나눔 불용어
ko = [each_word for each_word in ko if each_word not in stopwords]
#print(f'불용어 제거 후 타입 : {type(ko)}')

#빈도수 처리
ko = nltk.Text(ko)
#print(f'다시 타입 되돌리기 : {type(ko)}')

data = ko.vocab()
#data = ko.vocab().most_common(500) # 상위 500개 단어만 처리

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