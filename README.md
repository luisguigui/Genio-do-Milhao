# 🎯 Gênio do Milhão - Quiz Edition

<div align="center">
  
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-green.svg?style=flat-square)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg?style=flat-square)]()

**Um jogo de quiz interativo inspirado no "Show do Milhão", desenvolvido em Python com mecânicas desafiadoras e interface moderna.**

[🎮 Jogar](#-como-executar) • [📚 Documentação](#-documentação-técnica) • [🏗️ Arquitetura](#-arquitetura-do-código) • [🚀 Features](#-funcionalidades-principais)

</div>

---

## 📖 Sobre o Projeto

**Gênio do Milhão** é uma aplicação educacional e divertida que recria a experiência clássica do programa de TV "Show do Milhão" com um toque inovador: **mecânicas de jogo dinâmicas** que desafiam não apenas o conhecimento, mas também os reflexos e o raciocínio lógico do jogador.

O projeto demonstra competências avançadas em:
- ✅ **Programação Orientada a Objetos (POO)**
- ✅ **Desenvolvimento de Interfaces Gráficas (GUI)**
- ✅ **Arquitetura clean (MVC/Separação de Responsabilidades)**
- ✅ **Event Handling e Animações em tempo real**
- ✅ **Gestão de estado complexa**

---

## 🌟 Funcionalidades Principais

### 1. **Três Tipos de Desafios** 🎯

#### 🔹 Pergunta Normal
- Quiz tradicional com 4 opções de resposta
- Lógica e conhecimento geral
- Prêmios progressivos: R$ 1.000 até R$ 1.000.000

```
Pergunta: Qual a capital do Brasil?
[A) São Paulo]  [B) Rio de Janeiro]
[C) Brasília]   [D) Salvador]
```

#### 🔹 Botão Fugitivo (Genius Mode 🧠)
- O botão correto **FOGE DO MOUSE** quando você tenta clicar!
- Desafia reflexos e precisão
- Implementado com bind de eventos de mouse e reposit posição aleatória

```python
# Quando o mouse se aproxima do botão correto:
def _fugir(self, btn):
    nx = random.randint(10, w - 290)  # Nova posição aleatória
    ny = random.randint(10, h - 70)
    btn.place(x=nx, y=ny)  # Move para nova localização
```

#### 🔹 Resposta no Texto (Brain Mode 🧠)
- A resposta correta está **OCULTA NO ENUNCIADO**
- O jogador deve clicar na pergunta, não nos botões
- Ativa pensamento lateral e atenção aos detalhes

```
Pergunta: "Qual a cor do cavalo BRANCO de Napoleão?"
Resposta: BRANCO (escondida na própria pergunta)
```

---

### 2. **Sistema de Prêmios Progressivos** 💰

| Nível | Pergunta | Prêmio | Dificuldade |
|-------|----------|--------|------------|
| 1 | Q1 | R$ 1.000 | ⭐ Fácil |
| 2 | Q2 | R$ 5.000 | ⭐⭐ Fácil |
| 3 | Q3 | R$ 10.000 | ⭐⭐ Médio |
| 4 | Q4 | R$ 50.000 | ⭐⭐⭐ Difícil |
| 5 | Q5 | R$ 100.000 | ⭐⭐⭐⭐ Difícil |
| 6 | Q6 | R$ 500.000 | ⭐⭐⭐⭐ Muito Difícil |
| 7 | Q7 | **R$ 1.000.000** | ⭐⭐⭐⭐⭐ Gênio |

**Sistema de Segurança:**
- Prêmios conquistados em níveis anteriores nunca são perdidos
- Errar = Game Over e você fica com o prêmio do nível anterior

---

### 3. **Ajudas Estratégicas** 🆘

#### 🎯 50/50
- **Efeito:** Elimina 2 respostas incorretas, deixando 2 opções
- **Implementação:**
```python
def usar_50(self, opcoes_atuais: list) -> list:
    correta = self.pergunta_atual["correta"]
    erradas = [o for o in opcoes_atuais if o != correta]
    random.shuffle(erradas)
    eliminar = erradas[:2]  # Remove as 2 primeiras erradas
    self.ajuda_50_disponivel = False
    return eliminar
```
- **Limite:** Apenas 1 uso por jogo
- **Visual:** Botões desabilitados mostram "—"

#### ⏭️ PULAR
- **Efeito:** Avança para próxima pergunta SEM penalidade
- **Limite:** Apenas 1 uso por jogo
- **Não conta como:** Acerto ou Erro
- **Implementação:**
```python
def usar_pular(self):
    self.ajuda_pular_disponivel = False
    self.nivel += 1  # Avança sem incrementar respostas_certas
```

---

### 4. **Interface Moderna e Responsiva** 🎨

- **Tema Dark Mode** nativo com CustomTkinter
- **Paleta de cores profissional:**
  - 🟦 Azul (Principal)
  - 🟨 Ouro (Prêmios e destaque)
  - 🟩 Verde (Acertos e ajudas)
  - 🟥 Vermelho (Erros)
  
- **Componentes UI:**
  - Sidebar com visualização de prêmios
  - Grade 2×2 de botões responsivos
  - Feedback visual imediato
  - Animações suaves e intuitivas

---

## 🛠️ Stack Técnico

| Componente | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|----------|
| **Linguagem** | Python | 3.8+ | Backend e lógica |
| **GUI Framework** | CustomTkinter | Latest | Interface moderna |
| **Toolkit Base** | Tkinter | Built-in | Renderização gráfica |
| **Randomização** | random | Built-in | Embaralhamento de perguntas/opções |

---

## 🏗️ Arquitetura do Código

### 📁 Estrutura Geral

```
Genio-do-Milhao/
├── game.py                  # Arquivo principal (tudo em um)
├── README.md               # Este arquivo
└── requirements.txt        # Dependências
```

### 🧠 Arquitetura MVC Implementada

```
┌─────────────────────────────────────────┐
│         JogoGenioMilhao (View)          │
│   - Renderiza interface (CustomTkinter) │
│   - Gerencia eventos de UI              │
│   - Exibe feedback visual               │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│       Métodos de Controle (Controller)  │
│   - _clicar_botao()                     │
│   - _processar_resposta()               │
│   - _usar_50()                          │
│   - _usar_pular()                       │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│          EstadoJogo (Model)             │
│   - Perguntas e Respostas              │
│   - Lógica de validação                │
│   - Estado das ajudas                  │
│   - Prêmios e progressão               │
└─────────────────────────────────────────┘
```

### 📋 Classes Principais

#### 🎮 **EstadoJogo**
Gerencia toda a lógica pura do jogo, sem dependência de UI.

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `perguntas` | `list[dict]` | Perguntas do jogo (embaralhadas) |
| `nivel` | `int` | Pergunta atual (0-6) |
| `respostas_certas` | `int` | Contador de acertos |
| `ajuda_50_disponivel` | `bool` | Status da ajuda 50/50 |
| `ajuda_pular_disponivel` | `bool` | Status da ajuda Pular |

| Método | Parâmetros | Retorno | Descrição |
|--------|-----------|---------|-----------|
| `verificar()` | `resposta: str` | `bool` | Valida se resposta está correta |
| `avancar()` | - | `None` | Incrementa nível e acertos |
| `usar_50()` | `opcoes_atuais: list` | `list` | Remove 2 opções, retorna quais eliminar |
| `usar_pular()` | - | `None` | Avança sem contar como acerto |

**Exemplo de Uso:**
```python
jogo = EstadoJogo()
pergunta = jogo.pergunta_atual  # Obtém pergunta atual

if jogo.verificar("Brasília"):
    jogo.avancar()  # Resposta correta!
else:
    # Game Over
    print(f"Perdeu! A resposta era: {pergunta['correta']}")
```

---

#### 🖼️ **JogoGenioMilhao (Janela Principal)**
Classe que herda de `ctk.CTk` e gerencia toda a interface.

**Seções Principais:**

##### 1. **Construção da UI** (`_build_ui`)
```
┌────────────────────────────────────────┐
│ PREMIAÇÃO (Sidebar Esquerda)           │
│ R$ 1.000.000 ← Objetivo final          │
│ R$ 500.000                             │
│ R$ 100.000                             │
│ R$ 50.000                              │
│ R$ 10.000                              │
│ R$ 5.000                               │
│ R$ 1.000 ← Início                      │
│                                        │
├────────────────────────────────────────┤
│ ÁREA PRINCIPAL                         │
│                                        │
│ Pergunta 3 de 7 — Prêmio: R$ 10.000  │
│                                        │
│ "Qual a cor do cavalo branco?"        │
│                                        │
│ [A) São Paulo]  [B) Rio de Janeiro]   │
│ [C) Brasília]   [D) Salvador]         │
│                                        │
│ [50/50]  [⏭ PULAR]                    │
│ [➡ PRÓXIMA PERGUNTA]                  │
└────────────────────────────────────────┘
```

##### 2. **Fluxo de Telas**
```
_mostrar_tela_inicial()
    ↓ [Clica em JOGAR]
_carregar_pergunta()
    ↓
[Responde pergunta]
    ├─ Correta? → Feedback ✅ → Próxima pergunta
    ├─ Errada?  → Feedback ❌ → _tela_game_over()
    └─ Pula?    → Próxima pergunta (sem ajuda)
    ↓
[7 perguntas?] → _tela_vitoria() 🏆
```

##### 3. **Sistema de Mecânicas Especiais**

**Pergunta com Texto Oculto:**
```python
if dados["tipo"] == "texto_pergunta":
    self.lbl_pergunta.bind("<Button-1>", lambda e: self._responder_correto())
    self.lbl_pergunta.configure(cursor="hand2")  # Indica clickável
    for btn in self.botoes:
        btn.configure(state="disabled")  # Desabilita botões
```

**Botão Fugitivo:**
```python
if dados["tipo"] == "botao_fujao":
    idx_fugitivo = self._opcoes_atuais.index(correta)
    self._ativar_fugitivo(self.botoes[idx_fugitivo])
    # Cada vez que passa o mouse próximo, o botão se move!
```

---

## 💾 Banco de Dados de Perguntas

O arquivo contém **20 perguntas** com três atributos cada:

```python
{
    "pergunta": "Qual a capital do Brasil?",
    "opcoes": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
    "correta": "Brasília",
    "tipo": "normal"  # ou "texto_pergunta" ou "botao_fujao"
}
```

**Mecânica de Seleção:**
1. Pool de 20 perguntas é embaralhado (shuffle)
2. Apenas 7 são selecionadas (conforme quantidade de prêmios)
3. Nenhuma pergunta se repete no mesmo jogo

```python
pool = PERGUNTAS[:]
random.shuffle(pool)
self.perguntas = pool[:self.MAX_PERGUNTAS]  # Pega apenas 7
```

---

## 🎮 Como Executar

### ✅ Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)
- ~20MB de espaço em disco

### 🔧 Instalação Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/luisguigui/Genio-do-Milhao.git
cd Genio-do-Milhao
```

2. **Crie um ambiente virtual (recomendado):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instale a dependência:**
```bash
pip install customtkinter
```

4. **Execute o jogo:**
```bash
python game.py
```

### 🎮 Como Jogar

1. **Clique em "▶ JOGAR"** para iniciar
2. **Leia a pergunta** cuidadosamente
3. **Escolha sua resposta:**
   - Clique em um dos 4 botões (A, B, C, D) para respostas normais
   - Clique na pergunta para perguntas de texto oculto
   - Tente clicar no botão antes de ele fugir (botão fugitivo)
4. **Use suas ajudas estrategicamente:**
   - **50/50:** Quando estiver em dúvida
   - **PULAR:** Para perguntas muito difíceis
5. **Acerte todas as 7 perguntas** para virar um Gênio Milionário! 🏆

---

## 🔑 Conceitos Técnicos Explicados

### 1. **Event Binding em Tkinter**

O código usa `bind()` para associar eventos do mouse a ações:

```python
# Ao passar mouse sobre botão fugitivo, ele se move
btn.bind("<Enter>", lambda e: self._fugir(btn))

# Ao clicar na pergunta (tipo texto_pergunta), responde
self.lbl_pergunta.bind("<Button-1>", lambda e: self._responder_correto())
```

**Eventos comuns:**
- `<Button-1>`: Clique esquerdo do mouse
- `<Enter>`: Mouse entra na área do widget
- `<Return>`: Tecla Enter pressionada
- `<space>`: Barra de espaço pressionada

### 2. **State Management (Gestão de Estado)**

O atributo `_respondendo` previne cliques duplos:

```python
def _clicar_botao(self, idx: int):
    if self._respondendo or not self._opcoes_atuais:
        return  # Ignora clique se já respondendo
    # ... processa resposta
    self._respondendo = True  # Bloqueia outros cliques
```

### 3. **Grid System em CustomTkinter**

Botões organizados em grid 2×2:

```python
for i, btn in enumerate(self.botoes):
    btn.grid(row=i // 2, column=i % 2, padx=10, pady=8)
    # i=0 → row=0, col=0 (canto superior esquerdo)
    # i=1 → row=0, col=1 (canto superior direito)
    # i=2 → row=1, col=0 (canto inferior esquerdo)
    # i=3 → row=1, col=1 (canto inferior direito)
```

### 4. **Scheduling com after()**

CustomTkinter permite agendar funções:

```python
# Mostra tela de vitória após 1 segundo
self.after(1200, self._tela_vitoria)

# Move botão fugitivo a cada 60ms
self._fugitivo_job = self.after(60, lambda: self._fugir(btn))

# Cancela agendamento
self.after_cancel(self._fugitivo_job)
```

### 5. **Propriedades Computed (@property)**

O `EstadoJogo` usa propriedades para lógica apenas leitura:

```python
@property
def premio_atual(self):
    """Retorna o prêmio em jogo do nível atual"""
    idx = min(self.nivel, len(PREMIOS) - 1)
    return PREMIOS[idx]

@property
def concluido(self):
    """True quando todas as 7 perguntas foram respondidas"""
    return self.nivel >= len(self.perguntas)
```

---

## 📊 Fluxo de Execução Completo

```
START
  ↓
[Criar JogoGenioMilhao()] ──→ Construir UI
  ↓
_mostrar_tela_inicial()
  │
  ├─→ Limpar sidebar
  ├─→ Mostrar título "Gênio Edition"
  ├─→ Ocultar botões de resposta
  └─→ Botão "▶ JOGAR" ativo
         ↓
    [Clique em JOGAR]
         ↓
    EstadoJogo() ──→ Embaralha 7 de 20 perguntas
         ↓
    _carregar_pergunta() (Nível 0)
         │
         ├─→ Atualizar sidebar (highlight prêmio em jogo)
         ├─→ Mostrar pergunta
         ├─→ Embaralhar e mostrar 4 opções
         ├─→ Aplicar mecânica especial (se houver)
         └─→ Ativar botões de ajuda (se tipo == "normal")
                ↓
           [Jogador responde...]
                ├─ Clica em botão A, B, C ou D
                ├─ Ou clica na pergunta (texto oculto)
                └─ Ou tenta clicar em botão fugitivo
                       ↓
              _processar_resposta()
                       │
                       ├─→ Desabilitar botões
                       ├─→ Verificar resposta (EstadoJogo.verificar())
                       │
                       ├─ ACERTOU? ✅
                       │   ├─→ Botão fica verde
                       │   ├─→ "✅ Correto!" aparece
                       │   ├─→ jogo.avancar()
                       │   │
                       │   ├─ São todas 7? → _tela_vitoria() 🏆
                       │   └─ Senão → Botão "➡ PRÓXIMA PERGUNTA"
                       │
                       └─ ERROU? ❌
                           ├─→ Botão fica vermelho
                           ├─→ "❌ Errado! A resposta era: ..." aparece
                           └─→ _tela_game_over() (após 2.2s)
                                  │
                                  └─→ Botão "🔄 JOGAR NOVAMENTE"
                                         ↓
                                      [Clique]
                                         ↓
                                    Volta ao JOGAR
                                         ↓
                                        END
```

---

## 🐛 Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'customtkinter'"

**Solução:**
```bash
pip install customtkinter
```

### ❌ "Janela não abre ou fica vazia"

**Possível causa:** Versão do Python incompatível
**Solução:** Use Python 3.8 ou superior
```bash
python --version
python3 --version  # Se disponível
```

### ❌ "Botões não aparecem ou interface deformada"

**Solução:** Redimensione a janela manualmente (arraste a borda)

### ❌ "CustomTkinter não encontra biblioteca Tcl/Tk"

**Solução (Windows):**
```bash
pip install --upgrade customtkinter
```

**Solução (macOS):**
```bash
brew install python-tk@3.11  # Ou sua versão de Python
```

---

## 🚀 Roadmap Futuro

- [ ] **v2.0:** Sistema de pontuação e ranking local
- [ ] **v2.0:** Temas customizáveis (Light Mode, etc)
- [ ] **v2.1:** Base de dados de perguntas expansível (JSON externo)
- [ ] **v2.1:** Modo multiplayer local (2 jogadores alternados)
- [ ] **v3.0:** Integração com API de perguntas online
- [ ] **v3.0:** Desktop notificações de novo recorde
- [ ] **v4.0:** Versão mobile (Kivy)
- [ ] **v4.0:** Modo "Time do Conhecimento" (2v2)

---

## 📝 Documentação do Código

### Comentários Importantes

O código é bem comentado com seções claramente marcadas:

```python
# ──────────────────────────────────────────
#  BANCO DE PERGUNTAS (sem duplicatas)
# ──────────────────────────────────────────

# ── Cores ──────────────────────────────────────

# ──────────────────────────────────────────
#  CONSTRUÇÃO DA INTERFACE
# ──────────────────────────────────────────
```

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Se encontrou um bug ou tem uma ideia:

1. **Abra uma Issue** descrevendo o problema/sugestão
2. **Faça um Fork** do repositório
3. **Crie uma branch** para sua feature:
   ```bash
   git checkout -b feature/sua-ideia
   ```
4. **Commit suas mudanças:**
   ```bash
   git commit -am 'Adiciona sua feature'
   ```
5. **Push para a branch:**
   ```bash
   git push origin feature/sua-ideia
   ```
6. **Abra um Pull Request**

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Você é livre para usar, modificar e distribuir, desde que mantenha a menção ao autor original.

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 📧 Entre em contato para sugestões e melhorias!

---

## 🙏 Agradecimentos

- Inspirado no "Show do Milhão" (SBT)
- CustomTkinter pela excelente biblioteca GUI
- Python community pelo suporte contínuo

---

## 📞 Suporte

Teve algum problema? Abra uma [Issue](https://github.com/luisguigui/Genio-do-Milhao/issues) e vou ajudar!

---

<div align="center">

**⭐ Se gostou do projeto, considere dar uma estrela! Isso nos ajuda muito!**

Última atualização: **20 de Abril de 2026**

</div>
```

---

Agora vou atualizar o arquivo no repositório:Perfeito! Vou criar um README profissional e detalhado para o seu projeto. Vou gerar o conteúdo completo que você pode copiar e colar diretamente no seu repositório:

```markdown
# 🎯 Gênio do Milhão — Quem Quer Ser um Milionário?

> Um jogo de quiz interativo e desafiador inspirado no clássico "Show do Milhão", desenvolvido em Python com a biblioteca **CustomTkinter**. Apresenta três tipos de desafios únicos, sistema de progressão com prêmios acumulativos e ajudas estratégicas.

[![Python](https://img.shields.io/badge/python-3.8+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)]()

<div align="center">
  
  **[🚀 Instalação](#-instalação-e-execução) • [📖 Documentação](#-arquitetura-e-estrutura) • [🎮 Como Jogar](#-como-jogar) • [🛠️ Tecnologias](#️-tecnologias-utilizadas)**
  
</div>

---

## 🌟 Visão Geral

O **Gênio do Milhão** é um simulador educacional e divertido do famoso programa de TV "Quem Quer Ser um Milionário?". O projeto combina **lógica de programação avançada** com **interface gráfica moderna**, implementando mecânicas de jogo sofisticadas que testam tanto o conhecimento quanto os reflexos do jogador.

### ✨ Destaques Principais

- 🎮 **3 Tipos de Desafios Únicos**: Perguntas normais, botões fugitivos e respostas ocultas no texto
- 💰 **Sistema de Progressão**: 7 níveis de prêmios (R$ 1.000 até R$ 1.000.000)
- 🆘 **Ajudas Estratégicas**: 50/50 (elimina 2 opções) e PULAR (avança sem penalidade)
- 🎨 **Interface Dark Mode**: Design moderno e responsivo com CustomTkinter
- 🏗️ **Arquitetura Limpa**: Separação clara entre lógica de jogo (Model) e interface (View)
- 🔀 **Embaralhamento Inteligente**: Perguntas e opções são sempre aleatórias

---

## 🎮 Como Jogar

### 🎯 Objetivo
Responder corretamente a 7 perguntas progressivamente mais difíceis para conquistar o prêmio de **R$ 1.000.000** e se tornar um "Gênio Milionário".

### 📋 Regras Básicas

1. **Cada pergunta** tem 4 opções de resposta
2. **Resposta correta** = avança para o próximo nível
3. **Resposta errada** = FIM DE JOGO (mas você mantém o prêmio do nível anterior)
4. **Você começa com 2 ajudas**:
   - **50/50**: Elimina 2 opções incorretas
   - **PULAR**: Avança para a próxima pergunta sem responder

### 🎲 Os 3 Tipos de Desafios

#### 1️⃣ **Pergunta Normal** ⭐
A resposta correta está entre os 4 botões. Clique na opção que você acredita.

```
┌─────────────────────────────────────┐
│  Qual a capital do Brasil?          │
├─────────────────────────────────────┤
│ A) São Paulo    │  B) Rio de Janeiro│
├─────────────────────────────────────┤
│ C) Brasília     │  D) Salvador      │
└─────────────────────────────────────┘
```

**Dificuldade**: Depende do nível da pergunta  
**Estratégia**: Use seus conhecimentos

---

#### 2️⃣ **Botão Fugitivo** 🏃‍♂️
O botão com a resposta correta **FOGE DO SEU MOUSE**! Você precisa conseguir clicar nele antes que seja tarde demais.

```python
# Exemplo de pergunta tipo "botão fugitivo"
{
    "pergunta": "Clique no botão de MENOR valor:",
    "opcoes": ["R$ 100", "R$ 50", "R$ 10", "R$ 1"],
    "correta": "R$ 1",
    "tipo": "botao_fujao"  # 🏃‍♂️ Este botão vai fugir!
}
```

**Dificuldade**: ⭐⭐⭐⭐ (Reflexos + Conhecimento)  
**Estratégia**: 
- Saiba qual é a resposta ANTES de tentar clicar
- Mova o mouse devagar e com precisão
- Ou use a ajuda **50/50** para ter apenas 2 opções

---

#### 3️⃣ **Resposta no Texto** 🧠
A resposta correta está **OCULTA NO PRÓPRIO ENUNCIADO** da pergunta! Os botões ficarão desabilitados até você clicar na pergunta.

```python
# Exemplo de pergunta com resposta no texto
{
    "pergunta": "Qual a cor do cavalo BRANCO de Napoleão?",
    "opcoes": ["Preto", "Marrom", "Cinza", "Azul"],
    "correta": "Branco",
    "tipo": "texto_pergunta"  # 🧠 Resposta está na pergunta!
}
```

**Dificuldade**: ⭐⭐⭐ (Atenção + Lógica)  
**Estratégia**: 
- Leia a pergunta COM ATENÇÃO
- A resposta sempre está subliminarmente no texto
- Clique na pergunta quando tiver a resposta

---

### 💰 Tabela de Prêmios

| Nível | Prêmio | Dificuldade |
|-------|--------|-----------|
| 1 | R$ 1.000 | ⭐ Fácil |
| 2 | R$ 5.000 | ⭐⭐ Médio |
| 3 | R$ 10.000 | ⭐⭐ Médio |
| 4 | R$ 50.000 | ⭐⭐⭐ Difícil |
| 5 | R$ 100.000 | ⭐⭐⭐ Difícil |
| 6 | R$ 500.000 | ⭐⭐⭐⭐ Muito Difícil |
| 7 | R$ 1.000.000 | ⭐⭐⭐⭐⭐ Genius Mode |

**💡 Dica**: O prêmio que você já conquistou está garantido. Se errar, você sai com o prêmio do nível anterior!

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Propósito |
|-----------|-----------|----------|
| **Linguagem** | Python 3.8+ | Lógica e automação |
| **GUI** | CustomTkinter | Interface moderna Dark Mode |
| **Eventos** | Tkinter (nativo) | Manipulação de eventos |
| **Aleatoriedade** | Random | Embaralhamento de perguntas |
| **Persistência** | JSON (opcional) | Salvar progresso (futuro) |

### Por que CustomTkinter?

- ✅ Interface moderna sem parecer "antiga"
- ✅ Dark Mode nativo (esteticamente agradável)
- ✅ Componentes customizáveis (cores, fontes, tamanhos)
- ✅ Leve (sem dependências pesadas)
- ✅ Multiplataforma (Windows, macOS, Linux)

---

## 📋 Instalação e Execução

### ✅ Pré-requisitos

- **Python 3.8** ou superior
- **pip** (gerenciador de pacotes)
- Espaço em disco: ~20MB

### 🔧 Passos de Instalação

#### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/luisguigui/Genio-do-Milhao.git
cd Genio-do-Milhao
```

