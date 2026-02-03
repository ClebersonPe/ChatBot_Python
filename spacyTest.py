import spacy

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Boa tarde, como estão as coisas ai? Já terminou o que estava fazendo?")

for token in doc:
    print(token.text, token.lemma_, token.pos_)