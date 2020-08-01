#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Librerias usadas en este documento
import pandas as pd


# In[2]:


#################################################################################################################
######################################## JJOO ###################################################################
#################################################################################################################


# In[3]:


#Olimpiadas 1912
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1912AT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1912'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-100-metres_results56971.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1912AT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-long-jump_results56982.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1912AT)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-shot-put_results56983.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1912AT)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-high-jump_results56984.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1912AT)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-400-metres_results56985.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1912AT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-110-metre-hurdles_results56993.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1912AT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-discus-throw_results56992.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1912AT)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-pole-vault_results57000.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1912AT)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-javelin-throw_results57001.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1912AT)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1912/olympics_summer_1912_ATH_mens-decathlon-1500-metres_results57002.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1912AT)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
########################################################################################
#Unir cada dataframe de cada prueba
ddbb = pd.merge(pFinal, p100, on='Athlete')
ddbb = pd.merge(ddbb, plj, on='Athlete')
ddbb = pd.merge(ddbb, pst, on='Athlete')
ddbb = pd.merge(ddbb, phj, on='Athlete')
ddbb = pd.merge(ddbb, p400, on='Athlete')
ddbb = pd.merge(ddbb, p110h, on='Athlete')
ddbb = pd.merge(ddbb, pdt, on='Athlete')
ddbb = pd.merge(ddbb, ppv, on='Athlete')
ddbb = pd.merge(ddbb, pjt, on='Athlete')
ddbb = pd.merge(ddbb, p1500, on='Athlete')


# In[4]:


#Olimpiadas 1920
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1912BT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1920'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-100-metres_results57229.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1912BT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-long-jump_results57238.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1912BT)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-shot-put_results57239.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1912BT)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-high-jump_results57240.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1912BT)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-400-metres_results57241.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1912BT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-110-metre-hurdles_results57249.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1912BT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-discus-throw_results57256.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1912BT)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-pole-vault_results57257.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1912BT)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-javelin-throw_results57258.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1912BT)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1920/olympics_summer_1920_ATH_mens-decathlon-1500-metres_results57259.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1912BT)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1920 = pd.merge(pFinal, p100, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, plj, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, pst, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, phj, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, p400, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, p110h, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, pdt, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, ppv, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, pjt, on='Athlete')
ddbb1920 = pd.merge(ddbb1920, p1500, on='Athlete')


# In[5]:


#Olimpiadas 1924
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1912BT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1924'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']

########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-100-metres_results57516.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1912BT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-long-jump_results57529.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1912BT)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-shot-put_results57530.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1912BT)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-high-jump_results57531.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1912BT)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-400-metres_results57532.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1912BT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-110-metre-hurdles_results57545.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1912BT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-discus-throw_results57554.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1912BT)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-pole-vault_results57555.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1912BT)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-javelin-throw_results57556.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1912BT)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1924/olympics_summer_1924_ATH_mens-decathlon-1500-metres_results57557.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1912BT)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1924 = pd.merge(pFinal, p100, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, plj, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, pst, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, phj, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, p400, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, p110h, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, pdt, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, ppv, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, pjt, on='Athlete')
ddbb1924 = pd.merge(ddbb1924, p1500, on='Athlete')


# In[6]:


#Olimpiadas 1928
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1912BT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1928'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']

########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-100-metres_results57844.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1912BT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-long-jump_results57858.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1912BT)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-shot-put_results57859.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1912BT)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-high-jump_results57860.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1912BT)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-400-metres_results57861.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1912BT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-110-metre-hurdles_results57862.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1912BT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-discus-throw_results57863.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1912BT)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-pole-vault_results57864.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1912BT)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-javelin-throw_results57865.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1912BT)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1928/olympics_summer_1928_ATH_mens-decathlon-1500-metres_results57866.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1912BT)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1928 = pd.merge(pFinal, p100, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, plj, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, pst, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, phj, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, p400, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, p110h, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, pdt, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, ppv, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, pjt, on='Athlete')
ddbb1928 = pd.merge(ddbb1928, p1500, on='Athlete')


# In[7]:


#Olimpiadas 1932
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1912BT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1932'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']

########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-100-metres_results58081.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1912BT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-long-jump_results58087.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1912BT)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-shot-put_results58088.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1912BT)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-high-jump_results58089.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1912BT)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-400-metres_results58090.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1912BT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-110-metre-hurdles_results58091.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1912BT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-discus-throw_results58097.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1912BT)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-pole-vault_results58098.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1912BT)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-javelin-throw_results58099.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1912BT)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1932/olympics_summer_1932_ATH_mens-decathlon-1500-metres_results58100.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1912BT)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1932 = pd.merge(pFinal, p100, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, plj, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, pst, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, phj, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, p400, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, p110h, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, pdt, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, ppv, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, pjt, on='Athlete')
ddbb1932 = pd.merge(ddbb1932, p1500, on='Athlete')


