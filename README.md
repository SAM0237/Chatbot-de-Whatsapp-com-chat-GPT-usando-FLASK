# Chatbot-de-Whatsapp-com-chat-GPT
(O projeto foi descuntinuado ainda na fase inicial, então não existem muitas funcionalidades)



Chatbot de conversação com opções visuais de botão para registrar pedidos de clientes em uma pizzaria.

o chat bot usa openAI e lang chain

webhook pro wpp (talvez fastAPI)

api do whatsapp para enviar pro webhook

sistema em python

Banco de dados para armazenamento de pedidos e envio posterior para front end da pizzaria

resumo de ferramentas:
____________________

FLASK
langCHAIN
FastAPI
APIwhatsapp Business
OPENAI
mySQL
_____________________

FUNCIONAMENTO:
______________________________________________FUNCIONAMENTO:______________________________________________

O cliente enviará mensagens ao Whatsapp do estabelecimento. O whatsapp da loja recebe a mensagem,
a API do whatsapp vai enviar pro WEBhook que estará fazendo varreduras esperando novas mensagens.
Após a captura da mensagem a mensagem será passada para o sistema em python entrando diretamente
no chatBOT da open AI através do langCHAIN. o chat bot ao captar a mensagem realizará o tratamento
necessario com base na mensagem, por exemplo: Caso o chatBOT perceba a intenção do cliente fazer
um pedido, ele ativará o modulo que irá enviar a marcação do menu, botões, sub marcações com as opções
disponiveis para realizar o pedido.
_________________________________________________________________________________________________________


_____________________________________________FLUXO ESPERADO:___________________________________________________________________________
CLIENTE ENVIA MENSAGEM -> API DO WHATSAPP REGISTRA -> WEBHOOK AGUARDANDO NOVAS INFORMAÇÕES PARA ENVIO PRO SISTEMA ->
WEBHOOK ENVIA PRO SISTEMA -> SISTEMA TRATA A MENSAGEM DE ACORDO COM O CONTEXTO -> RETORNA PRO CLIENTE INFORMAÇÕES/RESPOSTAS/
MENÚS/ETC....
___________________________________________________________________________________________________________________________

