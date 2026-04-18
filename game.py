import random
import tkinter as tk
import customtkinter as ctk

# ──────────────────────────────────────────────
#  BANCO DE PERGUNTAS (sem duplicatas)
# ──────────────────────────────────────────────

PERGUNTAS = [
    {
        "pergunta": "Quanto é 2 + 2?",
        "opcoes": ["3", "4", "5", "22"],
        "correta": "4",
        "tipo": "normal",
    },
    {
        "pergunta": "Qual a capital do Brasil?",
        "opcoes": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "correta": "Brasília",
        "tipo": "normal",
    },
    {
        "pergunta": "Qual a cor do cavalo BRANCO de Napoleão?",
        "opcoes": ["Preto", "Marrom", "Cinza", "Azul"],
        "correta": "Branco",
        "tipo": "texto_pergunta",
    },
    {
        "pergunta": "Clique no botão de MENOR valor:",
        "opcoes": ["R$ 100", "R$ 50", "R$ 10", "R$ 1"],
        "correta": "R$ 1",
        "tipo": "botao_fujao",
    },
    {
        "pergunta": "Em que ano o Brasil foi descoberto?",
        "opcoes": ["1488", "1500", "1532", "1600"],
        "correta": "1500",
        "tipo": "normal",
    },
    {
        "pergunta": "Quantos lados tem um hexágono?",
        "opcoes": ["5", "7", "6", "8"],
        "correta": "6",
        "tipo": "normal",
    },
    {
        "pergunta": "Qual o nome do inventor da lâmpada?",
        "opcoes": ["Nikola Tesla", "Graham Bell", "Thomas Edison", "Einstein"],
        "correta": "Thomas Edison",
        "tipo": "normal",
    },
    {
        "pergunta": "Se ontem fosse amanhã, hoje seria sexta-feira. Que dia é hoje?",
        "opcoes": ["Quarta", "Quinta", "Sexta", "Domingo"],
        "correta": "Domingo",
        "tipo": "normal",
    },
    {
        "pergunta": "Qual planeta é conhecido como o Planeta Vermelho?",
        "opcoes": ["Vênus", "Marte", "Júpiter", "Saturno"],
        "correta": "Marte",
        "tipo": "normal",
    },
    {
        "pergunta": "O rato roeu a roupa do rei de...",
        "opcoes": ["Roma", "Rússia", "Recife", "Rondônia"],
        "correta": "Roma",
        "tipo": "normal",
    },
    {
        "pergunta": "Clique no número que NÃO é primo:",
        "opcoes": ["2", "3", "5", "9"],
        "correta": "9",
        "tipo": "normal",
    },
    {
        "pergunta": "Tente clicar no botão premiado:",
        "opcoes": ["Vazio", "Nada", "Zero", "MILHÃO"],
        "correta": "MILHÃO",
        "tipo": "botao_fujao",
    },
    {
        "pergunta": "Quantos meses têm 28 dias?",
        "opcoes": ["1", "6", "12", "Depende do ano"],
        "correta": "12",
        "tipo": "normal",
    },
    {
        "pergunta": "Qual a maior montanha do mundo?",
        "opcoes": ["K2", "Everest", "Monte Branco", "Fuji"],
        "correta": "Everest",
        "tipo": "normal",
    },
    {
        "pergunta": "Para ganhar, clique no AZUL abaixo:",
        "opcoes": ["Amarelo", "Verde", "Vermelho", "Preto"],
        "correta": "Azul",
        "tipo": "texto_pergunta",
    },
    {
        "pergunta": "Quantos continentes existem no mundo?",
        "opcoes": ["5", "6", "7", "8"],
        "correta": "7",
        "tipo": "normal",
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "opcoes": ["Saturno", "Netuno", "Júpiter", "Urano"],
        "correta": "Júpiter",
        "tipo": "normal",
    },
    {
        "pergunta": "Quem escreveu Dom Casmurro?",
        "opcoes": ["José de Alencar", "Machado de Assis", "Graciliano Ramos", "Drummond"],
        "correta": "Machado de Assis",
        "tipo": "normal",
    },
    {
        "pergunta": "Qual o menor país do mundo?",
        "opcoes": ["Mônaco", "San Marino", "Vaticano", "Liechtenstein"],
        "correta": "Vaticano",
        "tipo": "normal",
    },
    {
        "pergunta": "Onde está a resposta CERTA nesta pergunta CERTA?",
        "opcoes": ["Na segunda opção", "No botão A", "No botão D", "Na pergunta"],
        "correta": "Na pergunta",
        "tipo": "texto_pergunta",
    },
]

