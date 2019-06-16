class Arquivo:
    def __init__(self, caminho, cod=None):
        self.caminho = caminho
        self.cod = cod
    
    def _get_caminho(self):
        try:
            return self._caminho
        except AttributeError:
            return None
    
    def _set_caminho(self, caminho):
        if type(caminho) != str:
            raise ValueError()
        self._caminho = caminho
    
    caminho = property(_get_caminho, _set_caminho)

    def _get_cod(self):
        try:
            return self._cod
        except AttributeError:
            return None
    
    def _set_cod(self, cod):
        if type(cod) != int and cod is not None:
            raise ValueError()
        self._cod = cod
    
    cod = property(_get_cod, _set_cod)