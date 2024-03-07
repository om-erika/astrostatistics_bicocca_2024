# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:38:07 2024

@author: hp
"""

import numpy as np

# =============================================================================
# FUNZIONE PER CREARE IN SEQUENZA: UN ARRAY DI N PORTE, L'INDICE CORRISPONDENTE
# AL PREMIO E GLI INDICI CORRISPONDENTI ALLE PORTE VUOTE. L'ESPLICITARE IL NUMERO
# DI PORTE MI PERMETTE DI USARE LA STESSA FUNZIONE SIA PER LA CREAZIONE DELLE PORTE
# E LA SCELTA DEL PRIMO CONCORRENTE, SIA LA SCELTA DELL'ULTIMO ARRIVATO CHE NON
# HA FUNZIONI A PRIORI
# =============================================================================
def select_door(N):
    x = np.random.rand(1,1)
    if N == 3:
        
        if x <= 0.33:
            selected_door = [1,0,0]
            index_door = 0
            wrong_doors = [1,2]
        elif x > 0.33 : 
            if x <=0.66:
                selected_door = [0,1,0]
                index_door = 1
                wrong_doors = [0,2]
            else:
                selected_door = [0,0,1]
                index_door = 2
                wrong_doors = [0,1]
        return selected_door, index_door, wrong_doors
    if N == 2:
        if x <= 0.5:
            return [1,0]
        else:
            return [0,1]

# =============================================================================
# FUNZIONE PER APRIRE UNA PORTA TRA QUELLE VUOTE. IN QUESTA FUNZIONE, DEVO
# TENERE CONTO SIA DEL FATTO CHE IL PRESENTATORE NON APRA LA PORTA CON IL
# PREMIO, SIA CHE NON APRA LA PORTA SCELTA DAL GIOCATORE - SE QUEST'ULTIMO
# HA SCELTO UNA PORTA VUOTA
# =============================================================================
def open_door(doors, choice_num, choice, i):
   x = np.random.rand(1,1)
   
# =============================================================================
# In questa prima serie di if, gestisco il caso in cui il giocatore sceglie
# una delle porte vuote. In questo caso, so già che il presentatore dovrà aprire
# l'altra porta vuota, quindi sfrutto gli indici delle porte vuote per eliminare
# subito la seconda porta.
# =============================================================================
   #caso in cui il giocatore ha scelto la prima porta vuota. Elimino la seconda 
   if choice_num == i[0]:   
       del doors[i[1]], choice[i[1]]
       return doors
   if choice_num == i[1]:
       
       del doors[i[0]], choice[i[0]]
       return doors
   
   #caso in cui il giocatore ha scelto la seconda porta vuota. Elimino la prima 
   if x <= 0.5:
       del doors[i[0]], choice[i[0]]
       return doors
   else:
       del doors[i[1]], choice[i[1]]
       return doors


n = 0
N_rip = 5000
count_c, count_s, count_u = 0, 0, 0 #variabili per tenere i conteggi delle vittorie
#per fare N_rip ripetizioni, faccio un ciclo while su n
while n < N_rip:        
    #salvo l'array delle porte, l'indice del premio e gli indici delle porte vuote
    #per il presentatore e per il giocatore
    porte, index_prize, index_loss = list(select_door(3))
    porte_player, index_player, _ = list(select_door(3))
    #scelgo una delle porte vuote e la apro, eliminandola di fatto
    #da entrambe le liste delle porte del presentatore e del giocatore
    porte = open_door(porte, index_player, porte_player, index_loss)
    
# =============================================================================
# NOTA: DEVO TENER CONTO DELL'ELIMINAZIONE DI UN ELEMENTO DALLE LISTE DELLE
# PORTE NEL CALCOLO DELL'INDICE A CUI SI TROVA IL PREMIO. LO RICALCOLO TRAMITE
# LA NUOVA LISTA DELLE PORTE DEL PRESENTATORE 
# =============================================================================
    if porte[0] == 1:
        index_prize = 0
    else:
        index_prize = 1
    
    #creo il secondo giocatore, che non ha l'informazione a priori
    #a differenza del primo
    last_player = list(select_door(2))
    
    #tengo il conto di chi ha scelto la porta giusta. Visto che se il giocatore
    #conservativo vince, il giocatore che switcha perde e viceversa, non ho
    #bisogno di creare un array per il secondo ma utilizzo sempre il primo.
    if porte_player[index_prize] == 1:
        count_c = count_c + 1
    if porte_player[index_prize] == 0:
        count_s = count_s + 1
    if last_player[index_prize] == 1:
        count_u = count_u + 1
    n = n+1

#Stampa dei risultati (numero di vittorie)
print('Il conservatore ha vinto: '+ str(count_c) +' volte')
print('Lo switcher ha vinto: '+ str(count_s) +' volte')
print('L\'ultimo arrivato ha vinto: ', str(count_u) + ' volte')
#Stampa dei risultati (probabilità di vittoria)
print('Il conservatore ha probabilità di vincere pari a: '+ str(count_c/N_rip))
print('Lo switcher ha probabilità di vincere pari a: '+ str(count_s/N_rip))
print('L\'ultimo arrivato ha probabilità di vincere pari a: ', str(count_u/N_rip))