from wordcloud import WordCloud
import nltk
from konlpy.tag import Okt
from konlpy.tag import Hannanum

with open('blog_irum.txt') as f :
    file_text = f.read()

okt = Okt()
tokens_ko = okt.nouns(file_text)

#빈도수 처리
ko = nltk.Text(tokens_ko)

# stopwords 불용어 : 의미없는 단어 제외
stopwords = ['것','8','때','+','등','후','이','수', '중', '들', '\u200b', '\u200b\u200b']
ko = [each_word for each_word in ko if each_word not in stopwords]

#빈도수 처리
ko = nltk.Text(ko)

data = ko.vocab().most_common(500) # 상위 500개 단어만 처리

wc = WordCloud(font_path='/usr/share/fonts/truetype/nanum/NanumGothicEco.ttf', \
               background_color = 'white', \
               width=500, \
               height=500, \
               max_words=5000, \
               max_font_size=200)

wc = wc.generate_from_frequencies(dict(data))

wc.to_file('blog_irum.png')