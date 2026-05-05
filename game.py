import random
import tkinter as tk
import customtkinter as ctk
from perguntas import BANCO_TEMAS

PREMIOS = (
    "R$ 1.000", "R$ 5.000", "R$ 10.000", "R$ 25.000",
    "R$ 50.000", "R$ 100.000", "R$ 250.000",
    "R$ 500.000", "R$ 800.000", "R$ 1.000.000"
)

# ── Ícones por tema ────────────────────────────
ICONES_TEMAS = {
    "Alimentação": "🍽️",
    "Geografia":   "🌎",
    "Tecnologia":  "💻",
    "Ciência":     "🔬",
    "Esportes":    "⚽",
    "Gênio Quiz":  "🧠",
    "Matemática":  "📐",
    "Física":      "⚛️",
    "Misto":       "🎲",
}

# ── Cores ──────────────────────────────────────
COR_BG_ESCURO   = "#05051a"
COR_BG_PAINEL   = "#0b0b2e"
COR_BORDA       = "#1e3a8a"
COR_OURO        = "#fbbf24"
COR_OURO_ESCURO = "#92400e"
COR_BRANCO      = "#f1f5f9"
COR_CINZA       = "#64748b"
COR_BTN_NORMAL  = "#1e1e4a"
COR_BTN_HOVER   = "#2d2d7a"
COR_VERDE       = "#22c55e"
COR_VERMELHO    = "#ef4444"

# ── Cores especiais por tema ───────────────────
CORES_TEMAS = {
    "Alimentação": ("#7c2d12", "#ea580c"),
    "Geografia":   ("#064e3b", "#10b981"),
    "Tecnologia":  ("#1e3a5f", "#38bdf8"),
    "Ciência":     ("#4c1d95", "#a78bfa"),
    "Esportes":    ("#14532d", "#4ade80"),
    "Gênio Quiz":  ("#713f12", "#fbbf24"),
    "Matemática":  ("#1e1b4b", "#818cf8"),
    "Física":      ("#1c1917", "#f97316"),
    "Misto":       ("#3b0764", "#e879f9"),
}


class EstadoJogo:
    def __init__(self, tema_escolhido):
        self.tema = tema_escolhido
        if tema_escolhido == "Misto":
            pool = []
            for lista in BANCO_TEMAS.values():
                pool.extend(lista)
        else:
            pool = BANCO_TEMAS[tema_escolhido][:]

        random.shuffle(pool)
        self.perguntas = pool[:len(PREMIOS)]
        self.nivel = 0
        self.ajuda_50 = True
        self.ajuda_pular = True

    @property
    def pergunta_atual(self):
        return self.perguntas[self.nivel] if self.nivel < len(self.perguntas) else None

    def verificar(self, resposta: str) -> bool:
        return resposta.strip() == self.pergunta_atual["correta"].strip()


