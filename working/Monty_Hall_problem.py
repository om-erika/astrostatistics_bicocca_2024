# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:38:07 2024

@author: hp
"""

import numpy as np

# =============================================================================
# FUNZIONE PER CREARE IN SEQUENZA: UN ARRAY DI N PORTE, L'INDICE CORRISPONDENTE
# AL PREMIO (O ALLA PORTA SCELTA) E GLI INDICI CORRISPONDENTI ALLE PORTE VUOTE. 
# L'ESPLICITARE IL NUMERO DI PORTE MI PERMETTE DI USARE LA STESSA FUNZIONE
# PER I DIVERSI CASI
# =============================================================================
def select_door(N):
    x = np.random.randint(0,N)
    selected_door = np.zeros(N)
    selected_door[x] = 1
    i = 0
    wrong_doors = []
    #Ciclo while per salvare gli indici delle porte vuote
    while i < N:
        if i != x:
            wrong_doors.append(i)
        i = i+1
    return list(selected_door), x, list(wrong_doors)

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
   #caso in cui il giocatore ha scelto la seconda porta vuota. Elimino la prima 
   if choice_num == i[1]:
       
       del doors[i[0]], choice[i[0]]
       return doors
   
   #caso in cui il giocatore ha scelto la porta con il premio. 
   #in questo caso, devo eliminare randomicamente una delle due porte vuote
   if x <= 0.5:
       del doors[i[0]], choice[i[0]]
       return doors
   else:
       del doors[i[1]], choice[i[1]]
       return doors

N_rip = 5000
numero_porte = [3, 100] #per fare il caso con 3 o 100 porte iniziali
for n_porte in numero_porte:
    #per ogni numero di porte iniziali i dati di partenza devono essere a 0
    n = 0   
    count_c, count_s, count_u = 0, 0, 0
    while n < N_rip:        
        #salvo l'array delle porte, l'indice del premio e gli indici delle porte vuote
        #per il presentatore e per il giocatore
        porte, index_prize, index_loss = select_door(n_porte)
        porte_player, index_player, _ = select_door(n_porte)

# =============================================================================
# scelgo una delle porte vuote e la apro, eliminandola di fatto
# da entrambe le liste delle porte del presentatore e del giocatore
# ripeto ciò finché non rimango con 2 porte. 
# =============================================================================
# NOTA: DEVO TENER CONTO OGNI VOLTA DELL'ELIMINAZIONE DI UN ELEMENTO DALLE LISTE
# PERCHÉ POTREBBE SPOSTARE L'INDICE DEL PREMIO. PER QUESTO, RICALCOLO LA POSIZIONE
# DEL PREMIO TRAMITE LA NUOVA LISTA DELLE PORTE DEL PRESENTATORE 
# =============================================================================
        i = 0
        while i < n_porte-2:
            k = 0
            porte = open_door(porte, index_player, porte_player, index_loss)
            while k < n_porte-1-i:
                if porte[k] == 1:
                    index_prize = k
                k = k+1
            i = i+1
        
        #creo il secondo giocatore, che non ha l'informazione a priori
        #a differenza del primo
        last_player = select_door(2)[0]
        
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
    if n_porte == 3:
        print('CASO CON 3 PORTE:')
    else:
        print('\nCASO CON 100 PORTE:')
    print('Il conservatore ha vinto: '+ str(count_c) +' volte')
    print('Lo switcher ha vinto: '+ str(count_s) +' volte')
    print('L\'ultimo arrivato ha vinto: ', str(count_u) + ' volte')
    #Stampa dei risultati (probabilità di vittoria)
    print('Il conservatore ha probabilità di vincere pari a: '+ str(count_c/N_rip))
    print('Lo switcher ha probabilità di vincere pari a: '+ str(count_s/N_rip))
    print('L\'ultimo arrivato ha probabilità di vincere pari a: ', str(count_u/N_rip))