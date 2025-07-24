from __init__ import create_app

#Inicia a aplicação com o Flask na porta 5100
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5100)