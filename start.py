
from flask import Flask
from flask import jsonify
import randomCNF

if __name__ == "__main__":

    app = Flask(__name__)

    @app.route('/')
    def get():
        solution = randomCNF.ok()
        return {'cnf':solution}

    app.run(host='0.0.0.0', port=8000)