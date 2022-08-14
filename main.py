from ast import While
import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estamos ubicado en la caleta, por las americas', ['ubicados', 'direccion', 'donde', 'ubicacion', 'Please'], single_response=True)
        response('Impartimos las siguientes carreras: Software, Redes de la informacion, Diseño industrial, seguridad informatica, Multimedia, Mecatronica',['que carreras imparten?'], single_response=True)
        response('Mira, de matriculacion se pagan 6,520 pesos, pero eso nada mas es de iscripcion', ['Cuanto se paga', 'pago?', 'iscripcion', 'buenas, cuanto se paga?'], single_response = True)
        response('Omar lluberes', ['como', 'llama', 'rector'], required_words=['como'])
        response('Si, tenemos transporte en Villa mella y la 27', ['Tienen transporte', 'guagua', '27', 'villa mella'], single_response=True)
        response('En villa mella nos paramos cerca de la sirena de la mama tingo', ['donde se paran en villa mella', 'estacionan'], single_response=True)
        response('En la 27 nos paramos en la duarte', ['donde se paran en la 27', 'estacionan'], single_response = True)
        response('Hay 4 edifcios', ['cuantos', 'edificios', 'hay', 'en el ', 'ITLA'], required_words=['como'])
        response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['Puedes repetirlo please?', 'No estoy seguro de lo quieres decir', 'Lo siento, mi sistema no esta reconoce esa palabra'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))