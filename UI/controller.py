import flet as ft


class Controller:
    def __init__(self,view,model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        role=self._view.dd_ruolo.value
        grafo=self._model.build_graph(role)
        num_nodi=self._model.grafo.number_of_nodes()
        num_archi=self._model.grafo.number_of_edges()
        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Nodi: {num_nodi}\n"
                                                                 f"Archi: {num_archi}\n"))
        lista=self._model.get_lista()#name,peso
        for name,score in lista:
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{name} score: {score}"))
        self._view.update()



    def handle_classifica(self, e):
        pass


    def populate_dd_role(self):
        lista=self._model.load_roles()
        if len(lista)==0:
            print("Lista vuota roles")
            return []
        self._view.dd_ruolo.options.clear()
        for n in lista:
            role=n["role"]
            self._view.dd_ruolo.options.append(ft.dropdown.Option(key=role, text=role))
        self._view.update()