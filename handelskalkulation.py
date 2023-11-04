"""
Alle benötigten Werte in handel_input eingeben und dann laufen lassen. sollte ein zb. keinen kundenrabatt geben diesen wert auf 0.00 setzen
"""

    
class handels_kalkulator:
    input = {
    "listeneinkaufspreis": 300,
    "lieferrabatt" : 0.20,
    "lieferskonto" : 0.03,
    "bezugskosten" : 3.00,
    "handlungskosten" : 0.7,

    "gewinnzuschlag" : 0.08,
    "kundenskonto" : 0.03,
    "vertreterprovision" : 0.00,
    "kundenrabatt" : 0.00,
    "umsatzsteuer" : 0.19
    }

    output = {
    "zieleinkaufspreis" : None,
    "bareinkaufspreis" : None,
    "bezugspreis" : None,
    "selbstkosten" : None,
    "barverkaufspreis" : None,
    "zielverkaufspreis" : None,
    "listenverkaufspreis" : None
    }
    
    def __init__(self, input = None, output = None):
        if(input):
            self.input = input
        if(output):
            self.input = input

    def get_zieleinkaufspreis(self):    
        self.output["zieleinkaufspreis"] = self.input["listeneinkaufspreis"] * (1 - self.input["lieferrabatt"]) 
    def get_bareinkaufspreis(self):
        self.output["bareinkaufspreis"] =  self.output["zieleinkaufspreis"] * (1 - self.input["lieferskonto"]) 
    def get_bezugspreis(self):
        self.output["bezugspreis"] = self.output["bareinkaufspreis"] + self.input["bezugskosten"]
    def get_selbstkosten(self):
        self.output["selbstkosten"] = self.output["bezugspreis"] * (1 + self.input["handlungskosten"])
    def get_barverkaufspreis(self):
        self.output["barverkaufspreis"] = self.output["selbstkosten"] * (1 + self.input["gewinnzuschlag"])
    def get_zielverkaufspreis(self):
        self.output["zielverkaufspreis"] = self.output["barverkaufspreis"] * (1 + self.input["kundenskonto"] + self.input["vertreterprovision"])
    def get_listenverkaufspreis(self):
        self.output["listenverkaufspreis"] = self.output["zielverkaufspreis"] * (1 + self.input["kundenrabatt"])
    def get_listverkaufpreisMwst(self):
        self.output["listenverkaufpreisMwst"] = self.output["listenverkaufspreis"] * (1 + self.input["umsatzsteuer"])

    def calculate(self):
        self.get_zieleinkaufspreis()
        self.get_bareinkaufspreis()
        self.get_bezugspreis()
        self.get_selbstkosten()
        self.get_barverkaufspreis()
        self.get_zielverkaufspreis()
        self.get_listenverkaufspreis()
        self.get_listverkaufpreisMwst()

    def print(self):
        for i in self.output:
            print(f"{i.capitalize()}: {round(self.output[i],2)} €")


mycalc = handels_kalkulator()
mycalc.calculate()
mycalc.print()