# In[8]:


#Olimpiadas 1936
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1934T)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1936'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']

########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-100-metres_results58377.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1934T)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-long-jump_results58388.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1934T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-shot-put_results58392.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1934T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-high-jump_results58396.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1934T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-400-metres_results58397.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1934T)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-110-metre-hurdles_results58403.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1934T)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-discus-throw_results58412.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1934T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-pole-vault_results58416.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1934T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-javelin-throw_results58417.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1934T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1936/olympics_summer_1936_ATH_mens-decathlon-1500-metres_results58418.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1934T)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1936 = pd.merge(pFinal, p100, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, plj, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, pst, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, phj, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, p400, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, p110h, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, pdt, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, ppv, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, pjt, on='Athlete')
ddbb1936 = pd.merge(ddbb1936, p1500, on='Athlete')


# In[9]:


#Olimpiadas 1948
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1934T)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1948'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']

########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-100-metres_results58716.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1934T)']
#del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-long-jump_results58726.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1934T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-shot-put_results58727.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1934T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-high-jump_results58728.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1934T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-400-metres_results58729.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1934T)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-110-metre-hurdles_results58739.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1934T)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-discus-throw_results58749.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1934T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-pole-vault_results58750.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1934T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-javelin-throw_results58751.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1934T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1948/olympics_summer_1948_ATH_mens-decathlon-1500-metres_results58752.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1934T)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1948 = pd.merge(pFinal, p100, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, plj, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, pst, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, phj, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, p400, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, p110h, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, pdt, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, ppv, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, pjt, on='Athlete')
ddbb1948 = pd.merge(ddbb1948, p1500, on='Athlete')


# In[10]:


#Olimpiadas 1952
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1952T)']
del pFinal['P(1985HT)']
del pFinal['Unnamed: 9']
del pFinal['Medal']

pFinal['Year'] = '1952'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-100-metres_results59090.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['T(A)']
del p100['P(1952T)']
del p100['P(1985HT)']
del p100['Unnamed: 10']

p100.columns = ['Athlete', '100m', '100m Points']
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-long-jump_results59100.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1952T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
#plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-shot-put_results59101.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1952T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-high-jump_results59102.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1952T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-400-metres_results59103.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1952T)']
del p400['P(1985HT)']
del p400['Unnamed: 10']
del p400['T(H)']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-110-metre-hurdles_results59112.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1952T)']
del p110h['Unnamed: 9']
del p110h['T(H)']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-discus-throw_results59121.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1952T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-pole-vault_results59122.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1952T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-javelin-throw_results59123.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1952T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1952/olympics_summer_1952_ATH_mens-decathlon-1500-metres_results59124.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1952T)']
del p1500['P(1985HT)']
del p1500['Unnamed: 10']
del p1500['T(H)']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1952 = pd.merge(pFinal, p100, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, plj, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, pst, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, phj, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, p400, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, p110h, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, pdt, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, ppv, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, pjt, on='Athlete')
ddbb1952 = pd.merge(ddbb1952, p1500, on='Athlete')


# In[11]:


#Olimpiadas 1956
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1952HT)']
del pFinal['P(1985HT)']
del pFinal['Unnamed: 9']
del pFinal['Medal']

pFinal['Year'] = '1956'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-100-metres_results59476.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['T(A)']
del p100['P(1952HT)']
del p100['P(1985HT)']
del p100['Unnamed: 10']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-long-jump_results59483.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1952T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-shot-put_results59484.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1952T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-high-jump_results59485.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1952T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-400-metres_results59486.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1952HT)']
del p400['P(1985HT)']
del p400['Unnamed: 10']
del p400['T(H)']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-110-metre-hurdles_results59491.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1952HT)']
del p110h['P(1985HT)']
del p110h['Unnamed: 10']
del p110h['T(H)']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-discus-throw_results59497.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1952T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-pole-vault_results59498.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1952T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-javelin-throw_results59499.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1952T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1956/olympics_summer_1956_ATH_mens-decathlon-1500-metres_results59500.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1952HT)']
del p1500['Unnamed: 9']
del p1500['T(H)']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1956 = pd.merge(pFinal, p100, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, plj, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, pst, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, phj, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, p400, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, p110h, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, pdt, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, ppv, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, pjt, on='Athlete')
ddbb1956 = pd.merge(ddbb1956, p1500, on='Athlete')


# In[12]:


#Olimpiadas 1960
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1952HT)']
del pFinal['P(1985HT)']
del pFinal['Unnamed: 9']
del pFinal['Medal']