#### 2️⃣ Crie um Ambiente Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Instale a Dependência
```bash
pip install customtkinter
```

#### 4️⃣ Execute o Jogo
```bash
python game.py
```

A janela do jogo deve abrir. Clique em **▶ JOGAR** para começar!

### 🐛 Troubleshooting

**Problema**: `ModuleNotFoundError: No module named 'customtkinter'`  
**Solução**: Execute `pip install customtkinter` novamente

**Problema**: A janela não abre no Linux  
**Solução**: Você pode precisar instalar `python3-tk`: `sudo apt-get install python3-tk`

**Problema**: Botões não aparecem corretamente  
**Solução**: Verifique se está usando Python 3.8+ (`python --version`)

---

## 🏗️ Arquitetura e Estrutura

### 📊 Fluxo de Dados

```
┌─────────────────────────────────────┐
│   JogoGenioMilhao (Main Window)     │
│   (Classe Principal - UI Controller)│
└────────────────┬────────────────────┘
                 │
         ┌───────▼────────┐
         │  EstadoJogo    │
         │  (Game Logic)  │
         │  [Model]       │
         └───────┬────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼──┐              ┌──────▼────┐
│BANCO │              │  Eventos  │
│ DE   │              │  do       │
│PEGUNTAS         │  Usuário│
└──────┘              └───────────┘
```

