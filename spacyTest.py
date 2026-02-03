import spacy

nlp = spacy.load("pt_core_news_sm")
doc = nlp("Boa tarde, como estão as coisas ai? Já terminou o que estava fazendo?")

for token in doc:
    print(token.text, token.lemma_, token.pos_)


# Vou usar essa lib para ajudar na verificação de cada intent do usuário, o papel dela aqui foi destrinchar essa frase em tokens
# Resultado Obtido:
# Boa Boa ADJ  -- Adjetivo
# tarde tarde ADV -- Advérbio
# , , PUNCT -- Pontuação
# como como ADV -- Advérbio
# estão estar VERB - Verbo
# as o DET -- Artigo     
# coisas coisa NOUN - Substantivo
# ai ai ADJ - Adjetivo -- Erro de ambiguidade interessante aqui, ao invés de usar "aí", usei "ai". Um erro meu, porém, é importante observar o contexto da frase
# ? ? PUNCT -- Pontuação
# Já já ADV -- Advérbio
# terminou terminar VERB -- Verbo
# o o PRON -- Pronome
# que que PRON -- Pronome
# estava estar AUX - Verbo Auxiliar
# fazendo fazer VERB - Verbo
# ? ? PUNCT -- Pontuação


#text == palavra da frase / lemma == lemantização, palavra crua do dicionário / Pos == classe gramatical (part of speach)
