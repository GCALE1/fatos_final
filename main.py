import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class HistoricalFactsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fatos Históricos por Ano (1980-2024)")
        self.setGeometry(100, 100, 600, 300)

        # Dicionário com os fatos
        self.facts_database = {
            "1980": ["Ronald Reagan é eleito presidente dos EUA.", "Começo da Guerra Irã-Iraque."],
            "1981": ["Lançamento do primeiro voo do ônibus espacial Columbia.", "Anwar Sadat é assassinado."],
            "1982": ["Início da Guerra das Malvinas.", "Michael Jackson lança 'Thriller'."],
            "1983": ["Primeiro computador pessoal da Apple.", "Início da Guerra Civil Libanesa."],
            "1984": ["Mikhail Gorbachev se torna líder da União Soviética.", "Lançamento do Windows 1.0."],
            "1985": ["Live Aid arrecada milhões para a fome na África.", "Gorbachev introduz a política de Glasnost."],
            "1986": ["Chernobyl sofre o maior desastre nuclear da história.", "Fernando Collor é eleito presidente do Brasil."],
            "1987": ["Acordo de Paz de Montréal é assinado entre EUA e URSS.", "O Brasil adere ao Protocolo de Montreal."],
            "1988": ["Michael Jackson lança 'Bad'.", "Gorbachev é eleito para um segundo mandato na União Soviética."],
            "1989": ["Queda do Muro de Berlim."],
            "1990": ["Nelson Mandela é libertado."],
            "1991": ["Fim da União Soviética.", "Início da Guerra do Golfo Pérsico."],
            "1992": ["Bill Clinton é eleito presidente dos EUA.", "Acordo de Paz de Oslo."],
            "1993": ["Acordo de Paz de Oslo é assinado.", "Criação da União Europeia."],
            "1994": ["Nelson Mandela é eleito presidente da África do Sul.", "Acordo de Paz de Jerusalém."],
            "1995": ["Windows 95 é lançado.", "Java é criado por Sun Microsystems."],
            "1996": ["Primeiro clone de ovelha, Dolly, é criada.", "Primeiro DVD é lançado."],
            "1997": ["Morte de Lady Diana.", "Início da Crise Asiática."],
            "1998": ["Início da crise financeira russa.", "Google é fundado."],
            "1999": ["Fim do século XX.", "Euro é introduzido como moeda."],
            "2000": ["Y2K - o medo do bug do milênio.", "Giro da Terra desacelera levemente."],
            "2001": ["Atentados de 11 de setembro.", "Início da Guerra ao Terror."],
            "2002": ["Criação da União Europeia com moeda única.", "Início da Guerra no Afeganistão."],
            "2003": ["Invasão do Iraque.", "Saddam Hussein é capturado na Operação."],
            "2004": ["Tsunami no Sudeste Asiático.", "Morte de Yasser Arafat."],
            "2005": ["Furacão Katrina atinge a costa sul dos EUA.", "Acordo de Paris sobre mudança climática."],
            "2006": ["Criação do Facebook.", "Primeira vitória do Brasil na Copa do Mundo feminina."],
            "2007": ["Primeiro iPhone é lançado.", "Crise financeira global começa."],
            "2008": ["Crise financeira global.", "Obama é eleito presidente dos EUA."],
            "2009": ["Michael Jackson morre.", "Lançamento do Bitcoin."],
            "2010": ["Terremoto no Haiti.", "Inicio da Primavera Árabe."],
            "2011": ["Morte de Osama bin Laden.", "Início da Guerra na Síria."],
            "2012": ["Fim do calendário maia e previsão do fim do mundo.", "O Twitter alcança 1 bilhão de tweets por dia."],
            "2013": ["Escândalos de espionagem envolvendo Edward Snowden.", "Papa Francisco é eleito."],
            "2014": ["Crise na Ucrânia e anexação da Crimeia.", "Guerra no Oriente Médio."],
            "2015": ["Acordo de Paris sobre mudanças climáticas.", "Refugiados sírios migram para a Europa."],
            "2016": ["Brexit: Reino Unido vota para sair da União Europeia.", "Rio de Janeiro sediou os Jogos Olímpicos."],
            "2017": ["Donald Trump assume a presidência dos EUA.", "Assassinatos em massa em Las Vegas."],
            "2018": ["Início da crise política no Brasil.", "Jair Bolsonaro é eleito presidente do Brasil."],
            "2019": ["Incêndios na Amazônia.", "Aprovação da reforma da previdência no Brasil."],
            "2020": ["COVID-19 é considerado pandemia.", "Joe Biden é eleito presidente dos EUA."],
            "2021": ["Vacinação contra a COVID-19 começa mundialmente.", "Início da recuperação econômica pós-COVID."],
            "2022": ["Guerra na Ucrânia.", "Primeiro astronauta brasileiro a ir ao espaço."],
            "2023": ["Crise energética global.", "Novo governo de Luiz Inácio Lula da Silva no Brasil."],
            "2024": ["Expansão de tecnologias de inteligência artificial.", "Aumento das questões ambientais e climáticas."]
        }

        # Criação do layout
        layout = QVBoxLayout()

        # Campo para por o ano
        self.year_input = QLineEdit(self)
        self.year_input.setPlaceholderText("Digite um ano entre o ano de 1980 e o ano de 2024")
        layout.addWidget(self.year_input)

        # Criação do butão de busca
        self.search_button = QPushButton("Buscar Fatos", self)
        self.search_button.clicked.connect(self.show_facts)
        layout.addWidget(self.search_button)

        # Local onde são exibidos os fatos historicos
        self.facts_label = QLabel("Fatos históricos aparecerão aqui.", self)
        layout.addWidget(self.facts_label)

        # Define o layout da janela
        self.setLayout(layout)

    def show_facts(self):
        # Obtém o ano inserido pelo usuário
        year = self.year_input.text()

        # Verifica se o ano está no dicionario
        if year in self.facts_database:
            facts = self.facts_database[year]
            # Alteração no formato para exibir os fatos diretamente
            facts_text = "\n".join(fact for fact in facts)
        else:
            facts_text = "Ano não encontrado ou inválido. Tente entre o ano de 1980 e o ano de 2024."

        # Atualiza a label com os fatos históricos encontrados
        self.facts_label.setText(facts_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HistoricalFactsApp()
    window.show()
    sys.exit(app.exec_())

