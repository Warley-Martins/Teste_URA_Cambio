import request 

class EconomiaAPI
    def __init__ (self, urlAuxiliar):
        self.urlAuxiliar = urlAuxiliar

    def olharCotacaoMoedaParteInteira(self):
        response = request.get(self.urlAuxiliarr)
        json = response.json()
        valorFinalAuxiliar = str(json['bid'])
        arrayValorFinal = valorFinalAuxiliar.split('.')
        valorFinal = int(arrayValorFinal[0])
        return valorFinal
  
    def olharCotacaoMoedaParteFracionada(self):
        response = request.get(self.urlAuxiliarr)
        json = response.json()
        valorFinalAuxiliar = str(json['bid'])
        arrayValorFinal = valorFinalAuxiliar.split('.')
        valorFinal = int(arrayValorFinal[1])
        return valorFinal
    
  