import os 
import gensim 

from nltk import sent_tokenize 
from gensim.utils import simple_preprocess

story=[]

for filename in os.listdir('Data'):

    f=open(os.path.join('Data',filename))
    corpus=f.read()

    raw_sent=sent_tokenize(corpus)

    for sent in raw_sent:
        story.append(simple_preprocess(sent))

print(f" Total number of sentences {len(story)}")

print(story[0])