PREMIOS = [
    "R$ 1.000",
    "R$ 5.000",
    "R$ 10.000",
    "R$ 50.000",
    "R$ 100.000",
    "R$ 500.000",
    "R$ 1.000.000",
]

# ── Cores ──────────────────────────────────────
COR_BG_ESCURO   = "#05051a"
COR_BG_PAINEL   = "#0b0b2e"
COR_BORDA       = "#1e3a8a"
COR_OURO        = "#fbbf24"
COR_OURO_ESCURO = "#92400e"
COR_AZUL        = "#3b82f6"
COR_AZUL_ESCURO = "#1d4ed8"
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
    """Gerencia o estado puro do jogo, sem lógica de UI."""

    MAX_PERGUNTAS = len(PREMIOS)  # 7 perguntas = 7 prêmios

    def __init__(self):
        pool = PERGUNTAS[:]
        random.shuffle(pool)
        self.perguntas = pool[:self.MAX_PERGUNTAS]
        self.nivel = 0
        self.respostas_certas = 0

        # Ajudas disponíveis
        self.ajuda_50_disponivel = True
        self.ajuda_pular_disponivel = True

    @property
    def pergunta_atual(self):
        if self.nivel < len(self.perguntas):
            return self.perguntas[self.nivel]
        return None

    @property
    def premio_atual(self):
        idx = min(self.nivel, len(PREMIOS) - 1)
        return PREMIOS[idx]

    @property
    def premio_conquistado(self):
        """Prêmio do nível anterior (já garantido)."""
        idx = max(0, self.nivel - 1)
        return PREMIOS[idx] if self.nivel > 0 else "R$ 0"

    @property
    def concluido(self):
        return self.nivel >= len(self.perguntas)

    def verificar(self, resposta: str) -> bool:
        return resposta.strip() == self.pergunta_atual["correta"].strip()

    def avancar(self):
        self.nivel += 1
        self.respostas_certas += 1

    def usar_50(self, opcoes_atuais: list) -> list:
        """Remove 2 opções erradas. Retorna lista com as 2 que devem ser mantidas."""
        correta = self.pergunta_atual["correta"]
        erradas = [o for o in opcoes_atuais if o != correta]
        random.shuffle(erradas)
        eliminar = erradas[:2]
        self.ajuda_50_disponivel = False
        return eliminar  # botões com esses textos devem ser desabilitados

    def usar_pular(self):
        """Pula a pergunta atual sem penalidade."""
        self.ajuda_pular_disponivel = False
        self.nivel += 1  # avança sem contar como acerto


