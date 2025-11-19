import numpy as np

G = np.array([
    [0,6,0,0,0,0,2,0,5],\
    [4,0,0,9,2,1,0,0,0],\
    [0,7,0,0,0,8,0,0,1],\
    [0,0,0,0,0,5,0,0,9],\
    [6,4,0,0,0,0,0,7,3],\
    [1,0,0,4,0,0,0,0,0],\
    [3,0,0,7,0,0,0,6,0],\
    [0,0,0,1,4,6,0,0,2],\
    [2,0,6,0,0,0,0,1,0]])

M = np.array([\
    [2,0,0,0,9,0,3,0,0],\
    [0,1,9,0,8,0,0,7,4],\
    [0,0,8,4,0,0,6,2,0],\
    [5,9,0,6,2,1,0,0,0],\
    [0,2,7,0,0,0,1,6,0],\
    [0,0,0,5,7,4,0,9,3],\
    [0,8,5,0,0,9,7,0,0],\
    [9,3,0,0,5,0,8,4,0],\
    [0,0,2,0,6,0,0,0,1]])

G2 = np.array([\
    [0,3,0,0,0,8,0,0,0],\
    [9,0,0,2,0,3,0,0,1],\
    [4,0,1,0,0,9,6,0,0],\
    [0,5,0,0,0,0,4,3,0],\
    [0,0,0,0,0,0,0,0,0],\
    [0,6,9,0,0,0,0,2,0],\
    [0,0,8,6,0,0,7,0,2],\
    [2,0,0,9,0,4,0,0,8],\
    [0,0,0,7,0,0,0,1,0]])

def carre(G, i, j):
    icoin = 3*(i//3)
    jcoin = 3*(j//3)
    chiffre = set()
    for u in range(icoin, icoin+3):
        for v in range(jcoin, jcoin+3):
            if G[u,v]!=0:
                chiffre.add(G[u,v])
    return chiffre
#print(carre(G,4,5))

def ligne(G, i):
    chiffre = set()
    for u in range(9):
        if G[i,u] != 0:
            chiffre.add(G[i,u])
    return chiffre
#print(ligne(G,0))

def colonne(G, j):
    chiffre = set()
    for u in range(9):
        if G[u,j] != 0:
            chiffre.add(G[u,j])
    return chiffre
#print(colonne(G,0))

def ligne_complete(G, i):
    for u in range(9):
        if G[i,u] == 0:
            return False
    return True
#print(ligne_complete(G,0))

def colonne_complete(G, j):
    for u in range(9):
        if G[u,j] == 0:
            return False
    return True
#print(colonne_complete(G,0))

def carre_complet(G, i, j):
    icoin = 3*(i//3)
    jcoin = 3*(j//3)
    for u in range(icoin, icoin+3):
        for v in range(jcoin, jcoin+3):
            if G[u,v] == 0:
                return False
    return True
#print(carre_complet(G,0,0))

def finie(G):
    for i in range(9):
        for j in range(9):
            if G[i,j] == 0:
                return False
    return True
#print(finie(G))

def nb_possibles(G, i, j):
    chiffres_utilises = ligne(G, i).union(colonne(G, j)).union(carre(G, i, j))
    return set(range(1, 10)) - chiffres_utilises, chiffres_utilises

def eliminer_possibles(G, i, j):
    possibles, _ = nb_possibles(G, i, j)

    all_possible_carre = set()
    icoin = 3*(i//3)
    jcoin = 3*(j//3)
    for u in range(icoin, icoin+3):
        for v in range(jcoin, jcoin+3):
            #print(f"Examining cell ({u},{v}) with value {G[u,v]}")
            if G[u,v] == 0  and (u != i or v != j):
                all_possible_carre = all_possible_carre.union(nb_possibles(G, u, v)[0])
                #print(all_possible_carre)

    all_possible_ligne = set()
    for v in range(9):
        if G[i,v] == 0 and v != j:
            all_possible_ligne = all_possible_ligne.union(nb_possibles(G, i, v)[0])

    all_possible_colonne = set()
    for u in range(9):
        if G[u,j] == 0 and u != i:
            all_possible_colonne = all_possible_colonne.union(nb_possibles(G, u, j)[0])

    carre_utilises = possibles - all_possible_carre
    ligne_utilises = possibles - all_possible_ligne
    colonne_utilises = possibles - all_possible_colonne

    return carre_utilises, ligne_utilises, colonne_utilises

def recherche_double(G, i, j):
    possibles, _ = nb_possibles(G, i, j)
    autres_possibles = {}
    for u in range(9):
        if G[i,u] == 0 and u != j:
            possibles_, _ = nb_possibles(G, i, u)
            if tuple(possibles_) in autres_possibles and len(possibles_) == 2:
                if autres_possibles[tuple(possibles_)]//3 == u//3 and set(range(1, 10)) - carre(G, i, u) == possibles_:
                    #print(f"Double trouvé en ligne {i} colonne {u} : {possibles_}")
                    possibles = possibles - possibles_

            autres_possibles[tuple(possibles_)] = u

    for v in range(9):
        if G[v,j] == 0 and v != i:
            possibles_, _ = nb_possibles(G, v, j)
            if tuple(possibles_) in autres_possibles and len(possibles_) == 2:
                if autres_possibles[tuple(possibles_)]//3 == v//3 and set(range(1, 10)) - carre(G, v, j) == possibles_:
                    #print(f"Double trouvé en colonne {j} ligne {v} : {possibles_}")
                    possibles = possibles - possibles_

            autres_possibles[tuple(possibles_)] = v
    return possibles

def un_tour(G):
    modifie = False
    for i in range(9):
        for j in range(9):
            if G[i,j] == 0:
                possibles, _ = nb_possibles(G, i, j)
                if len(possibles) == 1:
                    G[i,j] = possibles.pop()
                    modifie = True
                else:
                    carre_utilises, ligne_utilises, colonne_utilises = eliminer_possibles(G, i, j)
                    #print(f"Cellule ({i},{j}) : possibles = {possibles}, carre_utilises = {carre_utilises}, ligne_utilises = {ligne_utilises}, colonne_utilises = {colonne_utilises}")
                    if len(carre_utilises) == 1:
                        G[i,j] = carre_utilises.pop()
                        modifie = True
                    elif len(ligne_utilises) == 1:
                        G[i,j] = ligne_utilises.pop()
                        modifie = True
                    elif len(colonne_utilises) == 1:
                        G[i,j] = colonne_utilises.pop()
                        modifie = True

                    elif len(recherche_double(G, i, j))==1:
                        G[i,j] = recherche_double(G, i, j).pop()
                        modifie = True

    return modifie

def resoudre(G):
    while not finie(G):
        if not un_tour(G):
            break
    return finie(G)

resoudre(G)
print(G)

resoudre(M)
print(M)

resoudre(G2)
print(G2)






