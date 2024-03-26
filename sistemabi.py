import pandas as pd
# pip install pandas
# pip install openpyxl
dados_produto={
    'id_produto':[10,20,30],
    'nome_produto':["camisa","calca","sapato"],
    'preco_produto':[100,300,500],
    'quantidade_produto':[1,2,2]
}

df_dados_compra = pd.DataFrame(dados_produto)

print("Resultado 1")
print (df_dados_compra)

df_dados_compra.to_csv('dadoscompra.csv', index=False)

print("Convertido em csv")

with pd.ExcelWriter('dados_excel.xlsx') as writer:
    df_dados_compra.to_excel(writer, sheet_name='dados_compra', index=False)

print ("convertido em xls")