pFinal['Year'] = '1960'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-100-metres_results59907.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['T(A)']
del p100['P(1952HT)']
del p100['P(1985HT)']
del p100['Unnamed: 10']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-long-jump_results59916.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1952T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-shot-put_results59920.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1952T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-high-jump_results59924.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1952T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-400-metres_results59925.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1952T)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-110-metre-hurdles_results59926.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1952HT)']
del p110h['P(1985HT)']
del p110h['Unnamed: 10']
del p110h['T(H)']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-discus-throw_results59497.csv")
del pdt['Unnamed: 3']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-pole-vault_results59938.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1952T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-javelin-throw_results59939.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1952T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1960/olympics_summer_1960_ATH_mens-decathlon-1500-metres_results59943.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1952T)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1960 = pd.merge(pFinal, p100, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, plj, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, pst, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, phj, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, p400, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, p110h, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, pdt, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, ppv, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, pjt, on='Athlete')
ddbb1960 = pd.merge(ddbb1960, p1500, on='Athlete')


# In[13]:


#Olimpiadas 1964
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1962HT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1964'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-100-metres_results60319.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1962HT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-long-jump_results60326.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1962T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-shot-put_results60327.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1962T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-high-jump_results60328.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1962T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-400-metres_results60329.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1962HT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-110-metre-hurdles_results60336.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1962HT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-discus-throw_results60343.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1962T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-pole-vault_results60344.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1962T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-javelin-throw_results60345.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1962T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1964/olympics_summer_1964_ATH_mens-decathlon-1500-metres_results60346.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1962T)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1964 = pd.merge(pFinal, p100, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, plj, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, pst, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, phj, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, p400, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, p110h, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, pdt, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, ppv, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, pjt, on='Athlete')
ddbb1964 = pd.merge(ddbb1964, p1500, on='Athlete')


# In[14]:


#Olimpiadas 1968
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1962HT)']
del pFinal['P(1985HT)']
del pFinal['Unnamed: 9']
del pFinal['Medal']

pFinal['Year'] = '1968'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-100-metres_results60815.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['T(H)']
del p100['P(1962HT)']
del p100['P(1985HT)']
del p100['Unnamed: 10']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-long-jump_results60823.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1962T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-shot-put_results60824.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1962T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-high-jump_results60825.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1962T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-400-metres_results60826.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['T(H)']
del p400['P(1962HT)']
del p400['P(1985HT)']
del p400['Unnamed: 10']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-110-metre-hurdles_results60833.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['T(H)']
del p110h['P(1962HT)']
del p110h['P(1985HT)']


p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-discus-throw_results60839.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1962T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-pole-vault_results60840.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1962T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-javelin-throw_results60841.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1962T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1968/olympics_summer_1968_ATH_mens-decathlon-1500-metres_results60842.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1962T)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1968 = pd.merge(pFinal, p100, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, plj, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, pst, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, phj, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, p400, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, p110h, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, pdt, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, ppv, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, pjt, on='Athlete')
ddbb1968 = pd.merge(ddbb1968, p1500, on='Athlete')


# In[15]:


#Olimpiadas 1972
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1962HT)']
del pFinal['P(1971AT)']
del pFinal['Unnamed: 9']
del pFinal['Medal']

pFinal['Year'] = '1972'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-100-metres_results61312.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1971AT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-long-jump_results61318.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1962T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-shot-put_results61322.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1962T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-high-jump_results61326.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1962T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-400-metres_results61345.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['T(H)']
del p400['P(1962HT)']
del p400['P(1971AT)']
del p400['Unnamed: 10']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-110-metre-hurdles_results61351.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1971AT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-discus-throw_results61357.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1962T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-pole-vault_results61361.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1962T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-javelin-throw_results61380.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1962T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1972/olympics_summer_1972_ATH_mens-decathlon-1500-metres_results61384.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1962T)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1972 = pd.merge(pFinal, p100, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, plj, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, pst, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, phj, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, p400, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, p110h, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, pdt, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, ppv, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, pjt, on='Athlete')
ddbb1972 = pd.merge(ddbb1972, p1500, on='Athlete')


# In[16]:


#Olimpiadas 1976
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1977AT)']
del pFinal['P(1971AT)']
del pFinal['Unnamed: 9']
del pFinal['Medal']

pFinal['Year'] = '1976'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-100-metres_results61886.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1977AT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-long-jump_results61891.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1977T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-shot-put_results61895.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1977T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-high-jump_results61899.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1977T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-400-metres_results61915.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['T(H)']
del p400['P(1971HT)']
del p400['P(1977AT)']
del p400['Unnamed: 10']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-110-metre-hurdles_results61920.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1977AT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-discus-throw_results61925.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1977T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-pole-vault_results61929.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1977T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-javelin-throw_results61947.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1977T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1976/olympics_summer_1976_ATH_mens-decathlon-1500-metres_results61951.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1977AT)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1976 = pd.merge(pFinal, p100, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, plj, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, pst, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, phj, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, p400, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, p110h, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, pdt, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, ppv, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, pjt, on='Athlete')
ddbb1976 = pd.merge(ddbb1976, p1500, on='Athlete')


