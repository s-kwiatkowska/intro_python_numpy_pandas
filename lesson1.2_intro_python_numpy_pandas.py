# In[1]:

get_ipython().run_cell_magic('html', '', '<iframe style="height:500px;width:100%" src="https://bit.ly/39pJ40n" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>')


# ## Python (3.7)

# In[1]:


print("Hello world!")


# **Uwaga!** Wykonując jakąś komórkę w *Jupyter*, zwracana jest wartość ostatniego wiersza. W następnej komórce jest zakomentowany wiersz z `#print(name)`. Pamiętaj jednak, że samo `"name"` da dokładnie to, co w cudzysłowiu. Możesz to sprawdzić.

# In[2]:


name = "Jacek"
name
#print(name)


# In[1]:


name = "Sandra"
name


# In[3]:


years = [2015, 2016, 2017, 2018]
#print(years)
years


# In[3]:


years = [2020, 2021, 2022, 2023]
print(years)


# In[4]:


years = list(range(2015, 2019)) #range(start, finish + 1)
years


# In[5]:


print(years[0]) #pierwszy element
print(years[1]) #drugi element
print(years[-1]) #ostatni element
print(years[-2]) #przedostatni element


# In[6]:


name = "Jan Kowalski"
print(name[0]) #pierwsza litera
print(name[-1]) #ostatnia litera
print(name.lower())#małe litery
print(name.upper())#duże litery
print(name.split(' ')) #rozdziel string na listę używając danego separatora (w tym przypadku jest to spacja)


# In[7]:


years = range(2010, 2019)
print([year for year in years])
print([year * 2 for year in years]) #podwojone wartości
print([year * 2 for year in years if year % 2 == 0]) #podwój wartość, jeśli to liczba parzysta


# In[8]:


[x-50 for x in years]


output = []
for year in years:
    if year % 2 == 0: 
        output.append(year*2)
output  


# ## [numpy](https://bit.ly/3u2hM8m)
# To biblioteka do pracy z wektorami lub macierzami. Jest bardzo szybka (w porównaniu do "czystego" Pythona) i dlatego będziemy jej używać.

# In[10]:


import numpy as np #przyjęło się, że dla numpy jest nadawy alias "np"


# In[11]:


arr = np.array([1, 2, 3, 4, 5, 6]) # tablica
arr


# In[12]:


type(arr)


# In[13]:


np.array([1, 2, 3]) + np.array([5, 6, 7])


# In[14]:


np.mean([1, 2, 3])


# In[15]:


np.array([1, 2, 3]).mean()


# In[16]:


print(arr == 1) #tylko pierwszy element jest True (bo jest równy 1)
print(arr == 2) #tylko drugie element jest True (bo jest równy 2)
print(arr > 2) #pierwsze dwa nie pasują (tylko 3 i wyżej są większe od 2), reszt pasuję
print(arr %2 == 0) # tylko parzyste


# Zostawiamy tylko parzyste elementy w tablicy. Operator "%" to jest [modulo](https://bit.ly/39njYPS).

# In[17]:


arr[ arr % 2 == 0 ]


# Na samym dole strony są dwa linki do 2-godzinnych webinarów na temat: python/numpy + pandas. Są tam również przykłady na githubie. Zapoznaj się z tym i spróbuj to wykonać samodzielnie (przynajmniej część).

# # Zadania domowe

# ## Zadanie 1.2.1
# Masz listę od 0 do 18. Twoim zadaniem jest zostawić tylko liczby, które dzielą się na 4 bez reszty (czyli 0, 4, 8, 12 i 16).
# 

# In[21]:


numbers = range(19)
[ x for x in numbers if x % 4 == 0]


# ```python
# my_arr = range(19)
# [ x for x in my_arr if x % 4 == 0]
#     
# #numpy
# my_arr = np.array(my_arr)
# my_arr[ my_arr %4 == 0 ]
# ```
# Pamiętaj, aby zerkać tutaj dopiero, gdy już spróbujesz wykonać zadanie samodzielnie. 
# </p>
# </details>
# </p>
# </details> 

# ## Zadanie 1.2.2
# Masz dwie listy i chcesz zsumować każdą parę (np. pierwszy element list_c[0] = list_a[0] + list_b[0]), w wyniku dostaniesz trzecią listę (`list_c`). Następnie chcesz znaleźć medianę trzeciej listy (czyli `median_list_c`).

