from twilio.rest import Client
from configure import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_SANDBOX_NUMBER
from flask import request
from flask import Blueprint
from openai import OpenAI


bp = Blueprint('routes', __name__)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) #inicia o client do TWILIO com a conta especificada

#webhook para verificar se à novas MENSAGENS
@bp.route("/webhook", methods=["POST"]) # type: ignore
def webhook():
    
    print("Numero: ", TWILIO_SANDBOX_NUMBER)
    
    mensagemcaptada = request.values.get('Body', '').lower() #Capta o corpo da requisição e filtra apenas o body (conteúdo da mensagem)
    numerocliente = request.values.get('From', '').lower() #Capta o corpo da requisição e filtra apenas o from (de onde veio a mensagem, o numero do cliente)
    
    print('mensagem: ', mensagemcaptada, 'do numero: ', numerocliente, 'captada')
    
    if mensagemcaptada is not None: #Verifica se á conteudo na mensagem captada
        
        clientgpt = OpenAI(api_key="API DO CHAT GPT")

        response = clientgpt.responses.create(
            model="gpt-4.1",   #passa a mensagem captada para o chatGPT e guarda a resposta
            input=str(mensagemcaptada)
        )
        mensagemdevolta = response.output_text #pega a resposta do chatGPT
    try:
        mensagemenviadadevolta = client.messages.create(
            from_=TWILIO_SANDBOX_NUMBER,
            body=mensagemdevolta, #envia a resposta pro cliente
            to=numerocliente
        )
    except Exception as e:
        print(f"Falha ao enviar mensagem: {e}") 
    return "ok"

