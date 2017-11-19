from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
             <form id="contact-form" action="script.php" method="post">
                <input type="hidden" name="redirect" value="http://www.opera.com" />
                <ul>
                    <li>
                        <label for="input">Input</label>
                        <textarea name="input" id="input" cols="25" rows="3"></textarea>
                    </li>
                    <li>
                        <label for="output">Output</label>
                        <textarea name="rot" id="rot" cols="25" rows="3"></textarea>
                    </li>
                    <li>
                        <input type="submit" value="submit" />
                        <input type="reset" value="reset" />
                    </li>
                </ul>
            </form>
        </body>
    </html>
"""

@app.route('/', methods=['POST'])
def index():
    return form


def encrypt():

app.run()