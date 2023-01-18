import pandas as pd
from IPython.display import display
funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
display(funcionarios_df)
display(clientes_df)
display(servicos_df)

print('Qual Valor Total da folha salarial')
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print('Total de folha salarial é de R${:,}'.format(sum(funcionarios_df['Salario Total'])))

print('Qual foi o faturamento da empresa?')
faturamento_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']])
print('Faturamento foi de R${:,}'.format(sum(faturamento_df['Tempo Total de Contrato (Meses)'] * faturamento_df['Valor Contrato Mensal'])))

print('Qual o % de funcionários que já fechou algum contrato?')
qtde_funcionarios_fecharam = len(servicos_df['ID Funcionário'].unique())
qtde_funcionarios_totais = len(funcionarios_df['ID Funcionário'])
print('Percentual foi de {:.2%}'.format(qtde_funcionarios_fecharam / qtde_funcionarios_totais))

print('Qual o total de contratos por área?')
contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']])
qtde_contratos_area = contratos_area_df['Area'].value_counts()
print(qtde_contratos_area)
qtde_contratos_area.plot(kind='bar')


print('Qual o total de funcionários por área?')
qtde_funcionarios_area = funcionarios_df['Area'].value_counts()
print(qtde_funcionarios_area)
qtde_funcionarios_area.plot(kind='bar')

print('Qual o ticket médio mensal?')
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio mensal é de R${:,.2f}'.format(ticket_medio))