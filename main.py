#biblioteca Pandas importada
import pandas as pd

agua_db = pd.read_excel ("DB2.xlsx")

lista = agua_db.to_dict(orient="records")

print (lista[0])