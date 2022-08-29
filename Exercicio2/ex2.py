from tokenize import Double
import numpy as np

anos = np.array(np.loadtxt("./PI-4o-Semestre/Exercicio2/anos.txt"), dtype=int)

altura = np.array(np.loadtxt("./PI-4o-Semestre/Exercicio2/altura.txt"), dtype=float)

TotalAltura = 0;
TotalPessoas = 0;

for i,j in zip(anos,altura):
    # print("Ano:", i, "Altura:", j)
    if i > 1998 and i < 2005:
        TotalAltura += j
        TotalPessoas += 1
    

MediaAltura = TotalAltura/TotalPessoas
print(MediaAltura)


