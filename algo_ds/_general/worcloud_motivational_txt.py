import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud
from PIL import Image 

d = path.dirname(__file__)
dir_name=path.dirname(__file__)

##    text=f.read()
# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
text="i am here how are you doing th w word is awesome"
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
image.show()