### 🧩 Componentes Principais

```
game.py
│
├── 📦 BANCO DE DADOS
│   ├── PERGUNTAS[] ........... Lista com 20+ perguntas
│   └── PREMIOS[] ............ Tabela de prêmios
│
├── 🎨 PALETA DE CORES
│   ├── COR_BG_ESCURO ........ Fundo principal (#05051a)
│   ├── COR_BORDA ........... Bordas azuis
│   ├── COR_OURO ........... Destacar prêmios
│   └── ... (mais 10+ cores)
│
├── 🧠 CLASSE: EstadoJogo (Model)
│   ├── __init__() .......... Inicializa estado
│   ├── pergunta_atual ..... Retorna pergunta do nível
│   ├── premio_atual ....... Prêmio em jogo agora
│   ├── premio_conquistado . Prêmio do nível anterior
│   ├── concluido ......... Verifica se ganhou
│   ├── verificar() ....... Valida resposta
│   ├── avancar() ......... Próximo nível
│   ├── usar_50() ........ Elimina 2 opções
│   └── usar_pular() ..... Pula pergunta
│
└── 🎮 CLASSE: JogoGenioMilhao (View/Controller)
    ├── _build_ui() ............. Constrói interface
    ├── _mostrar_tela_inicial() . Tela inicial
    ├── _carregar_pergunta() ... Carrega próxima pergunta
    ├── _tela_game_over() ...... Tela de derrota
    ├── _tela_vitoria() ........ Tela de vitória
    ├── _clicar_botao() ....... Processa clique
    ├── _processar_resposta() . Valida e processa
    ├── _ativar_fugitivo() .... Ativa botão fugitivo
    ├── _fugir() ............ Faz botão fugir
    └── ... (10+ métodos de UI)
```

