#!/usr/bin/env python
# coding: utf-8

# # Python i biblioteki
# 
# ### Celem jest przypomnieć lub poznać składnię Pythona oraz potrzebnych bibliotek.
# 
# Te ćwiczenia są obowiązkowe, jeśli chcesz sobie przypomnieć lub poznać potrzebne podstawy [Python](https://bit.ly/2O0HJFQ) oraz potrzebne biblioteki.
# 
# Oczywiście to będzie tylko kawałek wiedzy, która nam się przyda. Sam język Python, jak i biblioteki, wymagają znacznie więcej czasu niż godzinka, ale musimy od czegoś zacząć :).
# 
# **Uwaga!** Jeśli czujesz się pewnie z Python i bibliotekami: [numpy](https://bit.ly/3sAqEl2), [pandas](https://bit.ly/2O4s8Fm) to zapraszam do kolejnego ćwiczenia - **[lesson1.3](./lesson1.3_basic_model_predict_name.ipynb)**.
# 
# Natomiast jeśli czujesz, że jest to zbyt trudne, to przypominam o notebooku "[krok po kroku](step_by_step.ipynb)", w którym na wideo jeszcze dokładniej tłumaczę, co się dzieje.

# ### Krok po kroku 
# 
# Jeśli wolisz najpierw słuchać i oglądać, to obejrzyj nagranie poniżej, które omawia tę lekcję. 

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


# **Uwaga!**
# 
# Funkcja `range` generuje przedział od ... do, natomiast zwróć uwagę, że `range` zatrzymuje się tuż przed "do" (nie włączając). Na przykład jeśli chcemy wygenerować przedział do roku 2018, to należy podać o jeden więcej (czyli 2019). Wtedy `range` zatrzyma się tuż przed (czyli na roku 2018).
# 
# Stąd jest w komentarzu: `finish + 1`, do oczekiwanego końca należy dodać jeszcze jeden.

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


# **Uwaga!**
# Tu łatwo przeoczyć, że całość `for` jest w nawiasach kwadratowych, co dla osoby początkującej może wydawać się dziwne - zamiast wartości tablicy mamy kod. Przyjrzyj się dokładniej. Zwróć uwagę, że są to nawiasy kwadratowe i takie coś:  `print(year for year in years)` nie działa.

# In[9]:


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


# <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć podpowiedź 👈 </summary>
# <p>
# Pamiętaj, że możesz to napisać w czystym Python (spróbuj), ale do bardziej eleganckiego rozwiązania warto użyć `numpy`.
# <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć odpowiedź 👈 </summary>
# <p>
# 
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

# ### 🤝🗣️ Współpraca 💪 i komunikacja 💬
# 
# - 👉 [#pml_module1](https://practicalmlcourse.slack.com/archives/C045CNLNH89) - to jest miejsce, gdzie można szukać pomocy i dzielić się doświadczeniem - także pomagać innym 🥰. 
# 
# Jeśli masz pytanie, to staraj się jak najdokładniej je sprecyzować, najlepiej wrzuć screen z twoim kodem i błędem, który się pojawił ✔️
# 
# - 👉 [#pml_module1_done](https://practicalmlcourse.slack.com/archives/C045CP89KND) - to miejsce, gdzie możesz dzielić się swoimi przerobionymi zadaniami, wystarczy, że wrzucisz screen z #done i numerem lekcji np. *#1.2.1_done*, śmiało dodaj komentarz, jeśli czujesz taką potrzebę, a także rozmawiaj z innymi o ich rozwiązaniach 😊 
# 
# - 👉 [#pml_module1_ideas](https://practicalmlcourse.slack.com/archives/C044TFZLF1U)- tutaj możesz dzielić się swoimi pomysłami
# 

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


# # <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć podpowiedź 👈 </summary>
# <p>
# Należy użyć łącznie 4 filtrów (po dwie grupy, wewnątrz operatora i i na zewnątrz, między grupami, operator)
# <details>
#     <summary style="background: #e6eaeb; padding: 4px 0; text-align: center; font-size: 20px; font-weight: 900;"> 👉 Kliknij tutaj (1 klik), aby zobaczyć odpowiedź 👈 </summary>
# <p>
# 
# ```python
# my_list = np.arange(1000)
# 
# 
# frst_ = (my_list >= 50) & (my_list < 100)
# scnd_ = (my_list >= 325) & (my_list < 389)
# my_list[  frst_ | scnd_ ]
# ```
#  
# </p>
# </details>
# </p>
# </details> 

# ## [pandas](https://bit.ly/3fmipW5)
# To biblioteka, która będzie nam bardzo potrzebna dalej. O `pandas` możesz myśleć jak o `numpy` na "sterydach" albo jak o tabelce z danymi jak w Excelu, w którym możesz w bardzo łatwy sposób filtrować i grupować dane, wybierać potrzebne kolumny itd.

