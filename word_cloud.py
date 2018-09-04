from wordcloud import WordCloud 
import matplotlib.pyplot as plt

data= "My name is Shivam Agrawal Artificila Intelligence Machine Learning Algorithms Robotics Mathamatics Science Physics Cancer Stock market"

cloud= WordCloud().generate(data)
plt.imshow(cloud)
plt.axis('off')
plt.show()