from pypresence import Presence
import time

# ID do aplicativo no Discord Developer Portal
CLIENT_ID = "1094988729850003486"

# Conecta ao Rich Presence
rpc = Presence(CLIENT_ID)
rpc.connect()

# Função para atualizar o Rich Presence
def atualizar_status():
    agora = int(time.time())  # Tempo atual
    dois_anos_atras = agora - 63072000  # 2 anos atrás em segundos

    rpc.update(
        large_image="Kasane Teto",  # Nome da imagem enviada no Developer Portal
        large_text="Teto Teto Teto Teto",
        small_image="nome_da_imagem_pequena",  # (Opcional) Nome da imagem pequena
        small_text="Texto para imagem pequena",
        details="Brincando com Conceitos",  # Título do status
        state="Progresso: Consumindo sua alma.",  # Descrição do status
        start=dois_anos_atras  # Início do tempo
    )
    print("Status atualizado!")

if __name__ == "__main__":
    while True:
        atualizar_status()
        time.sleep(15)  # Atualiza o status a cada 15 segundos
