#!/usr/bin/env python
# coding: utf-8

# In[7]:


filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)


# In[8]:


import numpy as np


# In[9]:


matriz2=np.copy(matriz)


# In[19]:


matriz3=np.concatenate((matriz, matriz2), axis=1)


# In[11]:


array = np.array(matriz3)
sumaF=np.sum(array, axis=1)
sumaC=np.sum(array, axis=0)
sumaD = 0
for i in range(0, filas):
    sumaD = sumaD +matriz3[i][i]
    if (i > 1):
        sumaD = sumaD + matriz3[i][2-i]


# In[14]:


print("""
    1) Suma de filas       3) Sumas de diagonal
    2) Suma de columnas:        
    """)
op=input("Opcion: ")
if op=="1":
    print("Suma de filas: ", sumaF)
elif op=="2":
    print("Suma de columnas: ", sumaC)
elif op=="3":
    print("Sumas de diagonal", sumaD)
else:
    print("Opción no válida")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