class JogoGenioMilhao(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")

        self.title("Quem Quer Ser um Milionário? — Gênio Edition")
        self.geometry("980x660")
        self.minsize(820, 580)
        self.configure(fg_color=COR_BG_ESCURO)

        self.jogo = EstadoJogo()
        self._fugitivo_job = None
        self._opcoes_atuais: list = []
        self._respondendo = False  # trava para evitar duplo clique

        self._build_ui()
        self._mostrar_tela_inicial()

    # ──────────────────────────────────────────
    #  CONSTRUÇÃO DA INTERFACE
    # ──────────────────────────────────────────

    def _build_ui(self):

        # ── Sidebar ────────────────────────────
        self.sidebar = ctk.CTkFrame(self, width=190, fg_color=COR_BG_PAINEL,
                                    border_width=1, border_color=COR_BORDA)
        self.sidebar.pack(side="left", fill="y", padx=(10, 0), pady=10)
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(self.sidebar, text="PREMIAÇÃO",
                     font=("Georgia", 18, "bold"),
                     text_color=COR_OURO).pack(pady=(20, 10))

        self.labels_premios = []
        for p in reversed(PREMIOS):
            lbl = ctk.CTkLabel(self.sidebar, text=p,
                               font=("Courier", 13), text_color=COR_CINZA)
            lbl.pack(pady=3)
            self.labels_premios.append(lbl)

        # ── Área principal ──────────────────────
        self.main = ctk.CTkFrame(self, fg_color=COR_BG_PAINEL,
                                 border_width=1, border_color=COR_BORDA)
        self.main.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        # Nível / prêmio
        self.lbl_nivel = ctk.CTkLabel(self.main, text="",
                                      font=("Georgia", 13), text_color=COR_CINZA)
        self.lbl_nivel.pack(pady=(18, 0))

        # Pergunta
        self.lbl_pergunta = ctk.CTkLabel(
            self.main, text="",
            font=("Georgia", 21, "bold"),
            text_color=COR_BRANCO,
            wraplength=580,
            cursor="hand2",
        )
        self.lbl_pergunta.pack(pady=(10, 4), padx=20)

        # Feedback
        self.lbl_feedback = ctk.CTkLabel(self.main, text="",
                                         font=("Georgia", 15, "bold"),
                                         text_color=COR_VERDE)
        self.lbl_feedback.pack(pady=4)

        # Grade de botões 2 × 2
        self.frame_botoes = ctk.CTkFrame(self.main, fg_color="transparent")
        self.frame_botoes.pack(pady=10)

        self.botoes: list[ctk.CTkButton] = []
        for i in range(4):
            btn = ctk.CTkButton(
                self.frame_botoes,
                text="",
                width=268, height=58,
                fg_color=COR_BTN_NORMAL,
                hover_color=COR_BTN_HOVER,
                text_color=COR_BRANCO,
                font=("Courier", 14, "bold"),
                border_width=1, border_color=COR_BORDA,
                command=lambda idx=i: self._clicar_botao(idx),
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=8)
            btn.bind("<Return>", lambda e, idx=i: self._clicar_botao(idx))
            btn.bind("<space>",  lambda e, idx=i: self._clicar_botao(idx))
            self.botoes.append(btn)

        # ── Linha de ajudas ─────────────────────
        self.frame_ajudas = ctk.CTkFrame(self.main, fg_color="transparent")
        self.frame_ajudas.pack(pady=(0, 6))

        self.btn_50 = ctk.CTkButton(
            self.frame_ajudas,
            text="50/50",
            width=130, height=38,
            fg_color=COR_BTN_AJUDA,
            hover_color=COR_BTN_AJUDA_H,
            text_color=COR_VERDE,
            font=("Courier", 13, "bold"),
            border_width=1, border_color=COR_VERDE,
            command=self._usar_50,
        )
        self.btn_50.pack(side="left", padx=10)

        self.btn_pular = ctk.CTkButton(
            self.frame_ajudas,
            text="⏭  PULAR",
            width=130, height=38,
            fg_color=COR_BTN_AJUDA,
            hover_color=COR_BTN_AJUDA_H,
            text_color=COR_AZUL,
            font=("Courier", 13, "bold"),
            border_width=1, border_color=COR_AZUL,
            command=self._usar_pular,
        )
        self.btn_pular.pack(side="left", padx=10)

        # Botão de ação principal
        self.btn_acao = ctk.CTkButton(
            self.main, text="▶  JOGAR",
            width=220, height=48,
            fg_color=COR_OURO_ESCURO, hover_color="#78350f",
            text_color=COR_OURO,
            font=("Georgia", 16, "bold"),
            command=self._acao_principal,
        )
        self.btn_acao.pack(pady=14)

    # ──────────────────────────────────────────
    #  TELAS
    # ──────────────────────────────────────────

    def _mostrar_tela_inicial(self):
        self._parar_fugitivo()
        self._atualizar_sidebar(-1)
        self._respondendo = False

        self.lbl_nivel.configure(text="")
        self.lbl_pergunta.configure(
            text="🎯  Quem Quer Ser um Milionário?\nGênio Edition",
            text_color=COR_OURO, cursor="",
        )
        self.lbl_pergunta.unbind("<Button-1>")
        self.lbl_feedback.configure(text="")

        for i, btn in enumerate(self.botoes):
            btn.configure(text="", state="disabled",
                          fg_color=COR_BTN_NORMAL)
            btn.place_forget()
            btn.grid(row=i // 2, column=i % 2)

        self._set_ajudas_visiveis(False)
        self.btn_acao.configure(text="▶  JOGAR", state="normal")

    def _carregar_pergunta(self):
        self._parar_fugitivo()
        self._respondendo = False
        self._atualizar_sidebar(self.jogo.nivel)
        self.lbl_feedback.configure(text="")

        dados = self.jogo.pergunta_atual
        self.lbl_nivel.configure(
            text=f"Pergunta {self.jogo.nivel + 1} de {len(self.jogo.perguntas)}  —  Prêmio em jogo: {self.jogo.premio_atual}"
        )
        self.lbl_pergunta.configure(
            text=dados["pergunta"], text_color=COR_BRANCO, cursor="",
        )
        self.lbl_pergunta.unbind("<Button-1>")

        # Embaralha opções
        opcoes = dados["opcoes"][:]
        random.shuffle(opcoes)
        self._opcoes_atuais = opcoes

        letras = ["A", "B", "C", "D"]
        for i, btn in enumerate(self.botoes):
            btn.configure(
                text=f"{letras[i]})  {opcoes[i]}",
                state="normal",
                fg_color=COR_BTN_NORMAL,
                hover_color=COR_BTN_HOVER,
                text_color=COR_BRANCO,
            )
            btn.place_forget()
            btn.grid(row=i // 2, column=i % 2)
            btn.unbind("<Enter>")

        # Mecânicas especiais
        if dados["tipo"] == "texto_pergunta":
            self.lbl_pergunta.bind("<Button-1>", lambda e: self._responder_correto())
            self.lbl_pergunta.configure(cursor="hand2", text_color=COR_AZUL)
            for btn in self.botoes:
                btn.configure(state="disabled", fg_color=COR_BTN_DESATIV,
                              text_color=COR_CINZA)

        if dados["tipo"] == "botao_fujao":
            correta = dados["correta"]
            if correta in self._opcoes_atuais:
                idx_fugitivo = self._opcoes_atuais.index(correta)
                self._ativar_fugitivo(self.botoes[idx_fugitivo])

        # Atualiza estado dos botões de ajuda
        self._atualizar_botoes_ajuda()
        self._set_ajudas_visiveis(dados["tipo"] == "normal")
        self.btn_acao.configure(text="", state="disabled")

    def _tela_game_over(self):
        self._parar_fugitivo()
        self.lbl_nivel.configure(text="")
        self.lbl_pergunta.configure(
            text=f"💸  Você perdeu!\nChegou até a pergunta {self.jogo.nivel + 1}.",
            text_color=COR_VERMELHO,
        )
        self.lbl_feedback.configure(text="")
        for btn in self.botoes:
            btn.configure(state="disabled")
        self._set_ajudas_visiveis(False)
        self.btn_acao.configure(text="🔄  JOGAR NOVAMENTE", state="normal")

    def _tela_vitoria(self):
        self._parar_fugitivo()
        self.lbl_nivel.configure(text="")
        self.lbl_pergunta.configure(
            text="🏆  PARABÉNS!\nVocê é um Gênio Milionário!", text_color=COR_VERDE
        )
        self.lbl_feedback.configure(text="")
        for btn in self.botoes:
            btn.configure(state="disabled")
        self._set_ajudas_visiveis(False)
        self.btn_acao.configure(text="🔄  JOGAR NOVAMENTE", state="normal")

    # ──────────────────────────────────────────
    #  AJUDAS
    # ──────────────────────────────────────────

    def _set_ajudas_visiveis(self, visivel: bool):
        if visivel:
            self.frame_ajudas.pack(pady=(0, 6))
        else:
            self.frame_ajudas.pack_forget()

    def _atualizar_botoes_ajuda(self):
        if self.jogo.ajuda_50_disponivel:
            self.btn_50.configure(state="normal", fg_color=COR_BTN_AJUDA,
                                  text_color=COR_VERDE)
        else:
            self.btn_50.configure(state="disabled", fg_color=COR_BTN_DESATIV,
                                  text_color=COR_CINZA)

        if self.jogo.ajuda_pular_disponivel:
            self.btn_pular.configure(state="normal", fg_color=COR_BTN_AJUDA,
                                     text_color=COR_AZUL)
        else:
            self.btn_pular.configure(state="disabled", fg_color=COR_BTN_DESATIV,
                                     text_color=COR_CINZA)

    def _usar_50(self):
        if not self.jogo.ajuda_50_disponivel or self._respondendo:
            return
        eliminar = self.jogo.usar_50(self._opcoes_atuais)
        letras = ["A", "B", "C", "D"]
        for i, btn in enumerate(self.botoes):
            if self._opcoes_atuais[i] in eliminar:
                btn.configure(state="disabled", fg_color=COR_BTN_DESATIV,
                              text_color=COR_CINZA,
                              text=f"{letras[i]})  —")
        self.btn_50.configure(state="disabled", fg_color=COR_BTN_DESATIV,
                              text_color=COR_CINZA)

    def _usar_pular(self):
        if not self.jogo.ajuda_pular_disponivel or self._respondendo:
            return
        self._parar_fugitivo()
        self._respondendo = True
        self.lbl_feedback.configure(
            text="⏭  Pergunta pulada!", text_color=COR_AZUL
        )
        for btn in self.botoes:
            btn.configure(state="disabled")
        self._set_ajudas_visiveis(False)
        self.jogo.usar_pular()

        if self.jogo.concluido:
            self.after(1000, self._tela_vitoria)
        else:
            self.btn_acao.configure(text="➡  PRÓXIMA PERGUNTA", state="normal")

    # ──────────────────────────────────────────
    #  LÓGICA DE RESPOSTA
    # ──────────────────────────────────────────

    def _clicar_botao(self, idx: int):
        if self._respondendo or not self._opcoes_atuais:
            return
        resposta = self._opcoes_atuais[idx]
        self._processar_resposta(resposta, botao_idx=idx)

    def _responder_correto(self):
        if self._respondendo:
            return
        self._processar_resposta(self.jogo.pergunta_atual["correta"])

    def _processar_resposta(self, resposta: str, botao_idx: int = None):
        self._respondendo = True
        self._parar_fugitivo()

        for btn in self.botoes:
            btn.configure(state="disabled")
        self.lbl_pergunta.unbind("<Button-1>")
        self._set_ajudas_visiveis(False)

        acertou = self.jogo.verificar(resposta)

        if acertou:
            if botao_idx is not None:
                self.botoes[botao_idx].configure(fg_color=COR_BTN_CORRETO)
            self.lbl_feedback.configure(text="✅  Correto!", text_color=COR_VERDE)
            self.jogo.avancar()
            if self.jogo.concluido:
                self.after(1200, self._tela_vitoria)
            else:
                self.btn_acao.configure(text="➡  PRÓXIMA PERGUNTA", state="normal")
        else:
            if botao_idx is not None:
                self.botoes[botao_idx].configure(fg_color=COR_BTN_ERRADO)
            self.lbl_feedback.configure(
                text=f"❌  Errado!  A resposta era: {self.jogo.pergunta_atual['correta']}",
                text_color=COR_VERMELHO,
            )
            self.after(2200, self._tela_game_over)

    # ──────────────────────────────────────────
    #  BOTÃO FUGITIVO
    # ──────────────────────────────────────────

    def _ativar_fugitivo(self, btn: ctk.CTkButton):
        btn.bind("<Enter>", lambda e: self._fugir(btn))

    def _fugir(self, btn: ctk.CTkButton):
        self._parar_fugitivo()
        self.frame_botoes.update_idletasks()
        w = self.frame_botoes.winfo_width()
        h = self.frame_botoes.winfo_height()

        if w < 50 or h < 50:
            # Frame ainda não renderizado; tenta novamente em breve
            self._fugitivo_job = self.after(100, lambda: self._fugir(btn))
            return

        nx = random.randint(10, max(10, w - 290))
        ny = random.randint(10, max(10, h - 70))
        btn.place(x=nx, y=ny)

        self._fugitivo_job = self.after(
            60, lambda: btn.bind("<Enter>", lambda e: self._fugir(btn))
        )

    def _parar_fugitivo(self):
        if self._fugitivo_job:
            self.after_cancel(self._fugitivo_job)
            self._fugitivo_job = None
        for btn in self.botoes:
            btn.unbind("<Enter>")

    # ──────────────────────────────────────────
    #  SIDEBAR & AÇÃO PRINCIPAL
    # ──────────────────────────────────────────

    def _atualizar_sidebar(self, nivel_atual: int):
        total = len(PREMIOS)
        for i, lbl in enumerate(self.labels_premios):
            idx_premio = total - 1 - i
            if idx_premio == nivel_atual:
                lbl.configure(text_color=COR_OURO, font=("Courier", 14, "bold"))
            elif idx_premio < nivel_atual:
                lbl.configure(text_color=COR_VERDE, font=("Courier", 13))
            else:
                lbl.configure(text_color=COR_CINZA, font=("Courier", 13))

    def _acao_principal(self):
        texto = self.btn_acao.cget("text")
        if "JOGAR" in texto:
            self.jogo = EstadoJogo()
            self._opcoes_atuais = []
            self._respondendo = False
            self._carregar_pergunta()
        elif "PRÓXIMA" in texto:
            self._carregar_pergunta()


# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    app = JogoGenioMilhao()
    app.mainloop()