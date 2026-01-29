from intents import INTENTS
from context import Context

context = Context()

def detect_intent(message):
    message = message.lower()
    for intent, keywords in INTENTS.items():   #keywords é o tipo de intenção, o for percorre a palavra chave(Intenção) e cada palavra chave tem varias keywords(oi, ola)
        for word in keywords:
            if word in message:
                return intent
    
    return None
    
def respond(intent):
    if intent == "saudacao":
        return "Olá, como posso te ajudar?"
    elif intent == "ajuda":
        return "Voce pode pagar ou optar por sair"    #intenção é o ato de querer realizar algo/ ex: com a INTENÇAO de ABRIR uma porta - algo que provavelmente vai ser feito
    elif intent == "pagamento":
        return "Deseja pagar no pix ou cartão?"
    elif intent == "despedida":
        return "Saindo... Zzzz"
    else:
        return "Desculpa, não entendi"
    
print ("Digite sair para encerrar o chatBot")

while True:
    user_input = input("Você: ")

    intent = detect_intent(user_input)
    response = respond(intent)

    print("Bot", response)

    if intent == "despedida":
        break