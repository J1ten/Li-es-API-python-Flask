import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/cep', methods=['POST'])
def buscar_enderecos():
    data = request.get_json()
    cep = data.get('cep')

    #validar se é um CEP válido 
    if not cep or len(cep) != 8 or not cep.isdigit():
        return {"error": "CEP inválido"}, 400

    cep = cep.replace("-", "").strip()

    #consulta a API no ViaCEP (app gratuito de consulta de CEPs)
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code != 200:
        return ({"error": "erro ao consultar o CEP tente novamente!"}), 500
    
    dados = response.json()
    if "error" in dados:
        return jsonify({"error": "CEP não encontrado"}), 404
    
    return jsonify(dados)