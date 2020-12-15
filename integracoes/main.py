import request
import config
import time
import logging 

try:
    method = sys.argv[1]
except Exception, e:
    method = ''

if str(method) == 'conversaoDolar':
    tempoInicial = time.time()
    urlDolar = config.SERVER['urlDolar']
    response = request.get(urlDolar)
    json = response.json()
    valorFinal = json['bid']
    tempoFinal = time.time() 
    duarcaoTotal = tempoFinal- tempoInicial
    logging.info('Tempo total gasto {duracaoTotal}'.format())
    print valorFinal