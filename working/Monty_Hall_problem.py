# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:38:07 2024

@author: hp
"""

import numpy as np
# =============================================================================
# funzione per selezionare la posizione della porta con il premio:
# tramite random la possibilità che esca una porta invece che l'altra è la stessa
# =============================================================================
def select_door():
    x = np.random.rand(1,1)
    
    if x <= 0.33:
        selected_door = [1,0,0]
    elif x > 0.33 : 
        if x <=0.66:
            selected_door = [0,1,0]
        else:
            selected_door = [0,0,1]
    return selected_door

# =============================================================================
# Funzione per aprire una porta tra quelle vuote in maniera random
# in questo caso, devo tener conto sia del fatto che il presentatore
# scelga una porta vuota, sia che non scelga quella vuota che il giocatore
# potrebbe aver preso
# =============================================================================
def open_door(doors, choice_num, choice):
   x = np.random.rand(1,1)
   
   i = []
   k = 0
   for door in doors:
       if door == 0:
           i.append(k)
       k = k + 1
       
   #questi due mi fanno evitare che non elimini la porta vuota scelta dal giocatore
   #in questo caso, so già che la porta aperta sarà l'altra vuota quindi
   #sostituisco subito e returno l'array
   if choice_num == i[0]:      
       doors[i[1]] = 5
       choice[i[1]] = 5
       return doors
   if choice_num == i[1]:
       
       doors[i[0]] = 5
       choice[i[0]] = 5
       return doors
   
   #seleziono in maniera random quale porta di quelle vuote viene aperta
   if x <= 0.5:
       doors[i[0]] = 5
       choice[i[0]] = 5
       return doors
   else:
       doors[i[1]] = 5
       choice[i[1]] = 5
       return doors

# =============================================================================
# funzione per salvare l'indice della porta aperta
# =============================================================================
def door_opened(doors):
    i = 0
    for door in doors:
        if door == 5:
            return i
        i = i+1

# =============================================================================
# funzione per salvare gli indici delle porte non aperte
# =============================================================================
def door_not_opened(doors):
    i = 0
    k = []
    for door in doors:
        if door != 5:
            k.append(i)
        i = i+1    
    return k
      
# =============================================================================
# Funzione per far scegliere a una persona una porta a caso
# tra le due porte ancora chiuse
# =============================================================================
def ultimo_arrivato(porta_aperta):
    x = np.random.rand(1,1)
    
    if porta_aperta == 0:
        if x <= 0.5:
            return [5,1,0]
        else:
            return[5,0,1]
    if porta_aperta == 1:
        if x <= 0.5:
            return [1,5,0]
        else:
            return[0,5,1]
    if porta_aperta == 2:
         if x <= 0.5:
             return [1,0,5]
         else:
             return[0,1,5]    

#funzione per salvare indice della porta con il premio
def door_prize(doors):
    i = 0
    for door in doors:
        if door == 1:
            return i
        i = i+1

n = 0 #variabile per ciclo for 

#variabili per contenere il numero di vittorie
count_c = 0 #conservatore
count_s = 0 #switcher
count_u = 0 #ultimo arrivato

#numero di cicli:5000
N = 5000
while n < N:
    porte = select_door()  #creazione delle porte, dove 1 indica la porta con il premio
        
    giocatore = np.random.randint(0,3) #scelta randomica da parte del giocatore
    #creazione dell'array delle porte del giocatore, dove 1 indica la porta scelta
    giocatore_array = np.zeros(3) 
    giocatore_array[giocatore] = 1 
    
    #apertura di una porta, che viene segnalata con il numero 5
    doors = open_door(porte, giocatore, giocatore_array)
    porta_aperta = door_opened(doors) #salvataggio indice porta aperta
    porte_chiuse = door_not_opened(doors) #salvataggio indici porte ancora chiuse
    porta_con_premio = door_prize(doors) #salvataggio indice porta premio
    
    #creazione del giocatore conservativo
    conservatore = giocatore_array.copy()
    #creazione del giocatore che switcha le porte
    giocatore_array[porte_chiuse[0]], giocatore_array[porte_chiuse[1]] = giocatore_array[porte_chiuse[1]], giocatore_array[porte_chiuse[0]]
    switcher = giocatore_array
    #creazione dell'ultimo arrivato
    ultimo = ultimo_arrivato(porta_aperta)
    
    #aggiunta eventuali vittorie nei 3 conteggi    
    if conservatore[porta_con_premio] == 1:
        count_c = count_c+1
    if switcher[porta_con_premio] == 1:
        count_s = count_s+1
    if ultimo[porta_con_premio] == 1:
        count_u = count_u+1
    n = n+1


print('Il conservatore ha vinto: '+ str(count_c) +' volte')
print('Lo switcher ha vinto: '+ str(count_s) +' volte')
print('L\'ultimo arrivato ha vinto: ', str(count_u) + ' volte')

print('Il conservatore ha probabilità di vincere pari a: '+ str(count_c/N))
print('Lo switcher ha probabilità di vincere pari a: '+ str(count_s/N))
print('L\'ultimo arrivato ha probabilità di vincere pari a: ', str(count_u/N))

