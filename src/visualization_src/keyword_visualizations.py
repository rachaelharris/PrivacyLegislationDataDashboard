import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
# matplotlib inline


# State Legislation keywords
state_df = pd.read_csv("/Users/rachaelharris/Desktop/computer science/cs580s2022/assignment6-rachaelharris/results/state_results.csv", index_col=0)

# Join all keywords together:
state_keyword1 = " ".join(review for review in state_df.keyword_1)
state_keyword2 = " ".join(review for review in state_df.keyword_2)
state_keyword3 = " ".join(review for review in state_df.keyword_3)
state_keyword4 = " ".join(review for review in state_df.keyword_4)
state_keyword5 = " ".join(review for review in state_df.keyword_5)
state_text = state_keyword1 + state_keyword2 + state_keyword3 + state_keyword4 + state_keyword5

# Create and generate a word cloud image:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(state_text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("/Users/rachaelharris/Desktop/computer science/cs580s2022/assignment6-rachaelharris/visualizations/final-visualizations/state/state-keyword.png", format="png")



# Federal Legislation keywords
federal_df = pd.read_csv("/Users/rachaelharris/Desktop/computer science/cs580s2022/assignment6-rachaelharris/results/federal_results.csv", index_col=0)

# Join all keywords together:
federal_keyword1 = " ".join(review for review in federal_df.keyword_1)
federal_keyword2 = " ".join(review for review in federal_df.keyword_2)
federal_keyword3 = " ".join(review for review in federal_df.keyword_3)
federal_keyword4 = " ".join(review for review in federal_df.keyword_4)
federal_keyword5 = " ".join(review for review in federal_df.keyword_5)
federal_text = federal_keyword1 + federal_keyword2 + federal_keyword3 + federal_keyword4 + federal_keyword5

# Create and generate a word cloud image:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(federal_text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("/Users/rachaelharris/Desktop/computer science/cs580s2022/assignment6-rachaelharris/visualizations/final-visualizations/state/federal-keyword.png", format="png")