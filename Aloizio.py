import pandas as pd
ficticios = {'Nome': ['Alice', 'Laryssa', 'Samuel' , 'Luciano','Aloizio','Steffany','Kesya','Alenri','Javid', 'Angel'],
             'Idade': [25, 30, 35,45,34,46,56,67,41,22],
             'departamento': ['ADM','telemarketing','ADM','Estagiario','Front_end','Back_and','Telemarketing','Gerente','Telemarketing','Estagiario'],
             'salario': [3500,1800,5000,1000,10000,10000,2500,12000,2000,1000]
             }

df = pd.DataFrame(ficticios)

print(df.info('Nome'))

df['meses_empresa'] = [7,7,22,3,11,12,5,120,5,3]

print(df)

import matplotlib.pyplot as plt



plt.bar(df['Nome'],df['salario'])

plt.title('grafico de Nomes x salario')
plt.xlabel('eixo nome')
plt.ylabel('eixo salario')


plt.show()

import matplotlib.pyplot as plt

plt.plot(df['Nome'], df['Idade'])


plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.title('Vendas ao longo dos anos')


plt.show()

