import config
import time
import logging 

try:
    method = sys.argv[1]
except Exception, e:
    method = ''

if str(method) == 'conversaoDolarParteInteira':
    try:
        initialTime = time.time()
        urlDolar = config.server['urlDolar']
        economiaAPI = EconomiaAPI(urlDolar)
        result = economiaAPI.olharCotacaoMoedaParteInteira()
        endTime = time.time() 
        duarcaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result =  '0-0'
    print result

if str(method) == 'conversaoDolarParteFracionada':
    try:
        initialTime = time.time()
        urlDolar = config.server['urlDolar']
        economiaAPI = EconomiaAPI(urlDolar)
        result = economiaAPI.olharCotacaoMoedaParteFracionada()
        endTime = time.time() 
        duarcaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result =  '0-0'
    print result

if str(method) == 'conversaoEuroParteInteira':
    try:
        initialTime = time.time()
        urlEuro = config.server['urlEuro']
        economiaAPI = EconomiaAPI(urlEuro)
        result = economiaAPI.olharCotacaoMoedaParteInteira()
        endTime = time.time() 
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = '0-0'
    print result

if str(method) == 'conversaoEuroParteFracionada':
    try:
        initialTime = time.time()
        urlEuro = config.server['urlEuro']
        economiaAPI = EconomiaAPI(urlEuro)
        result = economiaAPI.olharCotacaoMoedaParteFracionada()
        endTime = time.time() 
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = '0-0'
    print result

if str(metthod) == 'conversaoLibraParteInteira':
    try:
        initialTime = time.time()
        urlLibra = config.server['urlLibra']
        economiaAPI = EconomiaAPI(urlLibra)
        result = economiaAPI.olharCotacaoMoedaParteInteira()
        endTime = time.time()
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = '0-0'
    return result

if str(metthod) == 'conversaoLibraParteFracionada':
    try:
        initialTime = time.time()
        urlLibra = config.server['urlLibra']
        economiaAPI = EconomiaAPI(urlLibra)
        result = economiaAPI.olharCotacaoMoedaParteFracionada()
        endTime = time.time()
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = '0-0'
    return result