# In[18]:


import numpy as np

list_a = np.array(range(10))
list_b = np.array(range(10,20))
list_c = list_a + list_b
print(list_c)
median_list_c = np.median(list_c)
print(median_list_c)


# <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć podpowiedź  👈 </summary>
# <p>
# Utwórz dwie listy (o tej samej długości) i użyj funkcji np.median
# <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć odpowiedź  👈 </summary>
# <p>
# 
# ```python
# list_a = np.arange(10)
# list_b = np.arange(10) * 2
# 
# np.median(list_a + list_b)
# ```
# Najpierw próbujesz zrobić zadanie samodzielnie, a dopiero potem tutaj zerkasz, prawda? ;)  
# </p>
# </details>
# </p>
# </details> 

# ## Zadanie 1.2.3
# Masz listę, która posiada 1000 elementów. Chcesz zostawić wszystkie elementy, które mają indeksy od 50 do 99 i od 325 do 388 (włącznie).

# In[19]:


import random

randomlist = []
for i in range(1000):
    n = random.randint(1,100)
    randomlist.append(n)
    
print(randomlist)

list1 = randomlist[50:99]
list2 = randomlist[325:388]

print("Output:", list1 + list2, sep='\n')


# In[21]:

import pandas as pd #przyjęło się nadawać dla pandas alias "pd"

# In[22]:


np.random.seed(2018)
rows = 15

df = pd.DataFrame({
    'height': np.random.randint(140, 210, rows),
    'weight': np.random.randint(50, 80, rows),
})

df


# Dostać się do danych w wybranej kolumnie można na co najmniej dwa sposoby.

# In[23]:


df.height

#lub

df['height']


# Dość często używany jest pierwszy sposób, bo ma mniej znaków (nie trzeba otwierać zamykać nawiasów kwadratowych i apostrofów). Natomiast druga wersja ma taką przewagę, że jest bardziej stabilna (np. jeśli kolumna nazywa się "count" to pierwsza wersja pomyli nazwę kolumny z nazwą funkcji `count()`, to samo dotyczy `min`, `max` itd). Sprawdźmy to.

# In[24]:


df['count'] = 1

print(type(df.count))
print(type(df.height))


# In[25]:


df['ratio'] = df['height'] / df['weight']

#lub
#df['ratio'] = df.height / df.weight

#źle (nie zadziała)
#df.ratio = df.height / df.weight

df.head()


# In[26]:


df[ (df.height < 145) | (df.height > 195) ]


# In[27]:


if 'ratio' in df: del df['ratio']


# # Zadanie 1.2.4
# 
# Zrób `dataframe`, który na początek zawiera dwie kolumny:
# - **age** (losowe wartości od 15 do 50)
# - **weight** (losowe wartości od 50 do 80)

# In[28]:


import pandas as pd

np.random.seed(1)
rows = 15

df = pd.DataFrame({
    'age': np.random.randint(15, 50, rows),
    'weight': np.random.randint(50, 80, rows),
})

df


# # <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć podpowiedź 👈 </summary>
# <p>
# Zainspiruj się powyższym przykładem i zmień nazwę kolumny na `age`. 
# 
# 
# <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć odpowiedź 👈 </summary>
# <p>
# 
# ```python
# np.random.seed(0)
# rows = 15
# 
# df = pd.DataFrame({
#     'age': np.random.randint(15, 50, rows),
#     'weight': np.random.randint(50, 80, rows),
# })
# 
# df
# ```
#  
# </p>
# </details>
# </p>
# </details> 

# Dawniej (teraz już są inne standardy, ale pomijam ten wątek) uważało się, że dla chłopców/mężczyzn wzrost w cm to `wzrost = waga + 110`. 
# 
# Twoim zadaniem jest stworzyć nową kolumnę o nazwie `height`, która będzie równa `weight + 110`.

# In[30]:


df['height'] = df['weight'] + 110
df


# ## Przydatne linki:
# * Ksiażka: [Python Data Science Handbook](https://bit.ly/31ubHFw)
# * [Webinar - python/numpy](https://bit.ly/3cwans0) + [github](https://bit.ly/3u58eJQ)
# * [Webinar - pandas](https://bit.ly/3dcQd5r) + [github](https://bit.ly/3u2jMxb)

# In[ ]:




