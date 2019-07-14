import nltk
from nltk.stem.porter import *

stemmer=PorterStemmer()
words=['grasses','flies','mules','denied',
       'matched','agreed','motoring','making',
       'traditional','rational','colonial','reference',
       'itemization','duration']
stems=[stemmer.stem(w) for w in words]
print(stems)

