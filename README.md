# Bot de Telegram

Um bot do Telegram feito para enviar mensagens, músicas, fotos de gatos e cachorros, além de lembretes diários personalizados.

## ✨ Funcionalidades

- `/start` — Inicia a conversa e salva o chat ID.
- `/song` — Envia uma música aleatória com um link do Spotify.
- `/gato` — Envia uma imagem de gato.
- `/dog` — Envia uma imagem de cachorro.
- 💌 Mensagem de bom dia — Enviada automaticamente todos os dias às 06:00.
- 💭 Mensagens aleatórias — Enviadas a cada 24 horas.

## 📦 Estrutura

- `bot.py` — Arquivo principal com as rotas de comandos e agendamentos.
- `audios.py` — Dicionário de músicas com título e link.
- `fotos.py` — URLs organizadas de fotos de gatos e cachorros.
- `utils.py` — Funções auxiliares para salvar e carregar os IDs dos chats.
- `chats.json` — Onde os IDs dos usuários são salvos (não deve ser versionado).
- `requirements.txt` — Lista de dependências para rodar o projeto.

## 🛠️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Cabana021/bot-telegram
   cd bot-telegram
   ```
