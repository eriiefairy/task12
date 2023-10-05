import spacy
nlp = spacy.load('en_core_web_sm')


# garden path sentences
gardenpathsentences = ['That Jill is never here hurts.',
                       'Mary gave the child a Band-Aid.',
                       'The cotton clothing is made of grows in Mississippi',
                       'Helen is expecting tomorrow to be a bad day.',
                       'While Tom was washing the dishes fell on the floor.'
                       ]

tokenized_sentences = []

for sentence in gardenpathsentences:
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    tokenized_sentences.append(tokens)

# Print the tokenized sentences
for sentence, tokens in zip(gardenpathsentences, tokenized_sentences):
    print(f'Sentence: {sentence}')
    print(f'Tokens: {tokens}\n')

# Process each sentence and perform tokenization and entity recognition
for sentence in gardenpathsentences:
    doc = nlp(sentence)
    print("\nSentence:", sentence)
    for ent in doc.ents:
        print("Entity:", ent.text, "Entity Type:", ent.label_)

print("\nEntity Recognition (ER):")
for sentence in gardenpathsentences:
    doc = nlp(sentence)
    for token in doc:
        if token.ent_type_ != "":
            print("Entity:", token.text, "Entity Type:", token.ent_type_)

entity_fac = spacy.explain("FAC")
print(f"\nFAC:{entity_fac}")

# "That Jill is never here hurts." Its entity was PERSON and the explanation is:
# (The fact) that Jill is never here hurts (me).
# The entity did make sense, this affects a person.

# "Helen is expecting tomorrow to be a bad day." Its entity was DATE and the explanation is
# "Helen is expecting (for) tomorrow to be a bad day"
# the entity does make sense, this affects time.

