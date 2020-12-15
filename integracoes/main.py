import config
import time
import logging 

try:
    method = sys.argv[1]
except Exception, e:
    method = ''

if str(method) == 'conversaoDolar':
    try:
        initialTime = time.time()
        urlDolar = config.SERVER['urlDolar']
        economiaAPI = EconomiaAPI(urlDolar)
        result = economiaAPI.olharCotacaoMoeda()
        endTime = time.time() 
        duarcaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result =  '0-0'
    print result

if str(method) == 'conversaoEuro':
    try:
        initialTime = time.time()
        urlEuro = config.SERVER['urlEuro']
        economiaAPI = EconomiaAPI(urlEuro)
        result = economiaAPI.olharCotacaoMoeda()
        endTime = time.time() 
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = '0-0'
    print result

if str(metthod) == 'conversaoLibra':
    try:
        initialTime = time.time()
        urlLibra = config.SERVER['urlLibra']
        economiaAPI = EconomiaAPI(urlLibra)
        result = economiaAPI.olharCotacaoMoeda()
        endTime = time.time()
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = '0-0'
    return result
