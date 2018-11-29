from dateutil.parser import parserinfo, parser


class BrParserInfo(parserinfo):
    JUMP = [" ", ".", ",", ";", "-", "/", "'",
            "as", "a", "e", "de", "do", "da", "em"]

    WEEKDAYS = [("Seg", "Segunda"),
                ("Ter", "Terça"),
                ("Qua", "Quarta"),
                ("Qui", "Quinta"),
                ("Sex", "Sexta"),
                ("Sab", "Sábado"),
                ("Dom", "Domingo")]

    MONTHS = [("Jan", "Janeiro"),
              ("Fev", "Fevereiro"),
              ("Mar", "Março"),
              ("Abr", "Abril"),
              ("Mai", "Maio"),
              ("Jun", "Junho"),
              ("Jul", "Julho"),
              ("Aug", "Agosto"),
              ("Set", "Setembro"),
              ("Out", "Outubro"),
              ("Nov", "Novembro"),
              ("Dez", "Dezembro")]

    HMS = [("h", "hora", "horas", "hs"),
           ("m", "minuto", "minutos", "min"),
           ("s", "segundo", "segundos")]

    AMPM = [("am", "a"),
            ("pm", "p")]

    UTCZONE = ["UTC", "GMT", "Z", "z"]
    PERTAIN = ["de"]
    TZOFFSET = {}

    def __init__(self, dayfirst=True, yearfirst=False):
        super().__init__(dayfirst, yearfirst)
