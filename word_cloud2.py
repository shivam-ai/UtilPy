from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
import sys
from PIL import Image
import numpy as np
import wikipedia


curdir= os.path.dirname(__file__)

def getWiki(query):
    title= wikipedia.search(query)
    page= wikipedia.page(title)
    return page.content

def createWordCloud(query, text):
    maskd= np.array(Image.open(os.path.join(curdir, 'dil.png')))
    print(maskd.shape)
    filter= maskd[:,:,0]<50
    maskd[filter]= 255
    stopwds= set(STOPWORDS)
    wc= WordCloud(mask=maskd, stopwords=stopwds, background_color='white', max_words=100)
    wc.generate(text)
    wc.to_file(os.path.join(curdir, query+'.png'))
    plt.imshow(np.array(Image.open(os.path.join(curdir, query+'.png'))))
    plt.axis('off')
    plt.show()


if(__name__=='__main__'):
    query= sys.argv[1]
    data= getWiki(query)
    createWordCloud(query, data)
