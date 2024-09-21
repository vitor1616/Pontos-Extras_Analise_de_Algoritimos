#Giovanna Mendes Garbácio
#  flask --app lower-high/server run
# http://127.0.0.1:5000/

from flask import Flask
import random

app = Flask(__name__)

min = 0
max = 9

random_number = random.randint(min,max)

@app.route("/")
def home():
    return "<h1>Adivinhe o número entre 0 e 9!</h1><br>"\
    "<h2>Adicione o número após uma barra no endereço.<br> Ex.:http://127.0.0.1:5000/2</h2>"\
    "<img src='https://i.giphy.com/tHufwMDTUi20E.webp' alt='gifhome'>"

@app.route("/<int:num_user>")
def check_number(num_user):
    if num_user < random_number:
        return f"<h1> VOCÊ ERROU!! HAHAHA</h1>"\
        f"<h2>Não é {num_user}. Era um número mais alto...</h2>"\
        "<img src='https://i.giphy.com/ray4IqT73lQhh24qKq.webp' alt='gifbaixo'>"
    elif num_user > random_number:
        return f"<h1> ERRADO!! KKKKKKKKKK</h1>"\
        f"<h2>Não é {num_user}. Era um número mais baixo...</h2>"\
        "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmtsNHM5dGRnMW50enhrN3RlcjZqeWxqaGdwbzI0c3MxM3p2OXQ5cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7cCw9MoRByrk6L4EVz/giphy.webp' alt='gifalto'>"
    else:
        return f"<h1>ACERTOU!! Era {num_user}. :)</h1>"\
        "<img src='https://media1.giphy.com/media/t4ujDuOYqa1OoJkwyU/giphy.webp?cid=790b7611ux7pxt4416qgmuvtr5cqx237jow8d2k2ehkieth2&ep=v1_gifs_search&rid=giphy.webp&ct=g' alt='gifacerto'>"

if __name__ == "__main__":
    app.run(debug=True)