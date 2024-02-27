# 한나눔
from konlpy.tag import Hannanum
hannanum = Hannanum()

# 명사 분석
print(hannanum.nouns('한국어 분석을 해보겠습니다. 과연 잘 나올지 두근두근'))

# 형태소 분석
print(hannanum.pos('한국어 분석을 해보겠습니다. 과연 잘 나올지 두근두근'))

# 형태소 분석2 (품사 표시 X)
print(hannanum.morphs('한국어 분석을 해보겠습니다. 과연 잘 나올지 두근두근'))

print(hannanum.tagset)


# OKT
from konlpy.tag import Okt
okt = Okt()

# 명사 분석
print(okt.nouns('한국어 분석을 해보겠습니다. 과연 잘 나올지 두근두근'))

# 형태소 분석
print(okt.morphs('한국어 분석을 해보겠습니다. 과연 잘 나올지 두근두근'))

# 형태소 분석
print(okt.pos('한국어 분석을 해보겠습니다. 과연 잘 나올지 두근두근'))

print(okt.tagset)