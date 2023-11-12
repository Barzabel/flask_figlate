from flask import Flask
from flask import render_template, request
from pyfiglet import Figlet

app = Flask(__name__)

font_type = {
    'one_line_mini': {'font': '3x5', 'width': 5},
    'one_line': {'font': '6x10', 'width': 10},
    'normal': {'font': 'com_sen_', 'width': 10},
    'univers': {'font': 'univers', 'width': 14},
}


class Render_text:
    def __init__(self, render):
        self.render = render
        self.space = b'\xe2\xa0\x80'.decode("utf-8")

    def render_text(self, word):
        res = []
        for x in word:
            char = self.render.renderText(x).replace(' ', self.space).split('\n')
            res.append(char)
        return res


@app.get('/')
def index():
    word = request.args.get('word', '').lower()
    str_font = request.args.get('font', 'normal')
    font = font_type[str_font]
    render = Render_text(Figlet(**font))
    text = render.render_text(word)

    return render_template('index.html', text=text, word=word, font=str_font)