class JogoGenioMilhao(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("Gênio do Milhão — Professional Edition")
        self.geometry("1100x760")
        self.minsize(900, 680)
        self.configure(fg_color=COR_BG_ESCURO)

        self.jogo = None
        self._respondendo = False

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(expand=True, fill="both")

        self._mostrar_menu_principal()

    def _limpar_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # ── TELA: MENU PRINCIPAL ──────────────────────
    def _mostrar_menu_principal(self):
        self._limpar_container()

        # ── Cabeçalho ──
        header = ctk.CTkFrame(self.container, fg_color="transparent")
        header.pack(pady=(32, 10))

        ctk.CTkLabel(
            header, text="✦  QUEM QUER SER UM  ✦",
            font=("Georgia", 20, "italic"), text_color=COR_CINZA
        ).pack()

        ctk.CTkLabel(
            header, text="MILIONÁRIO",
            font=("Georgia", 72, "bold"), text_color=COR_OURO
        ).pack()

        ctk.CTkLabel(
            header, text="GÊNIO  EDITION",
            font=("Courier", 20, "bold"), text_color="#4f6fa8",
            padx=30, pady=6
        ).pack()

        # Linha separadora decorativa
        sep = ctk.CTkFrame(self.container, height=2, fg_color=COR_BORDA)
        sep.pack(fill="x", padx=80, pady=(8, 20))

        # Subtítulo
        ctk.CTkLabel(
            self.container, text="Escolha uma categoria para começar",
            font=("Georgia", 15, "italic"), text_color=COR_CINZA
        ).pack(pady=(0, 18))

        # ── Grid de temas ──
        grid_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        grid_frame.pack(expand=True)

        temas = list(BANCO_TEMAS.keys()) + ["Misto"]
        colunas = 3

        for i, tema in enumerate(temas):
            cor_fundo, cor_destaque = CORES_TEMAS.get(tema, (COR_BTN_NORMAL, COR_OURO))
            icone = ICONES_TEMAS.get(tema, "❓")

            # Célula do tema
            cell = ctk.CTkFrame(
                grid_frame,
                width=240, height=120,
                fg_color=cor_fundo,
                border_width=2,
                border_color=cor_destaque,
                corner_radius=14,
            )
            cell.grid(row=i // colunas, column=i % colunas, padx=12, pady=12)
            cell.pack_propagate(False)

            # Ícone grande
            ctk.CTkLabel(
                cell, text=icone,
                font=("Arial", 30),
                text_color=cor_destaque
            ).pack(pady=(14, 0))

            # Nome do tema
            ctk.CTkLabel(
                cell, text=tema.upper(),
                font=("Georgia", 13, "bold"),
                text_color=COR_BRANCO
            ).pack()

            # Botão invisível que cobre a célula
            btn = ctk.CTkButton(
                cell, text="JOGAR",
                width=140, height=30,
                font=("Courier", 11, "bold"),
                fg_color="transparent",
                border_width=1,
                border_color=cor_destaque,
                hover_color=cor_destaque,
                text_color=cor_destaque,
                corner_radius=20,
                command=lambda t=tema: self._iniciar_jogo(t)
            )
            btn.pack(pady=(4, 0))

        # ── Rodapé ──
        ctk.CTkLabel(
            self.container,
            text="Use os botões 50/50 e PULAR com sabedoria!",
            font=("Courier", 11), text_color=COR_CINZA
        ).pack(pady=(18, 8))

    # ── TELA: JOGO ────────────────────────────────
    def _iniciar_jogo(self, tema):
        self.jogo = EstadoJogo(tema)
        self._limpar_container()
        self._build_game_ui()
        self._carregar_pergunta()

    def _build_game_ui(self):
        cor_fundo, cor_destaque = CORES_TEMAS.get(self.jogo.tema, (COR_BTN_NORMAL, COR_OURO))

        # Sidebar de Prêmios
        self.sidebar = ctk.CTkFrame(
            self.container, width=200,
            fg_color=COR_BG_PAINEL,
            border_width=1, border_color=COR_BORDA
        )
        self.sidebar.pack(side="left", fill="y", padx=15, pady=15)
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(
            self.sidebar, text="🏆 PRÊMIOS",
            font=("Georgia", 17, "bold"), text_color=COR_OURO
        ).pack(pady=20)

        self.labels_premios = []
        for p in reversed(PREMIOS):
            lbl = ctk.CTkLabel(self.sidebar, text=p, font=("Courier", 13), text_color=COR_CINZA)
            lbl.pack(pady=2)
            self.labels_premios.append(lbl)

        # Área Central
        self.main_game = ctk.CTkFrame(self.container, fg_color="transparent")
        self.main_game.pack(side="right", expand=True, fill="both", padx=15, pady=15)

        self.lbl_info = ctk.CTkLabel(
            self.main_game, text="",
            font=("Georgia", 13), text_color=cor_destaque
        )
        self.lbl_info.pack(pady=5)

        # Caixa da pergunta
        self.frame_pergunta = ctk.CTkFrame(
            self.main_game,
            fg_color=cor_fundo, border_width=2,
            border_color=cor_destaque, corner_radius=16
        )
        self.frame_pergunta.pack(fill="x", padx=20, pady=10)

        self.lbl_pergunta = ctk.CTkLabel(
            self.frame_pergunta, text="",
            font=("Georgia", 24, "bold"),
            text_color=COR_BRANCO, wraplength=620
        )
        self.lbl_pergunta.pack(pady=28, padx=20)

        # Botões de Resposta
        self.frame_respostas = ctk.CTkFrame(self.main_game, fg_color="transparent")
        self.frame_respostas.pack(pady=12)

        labels_letras = ["A", "B", "C", "D"]
        self.botoes = []
        for i in range(4):
            frame_btn = ctk.CTkFrame(self.frame_respostas, fg_color="transparent")
            frame_btn.grid(row=i // 2, column=i % 2, padx=10, pady=8)

            letra_lbl = ctk.CTkLabel(
                frame_btn, text=labels_letras[i],
                font=("Georgia", 16, "bold"),
                text_color=cor_destaque, width=24
            )
            letra_lbl.pack(side="left", padx=(0, 4))

            btn = ctk.CTkButton(
                frame_btn, text="", width=300, height=70,
                font=("Courier", 15, "bold"),
                fg_color=COR_BTN_NORMAL,
                border_width=1, border_color=COR_BORDA,
                hover_color=COR_BTN_HOVER,
                corner_radius=10,
                command=lambda idx=i: self._clicar_opcao(idx)
            )
            btn.pack(side="left")
            self.botoes.append(btn)

        # Rodapé com Ajudas e Voltar
        self.footer = ctk.CTkFrame(self.main_game, fg_color="transparent")
        self.footer.pack(side="bottom", fill="x", pady=16)

        self.btn_50 = ctk.CTkButton(
            self.footer, text="⚡ 50/50", width=120, height=44,
            font=("Courier", 13, "bold"),
            fg_color="#1a3a2a", border_width=1, border_color=COR_VERDE,
            hover_color="#2d6a4f", corner_radius=10,
            command=self._usar_50
        )
        self.btn_50.pack(side="left", padx=10)

        self.btn_pular = ctk.CTkButton(
            self.footer, text="⏭ PULAR", width=120, height=44,
            font=("Courier", 13, "bold"),
            fg_color="#1a2a3a", border_width=1, border_color="#38bdf8",
            hover_color="#1e3a5f", corner_radius=10,
            command=self._usar_pular
        )
        self.btn_pular.pack(side="left", padx=10)

        ctk.CTkButton(
            self.footer, text="✖ SAIR", width=110, height=44,
            font=("Courier", 12, "bold"),
            fg_color="#2a1515", border_width=1, border_color=COR_VERMELHO,
            hover_color="#4a1515", corner_radius=10,
            command=self._mostrar_menu_principal
        ).pack(side="right", padx=10)

    def _carregar_pergunta(self):
        self._respondendo = False
        p = self.jogo.pergunta_atual
        if not p:
            self._tela_vitoria()
            return

        self._atualizar_sidebar()
        cor_fundo, cor_destaque = CORES_TEMAS.get(self.jogo.tema, (COR_BTN_NORMAL, COR_OURO))

        self.lbl_info.configure(
            text=f"{ICONES_TEMAS.get(self.jogo.tema, '')}  {self.jogo.tema.upper()}  |  PERGUNTA {self.jogo.nivel + 1} / {len(PREMIOS)}"
        )
        self.lbl_pergunta.configure(text=p["pergunta"], text_color=COR_BRANCO)

        opcoes = p["opcoes"][:]
        random.shuffle(opcoes)
        self.opcoes_atuais = opcoes

        for i, btn in enumerate(self.botoes):
            btn.configure(text=opcoes[i], state="normal", fg_color=COR_BTN_NORMAL)
            btn.unbind("<Enter>")
            try:
                btn.place_forget()
            except Exception:
                pass
            btn.master.grid(row=i // 2, column=i % 2)

        if p["tipo"] == "botao_fujao":
            idx_c = opcoes.index(p["correta"])
            self.botoes[idx_c].bind("<Enter>", lambda e: self._fugir(self.botoes[idx_c]))

        self.btn_50.configure(state="normal" if self.jogo.ajuda_50 else "disabled")
        self.btn_pular.configure(state="normal" if self.jogo.ajuda_pular else "disabled")

    def _clicar_opcao(self, idx):
        if self._respondendo:
            return
        self._respondendo = True

        correta = self.jogo.pergunta_atual["correta"]
        if self.opcoes_atuais[idx] == correta:
            self.botoes[idx].configure(fg_color=COR_VERDE)
            self.jogo.nivel += 1
            self.after(1000, self._carregar_pergunta)
        else:
            self.botoes[idx].configure(fg_color=COR_VERMELHO)
            # Mostra a correta
            for j, btn in enumerate(self.botoes):
                if self.opcoes_atuais[j] == correta:
                    btn.configure(fg_color=COR_VERDE)
            self.after(1800, self._mostrar_menu_principal)

    def _fugir(self, btn):
        btn.place(x=random.randint(50, 400), y=random.randint(50, 300))

    def _usar_50(self):
        self.jogo.ajuda_50 = False
        correta = self.jogo.pergunta_atual["correta"]
        erradas = [o for o in self.opcoes_atuais if o != correta]
        eliminar = random.sample(erradas, 2)
        for i, btn in enumerate(self.botoes):
            if self.opcoes_atuais[i] in eliminar:
                btn.configure(state="disabled", text="---", fg_color="#111")
        self.btn_50.configure(state="disabled")

    def _usar_pular(self):
        self.jogo.ajuda_pular = False
        self.jogo.nivel += 1
        self._carregar_pergunta()

    def _atualizar_sidebar(self):
        for i, lbl in enumerate(self.labels_premios):
            idx = len(PREMIOS) - 1 - i
            if idx == self.jogo.nivel:
                lbl.configure(text_color=COR_OURO, font=("Courier", 14, "bold"))
            elif idx < self.jogo.nivel:
                lbl.configure(text_color=COR_VERDE, font=("Courier", 13))
            else:
                lbl.configure(text_color=COR_CINZA, font=("Courier", 13))

    def _tela_vitoria(self):
        self._limpar_container()

        ctk.CTkLabel(self.container, text="🏆", font=("Arial", 120)).pack(pady=(60, 10))
        ctk.CTkLabel(
            self.container, text="PARABÉNS, MILIONÁRIO!",
            font=("Georgia", 52, "bold"), text_color=COR_OURO
        ).pack()
        ctk.CTkLabel(
            self.container, text="Você conquistou R$ 1.000.000!",
            font=("Georgia", 20), text_color=COR_BRANCO
        ).pack(pady=10)

        ctk.CTkButton(
            self.container, text="🏠  VOLTAR AO MENU",
            width=280, height=64,
            font=("Georgia", 18, "bold"),
            fg_color=COR_OURO_ESCURO, hover_color=COR_OURO,
            text_color=COR_BG_ESCURO, corner_radius=14,
            command=self._mostrar_menu_principal
        ).pack(pady=50)


if __name__ == "__main__":
    app = JogoGenioMilhao()
    app.mainloop()
