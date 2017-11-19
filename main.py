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
                p.error {
                    color: red;
                }
            </style>
        </head>
        <body>
            <form method="post">
                <div>
                    <label for="rot">Rotate by:</label>
                    <input type="text" name="rot" value="0">
                    <p class="error"></p>
                </div>
                <textarea type="text" name="text"></textarea>
                <br>
                <input type="submit">
            </form>
        </body>
    </html>
"""
@app.route('/encrypt', methods=['POST'])
def encrypt(text, rot):

    return 

@app.route('/', methods=['POST'])
def index():
    return form

app.run()