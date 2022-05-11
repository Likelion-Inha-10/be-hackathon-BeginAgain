from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np


class MakeWordCloud:
    def getWordCloud():
        print ('o'*20)

        with open('task3.csv', 'r', encoding='utf-8') as f:
            text = f.read()

        okt = Okt()
        #nouns = okt.nouns(text) # 명사만 추출
        OKT_pos = Okt().pos(text, norm=True, stem=True)
        words = [x for x, y in OKT_pos if y in ['Noun', 'Adjective', 'Verb']]

        words = [n for n in words if len(n) > 1] # 단어의 길이가 1개인 것은 제외

        #불용어 라인 (지금은 를,의만 불용어 처리돼있는 상태 )
        stop_words = "하다 보다 있다 없다 가다 되다 "
        stop_words = set(stop_words.split(' '))

        #불용어 제거
        words = [word for word in words if not word in stop_words]

        c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함


        c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함


        wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
        gen = wc.generate_from_frequencies(c)
        plt.figure()
        plt.imshow(gen)


        wc.to_file('결과.png')
        plt.show()
