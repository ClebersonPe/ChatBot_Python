from intents import INTENTS
from context import Context
import spacy

nlp = spacy.load("pt_core_news_sm") # carrega em pt-br

context = Context()

def preprocessamento(text):
    return text.lower().strip() # tira os espaços e transforma em letra minuscula

def detect_intent_spacy(message):
    doc = nlp(message)

    verbos = [t.lemma_ for t in doc if t.pos_ == "VERB"]
    substantivos = [t.lemma_ for t in doc if t.pos_ in ["NOUN", "PROPN"]]

    if "pagar" in verbos:
        return "pagamento"
    
    if "status" in substantivos or "entrega" in substantivos:
        return "status_pedido"

    if "oi" in message or "olá" in message:
        return "saudacao"

    if "sair" in message or "tchau" in message:
        return "despedida"


def detect_intent(message):
    intent = detect_intent_spacy(message) #primeiro verifica usando o spacy, volta se achar
    if intent:
        return intent

    message = message.lower()
    for intent, keywords in INTENTS.items(): #só cai aqui se o spacy por ventura nao achar nada
        for word in keywords:
            if word in message:
                return intent

    return None
   
    
    
def respond(intent, message, context):

    if context.current_topic == "pagamento":
        if "pix" in message:
            context.current_topic = None
            return "Pagamento via Pix Confirmado!"
        
        elif "cartao" in message:
            context.current_topic = None
            return "Pagamento via Cartão Confirmado!"
        
        else:
            return "Por favor registre a forma de pagamento: Cartão ou Pix"
    
    if context.current_topic == "status_pedido":
        if "informacoes" in message:
            context.current_topic = None
            return "Seu pedido: Honda Civic 2012, prata"
        
        elif "status" in message or "pagamento" in message:
            context.current_topic = None
            return "Seu pagamento está em processo de confirmação, aguarde"
        
        elif "rastrear" in message or "entrega" in message:
            context.current_topic = None
            return "Entrega ainda não efetuada, esperando pagamento..."
        
        else:
            return "Desculpa, não entendi o que você quis dizer!"



    if intent == "saudacao":
        context.current_topic = "saudacao"
        return "Olá, como posso te ajudar?"
    
    elif intent == "ajuda":
        return "Voce pode pagar ou optar por sair"    #intenção é o ato de querer realizar algo/ ex: com a INTENÇAO de ABRIR uma porta - algo que provavelmente vai ser feito
    
    elif intent == "pagamento":
        context.current_topic = "pagamento"
        return "Deseja pagar no pix ou cartão?"
    
    elif intent == "status_pedido":
        context.current_topic = "status_pedido"
        return "Deseja saber as informacoes do pedido, status de pagamento ou rastrear entrega?"
    
    elif intent == "despedida":
        return "Saindo... Zzzz"
    
    else:
        return "Desculpa, não entendi"
    
    
    
print ("Digite sair para encerrar o chatBot")

while True:
    user_input = input("Você: ")

    intent = detect_intent(user_input)
    response = respond(intent, user_input.lower(), context)

    print("Bot", response)

    if intent == "despedida":
        break