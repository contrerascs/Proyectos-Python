import stylecloud
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from stop_words import get_stop_words

palabras_irrelevantes = get_stop_words('spanish')

stylecloud.gen_stylecloud(file_path=r'WordCloud/TaylorSwift.txt',
                          icon_name='fas fa-rocket',
                          palette='cartocolors.sequential.Magenta_7',
                          background_color='black',
                          output_name=r'WordCloud/TayTay.png',
                          collocations=False,
                          custom_stopwords=palabras_irrelevantes)

#Creando nube de palabras con imagen propia
my_mask = np.array(Image.open(r'WordCloud/Taylor_Swift.png'))
wc = WordCloud(background_color='white',
               mask=my_mask,
               collocations=False,
               width=600,
               height=600)

with open(r'WordCloud/TaylorSwift.txt','r', encoding='utf-8') as txt_file:
    texto = txt_file.read()

wc.generate(texto)

#Extraer colores
image_colors = ImageColorGenerator(my_mask)
wc.recolor(color_func=image_colors)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
wc.to_file(r'WordCloud/TayTay_WordCloud.png')
plt.show()