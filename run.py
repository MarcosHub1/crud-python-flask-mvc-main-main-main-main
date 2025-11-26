from app import app, db
#from openai import OpenAI

#client = OpenAI(api_key="SUA_CHAVE_AQUI")  # <-- você vai colocar sua chave aqui


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)