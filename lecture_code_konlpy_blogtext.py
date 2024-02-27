import nltk
from konlpy.tag import Okt
from konlpy.tag import Hannanum

with open('blog_irum.txt') as f :
    file_text = f.read()

# 한나눔
#han = Hannanum()
#tokens_ko = han.nouns(file_text)

# Okt
#okt = Okt()
#tokens_ko = okt.nouns(file_text)

#빈도수 처리
ko = nltk.Text(tokens_ko)

print(dict(ko.vocab()))