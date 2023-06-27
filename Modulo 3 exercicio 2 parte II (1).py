#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# ### 1) Alturas  
# i. No trecho de código abaixo, crie um ndarray chamado ```altura_em_centimetros``` transformando a lista ```lista_de_alturas``` em um ndarray do numpy com a função ```np.array()```  
# ii. Crie um outro objeto ```altura_em_metros```, com os valores de ```altura_em_centimetros``` convertidos para metros.

# In[27]:


lista_de_centimetros = list(range(170, 190, 5))
lista_de_centimetros


# In[11]:


import numpy as np

# Criar o ndarray altura_em_centimetros a partir da lista_de_centimetros
lista_de_centimetros = list(range(170, 190, 5))
altura_em_centimetros = np.array(lista_de_centimetros)

# Imprimir os resultados
print("Altura em centímetros:", altura_em_centimetros)



# In[12]:


# Converter altura_em_centimetros para metros
altura_em_metros = altura_em_centimetros / 100

# Imprimir os resultados
print("Altura em metros:", altura_em_metros)


# ### 2) IMC  
# i. Considere que pesos em Kg dessas pessoas, na mesma ortem, estão na lista pesos ```lista_pesos = [70, 75, 80, 85]```. Crie um **ndarray** chamado ```pesos``` com a função ```np.array()``` que contenha esses valores.  
# ii. Utilizando o objeto que contém as alturas em metros e esse objeto que contém os respectivos pesos em quilos, calcule o IMC desses indivíduos utilizando a aritmética de arrays e guarde os resultados em um objeto chamado ```imc```.

# In[16]:


lista_pesos = [70, 75, 80, 85]
lista_pesos
import numpy as np

lista_pesos = [70, 75, 80, 85]

# Criação do ndarray 'pesos' a partir da lista_pesos
pesos = np.array(lista_pesos)

# Imprimir os resultados
print("Pesos:", pesos)




# In[18]:


# calcule o IMC dessas pessoas
# Cálculo do IMC utilizando a aritmética de arrays
imc = pesos / altura_em_metros ** 2
print("IMC:", imc)


# ### 3) Endividamento
# 
# Cálculos de novas variáveis como endividamento total e comprometimento de renda são essenciais para a construção de modelos financeiros em ciência de dados. Áreas não financeiras terão cálculos semelhantes também. Vamos praticar:
# 
# Considere que o seguinte ndarray contém os dados de 4 pessoas, total a ser pago a empréstimos mensalmente e renda familiar:
# 
# | custo fixo | dívida financeira | renda familiar |
# |:----:|:----:|:---|
# | 3000  | 1000 | 6000 |
# | 2500  | 2500 | 5500 |
# | 1000  | 3000 | 7000 |
# | 10000 | 5000 | 16000 |
# 
# i. Transforme a lista de listas ```dados_financeiros``` no ndarray ```nd_financeiros```.
# > ``` dados_financeiros[[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]] ```
# 
# ii. Utilize o método ```.transpose ``` e certifique-se de que esse ndarray tenha uma linha por indivíduo e uma coluna por informação. Utilizando a indexação do numpy, imprima no output a segunda linha do array, depois a segunda coluna.
# 
# iii. Pratique aritmética com nearrays e calcule o endividamento total como:
# $$endividamento\hspace{.2cm}total = \frac{custo \hspace{.2cm}fixo + dívida\hspace{.2cm}financeira}{renda\hspace{.2cm}familiar}$$
# Guarde os resultados em uma variável chamada ```endividamento_total``` e verifique os resultados imprimindo o conteúdo dessa variável no output.
# 
# iv. Considere que há um erro de digitação que precisa ser corrigido: 3o indivíduo na verdade não possui renda familiar de R\\$7.000,00, mas sim R\\$ 10.000,00. Corrija esse valor e refaça os cálculos.

# In[19]:


# lista dados_financeiros
dados_financeiros = [[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]]
dados_financeiros
#i) transforme essa lista em um ndarray


# In[21]:


# ii) import numpy as np

dados_financeiros = [[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]]

# Transforme a lista em um ndarray
ndarray_dados_financeiros = np.array(dados_financeiros)

# Imprima o ndarray
print(ndarray_dados_financeiros)


# In[22]:


# iii) Calcule o endividamento total
import numpy as np

dados_financeiros = [[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]]

# Transforme a lista em um ndarray
ndarray_dados_financeiros = np.array(dados_financeiros)

# Calcule o endividamento total
endividamento_total = np.sum(ndarray_dados_financeiros)

# Imprima o endividamento total
print("Endividamento total:", endividamento_total)


# In[23]:


# iv) corrigindo um valor específico
import numpy as np

dados_financeiros = [[3000, 2500, 1000, 10000],[1000, 2500, 3000, 5000],[6000, 5500, 7000, 16000]]

# Transforme a lista em um ndarray
ndarray_dados_financeiros = np.array(dados_financeiros)

# Imprima o ndarray antes da correção
print("Ndarray antes da correção:")
print(ndarray_dados_financeiros)

# Corrija um valor específico
linha = 1
coluna = 2
novo_valor = 4000
ndarray_dados_financeiros[linha, coluna] = novo_valor

# Imprima o ndarray depois da correção
print("\nNdarray depois da correção:")
print(ndarray_dados_financeiros)


# ### 4) É muito comum precisarmos identificar valores especiais e darmos tratamento a eles quer seja alterando-os quer seja descartando-os. 
# 
# O trecho de código abaixo gera um ndarray com números pseudo aleatórios. Considere que para efeitos do estudo que virá, devemos desconsiderar valores iguais a zero. Sendo assim:
# 
# i) crie um objeto ```bool_zero``` que traga uma sequencia de booleanos do mesmo tamanho que o objeto poi, e que vale ```True``` quando o valor de ```poi``` é zero, e ```False``` caso contrário.
# 
# ii) Conte quantos valores zero existem. Lembre-se de que no final das contas, ```True``` vale 1 para o Python, e ```False``` vale zero, então uma boa dica seria usar a função ```sum()```.
# 
# iii) Utilize a indexação booleana que você aprendeu para criar uma variável ```poi_nao_zero``` que aponta para os elementos de ```poi``` diferentes de zero. Dica: você vai pode inverter os elementos do objeto que criou em *ii)* ou escrever a comparação adequada.

# In[25]:


# objeto poi - obs: o comando np.random.seed(1234) garante que o mesmo resultado será gerado sempre
np.random.seed(1234)
poi = np.random.poisson(3, 100)
poi


# In[31]:


# i) crie o objeto bool_zero através do operador ==
bool_zero = poi == 0
print("Objeto bool_zero:")
print(bool_zero)


# In[33]:


# ii) Conte a quantidade de zeros (ou some os elementos de bool_zero)
quantidade_zeros = np.sum(bool_zero)
print("\nQuantidade de zeros:", quantidade_zeros)


# In[36]:


# iii) utilize a indexação booleana para criar uma seleção de não-zeros
# dica: inverta o objeto bool_zero
selecao_nao_zeros = poi[~bool_zero]

# Imprimir a seleção de não-zeros
print("Seleção de não-zeros:")
print(selecao_nao_zeros)


# In[ ]:




