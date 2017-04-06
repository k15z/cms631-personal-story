import csv
import string
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from collections import Counter

theme_to_questions = {}
with open("data/allquestions.csv", "rt", encoding="latin1") as fin:
    reader = csv.reader(fin)
    header = next(reader)
    print(header)
    for row in reader:
        if len(row) == 4:
            _, _, question, theme = row
            if theme not in theme_to_questions:
                theme_to_questions[theme] = []
            theme_to_questions[theme].append(question)
questions = theme_to_questions["Innovation-Technology"]

wc = WordCloud(background_color="white", max_words=10)
wc.generate(" ".join(questions))
wc.to_file("mockup/word.mini.png")

wc = WordCloud(background_color="white", max_words=100)
wc.generate(" ".join(questions))
wc.to_file("mockup/word.zoom.png")
