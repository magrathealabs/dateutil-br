from dateutil.parser import parserinfo, parser

class BrParserInfo(parserinfo):
    JUMP = [" ", ".", ",", ";", "-", "/", "'",
            "as", "a", "e", "de", "do", "em"]

    WEEKDAYS = [("Seg", "Segunda"),
                ("Ter", "Terça"),
                ("Qua", "Quarta"),
                ("Qui", "Quinta"),
                ("Sex", "cta"),
                ("Sab", "Sabado"),
                ("Dom", "Domingo")]

    MONTHS = [("Jan", "Janeiro"),
              ("Feb", "Fevereiro"),
              ("Mar", "Março"),
              ("Apr", "Abril"),
              ("May", "Maio"),
              ("Jun", "Junho"),
              ("Jul", "Julho"),
              ("Aug", "Agosto"),
              ("Sep", "Setembro"),
              ("Oct", "Outubro"),
              ("Nov", "Novembro"),
              ("Dec", "Dezembro")]

    HMS = [("h", "hora", "horas"),
           ("m", "minuto", "minutos", "min"),
           ("s", "segundo", "segundos")]

    AMPM = [("am", "a"),
            ("pm", "p")]

    UTCZONE = ["UTC", "GMT", "Z", "z"]
    PERTAIN = ["de"]
    TZOFFSET = {}

    def __init__(self, dayfirst=True, yearfirst=False):
        super().__init__(dayfirst, yearfirst)
