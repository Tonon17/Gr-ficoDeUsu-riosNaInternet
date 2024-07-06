import pandas as pd
import matplotlib.pyplot as plt

data = {
        'Categoria' : ['População Total', 'Celulares', 'Usuários de Internet', 'Usuários de Redes Socias'],
        'Quantidade (Bilhões)' : [8.08, 5.61, 5.35, 5.04]  
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
plt.bar(df['Categoria'], df['Quantidade (Bilhões)'], color=['purple', 'yellow', 'orange', 'red'])
plt.xlabel('Categoria')
plt.ylabel('Quantidade (Bilhões)')
plt.title('Dados Globais')
plt.ylim(0,9)

for i, value in enumerate(df['Quantidade (Bilhões)']):
  plt.text(i,value + 0.2, f'{value}Bi', ha='center')

plt.xticks(rotation=5)
plt.tight_layout()
plt.show()