# In[17]:


#Olimpiadas 1980
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1977AT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1980'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-100-metres_results62433.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1977AT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-long-jump_results62437.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1977T)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-shot-put_results62438.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1977T)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-high-jump_results62439.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1977T)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-400-metres_results62440.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1977AT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-110-metre-hurdles_results62444.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1977AT)']
#del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-discus-throw_results62448.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1977T)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-pole-vault_results62449.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1977T)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-javelin-throw_results62450.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1977T)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1980/olympics_summer_1980_ATH_mens-decathlon-1500-metres_results62451.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1977T)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1980 = pd.merge(pFinal, p100, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, plj, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, pst, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, phj, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, p400, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, p110h, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, pdt, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, ppv, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, pjt, on='Athlete')
ddbb1980 = pd.merge(ddbb1980, p1500, on='Athlete')


# In[18]:


#Olimpiadas 1984
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['P(1977AT)']
del pFinal['Unnamed: 8']
del pFinal['Medal']

pFinal['Year'] = '1984'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-100-metres_results62948.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['P(1977AT)']
del p100['Unnamed: 8']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-long-jump_results62953.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['P(1977AT)']
del plj['Unnamed: 8']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-shot-put_results62957.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['P(1977AT)']
del pst['Unnamed: 8']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-high-jump_results62961.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['P(1977AT)']
del phj['Unnamed: 8']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-400-metres_results62977.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['P(1977AT)']
del p400['Unnamed: 8']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-110-metre-hurdles_results62982.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['P(1977AT)']
del p110h['Unnamed: 8']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-discus-throw_results62987.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['P(1977AT)']
del pdt['Unnamed: 8']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-pole-vault_results62991.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['P(1977AT)']
del ppv['Unnamed: 8']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-javelin-throw_results63017.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['P(1977AT)']
del pjt['Unnamed: 8']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1984/olympics_summer_1984_ATH_mens-decathlon-1500-metres_results63021.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['P(1977AT)']
del p1500['Unnamed: 8']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb1984 = pd.merge(pFinal, p100, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, plj, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, pst, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, phj, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, p400, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, p110h, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, pdt, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, ppv, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, pjt, on='Athlete')
ddbb1984 = pd.merge(ddbb1984, p1500, on='Athlete')


# In[19]:


#Olimpiadas 1988
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '1988'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-100-metres_results63591.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-long-jump_results63597.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-shot-put_results63601.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-high-jump_results63605.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-400-metres_results63627.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-110-metre-hurdles_results63633.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-discus-throw_results63639.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-pole-vault_results63643.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-javelin-throw_results63667.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1988/olympics_summer_1988_ATH_mens-decathlon-1500-metres_results63671.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500

########################################################################################
#Unir cada dataframe de cada prueba
ddbb1988 = pd.merge(pFinal, p100, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, plj, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, pst, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, phj, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, p400, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, p110h, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, pdt, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, ppv, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, pjt, on='Athlete')
ddbb1988 = pd.merge(ddbb1988, p1500, on='Athlete')


# In[20]:


#Olimpiadas 1992
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '1992'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-100-metres_results64273.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-long-jump_results64278.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-shot-put_results64282.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-high-jump_results64286.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-400-metres_results64305.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-110-metre-hurdles_results64311.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-discus-throw_results64316.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-pole-vault_results64320.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-javelin-throw_results64340.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1992/olympics_summer_1992_ATH_mens-decathlon-1500-metres_results64344.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500

########################################################################################
#Unir cada dataframe de cada prueba
ddbb1992 = pd.merge(pFinal, p100, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, plj, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, pst, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, phj, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, p400, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, p110h, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, pdt, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, ppv, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, pjt, on='Athlete')
ddbb1992 = pd.merge(ddbb1992, p1500, on='Athlete')


# In[21]:


#Olimpiadas 1996
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '1996'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-100-metres_results64952.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-long-jump_results64958.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-shot-put_results64962.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-high-jump_results64966.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-400-metres_results64982.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-110-metre-hurdles_results64988.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-discus-throw_results64993.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-pole-vault_results64997.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-javelin-throw_results65014.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-1996/olympics_summer_1996_ATH_mens-decathlon-1500-metres_results65018.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500

