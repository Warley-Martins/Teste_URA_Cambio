import request 

class EconomiaAPI
    def __init__ (self, urlAuxiliar):
        self.urlAuxiliar = urlAuxiliar
    
    def olharCotacaoMoeda(self):
        response = request.get(self.urlAuxiliarr)
        json = response.json()
        valorFinal = json['bid']
        return valorFinal