from flask import Flask
import random

app = Flask(__name__)
N_0 = 'https://media.giphy.com/media/mc6HkypwhX0pMdRBuT/giphy.gif'
N_1 = 'https://media.giphy.com/media/13VLdHIQRb8zQc/giphy.gif'
N_2 = 'https://media.giphy.com/media/toKE0zZrzkjuLKBucs/giphy.gif'
N_3 = 'https://media.giphy.com/media/NRtZEyZjbLgr0BJ4B8/giphy.gif'
N_4 = 'https://media.giphy.com/media/U7oYLyQqXM9sA/giphy.gif'
N_5 = 'https://media.giphy.com/media/xRCASav6bgz9m/giphy.gif'
N_6 = 'https://media.giphy.com/media/FwxVGlrHvRgEUaE8G5/giphy.gif'
N_7 = 'https://media.giphy.com/media/l378atCG9uQQa1Fy8/giphy-downsized-large.gif'
N_8 = 'https://media.giphy.com/media/EANQxfprIq2A3g2zsc/giphy.gif'
N_9 = 'https://media.giphy.com/media/Cij37iSqbvzEpLgZmN/giphy.gif'
CORRECT = 'https://media.giphy.com/media/39lYbuIEDqiDHAD0KT/giphy.gif'
WRONG = 'https://media.giphy.com/media/h30Uk86LypXpe/giphy.gif'
HOME = 'https://media.giphy.com/media/3ohhwiSbK4IdpTIB0Y/giphy-downsized-large.gif'
ALL_N = [N_0, N_1, N_2, N_3, N_4, N_5, N_6, N_7, N_8, N_9]
Dict = {}
for i in range(len(ALL_N)):
    Dict[i] = ALL_N[i]


NUM = random.randint(0, 9)



def make_bold(function):
    def action():
        return "<b>" + function() + "</b>"
    return action


@app.route('/')
@make_bold
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           f"<img src={HOME}>"


@app.route('/<int:num>')
def answer(num):
    if num == NUM:
        num = NUM
        q = Dict[num]
        return "<h1>Correct</h1>" \
               f"<img src={q}>" \
               f"<img src={CORRECT}>" \
               f"<a href='/'>Home</a>"
    else:
        q = Dict[num]
        return "<h1>Incorrect</h1>" \
               f"<img src={q}>" \
               f"<img src={WRONG}>" \
               f"<a href='/{NUM}'>Check Answer</a>"


if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)



