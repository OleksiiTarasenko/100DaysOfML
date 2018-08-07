import zipfile
import os
import collections



file = zipfile.ZipFile('word_cloud.zip')

file.extractall()
file.close()

word_cloud_file = open('98-0.txt', 'rb')
word_cloud_content = word_cloud_file.read()
word_cloud_file.close()
word_cloud_content = str(word_cloud_content).lower().split(' ')

stop_file = open('stopwords', 'r')
stop_words = stop_file.read()
stop_file.close()
c = collections.Counter()
for word in word_cloud_content:
	word = word.replace(".",'')
	word = word.replace(",",'')
	word = word.replace("\"",'')
	word = word.replace("“",'')
    
	if word in stop_words:
		continue
	c[word] +=1

for word, count in c.most_common(10):
	print(word, ": ", count)