---

## 📚 Documentação das Classes Principais

### 1️⃣ `EstadoJogo` — Gerenciador de Lógica

**Responsabilidade**: Manter o estado puro do jogo, sem conhecimento de UI.

**Atributos**:

```python
class EstadoJogo:
    nivel: int                      # Pergunta atual (0-6)
    respostas_certas: int          # Contador de acertos
    ajuda_50_disponivel: bool      # 50/50 ainda pode ser usado?
    ajuda_pular_disponivel: bool   # PULAR ainda pode ser usado?
    perguntas: list[dict]          # Lista de 7 perguntas
```

**Métodos Chave**:

| Método | Entrada | Saída | Descrição |
|--------|---------|-------|-----------|
| `__init__()` | — | — | Cria novo jogo com 7 perguntas aleat��rias |
| `pergunta_atual` | — | `dict` | Retorna pergunta do nível atual |
| `premio_atual` | — | `str` | Ex: `"R$ 50.000"` |
| `verificar(resposta)` | `str` | `bool` | Compara resposta com gabarito |
| `avancar()` | — | — | Passa para próximo nível |
| `usar_50(opcoes)` | `list` | `list` | Retorna 2 opções a eliminar |
| `usar_pular()` | — | — | Pula pergunta sem contar |

**Exemplo de Uso**:

