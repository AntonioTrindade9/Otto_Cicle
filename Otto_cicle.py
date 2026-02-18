class CicloDeQuatroTempos:
    def __init__(self):
        self.valvula_admissao = False
        self.valvula_escape = False
        self.vela_ignicao = False
        self.mistura = False
        self.gases = False

        self.pistao_posicao = {
            "Inicio admissão": 0,
            "Admissão": 180,
            "Compressão": 360,
            "Expansão": 540,
            "Exaustão": 720
        }

        self.posicao_atual = 0

    def aspiracao(self):
        self.posicao_atual = self.pistao_posicao["Admissão"]
        self.valvula_admissao = True
        self.mistura = True
        print("Mistura entra na câmara")

    def compressao(self):
        self.posicao_atual = self.pistao_posicao["Compressão"]
        self.valvula_admissao = False
        print("A mistura é comprimida pelo pistão")

    def combustao(self):
        self.vela_ignicao = True
        self.mistura = False
        self.gases = True
        self.posicao_atual = self.pistao_posicao["Expansão"]
        print("A mistura explode e o pistão desce")

    def exaustao(self):
        self.valvula_escape = True
        self.gases = False
        self.posicao_atual = self.pistao_posicao["Exaustão"]
        print("Os gases são expelidos")

    def ciclo_completo(self):
        print("\n--- Início do ciclo ---")

        self.aspiracao()
        self.compressao()
        self.combustao()
        self.exaustao()

        # reset para novo ciclo
        self.valvula_escape = False
        self.vela_ignicao = False
        self.posicao_atual = self.pistao_posicao["Inicio admissão"]

        print("--- Fim do ciclo ---\n")

motor = CicloDeQuatroTempos()
motor.ciclo_completo()
