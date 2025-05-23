class Studente:
    def __init__(self, nome, classe):
        self.nome = nome   
        self.classe = classe     
        self.voti = []   

    def aggiungi_voto(self, voto):
        if 0 <= voto <= 10:
            self.voti.append(voto)
        else:
            print("voto non valido")

    def calcola_media(self):
        if len(self.voti) == 0:
            return 0
        return sum(self.voti) / len(self.voti)
    
    def stampa_info(self):
        