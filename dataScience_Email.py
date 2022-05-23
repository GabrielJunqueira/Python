import pandas as pd
import win32com.client as win32
tabela_vendas = pd.read_excel('Vendas.xlsx')

#agrupa a tabela somando todas as linha de um mesmo shopping e mostra a soma do valor final vendido
valor = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()


#print(ticketMedio)

######################
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'emailadress@gmail.com'
mail.Subject = 'Relatório de Vendas'
mail.HTMLBody = f'''
<p>Prezado,</p>
<p>Segue o relatório de vendas por loja:</p>
<p>Faturamento:</p>
{valor.to_html(formatters={'Valor Final':'R${:,.2f}'.format})}
'''

mail.Send()
######################
