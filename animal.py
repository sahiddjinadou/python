class Animal : 
    def __init__(self, nom, category) :
        self.nom = nom
        self.category = category
        
    def affiche_animale (self):
        print(f'Caci est un {self.category}. il s\'appelle {self.nom}')

class Chien(Animal):
    def __init__(self, nom, category,poids,race):
        super().__init__(nom, category)
        self.poids = poids
        self.race = race
        
    def affiche_animale(self):
        super().affiche_animale()
        #je suis en train de mettre un commntaire  