```python
# Criar novo jogo
jogo = EstadoJogo()

# Pegar pergunta atual
dados = jogo.pergunta_atual
print(dados["pergunta"])      # "Qual a capital do Brasil?"
print(dados["opcoes"])        # ["São Paulo", "Brasília", ...]
print(dados["correta"])       # "Brasília"

# Verificar resposta
if jogo.verificar("Brasília"):
    jogo.avancar()            # Vai para nível 1
    print(jogo.premio_atual)  # "R$ 5.000"

# Usar ajudas
opcoes_a_remover = jogo.usar_50(dados["opcoes"])
# Retorna: ["São Paulo", "Rio de Janeiro"]
```

---

### 2️⃣ `JogoGenioMilhao` — Interface Gráfica e Controller

**Responsabilidade**: Renderizar UI, processar eventos do usuário e coordenar lógica com `EstadoJogo`.

**Estrutura da Janela**:

```
┌───────────────────────────────────────────┐
│        Gênio do Milhão - Interface        │
├─────────────┬───────────────────────────────┤
│             │                               │
│ SIDEBAR     │         MAIN AREA              │
│ (Prêmios)   │                               │
│             │  Pergunta                      │
│ R$1M        │  ┌─────────────┬─────────────┐ │
│ R$500K      │  │  A) Opção 1 │ B) Opção 2 │ │
│ R$100K      │  ├─────────────┼─────────────┤ │
│ R$50K       │  │  C) Opção 3 │ D) Opção 4 │ │
│ R$10K       │  └─────────────┴─────────────┘ │
│ R$5K        │                               │
│ R$1K        │  [50/50]  [⏭ PULAR]         │
│             │                               │
│             │  [▶ JOGAR]                    │
└─────────────┴───────────────────────────────┘
```

