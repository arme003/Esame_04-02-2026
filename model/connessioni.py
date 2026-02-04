from dataclasses import dataclass
@dataclass
class Connessioni:
    id1:int
    name1:str
    id2:int
    name2:str
    produttivita1:int
    produttivita2:int

    def __hash__(self):
        return hash((self.id1,self.id2))



