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

    def load_connessioni(self,role):
        lista=self.dao.read_connessioni(role)
        if len(lista)==0:
            print("Lista connessioni vuota "
                  "we are in model!!!")
            return []
        return lista

    def load_artist(self,role):
        lista=self.dao.read_artisti(role)
        if len(lista)==0:
            print("Lista artisti vuota "
                  "we are in model!!!")
            return []
        return lista

    def load_names(self):
        lista=self.dao.read_name()
        if len(lista)==0:
            print("Lista nomi vuota "
                  "we are in model!!!")
            return []
        return lista


    def build_graph(self,role):
        self.grafo=nx.DiGraph()
        self.grafo.clear()
        lista=self.load_artist(role)
        if len(lista)==0:
            print("Lista ruoli vuota "
                  "we are in model!!!")
            return []
        for r in lista:
            id1=r["id"]
            oggetti1=int(r["oggetti"])
            for c in lista:
                id2=c["id"]
                oggetti2=int(c["oggetti"])
                if id1!=id2:
                    if oggetti1<oggetti2:
                        self.grafo.add_edge(id1,id2,weight=abs(oggetti1-oggetti2))
                    elif oggetti2<oggetti1:
                        self.grafo.add_edge(id2,id1,weight=abs(oggetti2-oggetti1))
                    elif oggetti1==oggetti2:
                        continue
        for n in self.grafo.nodes:
            self.grafo.nodes[n]["name"]=0

        lista_nomi=self.dao.read_name()
        if len(lista_nomi)==0:
            print("Lista ruoli vuota "
                  "we are in model!!!")
            return []
        for n in lista_nomi:
            id=int(n["id"])
            name=n["nome"]
            self.grafo.nodes[id]["name"]=name
        return self.grafo

    def get_lista(self):
        lista=[]
        for n in self.grafo.nodes:
            name=self.grafo.nodes[n]["name"]
            somma_out=0
            somma_in=0
            for u,s,attr in self.grafo.out_edges(n,data=True):
                somma_out+=attr["weight"]
            for u,s,attr in self.grafo.in_edges(n,data=True):
                somma_in+=attr["weight"]
            score=somma_out-somma_in
            lista.append([name,score])
        lista_ordinata=sorted(lista,key=lambda x: x[1],reverse=True)
        return lista_ordinata







