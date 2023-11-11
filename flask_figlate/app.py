from flask import Flask
from flask import render_template, request
from pyfiglet import Figlet

app = Flask(__name__)

font_type = {
    'one_line_mini': {'font': '3x5', 'width': 5},
    'one_line': {'font': '6x10', 'width': 10},
    'normal': {'font': 'com_sen_', 'width': 10},
    'univers': {'font': 'univers', 'width': 15},
}

space = {
    'clear': b'\xe2\xa0\x80'.decode("utf-8"),
    'line': '_'
}


@app.get('/')
def index():
    word = request.args.get('word', '').lower()
    str_font = request.args.get('font', 'normal')
    font = font_type[str_font ]
    f = Figlet(**font)
    text = f.renderText(word).split('\n')
    new_text = []
    s = space['clear']
    for x in text:
        new_text.append(x.replace(' ', s))
    return render_template('index.html', text=new_text, word=word, font=str_font)