import nltk
from nltk.corpus import names
labeled_names =([(name,'male') for name in names.words('male.txt')]+
                [(name,'female') for name in names.words('female.txt')]);
import random
random.shuffle(labeled_names)
print(labeled_names)

def gender_feature(word):
    return{'last_letter':word[-1]}

print(gender_feature('Arif'))


featuresets = [(gender_feature(n),gender) for (n,gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier,test_set))

classifier.show_most_informative_features(6)

print(classifier.classify(gender_feature('Chocho')))