import pandas as pd
from IPython.display import display
#importando os arquivos
vendas_df = pd.read_csv(r'Contoso - Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

#limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})

display(vendas_df)

print('Qual cliente que comprou mais vezes?')
frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()  #.value_counts() para contar quantas vezes cada valor do Dataframe aparece 
display(frequencia_clientes)

print('Qual a Loja que mais vendeu?')
vendas_lojas = vendas_df.groupby('Nome da Loja').sum() #.groupby para agrupar o nosso dataframe
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending = False)
display(vendas_lojas)

print('Qual a porcentagem das vendas foi devolvido?')
qtde_vendida = vendas_df['Quantidade Vendida'].sum()
qtde_devolvida = vendas_df['Quantidade Devolvida'].sum()
print('A porcetagem de devolução foi de : {:.2%}'.format(qtde_devolvida / qtde_vendida))

print('Faça uma analise apenas para uma loja.Queremos filtrar apenas os itens da Loja Contoso Europe Online e saber o % de devolução dessa loja.')
vendas_europeonline = vendas_df[vendas_df['ID Loja'] == 306] #filtrando o item pelo ID da loja
qtde_vendida = vendas_europeonline['Quantidade Vendida'].sum()
qtde_devolvida = vendas_europeonline['Quantidade Devolvida'].sum()
print('A porcetagem de devolução foi de : {:.2%}'.format(qtde_devolvida / qtde_vendida))


#Agora, e se quisermos acrescentar uma coluna com o mês, o dia e o ano de cada venda (e não só a data completa)
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y') #formatando a coluna de datas
vendas_df['Ano da Venda'] = vendas_df['Data da Venda'].dt.year #criando uma nova coluna separada
vendas_df['Mes da Venda'] = vendas_df['Data da Venda'].dt.month
vendas_df['Dia da Venda'] = vendas_df['Data da Venda'].dt.day


## Usando tqdm para criar uma barra de progresso
#Agora, imagina que a Loja Contoso Roma (ID 222), para tentar burlar o sistema de metas, diminuiu 1 da quantidade devolvida de todas as vendas que ela teve. Descobrindo isso, precisamos ajeitar a base
from tqdm import tqdm

pbar = tqdm(total=len(vendas_df['ID Loja']), position=0, leave=True)

for i, id_loja in enumerate(vendas_df['ID Loja']):
    pbar.update()
    if id_loja == 222:
        vendas_df.loc[i, 'Quantidade Devolvida'] += 1

display(vendas_df)