########################################################################################
#Unir cada dataframe de cada prueba
ddbb1996 = pd.merge(pFinal, p100, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, plj, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, pst, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, phj, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, p400, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, p110h, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, pdt, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, ppv, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, pjt, on='Athlete')
ddbb1996 = pd.merge(ddbb1996, p1500, on='Athlete')


# In[22]:


#Olimpiadas 2000
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '2000'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-100-metres_results65611.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-long-jump_results65617.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-shot-put_results65621.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-high-jump_results65625.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-400-metres_results65641.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-110-metre-hurdles_results65646.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-discus-throw_results65651.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-pole-vault_results65655.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-javelin-throw_results65668.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2000/olympics_summer_2000_ATH_mens-decathlon-1500-metres_results65672.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500

########################################################################################
#Unir cada dataframe de cada prueba
ddbb2000 = pd.merge(pFinal, p100, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, plj, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, pst, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, phj, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, p400, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, p110h, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, pdt, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, ppv, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, pjt, on='Athlete')
ddbb2000 = pd.merge(ddbb2000, p1500, on='Athlete')


# In[23]:


#Olimpiadas 2004
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '2004'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-100-metres_results66291.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-long-jump_results66297.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-shot-put_results66306.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-high-jump_results66315.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-400-metres_results66345.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-110-metre-hurdles_results66351.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-discus-throw_results66357.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-pole-vault_results66366.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-javelin-throw_results66391.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2004/olympics_summer_2004_ATH_mens-decathlon-1500-metres_results66400.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb2004 = pd.merge(pFinal, p100, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, plj, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, pst, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, phj, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, p400, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, p110h, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, pdt, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, ppv, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, pjt, on='Athlete')
ddbb2004 = pd.merge(ddbb2004, p1500, on='Athlete')


# In[24]:


#Olimpiadas 2008
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '2008'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-100-metres_results257424.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m', '100m Points']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-long-jump_results257430.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj', 'Lj Points']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-shot-put_results257439.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp', 'Sp Points']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-high-jump_results257448.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj', 'Hj Points']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-400-metres_results257479.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m', '400m Points']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-110-metre-hurdles_results257485.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H', '110m H Points']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-discus-throw_results257491.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt', 'Dt Points']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-pole-vault_results257500.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
#del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv', 'Pv Points']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-javelin-throw_results257533.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt', 'Jt Points']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2008/olympics_summer_2008_ATH_mens-decathlon-1500-metres_results257542.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m', '1500m Points']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb2008 = pd.merge(pFinal, p100, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, plj, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, pst, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, phj, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, p400, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, p110h, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, pdt, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, ppv, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, pjt, on='Athlete')
ddbb2008 = pd.merge(ddbb2008, p1500, on='Athlete')


# In[25]:


#Olimpiadas 2012
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '2012'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-100-metres_results302617.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m Points', '100m']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-long-jump_results302618.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj Points', 'Lj']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-shot-put_results302619.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp Points', 'Sp']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-high-jump_results302620.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj Points', 'Hj']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-400-metres_results302621.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m Points', '400m']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-110-metres-hurdles_results302622.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H Points', '110m H']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-discus-throw_results302623.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt Points', 'Dt']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-pole-vault_results302624.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv Points', 'Pv']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-javelin-throw_results302625.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt Points', 'Jt']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2012/olympics_summer_2012_ATH_mens-decathlon-1500-metres_results302626.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m Points', '1500m']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb2012 = pd.merge(pFinal, p100, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, plj, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, pst, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, phj, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, p400, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, p110h, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, pdt, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, ppv, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, pjt, on='Athlete')
ddbb2012 = pd.merge(ddbb2012, p1500, on='Athlete')
ddbb2012


# In[26]:


#Olimpiadas 2016
#Datos finales con el ranking y la puntuacion
pFinal=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon_final_standings.csv")
del pFinal['NOC']
del pFinal['Unnamed: 7']
del pFinal['Medal']

pFinal['Year'] = '2016'
pFinal['Competition'] = 'JJOO'

pFinal.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition']
pFinal
########################################################################################
#Datos para los 100m 
p100=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-100-metres_results358864.csv")
del p100['Rank']
del p100['Age']
del p100['Team']
del p100['NOC']
del p100['Unnamed: 7']

p100.columns = ['Athlete', '100m Points', '100m']
p100
########################################################################################
#Datos salto de longitud
plj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-long-jump_results358869.csv")
del plj['Rank']
del plj['Age']
del plj['Team']
del plj['NOC']
del plj['Unnamed: 7']

plj.columns = ['Athlete', 'Lj Points', 'Lj']
plj
########################################################################################
#Datos para lanzamiento de peso
pst=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-shot-put_results358880.csv")
del pst['Rank']
del pst['Age']
del pst['Team']
del pst['NOC']
del pst['Unnamed: 7']

