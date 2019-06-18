class Arquivo:
    def __init__(self, caminho=None, cod=None):
        self.caminho = caminho
        self.cod = cod
    
    def _get_caminho(self):
        try:
            return self._caminho
        except AttributeError:
            return None
    
    def _set_caminho(self, caminho):
        if type(caminho) != str and caminho is not None:
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

class ArquivoBinario(Arquivo):
    def __init__(self, cod=None, data=None, extension=None):
        super(ArquivoBinario, self).__init__(cod=cod)
        self.data = data
        self.extension = extension

    def _get_data(self):
        try:
            return self._data
        except AttributeError:
            return None
    
    def _set_data(self, data):
        print(type(data))
        if type(data) != bytes and data is not None:
            raise ValueError()
        self._data = data
    
    data = property(_get_data, _set_data)

    def _get_extension(self):
        try:
            return self._extension
        except AttributeError:
            return None
    
    def _set_extension(self, extension):
        if type(extension) != str and extension is not None:
            raise ValueError()
        self._extension = extension
    
    extension = property(_get_extension, _set_extension)