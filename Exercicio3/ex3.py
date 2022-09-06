from turtle import width
import matplotlib.pyplot as plt
import numpy as np

mes = np.arange(12) + 1 # meses de 1 a 12

# quantidades de produtos vendidos por mês
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])

# Gráfico 1 - Total de produtos Vendidos por mês - Linha
vendas_mes = np.array([creme_facial, limpeza_facial, pasta_dentaria, sabonete, shampoo, hidratante])

total_vendas = np.sum(vendas_mes, 0)

fig, ax = plt.subplots()

ax.plot(mes,total_vendas)
ax.set_title("Total de vendas/mes")
ax.set_xlabel("Meses")
ax.set_ylabel("Vendas")

# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha
fig, ax = plt.subplots()

ax.plot(mes, creme_facial, label="Creme Facial")
ax.plot(mes, limpeza_facial, label="Limpeza Facial")
ax.plot(mes, pasta_dentaria, label="Pasta Dentaria")
ax.plot(mes, sabonete, label="Sabonete")
ax.plot(mes, shampoo, label="Shampoo")
ax.plot(mes, hidratante, label="Hidratante")
ax.legend()
ax.set_title("Total de Produtos Vendidos por mês")
ax.set_xlabel("Meses")
ax.set_ylabel("Vendas")


# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras

fig, ax = plt.subplots()

largura_barra = 0.3

ax.bar(mes - largura_barra/2,creme_facial, width=largura_barra,label="Creme Facial")
ax.bar(mes + largura_barra/2,limpeza_facial, width=largura_barra,label="Limpeza Facial")
ax.set_xlabel("Meses")
ax.set_ylabel("Vendas")

ax.legend()

# Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)

faixas = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
fig, ax = plt.subplots()


ax.hist(vendas_mes)
ax.legend()

# Gráfico 5 - Pizza. % da quantidade produtos vendidos no ano em cada produto

fig, ax = plt.subplots()

ax.pie(total_vendas, autopct="%1.1f%%")

plt.show(block=True)