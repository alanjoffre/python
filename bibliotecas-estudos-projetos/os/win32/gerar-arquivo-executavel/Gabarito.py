# Importante: Todas as bibliotecas devem ser instaladas dentro da pasta do projeto, pelo terminal do VSCODE!
# Necessário criar um amiente virtual para o projeto: python -m venv venv
# Necessário ativar o ambiente virtual, caso esteja utilizando o powershell: .\venv\Scripts\Activate.ps1
# Necessário ativar o ambiente virtual, caso esteja utilizando o cmd: .\venv\Scripts\Activate.bat
# Para desativar o ambiente virtual: deactivate
# Necessário instalar pandas: pip install pandas
# Necessário instalar win32: pip install pywin32
# Necessário instalar openxl: pip install openpyxl
# Necessário instalar pyinstaller: pip install pyinstaller
# Comando para criar o arquivo executavel: pyinstaller --onefile Gabarito.py
# Depois que executar o comando pode excluir a pasta: build
# Exclua o arquivo: Gabarito.spec
# Mova o arquivo dentro da pasta dist para a pasta raiz do seu projeto
# Exclua a pasta dist
# Para rodar o arquivo exe, é necessário a base de dados!
# Envie a pasta com todos os arquivos necessários. 

import pandas as pd
import win32com.client as win32

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-' * 50)
# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

# enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'alanjoffre@outlook.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Lira</p>
'''

mail.Send()

print('Email Enviado')
