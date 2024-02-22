# konlpy 설치
!pip install konlpy

# wordcloud 설치
!pip install wordcloud

#한글 폰트 설치 : 설치 후 런타임 >> 세션 다시 시작
!apt-get update -qq
!apt-get install fonts-nanum* -qq

#한글 폰트 설치2 : 위에꺼 후 안 되는 경우
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

# 설치한 폰트 설정
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

path = '/usr/share/fonts/truetype/nanum/NanumGothicEco.ttf'
font_name = fm.FontProperties(fname=path, size=10).get_name()
plt.rc('font', family=font_name)

# 워드클라우드 실행
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from konlpy.tag import Okt
from konlpy.tag import Hannanum

file_text = open('diary.txt').read()

#okt = Okt()
#tokens_ko = okt.nouns(file_text)
han = Hannanum()
tokens_ko = han.nouns(file_text)
ko = nltk.Text(tokens_ko)

#stopwords = ['수','음','잔','함','분']
stopwords = ['수','한','잔','분']
ko = [each_word for each_word in ko if each_word not in stopwords]

ko = nltk.Text(ko)
data = ko.vocab()
#data = ko.vocab().most_common(500)

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