# In[21]:


import pandas as pd #przyjęło się nadawać dla pandas alias "pd"


# `Pandas` wewnątrz używa `numpy`, dlatego składnia na przykład filtrowania, jest podobna (lub czasem identyczna). Bardzo łatwo można także konwertować dane z `pandas` do `numpy`.
# 
# W terminologii `numpy` wszystko obraca się wokół wektorów i macierzy. W pandas mamy podobnie dwie struktury: `Series` (odpowiednik wektora) i `DataFrame` (odpowiednik macierzy).
# 
# Oczywiście `DataFrame` jest bardziej rozbudowany niż goła macierz. Zobacz poniżej. 

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


# Przeanalizujmy to krok po kroku.
# 
# 
# Po pierwsze: stworzyliśmy nową kolumnę w `dataframe`, w naszym przypadku `df` o nazwie `count`. Jak widzisz, stworzenie nowej kolumny wymaga użycia drugiego sposobu (czyli dłuższego). Jeśli spróbujesz stworzyć kolumnę w ten sposób: `df.count = 1`, to kolumna się nie utworzy. Sprawdź :).
# 
# Po drugie: możemy przypisać do kolumny stałą. W naszym przypadku to była 1. Czyli wszystkie wiersze w kolumnie `count` mają wartość 1.
# 
# Po trzecie: spróbujmy odwołać się do kolumn poprzez kropkę. Widzimy, że w przypadku z `height` to zadziałało, bo nie ma konfliktów w nazwie. Natomiast dla `count` to nie przeszło, bo uznało, że chodzi o funkcję o nazwie `count`, która zlicza ilość zamiast odwołać się do kolumny o nazwie `count`, dlatego należy podchodzić do tego ostrożnie.
# 
# Stwórzmy jeszcze jedną kolumnę bazując na dwóch obecnych. Możemy np. podzielić wzrost przez wagę.

# In[25]:


df['ratio'] = df['height'] / df['weight']

#lub
#df['ratio'] = df.height / df.weight

#źle (nie zadziała)
#df.ratio = df.height / df.weight

df.head()


# Pojawiła się nowa kolumna o nazwie `ratio`. Zwróć uwagę, że dzieląc jedną kolumnę przez drugą, traktowaliśmy to jako pojedynczą wartość (ale pod spodem są wektory). Wiem, że część osób, które przyzwyczaiły się do standardowych `for` (czyli zwykłej pętli) mają trudności z przełączeniem myślenia na sposób wektorowy. 
# 
# Jeśli również tak masz, to zatrzymaj się na chwilę i spróbuj się przestawić. Zamiast operować pojedynczymi wartościami, operujesz wektorami: `df['height'] / df['weight']` , gdzie `height` jest wektorem (lub `Series` w terminologii pandas) i `weight` również jest wektorem, a wynik działania również jest wektorem :).
# 
# ## Filtrowanie
# Kolejna operacja, która jest bardzo potrzebna, to filtrowanie. Załóżmy, że chcemy zostawić w tabelce ludzi, którzy mają mniej niż 145 cm lub więcej niż 195 cm.

# In[26]:


df[ (df.height < 145) | (df.height > 195) ]


# Zwróć uwagę na składnię.
# 
# Po pierwsze, jeśli jest więcej niż jeden filtr, należy pojedyncze wyrażenia trzymać w nawiasach (to jest konieczne).
# 
# Po drugie pomiędzy wyrażeniami logicznymi jest operator, w tym przypadku "lub" czyli pionowa kreska (ang. pipe) "|". 
# Również może być operator "i", wtedy należy użyć [ampersandy/etki](https://bit.ly/3rx5brO) "&".
# 
# Po trzecie, wyrażeń logicznych może być więcej niż jedno, ale powyżej trzech trudno jest to czytać i łatwo popełnić błąd.

# ## Usuwanie kolumn
# Czasem chcemy usunąć kolumnę i możemy zrobić to na wiele sposobów, jednak najlepszy jest jeden - użyć słowa kluczowego **`del`**. 
# 
# Jeśli natomiast odpalisz komórkę z usuwaniem dwa lub więcej razy, to pojawi się wyjątek `KeyError`. Dzieje się tak dlatego, że kolumna została już usunięta i trudno jest usunąć ją jeszcze raz (bo nie istnieje). 
# 
# Dlatego warto dodawać trochę więcej kodu, który najpierw sprawdzi, czy kolumna istnieje i jeśli tak, to usuwa ją. Dlaczego tak? Dlatego, że chcemy odpalać komórkę wiele razy i spodziewać się, że wynik za każdym razem będzie ten sam. Jeśli tego jeszcze teraz nie rozumiesz, to uwierz mi, że chcesz, aby taki był wynik :).

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




