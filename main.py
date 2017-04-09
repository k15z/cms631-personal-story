import csv
import string
import numpy as np
from glob import glob
from PIL import Image
from wordcloud import WordCloud
from collections import Counter

for file in glob("data/*.csv"):
    questions = []
    with open(file, "rt", encoding="latin1") as fin:
        reader = csv.reader(fin)
        header = next(reader)
        print(header)
        for row in reader:
            questions.append(row[3])

    wc = WordCloud(background_color="white", max_words=1000, width=1080, height=1080)
    wc.generate(" ".join(questions))
    wc.to_file(file.replace("data/", "prototype/images/").replace(".csv", ".png"))
