import config
import time
import logging 

try:
    method = sys.argv[1]
except Exception, e:
    method = ''

if str(method) == 'conversaoDolarParteInteira':
    result=''
    try:
        initialTime = time.time()
        urlDolar = config.server['urlDolar']
        keyNameCoin = 'USD'
        economiaAPI = EconomiaAPI(urlDolar, keyNameCoin)
        result = economiaAPI.olharCotacaoMoedaParteInteira()
        endTime = time.time() 
        duarcaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result =  404
    print int(result)

if str(method) == 'conversaoDolarParteFracionada':
    result=''
    try:
        initialTime = time.time()
        urlDolar = config.server['urlDolar']
        keyNameCoin = 'USD'
        economiaAPI = EconomiaAPI(urlDolar, keyNameCoin)
        result = economiaAPI.olharCotacaoMoedaParteFracionada()
        endTime = time.time() 
        duarcaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = 404
    print int(result)

if str(method) == 'conversaoEuroParteInteira':
    result=''
    try:
        initialTime = time.time()
        urlEuro = config.server['urlEuro']
        keyNameCoin = 'EUR'
        economiaAPI = EconomiaAPI(urlEuro, keyNameCoin)
        result = economiaAPI.olharCotacaoMoedaParteInteira()
        endTime = time.time() 
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = 404
    print int(result)

if str(method) == 'conversaoEuroParteFracionada':
    result=''
    try:
        initialTime = time.time()
        urlEuro = config.server['urlEuro']
        keyNameCoin = 'EUR'
        economiaAPI = EconomiaAPI(urlEuro, keyNameCoin)
        result = economiaAPI.olharCotacaoMoedaParteFracionada()
        endTime = time.time() 
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = 404
    print int(result)

if str(metthod) == 'conversaoLibraParteInteira':
    result=''
    try:
        initialTime = time.time()
        urlLibra = config.server['urlLibra']
        keyNameCoin = 'GBP'
        economiaAPI = EconomiaAPI(urlLibra, keyNameCoin)
        result = economiaAPI.olharCotacaoMoedaParteInteira()
        endTime = time.time()
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = 404
    print int(result)

if str(metthod) == 'conversaoLibraParteFracionada':
    result=''
    try:
        initialTime = time.time()
        urlLibra = config.server['urlLibra']
        keyNameCoin = 'GBP'
        economiaAPI = EconomiaAPI(urlLibra, keyNameCoin)
        result = economiaAPI.olharCotacaoMoedaParteFracionada()
        endTime = time.time()
        duracaoTotal = endTime - initialTime
        logging.info('Tempo total gasto {duracaoTotal}'.format())
    except Exception, e:
        result = 404
    print int(result)
