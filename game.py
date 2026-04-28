import random
import tkinter as tk
import customtkinter as ctk

# ──────────────────────────────────────────────
#  BANCO DE PERGUNTAS (Originais + Novas)
# ──────────────────────────────────────────────

PERGUNTAS = [
    # --- Perguntas de Capitais (Novas) ---
    {'pergunta': 'Qual é a capital da França?', 'opcoes': ['Paris', 'Lyon', 'Marselha', 'Toulouse'], 'correta': 'Paris', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital da Espanha?', 'opcoes': ['Madrid', 'Barcelona', 'Valência', 'Sevilha'], 'correta': 'Madrid', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital da Itália?', 'opcoes': ['Roma', 'Milão', 'Nápoles', 'Florença'], 'correta': 'Roma', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital da Alemanha?', 'opcoes': ['Berlim', 'Hamburgo', 'Munique', 'Frankfurt'], 'correta': 'Berlim', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital do Reino Unido?', 'opcoes': ['Londres', 'Manchester', 'Birmingham', 'Glasgow'], 'correta': 'Londres', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital do Brasil?', 'opcoes': ['Brasília', 'Rio de Janeiro', 'São Paulo', 'Salvador'], 'correta': 'Brasília', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital do Japão?', 'opcoes': ['Tóquio', 'Osaka', 'Kyoto', 'Hiroshima'], 'correta': 'Tóquio', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital da Austrália?', 'opcoes': ['Canberra', 'Sydney', 'Melbourne', 'Brisbane'], 'correta': 'Canberra', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital do Canadá?', 'opcoes': ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'], 'correta': 'Ottawa', 'tipo': 'normal'},
    {'pergunta': 'Qual é a capital da Rússia?', 'opcoes': ['Moscou', 'São Petersburgo', 'Novosibirsk', 'Yekaterinburg'], 'correta': 'Moscou', 'tipo': 'normal'},
    
    # --- Perguntas Originais (Lógica e Pegadinhas) ---
    {"pergunta": "Quanto é 2 + 2?", "opcoes": ["3", "4", "5", "22"], "correta": "4", "tipo": "normal"},
    {"pergunta": "Qual a cor do cavalo BRANCO de Napoleão?", "opcoes": ["Preto", "Marrom", "Cinza", "Azul"], "correta": "Branco", "tipo": "texto_pergunta"},
    {"pergunta": "Clique no botão de MENOR valor:", "opcoes": ["R$ 100", "R$ 50", "R$ 10", "R$ 1"], "correta": "R$ 1", "tipo": "botao_fujao"},
    {"pergunta": "Em que ano o Brasil foi descoberto?", "opcoes": ["1488", "1500", "1532", "1600"], "correta": "1500", "tipo": "normal"},
    {"pergunta": "Quantos lados tem um hexágono?", "opcoes": ["5", "7", "6", "8"], "correta": "6", "tipo": "normal"},
    {"pergunta": "Qual o nome do inventor da lâmpada?", "opcoes": ["Nikola Tesla", "Graham Bell", "Thomas Edison", "Einstein"], "correta": "Thomas Edison", "tipo": "normal"},
    {"pergunta": "Se ontem fosse amanhã, hoje seria sexta-feira. Que dia é hoje?", "opcoes": ["Quarta", "Quinta", "Sexta", "Domingo"], "correta": "Domingo", "tipo": "normal"},
    {"pergunta": "Qual planeta é conhecido como o Planeta Vermelho?", "opcoes": ["Vênus", "Marte", "Júpiter", "Saturno"], "correta": "Marte", "tipo": "normal"},
    {"pergunta": "O rato roeu a roupa do rei de...", "opcoes": ["Roma", "Rússia", "Recife", "Rondônia"], "correta": "Roma", "tipo": "normal"},
    {"pergunta": "Clique no número que NÃO é primo:", "opcoes": ["2", "3", "5", "9"], "correta": "9", "tipo": "normal"},
    {"pergunta": "Tente clicar no botão premiado:", "opcoes": ["Vazio", "Nada", "Zero", "MILHÃO"], "correta": "MILHÃO", "tipo": "botao_fujao"},
    {"pergunta": "Quantos meses têm 28 dias?", "opcoes": ["1", "6", "12", "Depende do ano"], "correta": "12", "tipo": "normal"},
    {"pergunta": "Qual a maior montanha do mundo?", "opcoes": ["K2", "Everest", "Monte Branco", "Fuji"], "correta": "Everest", "tipo": "normal"},
    {"pergunta": "Para ganhar, clique no AZUL abaixo:", "opcoes": ["Amarelo", "Verde", "Vermelho", "Preto"], "correta": "Azul", "tipo": "texto_pergunta"},
    {"pergunta": "Quantos continentes existem no mundo?", "opcoes": ["5", "6", "7", "8"], "correta": "7", "tipo": "normal"},
    {"pergunta": "Qual é o maior planeta do sistema solar?", "opcoes": ["Saturno", "Netuno", "Júpiter", "Urano"], "correta": "Júpiter", "tipo": "normal"},
    {"pergunta": "Quem escreveu Dom Casmurro?", "opcoes": ["José de Alencar", "Machado de Assis", "Graciliano Ramos", "Drummond"], "correta": "Machado de Assis", "tipo": "normal"},
    {"pergunta": "Qual o menor país do mundo?", "opcoes": ["Mônaco", "San Marino", "Vaticano", "Liechtenstein"], "correta": "Vaticano", "tipo": "normal"},
    {"pergunta": "Onde está a resposta CERTA nesta pergunta CERTA?", "opcoes": ["Na segunda opção", "No botão A", "No botão D", "Na pergunta"], "correta": "Na pergunta", "tipo": "texto_pergunta"},
]

# Agora com 10 níveis de prêmio
PREMIOS = [
    "R$ 1.000", "R$ 5.000", "R$ 10.000", "R$ 25.000", "R$ 50.000",
    "R$ 100.000", "R$ 250.000", "R$ 500.000", "R$ 800.000", "R$ 1.000.000",
]

# ── Cores ──────────────────────────────────────
COR_BG_ESCURO   = "#05051a"
COR_BG_PAINEL   = "#0b0b2e"
COR_BORDA       = "#1e3a8a"
COR_OURO        = "#fbbf24"
COR_OURO_ESCURO = "#92400e"
COR_AZUL        = "#3b82f6"
COR_VERDE       = "#22c55e"
COR_VERMELHO    = "#ef4444"
COR_BRANCO      = "#f1f5f9"
COR_CINZA       = "#64748b"
COR_BTN_NORMAL  = "#1e1e4a"
COR_BTN_HOVER   = "#2d2d7a"
COR_BTN_CORRETO = "#14532d"
COR_BTN_ERRADO  = "#7f1d1d"
COR_BTN_AJUDA   = "#1a3a2a"
COR_BTN_AJUDA_H = "#2a5a3a"
COR_BTN_DESATIV = "#111128"

class EstadoJogo:
    def __init__(self):
        pool = PERGUNTAS[:]
        random.shuffle(pool)
        self.perguntas = pool[:len(PREMIOS)] # Sorteia 10 do total
        self.nivel = 0
        self.ajuda_50_disponivel = True
        self.ajuda_pular_disponivel = True

    @property
    def pergunta_atual(self):
        return self.perguntas[self.nivel] if self.nivel < len(self.perguntas) else None

    @property
    def premio_atual(self):
        return PREMIOS[min(self.nivel, len(PREMIOS)-1)]

    def verificar(self, resposta: str) -> bool:
        return resposta.strip() == self.pergunta_atual["correta"].strip()

class JogoGenioMilhao(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("Quem Quer Ser um Milionário? — Gênio Edition")
        self.geometry("980x660")
        self.configure(fg_color=COR_BG_ESCURO)

        self.jogo = EstadoJogo()
        self._fugitivo_job = None
        self._opcoes_atuais = []
        self._respondendo = False

        self._build_ui()
        self._mostrar_tela_inicial()

    def _build_ui(self):
        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=190, fg_color=COR_BG_PAINEL, border_width=1, border_color=COR_BORDA)
        self.sidebar.pack(side="left", fill="y", padx=(10, 0), pady=10)
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(self.sidebar, text="PREMIAÇÃO", font=("Georgia", 18, "bold"), text_color=COR_OURO).pack(pady=(20, 10))
        self.labels_premios = []
        for p in reversed(PREMIOS):
            lbl = ctk.CTkLabel(self.sidebar, text=p, font=("Courier", 13), text_color=COR_CINZA)
            lbl.pack(pady=2)
            self.labels_premios.append(lbl)

        # Main
        self.main = ctk.CTkFrame(self, fg_color=COR_BG_PAINEL, border_width=1, border_color=COR_BORDA)
        self.main.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        self.lbl_nivel = ctk.CTkLabel(self.main, text="", font=("Georgia", 13), text_color=COR_CINZA)
        self.lbl_nivel.pack(pady=(18, 0))

        self.lbl_pergunta = ctk.CTkLabel(self.main, text="", font=("Georgia", 21, "bold"), text_color=COR_BRANCO, wraplength=580)
        self.lbl_pergunta.pack(pady=(10, 4), padx=20)

        self.lbl_feedback = ctk.CTkLabel(self.main, text="", font=("Georgia", 15, "bold"))
        self.lbl_feedback.pack(pady=4)

        self.frame_botoes = ctk.CTkFrame(self.main, fg_color="transparent")
        self.frame_botoes.pack(pady=10)

        self.botoes = []
        for i in range(4):
            btn = ctk.CTkButton(self.frame_botoes, text="", width=270, height=60, fg_color=COR_BTN_NORMAL, font=("Courier", 14, "bold"),
                                command=lambda idx=i: self._clicar_botao(idx))
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=8)
            self.botoes.append(btn)

        self.frame_ajudas = ctk.CTkFrame(self.main, fg_color="transparent")
        self.frame_ajudas.pack()

        self.btn_50 = ctk.CTkButton(self.frame_ajudas, text="50/50", width=120, command=self._usar_50, fg_color=COR_BTN_AJUDA)
        self.btn_50.pack(side="left", padx=5)
        self.btn_pular = ctk.CTkButton(self.frame_ajudas, text="PULAR", width=120, command=self._usar_pular, fg_color=COR_BTN_AJUDA)
        self.btn_pular.pack(side="left", padx=5)

        self.btn_acao = ctk.CTkButton(self.main, text="▶ JOGAR", width=220, height=48, fg_color=COR_OURO_ESCURO, text_color=COR_OURO, command=self._acao_principal)
        self.btn_acao.pack(pady=15)

    def _mostrar_tela_inicial(self):
        self._parar_fugitivo()
        self.lbl_pergunta.configure(text="🎯 Gênio do Milhão\nAs perguntas foram atualizadas!", text_color=COR_OURO)
        for btn in self.botoes: btn.configure(text="", state="disabled")
        self.frame_ajudas.pack_forget()
        self.btn_acao.configure(text="▶ JOGAR", state="normal")

    def _carregar_pergunta(self):
        self._parar_fugitivo()
        self._respondendo = False
        self._atualizar_sidebar(self.jogo.nivel)
        self.lbl_feedback.configure(text="")
        dados = self.jogo.pergunta_atual
        
        self.lbl_nivel.configure(text=f"Pergunta {self.jogo.nivel + 1} de 10 — Vale {self.jogo.premio_atual}")
        self.lbl_pergunta.configure(text=dados["pergunta"], text_color=COR_BRANCO, cursor="")
        self.lbl_pergunta.unbind("<Button-1>")

        opcoes = dados["opcoes"][:]
        random.shuffle(opcoes)
        self._opcoes_atuais = opcoes

        letras = ["A", "B", "C", "D"]
        for i, btn in enumerate(self.botoes):
            btn.configure(text=f"{letras[i]}) {opcoes[i]}", state="normal", fg_color=COR_BTN_NORMAL, text_color=COR_BRANCO)
            btn.place_forget()
            btn.grid(row=i // 2, column=i % 2)

        # Lógica especial
        if dados["tipo"] == "texto_pergunta":
            self.lbl_pergunta.bind("<Button-1>", lambda e: self._processar_resposta(dados["correta"]))
            self.lbl_pergunta.configure(cursor="hand2", text_color=COR_AZUL)
        elif dados["tipo"] == "botao_fujao":
            correta = dados["correta"]
            if correta in self._opcoes_atuais:
                self._ativar_fugitivo(self.botoes[self._opcoes_atuais.index(correta)])

        self.btn_50.configure(state="normal" if self.jogo.ajuda_50_disponivel else "disabled")
        self.btn_pular.configure(state="normal" if self.jogo.ajuda_pular_disponivel else "disabled")
        self.frame_ajudas.pack(pady=5) if dados["tipo"] == "normal" else self.frame_ajudas.pack_forget()
        self.btn_acao.configure(text="", state="disabled")

    def _clicar_botao(self, idx):
        if self._respondendo: return
        self._processar_resposta(self._opcoes_atuais[idx], idx)

    def _processar_resposta(self, resposta, idx=None):
        self._respondendo = True
        self._parar_fugitivo()
        acertou = self.jogo.verificar(resposta)
        
        for btn in self.botoes: btn.configure(state="disabled")

        if acertou:
            if idx is not None: self.botoes[idx].configure(fg_color=COR_BTN_CORRETO)
            self.lbl_feedback.configure(text="✅ Correto!", text_color=COR_VERDE)
            self.jogo.nivel += 1
            if self.jogo.nivel >= 10:
                self.after(1000, self._tela_vitoria)
            else:
                self.btn_acao.configure(text="➡ PRÓXIMA", state="normal")
        else:
            if idx is not None: self.botoes[idx].configure(fg_color=COR_BTN_ERRADO)
            self.lbl_feedback.configure(text=f"❌ Errou! Era: {self.jogo.pergunta_atual['correta']}", text_color=COR_VERMELHO)
            self.after(2000, self._mostrar_tela_inicial)

    def _ativar_fugitivo(self, btn):
        btn.bind("<Enter>", lambda e: self._fugir(btn))

    def _fugir(self, btn):
        nx, ny = random.randint(10, 600), random.randint(10, 200)
        btn.place(x=nx, y=ny)

    def _parar_fugitivo(self):
        if self._fugitivo_job: self.after_cancel(self._fugitivo_job)
        for btn in self.botoes: btn.unbind("<Enter>")

    def _usar_50(self):
        correta = self.jogo.pergunta_atual["correta"]
        erradas = [o for o in self._opcoes_atuais if o != correta]
        eliminar = random.sample(erradas, 2)
        for i, btn in enumerate(self.botoes):
            if self._opcoes_atuais[i] in eliminar:
                btn.configure(state="disabled", text="---")
        self.jogo.ajuda_50_disponivel = False
        self.btn_50.configure(state="disabled")

    def _usar_pular(self):
        self.jogo.ajuda_pular_disponivel = False
        self.jogo.nivel += 1
        self._carregar_pergunta()

    def _atualizar_sidebar(self, nivel):
        for i, lbl in enumerate(self.labels_premios):
            idx = len(PREMIOS) - 1 - i
            lbl.configure(text_color=COR_OURO if idx == nivel else (COR_VERDE if idx < nivel else COR_CINZA))

    def _tela_vitoria(self):
        self.lbl_pergunta.configure(text="🏆 PARABÉNS!\nVocê é um Milionário!", text_color=COR_VERDE)
        self.btn_acao.configure(text="▶ JOGAR NOVAMENTE", state="normal")

    def _acao_principal(self):
        if "JOGAR" in self.btn_acao.cget("text"): self.jogo = EstadoJogo()
        self._carregar_pergunta()

if __name__ == "__main__":
    app = JogoGenioMilhao()
    app.mainloop()