pst.columns = ['Athlete', 'Sp Points', 'Sp']
pst
########################################################################################
#Datos salto de altura
phj=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-high-jump_results358891.csv")
del phj['Rank']
del phj['Age']
del phj['Team']
del phj['NOC']
del phj['Unnamed: 7']

phj.columns = ['Athlete', 'Hj Points', 'Hj']
phj
########################################################################################
#Datos de 400m
p400=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-400-metres_results358919.csv")
del p400['Rank']
del p400['Age']
del p400['Team']
del p400['NOC']
del p400['Unnamed: 7']

p400.columns = ['Athlete', '400m Points', '400m']
p400
########################################################################################
#Datos de 110m vayas
p110h=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-110-metres-hurdles_results358924.csv")
del p110h['Rank']
del p110h['Age']
del p110h['Team']
del p110h['NOC']
del p110h['Unnamed: 7']

p110h.columns = ['Athlete', '110m H Points', '110m H']
p110h
########################################################################################
#Datos de lanzamiento de disco
pdt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-discus-throw_results358929.csv")
del pdt['Rank']
del pdt['Age']
del pdt['Team']
del pdt['NOC']
del pdt['Unnamed: 7']

pdt.columns = ['Athlete', 'Dt Points', 'Dt']
pdt
########################################################################################
#Datos de pertiga
ppv=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-pole-vault_results358940.csv")
del ppv['Rank']
del ppv['Age']
del ppv['Team']
del ppv['NOC']
del ppv['Unnamed: 7']

ppv.columns = ['Athlete', 'Pv Points', 'Pv']
ppv
########################################################################################
#Datos de javalina
pjt=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-javelin-throw_results358964.csv")
del pjt['Rank']
del pjt['Age']
del pjt['Team']
del pjt['NOC']
del pjt['Unnamed: 7']

pjt.columns = ['Athlete', 'Jt Points', 'Jt']
pjt
########################################################################################
#Datos de 1500m
p1500=pd.read_csv("/Github/DecatlonEstadistics/resources/JJOO-2016/olympics_summer_2016_ATH_mens-decathlon-1500-metres_results358975.csv")
del p1500['Rank']
del p1500['Age']
del p1500['Team']
del p1500['NOC']
del p1500['Unnamed: 7']

p1500.columns = ['Athlete', '1500m Points', '1500m']
p1500
########################################################################################
#Unir cada dataframe de cada prueba
ddbb2016 = pd.merge(pFinal, p100, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, plj, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, pst, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, phj, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, p400, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, p110h, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, pdt, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, ppv, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, pjt, on='Athlete')
ddbb2016 = pd.merge(ddbb2016, p1500, on='Athlete')


# In[27]:


#################################################################################################################
######################################## Mundiales ##############################################################
#################################################################################################################


# In[28]:


#Mundiales 2019
#Datos finales con el ranking y la puntuacion
ddbbWC2019=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2019/WC-2019.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2019)): 
    year[i]= 2019
    competition = "WC"
    age = 0

ddbbWC2019.insert(4, "Year", year) 
ddbbWC2019.insert(5, "Competiton", competition) 
ddbbWC2019.insert(2, "Age", age)

ddbbWC2019.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


# In[29]:


#Mundiales 2017
#Datos finales con el ranking y la puntuacion
ddbbWC2017=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2017/WC-2017.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2017)): 
    year[i]= 2017
    competition = "WC"
    age = 0

ddbbWC2017.insert(4, "Year", year) 
ddbbWC2017.insert(5, "Competiton", competition) 
ddbbWC2017.insert(2, "Age", age)

ddbbWC2017.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m Points', 
                 '100m', 'Lj Points', 'Lj', 'Sp Points', 'Sp', 'Hj Points', 'Hj', '400m Points', '400m', 
                 '110m H Points', '110m H', 'Dt Points', 'Dt', 'Pv Points', 'Pv', 'Jt Points', 'Jt', 
                 '1500m Points', '1500m']


# In[30]:


#Mundiales 2015
#Datos finales con el ranking y la puntuacion
ddbbWC2015=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2015/WC-2015.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2015)): 
    year[i]= 2015
    competition = "WC"
    age = 0

ddbbWC2015.insert(4, "Year", year) 
ddbbWC2015.insert(5, "Competiton", competition) 
ddbbWC2015.insert(2, "Age", age)

ddbbWC2015.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m Points', 
                 '100m', 'Lj Points', 'Lj', 'Sp Points', 'Sp', 'Hj Points', 'Hj', '400m Points', '400m', 
                 '110m H Points', '110m H', 'Dt Points', 'Dt', 'Pv Points', 'Pv', 'Jt Points', 'Jt', 
                 '1500m Points', '1500m']


