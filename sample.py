from flask import Flask, redirect
from flask_color_extended import color

app = Flask(__name__)
app.config['DEBUG'] = True
color.init_app(app)

@app.route("/demo_get", methods=['GET'])
def demo_get():
    import time
    time.sleep(0.3)
    return "Ok!"

@app.route("/demo_post", methods=['POST'])
def demo_post():
    import time
    time.sleep(0.8)
    return "Ok!"

if __name__ == '__main__':
    app.run()