class Personne:
    def __init__(self, nom, prenom, age, argent=100):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.argent = argent

    def dit_coucou(self):
        print(f"Coucou, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")

    def euros(self):
        print(f"{self.prenom} a {self.argent} euros.")

    def recoit(self, autre, montant=10):
        self.argent += montant
        autre.argent -= montant
        print(f"{self.prenom} reçoit {montant} euros de la part de {autre.prenom}.")


mat_star = Personne("Star", "Mat", 10)
other = Personne("Untitled", "Other", 24)
mat_star.dit_coucou()
other.dit_coucou()
mat_star.euros()
other.euros()
mat_star.recoit(autre=other, montant=50)
mat_star.euros()
other.euros()