**Métodos Importantes**:

| Método | Propósito |
|--------|-----------|
| `_build_ui()` | Constrói toda a interface (sidebar, botões, labels) |
| `_mostrar_tela_inicial()` | Exibe tela de boas-vindas |
| `_carregar_pergunta()` | Carrega pergunta e prepara UI para responder |
| `_clicar_botao(idx)` | Callback quando usuário clica em opção |
| `_processar_resposta(resposta)` | Valida resposta, mostra feedback |
| `_tela_game_over()` | Exibe tela de derrota |
| `_tela_vitoria()` | Exibe tela de vitória |
| `_usar_50()` | Implementa ajuda 50/50 |
| `_usar_pular()` | Implementa ajuda PULAR |
| `_ativar_fugitivo(btn)` | Prepara botão para fugir |
| `_fugir(btn)` | Faz botão se mover aleatoriamente |

---

## 🎯 Conceitos-Chave Explicados

### 1️⃣ **Padrão MVC (Model-View-Controller)**

Nosso código segue este padrão:

```
MODEL (Dados) ← EstadoJogo
├── Armazena: perguntas, nível, ajudas
├── Lógica: verificação, progressão

VIEW (Apresentação) ← JogoGenioMilhao
├── Renderiza: botões, labels, cores
├── Feedback: cores, mensagens

CONTROLLER (Coordenação) ← JogoGenioMilhao
├── Processa: cliques, eventos
├── Orquestra: M ↔ V
```

