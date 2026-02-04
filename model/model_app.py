import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.dao = DAO()
        self.grafo =None

    def load_roles(self):
        lista=self.dao.read_role()
        if len(lista)==0:
            print("Lista ruoli vuota "
                  "we are in model!!!")
            return []
        return lista


