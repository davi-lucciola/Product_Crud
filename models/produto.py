class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
    
    # Getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    # Setters
    @preco.setter
    def preco(self, new_preco):
        self.__preco = new_preco
    
    @nome.setter
    def nome(self, new_name):
        self.__nome = new_name