**Benefício**: Se você quer trocar a interface de Tkinter para Pygame, basta reescrever a VIEW! A MODEL continua igual.

---

### 2️⃣ **Embaralhamento Inteligente**

```python
# No início do jogo
pool = PERGUNTAS[:]           # Cria cópia de TODAS as perguntas
random.shuffle(pool)           # Embaralha
self.perguntas = pool[:7]     # Pega apenas 7 aleatórias

# Resultado: Cada jogo tem perguntas diferentes
```

Também embaralhamos as opções a cada pergunta:

```python
opcoes = dados["opcoes"][:]
random.shuffle(opcoes)  # Embaralha [A, B, C, D]
```

**Por que?** Evita que jogadores memorizem a posição da resposta correta (sempre na opção B, por exemplo).

---

### 3️⃣ **Mecânica do Botão Fugitivo**

O botão correto se move quando o mouse se aproxima:

```python
def _fugir(self, btn):
    # Pega tamanho do container
    w = self.frame_botoes.winfo_width()
    h = self.frame_botoes.winfo_height()
    
    # Gera posição aleatória dentro do container
    nx = random.randint(10, max(10, w - 290))
    ny = random.randint(10, max(10, h - 70))
    
    # Move botão usando place() ao invés de grid()
    btn.place(x=nx, y=ny)
    
    # Re-agenda a fuga em 60ms se mouse ainda estiver perto
    self._fugitivo_job = self.after(60, lambda: ...)
```

**Como funciona**:
1. Usuário move mouse perto do botão
2. Evento `<Enter>` é disparado
3. Botão se move para posição aleatória
4. Se mouse ainda estiver perto, repete (60ms de delay)

---

### 4️⃣ **Sistema de Ajudas**

#### **50/50** — Estratégia Probabilística

```python
def usar_50(self, opcoes_atuais: list) -> list:
    correta = self.pergunta_atual["correta"]
    erradas = [o for o in opcoes_atuais if o != correta]
    
    random.shuffle(erradas)     # Embaralha as erradas
    eliminar = erradas[:2]      # Pega 2 para eliminar
    
    self.ajuda_50_disponivel = False
    return eliminar
```

**Lógica**:
- Encontra todas as opções erradas
- Remove 2 delas aleatoriamente
- Mantém a correta + 1 errada

---

#### **PULAR** — Sem Penalidade

```python
def usar_pular(self):
    self.ajuda_pular_disponivel = False
    self.nivel += 1  # Avança nível SEM contar como acerto
    # Respostas certas não aumenta
```

**Diferença**:
- ❌ Resposta errada = FIM DE JOGO
- ✅ Resposta correta = Avança + Ganha
- ⏭ PULAR = Avança SEM ganhar

---

### 5️⃣ **Gerenciamento de Estados**

O jogo tem 3 estados principais:

```
┌──────────────────┐
│ Tela Inicial     │
│ (Botão: JOGAR)   │
└────────┬─────────┘
         │ Clica JOGAR
         │
┌────────▼──────────┐
│ Carregando        │
│ Pergunta          │ ←─────┐
│ (Respondendo)     │       │ Clica PRÓXIMA
└────────┬──────────┘       │
         │                  │
     Acertou?        Errou?
      /                \
┌────▼─┐        ┌─────▼──┐
│Check │        │Game    │
│Vitória       │Over    │
└────┬─┘        └────────┘
     │              │
   Todas as 7 perdeu uma
   perguntas?
     │
     └─► Tela Final
```

---

## 📊 Fluxo de Resposta Detalhado

```
1. Usuário clica em um botão
   ↓
2. _clicar_botao(idx) é chamado
   ↓
3. _processar_resposta(resposta) inicia
   ↓
4. Desabilita botões (evita duplo clique)
   ↓
5. jogo.verificar(resposta) compara com gabarito
   ↓
   ├─ CORRETO ✅
   │  ├─ Muda cor do botão para VERDE
   │  ├─ Mostra "✅ Correto!"
   │  ├─ jogo.avancar() passa para próximo nível
   │  ├─ Verifica se completou todas 7 perguntas
   │  │  ├─ SIM → _tela_vitoria()
   │  │  └─ NÃO → Mostra botão "PRÓXIMA PERGUNTA"
   │  └─ Aguarda 1200ms antes de mudar de tela
   │
   └─ ERRADO ❌
      ├─ Muda cor do botão para VERMELHO
      ├─ Mostra "❌ Errado! A resposta era: X"
      ├─ Aguarda 2200ms
      └─ Chama _tela_game_over()
```

