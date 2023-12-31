import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"
             ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# What I find interesting about the similarities between cat, monkey, and banana is that they can be related through
# their properties and attributes, such as being living organisms and having specific physical features. However,
# they also differ in various ways, such as their type of food consumption, behavior, and natural habitats.

# NOTES ON WHAT IS DIFFERENT:
# the results are different from the ones obtained with the 'en_core_web_md' model. This is because the 'en_core_web_sm'
# model has a smaller vocabulary and is less accurate in understanding complex sentences and nuanced language.