# In[31]:


#Mundiales 2013
#Datos finales con el ranking y la puntuacion
ddbbWC2013=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2013/WC-2013.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2013)): 
    year[i]= 2013
    competition = "WC"
    age = 0

ddbbWC2013.insert(4, "Year", year) 
ddbbWC2013.insert(5, "Competiton", competition) 
ddbbWC2013.insert(2, "Age", age)

ddbbWC2013.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m Points', 
                 '100m', 'Lj Points', 'Lj', 'Sp Points', 'Sp', 'Hj Points', 'Hj', '400m Points', '400m', 
                 '110m H Points', '110m H', 'Dt Points', 'Dt', 'Pv Points', 'Pv', 'Jt Points', 'Jt', 
                 '1500m Points', '1500m']


# In[32]:


#Mundiales 2011
#Datos finales con el ranking y la puntuacion
ddbbWC2011=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2011/WC-2011.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2011)): 
    year[i]= 2011
    competition = "WC"
    age = 0

ddbbWC2011.insert(4, "Year", year) 
ddbbWC2011.insert(5, "Competiton", competition) 
ddbbWC2011.insert(2, "Age", age)

ddbbWC2011.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


# In[33]:


#Mundiales 2009
#Datos finales con el ranking y la puntuacion
ddbbWC2009=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2009/WC-2009.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2009)): 
    year[i]= 2009
    competition = "WC"
    age = 0

ddbbWC2009.insert(4, "Year", year) 
ddbbWC2009.insert(5, "Competiton", competition) 
ddbbWC2009.insert(2, "Age", age)

ddbbWC2009.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


# In[34]:


#Mundiales 2007
#Datos finales con el ranking y la puntuacion
ddbbWC2007=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2007/WC-2007.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2007)): 
    year[i]= 2007
    competition = "WC"
    age = 0

ddbbWC2007.insert(4, "Year", year) 
ddbbWC2007.insert(5, "Competiton", competition) 
ddbbWC2007.insert(2, "Age", age)

ddbbWC2007.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m Points', 
                 '100m', 'Lj Points', 'Lj', 'Sp Points', 'Sp', 'Hj Points', 'Hj', '400m Points', '400m', 
                 '110m H Points', '110m H', 'Dt Points', 'Dt', 'Pv Points', 'Pv', 'Jt Points', 'Jt', 
                 '1500m Points', '1500m']

#Borra las filas vacias que use en el excel
ddbbWC2007.dropna(subset = ["Position"], inplace=True)


# In[35]:


#Mundiales 2005
#Datos finales con el ranking y la puntuacion
ddbbWC2005=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2005/WC-2005.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2005)): 
    year[i]= 2005
    competition = "WC"
    age = 0

ddbbWC2005.insert(4, "Year", year) 
ddbbWC2005.insert(5, "Competiton", competition) 
ddbbWC2005.insert(2, "Age", age)

ddbbWC2005.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']

#Borra las filas vacias que use en el excel
ddbbWC2005.dropna(subset = ["Position"], inplace=True)


# In[36]:


#Mundiales 2003
#Datos finales con el ranking y la puntuacion
ddbbWC2003=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2003/WC-2003.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2003)): 
    year[i]= 2003
    competition = "WC"
    age = 0

ddbbWC2003.insert(4, "Year", year) 
ddbbWC2003.insert(5, "Competiton", competition) 
ddbbWC2003.insert(2, "Age", age)

ddbbWC2003.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC2003.dropna(subset = ["Position"], inplace=True)


# In[37]:


#Mundiales 2001
#Datos finales con el ranking y la puntuacion
ddbbWC2001=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-2001/WC-2001.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC2001)): 
    year[i]= 2001
    competition = "WC"
    age = 0

ddbbWC2001.insert(4, "Year", year) 
ddbbWC2001.insert(5, "Competiton", competition) 
ddbbWC2001.insert(2, "Age", age)

ddbbWC2001.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC2001.dropna(subset = ["Position"], inplace=True)


# In[38]:


#Mundiales 1999
#Datos finales con el ranking y la puntuacion
ddbbWC1999=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-1999/WC-1999.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC1999)): 
    year[i]= 1999
    competition = "WC"
    age = 0

ddbbWC1999.insert(4, "Year", year) 
ddbbWC1999.insert(5, "Competiton", competition) 
ddbbWC1999.insert(2, "Age", age)

ddbbWC1999.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC1999.dropna(subset = ["Position"], inplace=True)


# In[39]:


#Mundiales 1997
#Datos finales con el ranking y la puntuacion
ddbbWC1997=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-1997/WC-1997.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC1997)): 
    year[i]= 1997
    competition = "WC"
    age = 0

