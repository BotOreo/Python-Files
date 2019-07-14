import nltk
from nltk.corpus import brown

sentences = "Time flies like AN ARROW"

sentences=sentences.lower().replace(".","").replace(",","")
sentences=sentences.split()
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(sentences)
print(unigram_tagger.tag(sentences))
size = int(len(sentences)*0.9)
print(size)
train_sents=brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger=nltk.UnigramTagger(train_sents)
unigram_tagger.evaluate(test_sents)
print(unigram_tagger.evaluate(test_sents))


'''
"My name is Archideus Dimaz Joseph, the third son " \
            "of William Dimaz Joseph, commander of the Black Seas, " \
            "captain of the Wicked Widow, a father of two sons, and I am hungry." \
            "I have been waiting for your arrival for seven days and seven night, without stepping" \
            "outside the realm of men. I have not eaten since then, and I am famished." \
            "So, tell me, boy. Why should I spare your soul when it can satisfy my hunger" \
            "even for a little bit?
'''