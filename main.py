from flask import Flask, request
from caesar import rotate_string

app= Flask(__name__)
app.config['DEBUG']=True

form= '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{

                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
                }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action = "/" method= "post" >
            <label for="rotate-by">Rotate by:</label>

            <input type="text" name="rot" value = "0" />
        
            <textarea name="textarea">{0}</textarea>

            <input type="submit" value="Rotate">

        </form>

    </body>
</html>
'''

@app.route('/')
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    textarea = request.form['textarea']

    return form.format(rotate_string(textarea, rot))

app.run()