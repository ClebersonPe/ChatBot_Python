import spacy

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Boa tarde, como estão as coisas ai? Já terminou o que estava fazendo?")

for token in doc:
    print(token.text, token.lemma_, token.pos_)


# Vou usar essa lib para ajudar na verificação de cada intent do usuário, o papel dela aqui foi destrinchar essa frase em tokens
# Resultado Obtido:
# Boa Boa ADJ  -- 
# tarde tarde ADV
# , , PUNCT
# como como ADV
# estão estar VERB
# as o DET
# coisas coisa NOUN
# ai ai ADJ
# ? ? PUNCT
# Já já ADV
# terminou terminar VERB
# o o PRON
# que que PRON
# estava estar AUX
# fazendo fazer VERB
# ? ? PUNCT


#text == palavra da frase / lemma == lemantização, palavra crua do dicionário / Pos == classe gramatical (part of speach)
