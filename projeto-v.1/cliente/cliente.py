import socket
import json

def enviar_json():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    endereco_servidor = ('localhost', 5000)

    try:
        cliente.connect(endereco_servidor)

        with open("system_info.json", "r") as arquivo:
            json_data = json.load(arquivo)
        dados = json.dumps(json_data)
        cliente.sendall(dados.encode())
        print("JSON enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar o JSON: {str(e)}")

    finally:
        cliente.close()

if __name__ == "__main__":
    enviar_json()
