from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello everyone, i am here to help you . Please let me know if you need any kind of assistance. i hope everyone is doing well.All izz well"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

