from flask import Flask

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def test():
    return "Rota de teste funcionando!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)