from flask import Flask, request, jsonify
import json
from os import listdir 

app = Flask(__name__)

@app.route('/dados_clientes', methods=['GET'])
def receive_json():
    files = [file for file in listdir('.') if file.startswith("dados")]
    data = {}
    for file_name in files:
        with open(file_name, 'r') as file:
            ip = file_name.split("-")[1][:-5]  
            data.update({ip:json.loads(file.read())})
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
