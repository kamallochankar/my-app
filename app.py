from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hi hello everyone, myself narendra modi.how are you all. i hope everyone is doing well and i am here to help you."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