ddbbWC1997.insert(4, "Year", year) 
ddbbWC1997.insert(5, "Competiton", competition) 
ddbbWC1997.insert(2, "Age", age)

ddbbWC1997.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC1997.dropna(subset = ["Position"], inplace=True)


# In[40]:


#Mundiales 1995
#Datos finales con el ranking y la puntuacion
ddbbWC1995=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-1995/WC-1995.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC1995)): 
    year[i]= 1995
    competition = "WC"
    age = 0

ddbbWC1995.insert(4, "Year", year) 
ddbbWC1995.insert(5, "Competiton", competition) 
ddbbWC1995.insert(2, "Age", age)

ddbbWC1995.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC1995.dropna(subset = ["Position"], inplace=True)


# In[41]:


#Mundiales 1993
#Datos finales con el ranking y la puntuacion
ddbbWC1993=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-1993/WC-1993.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC1993)): 
    year[i]= 1993
    competition = "WC"
    age = 0

ddbbWC1993.insert(4, "Year", year) 
ddbbWC1993.insert(5, "Competiton", competition) 
ddbbWC1993.insert(2, "Age", age)

ddbbWC1993.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC1993.dropna(subset = ["Position"], inplace=True)


# In[42]:


#Mundiales 1991
#Datos finales con el ranking y la puntuacion
ddbbWC1991=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-1991/WC-1991.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC1991)): 
    year[i]= 1991
    competition = "WC"
    age = 0

ddbbWC1991.insert(4, "Year", year) 
ddbbWC1991.insert(5, "Competiton", competition) 
ddbbWC1991.insert(2, "Age", age)

del ddbbWC1991['Pos']#Borra una columna repetida dentro del excel

ddbbWC1991.columns = ['Position', 'Age', 'Athlete', 'Country', 'Year', 'Competition', 'Total Points', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC1991.dropna(subset = ["Position"], inplace=True)


# In[43]:


#Mundiales 1987
#Datos finales con el ranking y la puntuacion
ddbbWC1987=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-1987/WC-1987.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC1987)): 
    year[i]= 1987
    competition = "WC"
    age = 0

ddbbWC1987.insert(4, "Year", year) 
ddbbWC1987.insert(5, "Competiton", competition) 
ddbbWC1987.insert(2, "Age", age)

ddbbWC1987.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC1987.dropna(subset = ["Position"], inplace=True)


# In[44]:


#Mundiales 1983
#Datos finales con el ranking y la puntuacion
ddbbWC1983=pd.read_excel("/Github/DecatlonEstadistics/resources/WC-1983/WC-1983.xlsx")

year = pd.Series([]) 
competition = pd.Series([])
age = pd.Series([])

for i in range(len(ddbbWC1983)): 
    year[i]= 1983
    competition = "WC"
    age = 0

ddbbWC1983.insert(4, "Year", year) 
ddbbWC1983.insert(5, "Competiton", competition) 
ddbbWC1983.insert(2, "Age", age)

ddbbWC1983.columns = ['Position', 'Athlete', 'Age', 'Country', 'Total Points', 'Year', 'Competition', '100m', 
                 '100m Points', 'Lj', 'Lj Points', 'Sp', 'Sp Points', 'Hj', 'Hj Points', '400m', '400m Points', 
                 '110m H', '110m H Points', 'Dt', 'Dt Points', 'Pv', 'Pv Points', 'Jt', 'Jt Points', 
                 '1500m', '1500m Points']


#Borra las filas vacias que use en el excel
ddbbWC1983.dropna(subset = ["Position"], inplace=True)


# In[47]:


#Concatenar diferentes dataframes
pFinal  = pd.concat([ddbb,ddbb1924,ddbb1928,ddbb1932,ddbb1936,ddbb1948,ddbb1952,ddbb1956,ddbb1960,ddbb1964,
                     ddbb1968,ddbb1972,ddbb1976,ddbb1980,ddbb1984,ddbb1988,ddbb1992,ddbb1996,ddbb2000,ddbb2004,
                     ddbb2008,ddbb2012,ddbb2016,ddbbWC2019,ddbbWC2017,ddbbWC2015,ddbbWC2013,ddbbWC2011,ddbbWC2009,
                     ddbbWC2007,ddbbWC2005,ddbbWC2003,ddbbWC2001,ddbbWC1999,ddbbWC1997,ddbbWC1995,ddbbWC1993,
                     ddbbWC1991,ddbbWC1987,ddbbWC1983])

#Create an excel with all the previous data
#pFinal.to_excel (r'/Github/DecatlonEstadistics/data.xlsx', index = False, header=True)


# In[46]:


def devuelveDataFframe():
       dataFrame = pFinal
       return dataFrame

