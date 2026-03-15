
import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

capital = float(input('Capital Inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = float(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual %: '))/100
perc_cdb = float(input('Percentual do CDI - CDB (%): '))/100
perc_lci = float(input('Percentual do CDI - LCI (%): '))/100
taxa_fii = float(input('Rentabilidade fo FII (%): '))/100
meta = float(input('Meta financeira (%): '))

# conversão VDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) - 1

# total investido
total_investido = capital + (aporte * meses)

# CDB
taxa_cdb = cdi_mensal * perc_cdb

montante_cdb = (capital * math.pow((1+taxa_cdb), meses)) + (aporte * meses)

lucro_cdb = montante_cdb - total_investido

montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

# LCI
taxa_lci = cdi_mensal * perc_lci

montante_lci = (capital * math.pow((1 + taxa_lci), meses)) + (aporte * meses)

# Poupanca
taxa_poupanca = 0.005

montante_poupanca = (capital * math.pow((1+taxa_poupanca),meses)) + (aporte * meses)

# FII com Simulação Estatística

resultados_fii = []

for i in range(5):

    montante_fii = (capital * math.pow((1+taxa_fii), meses)) + (aporte * meses)

    variacao = random.uniform(-0.03, 0.03)

    valor_final = montante_fii * (1 + variacao)

    resultados_fii.append(valor_final)

media_fii = statistics.mean(resultados_fii)

mediana_fii = statistics.median(resultados_fii)

desvio_fii = statistics.stdev(resultados_fii)


# Data de Resgate
hoje = datetime.date.today()

dias = int(meses * 30)

data_resgate = hoje + datetime.timedelta(days=dias)

# Relatório Final

print('\n RELATÓRIO DE INVESTIMENTOS ')

print('Total Investido:',
      locale.currency(total_investido, grouping=True))

print('\nCDB (líquido):',
      locale.currency(montante_cdb_liquido, grouping=True))

print('LCI:',
      locale.currency(montante_lci, grouping=True))

print('Poupança:',
      locale.currency(montante_poupanca, grouping=True))

print('\n------ FII (Simulação Estatística) ------')

print('Média:',
      locale.currency(media_fii, grouping=True))

print('Mediana:',
      locale.currency(mediana_fii, grouping=True))

print('Desvio padrão:',
      locale.currency(desvio_fii, grouping=True))

print('\nData estimada de resgate:',
      data_resgate.strftime('%d/%m/%Y'))
