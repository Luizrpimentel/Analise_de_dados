import pandas as pd
from IPython.display import display

produtos_df = pd.read_excel(r'produtos.xlsx')
produtos_df.loc[produtos_df['Tipo'] == 'Serviço','Multiplicador Imposto'] = 1.5
produtos_df['Preço Base Reais'] = produtos_df['Preço Base Original'] * produtos_df['Multiplicador Imposto']
display(produtos_df)
produtos_df.to_excel('NovoProdutosPandas.xlsx')

## Usando openpyxl para manter o grafico

from openpyxl import Workbook, load_workbook

planilha = load_workbook("Produtos.xlsx")

aba_ativa = planilha.active

for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5

planilha.save("ProdutosOpenPy.xlsx")


