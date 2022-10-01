import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud


frequency = {}

# data_modeling.csv is name of the file, you can change it to your own file
data = pd.read_csv('data_modeling.csv')
content = tuple(data.text)
print(content, file=open('newdata.txt','w')) #I'm creating a new file from CSV with .txt as the extension

new_data = open('newdata.txt','r')
new_data = new_data.read().lower() #I'm making the data in lower case

match_pattern = re.findall(r'\b[a-z]{3,15}\b', new_data)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

# showing data
frequency_list = frequency.keys()

# for words in frequency_list:
#     print (words, frequency[words])

#This for sorting data
sort_order = sorted(frequency.items(), key=lambda x:x[1], reverse=True)

# for i in sort_order:
#     print(i[0],i[1])

#This for generate graphic visualization
mc = dict(list(sort_order[0:15]))
names = list(mc.keys())
values = list(mc.values())

#You can uncomment these source code below to print the graphic visualization
# print(mc)

# plt.bar(range(len(mc)),values,tick_label=names)
# plt.savefig('bar01.png')
# plt.show()

#This for generate wordcloud visualization
wordcloud = WordCloud(width=1000, height=500).generate_from_frequencies(mc)

plt.figure()
plt.savefig('wordcloud01.png')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()