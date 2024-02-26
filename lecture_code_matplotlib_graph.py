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

# 빈도수 처리
ko = nltk.Text(tokens_ko)
#print(f'빈도 수 처리 타입 : {type(ko)}')

# stopwords 불용어 : 의미없는 단어 제외
#stopwords = ['수','음','잔','함','분'] # Okt 불용어
stopwords = ['수','한','잔','분'] # 한나눔 불용어
ko = [each_word for each_word in ko if each_word not in stopwords]
#print(f'불용어 제거 후 타입 : {type(ko)}')

# 빈도수 처리
ko = nltk.Text(ko)
#print(f'다시 타입 되돌리기 : {type(ko)}')

# 폰트설정
plt.rc('font', family='NanumBarunGothic')
plt.figure(figsize=(12,6))
ko.plot(50)
plt.show()