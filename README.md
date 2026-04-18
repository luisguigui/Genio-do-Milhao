🎯 Gênio Edition: Quem Quer Ser um Milionário?
Este é um jogo de quiz interativo desenvolvido em Python, utilizando a biblioteca CustomTkinter. Inspirado no clássico formato de programas de TV, o projeto combina lógica de programação, gestão de estados de jogo e uma interface visual moderna com estética "Cyber/Neon".

🚀 Funcionalidades
Mecânicas Especiais: Inclui níveis "Gênio" onde a resposta pode estar no enunciado ou o botão correto foge do cursor do rato.

Sistema de Progressão: 7 níveis de prémios, desde R$ 1.000 até ao prémio máximo de R$ 1.000.000.

Ajudas Disponíveis:

50/50: Elimina duas opções incorretas.

Pular: Permite avançar para a próxima pergunta sem penalização.

Interface Moderna: Construída com CustomTkinter para um visual dark mode refinado.

Arquitetura Limpa: Separação clara entre a lógica do jogo (EstadoJogo) e a interface gráfica (JogoGenioMilhao).

🛠️ Tecnologias Utilizadas
Python 3.x

CustomTkinter: Para a interface gráfica (GUI).

Tkinter: Para gestão de eventos e posicionamento.

Random: Para embaralhamento de perguntas e opções.

📋 Como Executar
Certifica-te de que tens o Python instalado.

Instala a biblioteca necessária:

Bash
pip install customtkinter
Executa o script:

Bash
python nome_do_arquivo.py
🧠 Estrutura do Código
O código está organizado para facilitar a manutenção:

PERGUNTAS: Base de dados contendo as questões, opções e o tipo de desafio.

EstadoJogo: Classe que controla a pontuação, o nível atual e o estado das ajudas.

JogoGenioMilhao: Classe principal que gere toda a renderização, animações do "botão fugitivo" e interações do utilizador.

🖼️ Pré-visualização da UI
A interface conta com uma barra lateral para acompanhar os prémios conquistados e uma área central dinâmica que se adapta conforme o tipo de pergunta (Normal, Fugitiva ou Texto).
