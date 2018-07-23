from flask import Flask, url_for, render_template

app = Flask(__main__)

@route('/')
def index():
    return (2*6)
    
if "__name__" == "__main__":
    app.run(debug=True)
