from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/dados_clientes', methods=['GET'])
def receive_json():
    data = request.get_json()
    with open('dados.json', 'w') as file:
        json.dump(data, file)
    return jsonify(data),'JSON recebido e armazenado com sucesso!'

if __name__ == '__main__':
    app.run()
