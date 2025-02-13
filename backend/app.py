from flask import Flask
from routes.product_routes import product_bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/test", methods=['GET'])
def test():
    return "Rota de teste funcionando!"

app.register_blueprint(product_bp, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True, port=5001)