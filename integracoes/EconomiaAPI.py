import requests

class EconomiaAPI
    def __init__ (self, urlAuxiliar,keyNameCoin):
        self.urlAuxiliar = urlAuxiliar
        self.keyNameCoin = keyNameCoin

    def olharCotacaoMoedaParteInteira(self):
        response = requests.get(self.urlAuxiliar)
        json = response.json()
        valorFinalAuxiliar = str(json[keyNameCoin]['bid'])
        arrayValorFinal = valorFinalAuxiliar.split('.')
        valorFinal = int(arrayValorFinal[0])
        return valorFinal
  
    def olharCotacaoMoedaParteFracionada(self):
        response = requests.get(self.urlAuxiliarr)
        json = response.json()
        valorFinalAuxiliar = str(json[keyNameCoin]['bid'])
        arrayValorFinal = valorFinalAuxiliar.split('.')
        valorFinal = int(arrayValorFinal[1])
        return valorFinal
    
  