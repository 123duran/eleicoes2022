import requests
import json
import pandas as pd
import os
from time import sleep
from datetime import datetime 

while True:

	data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')
	json_data = json.loads(data.content)
	print(json_data)

	candidato = []
	partido = []
	votos = []
	porcentagem = []
	numero = []

	for informacoes in json_data['cand']:
		if int(informacoes['seq']) in range(1,2):
			candidato.append(informacoes['nm'])
			votos.append(informacoes['vap'])
			porcentagem.append(informacoes['pvap'])
			numero.append(informacoes['n'])

	df_eleicao = pd.DataFrame(list(zip(candidato, numero, votos, porcentagem )), columns = ['Candidato', 'Número', 'Nº Votos', 'Porcentagem'])
	
	myobj = datetime.now()
	print('Horas:', myobj.hour, ':', myobj.minute, ':', myobj.second, '\n')

	print(df_eleicao)

	sleep(60)