---

## 🎨 Sistema de Cores

O jogo usa uma paleta **cyberpunk/neon** escura:

```python
COR_BG_ESCURO   = "#05051a"      # Preto bem escuro
COR_BG_PAINEL   = "#0b0b2e"      # Azul muito escuro
COR_BORDA       = "#1e3a8a"      # Azul escuro (bordas)
COR_OURO        = "#fbbf24"      # Ouro (destaques)
COR_AZUL        = "#3b82f6"      # Azul brilhante
COR_VERDE       = "#22c55e"      # Verde (correto)
COR_VERMELHO    = "#ef4444"      # Vermelho (errado)
COR_BTN_NORMAL  = "#1e1e4a"      # Botão padrão
COR_BTN_HOVER   = "#2d2d7a"      # Botão ao passar mouse
COR_BTN_CORRETO = "#14532d"      # Botão resposta certa
COR_BTN_ERRADO  = "#7f1d1d"      # Botão resposta errada
```

---

## 🔄 Fluxo de Início a Fim

### Cenário: Jogador completa o jogo

```
1. Inicializa aplicação
   JogoGenioMilhao()
   ↓
2. Mostra tela inicial
   "🎯 Quem Quer Ser um Milionário?"
   Botão: [▶ JOGAR]
   ↓
3. Usuário clica JOGAR
   _acao_principal() → EstadoJogo criado
   ↓
4. Carrega pergunta 1
   "Quanto é 2 + 2?"
   Opções: A) 3  B) 4  C) 5  D) 22
   ↓
5. Usuário clica B (4)
   _clicar_botao(1) → _processar_resposta("4")
   ✅ Correto! Avança.
   Mostra: [➡ PRÓXIMA PERGUNTA]
   ↓
6. Repete 5-6 para perguntas 2-6
   ↓
7. Pergunta 7 (última)
   Usuário acerta
   ✅ Correto! Verificou concluido = True
   ↓
8. Mostra tela de vitória
   "🏆 PARABÉNS! Você é um Gênio Milionário!"
   Prêmio: R$ 1.000.000
   Botão: [🔄 JOGAR NOVAMENTE]
   ↓
9. Usuário clica JOGAR NOVAMENTE
   Volta ao passo 3 (novo EstadoJogo criado)
```

---

## 🚀 Possíveis Melhorias Futuras

- [ ] **Salvar Progresso**: Persistir em JSON/SQLite
- [ ] **Multiplayer**: Modo competição entre jogadores
- [ ] **Temas Personalizados**: Diferentes categorias de perguntas
- [ ] **Sistema de Ranking**: Top 10 jogadores
- [ ] **Animações**: Efeitos de entrada/saída dos botões
- [ ] **Áudio**: Efeitos sonoros (acerto, erro, vitória)
- [ ] **Estatísticas**: Gráfico de desempenho do jogador

---

## 🐛 Troubleshooting Avançado

### ❌ Problema: Botões aparecem desalinhados
**Causa**: Janela muito pequena  
**Solução**: Redimensione a janela ou aumente `minsize(820, 580)`

### ❌ Problema: Botão fugitivo não funciona
**Causa**: Tipo de pergunta não configurado como `"botao_fujao"`  
**Solução**: Adicione perguntas com `"tipo": "botao_fujao"` no `PERGUNTAS`

### ❌ Problema: Ajuda 50/50 não desabilita corretamente
**Causa**: Verificação `if self.jogo.ajuda_50_disponivel` não foi chamada  
**Solução**: Certifique-se de que `_atualizar_botoes_ajuda()` é chamada após `usar_50()`

---

## 📝 Exemplo de Pergunta Customizada

Quer adicionar suas próprias perguntas? Siga este padrão:

```python
{
    "pergunta": "Qual é a maior lua de Júpiter?",
    "opcoes": ["Europa", "Ganimedes", "Io", "Calisto"],
    "correta": "Ganimedes",
    "tipo": "normal"  # Escolha: "normal", "botao_fujao" ou "texto_pergunta"
}
```

Ou de dificuldade expert:

```python
{
    "pergunta": "Insira isto na barra de endereço CHROME para ver dinossauro: chrome://",
    "opcoes": ["dino", "dinosaur", "game", "t-rex"],
    "correta": "dino",  # Se digitar chrome://dino aparece um jogo
    "tipo": "texto_pergunta"
}
```

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedor Python Full-Stack
- 📧 Contato: Abra uma issue no repositório

---

## 🙏 Créditos

- Inspirado no programa "Quem Quer Ser um Milionário?"
- Desenvolvido com ❤️ em Python
- Interface com **CustomTkinter** (Tom Schimansky)

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Você é livre para usar, modificar e distribuir este código.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🌟 Se gostou, considere dar uma ⭐!

```
   ⭐
  ⭐⭐⭐
 ⭐⭐⭐⭐⭐
   THANKS!
```

---

**Última atualização**: 2026-04-20  
**Versão**: 1.0 — Stable Release
```

---
