from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import matplotlib 
import  numpy as np
import requests
from PIL import Image
from io import BytesIO
import base64

english_stopwords = set(STOPWORDS)
with open('stopwords-fr.txt', encoding='utf-8') as f:
    french_stopwords = set(f.read().splitlines())

matplotlib.use('Agg')

def generate_text(text):
    comment_words = ''      
    tokens = text.split()       
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()   
    comment_words += " ".join(tokens)+" "
    return comment_words

def generate_word_cloud(text, language):
    comment_words = generate_text(text)
    if language == 'french':
        stopwords = french_stopwords
    else:
        stopwords = english_stopwords
    pic = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png',stream=True).raw))
    wordcloud = WordCloud(width = 500, height = 500, 
                    background_color ='white',
                    stopwords = stopwords, mask = pic,
                    min_font_size = 10).generate(comment_words)
    plot = plt.figure(figsize = (10, 10), facecolor = 'white', edgecolor='blue') 
    plt.imshow(wordcloud)
    plt.axis("off") 
    plt.tight_layout(pad = 0)
    return plot