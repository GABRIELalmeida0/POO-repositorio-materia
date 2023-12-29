import socket
import json

def receber_json():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    porta = 5000

    servidor.bind(('0.0.0.0', porta))

    servidor.listen()

    print(f"Servidor ouvindo na porta {porta}...")

    while True:
        conexao, endereco = servidor.accept()
        try:
            print(f"Conexão estabelecida com {endereco}")

            dados = conexao.recv(1024).decode()

            json_data = json.loads(dados)

            with open(f"dados-{endereco[0]}.json", "w") as arquivo:
                json.dump(json_data, arquivo)

            print("JSON recebido e armazenado com sucesso!")

        except Exception as e:
            print(f"Erro ao receber e armazenar o JSON: {str(e)}")

        finally:
            conexao.close()

if __name__ == "__main__":
    receber_json()