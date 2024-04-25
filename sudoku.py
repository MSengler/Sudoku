import numpy as np

G=np.array([
[9,0,3,0,0,5,0,0,0],[7,2,0,0,0,0,0,6,0],[0,0,0,7,6,0,0,0,0],\
[3,0,2,0,0,7,0,0,4],[6,0,0,0,4,0,0,0,5],[8,0,0,5,0,0,7,0,2],\
[0,0,0,0,7,4,0,0,0],[0,7,0,0,0,0,0,9,1],[0,0,0,2,0,0,5,0,8]])

def carre(G,i,j):
    icoin=3*(i//3)
    jcoin=3*(j//3)
    chiffre=[]
    for u in range(icoin,icoin+3):
        for v in range(jcoin,jcoin+3):
            if G[u][v]!=0:
                chiffre.append(G[u,v])
    return chiffre
#print(carre(G,4,5))

def ligne(G,i):
    chiffre=[]
    for u in range(9):
        if G[i][u]!=0:
                chiffre.append(G[i,u])
    return chiffre
#print(ligne(G,0))

def colonne(G,i):
    chiffre=[]
    for u in range(9):
        if G[u][i]!=0:
                chiffre.append(G[u,i])
    return chiffre
#print(colonne(G,0))

def ligne_complete(G,i):
    for u in range(9):
        if G[i][u]==0:
            return False
    return True
#print(ligne_complete(G,0))

def colonne_complete(G,i):
    for u in range(9):
        if G[u][i]==0:
            return False
    return True
#print(colonne_complete(G,0))

def carre_complet(G,i,j):
    icoin=3*(i//3)
    jcoin=3*(j//3)
    for u in range(icoin,icoin+3):
        for v in range(jcoin,jcoin+3):
            if G[u][v]==0:
                return False
    return True
#print(carre_complet(G,0,0))

def finie(G):
    for i in range(9):
        for j in range(9):
            if G[i][j]==0:
                return False
    return True
#print(finie(G))

def conflit(G,i,j):
    pok=[]
    l=ligne(G,i)
    co=colonne(G,j)
    ca=carre(G,i,j)
    for i in range(len(l)):
        if l[i]not in pok:
            pok.append(l[i])
    for i in range(len(co)):
        if co[i]not in pok:
            pok.append(co[i])
    for i in range(len(ca)):
        if ca[i]not in pok:
            pok.append(ca[i])
    return pok
#print(conflit(G,4,2))

def chiffres_OK(G,i,j):
    ok=[]
    if G[i,j]!=0:
        ok.append(G[i,j])
        return ok
    conflits=conflit(G,i,j)
    for k in range(1,10) :
        if k not in conflits :
            ok.append(k)
    return ok
#print(chiffres_OK(G,4,2))

def nb_possible(G,i,j):
    return len(chiffres_OK(G,i,j))
#print(nb_possible(G,4,2))

def occurrence_ligne(G,i,k):
    occ=0
    for v in range(0,9):
        if k in chiffres_OK(G,i,v):
            occ+=1
    return occ

def occurrence_colonne(G,j,k):
    occ=0
    for u in range(0,9):
        if k in chiffres_OK(G,u,j):
            occ+=1
    return occ

def occurrence_carre(G,i,j,k):
    icoin=3*(i//3)
    jcoin=3*(j//3)
    occ=0
    for u in range(icoin,icoin+3):
        for v in range(jcoin,jcoin+3):
            if k in chiffres_OK(G,u,v):
                occ+=1
    return occ


def meme_nombres_ligne(G):
    for i in range(0,9):
        for k in range(0,3):
            L=[]
            for j in range(3*k,3*(k+1)):
                L.append(chiffres_OK(G,i,j))
            if L[0]==L[1] and len(L[0])==2 and occurrence_carre(G,i,j,L[0][0])==2 and occurrence_carre(G,i,j,L[0][1])==2:
                for j in range(0,9): 
                    if j!=3*k and j!=3*k+1:
                        if L[0][0] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][0]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
                        if L[0][1] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][1]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
            if L[0]==L[2] and len(L[0])==2 and occurrence_carre(G,i,j,L[0][0])==2 and occurrence_carre(G,i,j,L[0][1])==2:
                for j in range(0,9): 
                    if j!=3*k and j!=3*k+2:
                        if L[0][0] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][0]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
                        if L[0][1] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][1]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
            if L[1]==L[2] and len(L[1])==2 and occurrence_carre(G,i,j,L[0][0])==2 and occurrence_carre(G,i,j,L[0][1])==2:
                for j in range(0,9): 
                    if j!=3*k+1 and j!=3*k+2:
                        if L[1][0] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[1][0]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
                        if L[0][1] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][1]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]


def meme_nombres_colonne(G):
    for j in range(0,9):
        for k in range(0,3):
            L=[]
            for i in range(3*k,3*(k+1)):
                L.append(chiffres_OK(G,i,j))
            if L[0]==L[1] and len(L[0])==2 and occurrence_carre(G,i,j,L[0][0])==2 and occurrence_carre(G,i,j,L[0][1])==2:
                for i in range(0,9): 
                    if i!=3*k and i!=3*k+1:
                        if L[0][0] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][0]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
                        if L[0][1] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][1]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
            if L[0]==L[2] and len(L[0])==2 and occurrence_carre(G,i,j,L[0][0])==2 and occurrence_carre(G,i,j,L[0][1])==2:
                for i in range(0,9): 
                    if i!=3*k and i!=3*k+2:
                        if L[0][0] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][0]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
                        if L[0][1] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][1]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
            if L[1]==L[2] and len(L[1])==2 and occurrence_carre(G,i,j,L[0][0])==2 and occurrence_carre(G,i,j,L[0][1])==2:
                for i in range(0,9): 
                    if i!=3*k+1 and i!=3*k+2:
                        if L[1][0] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[1][0]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]
                        if L[0][1] in chiffres_OK(G,i,j) and len(chiffres_OK(G,i,j))==2:
                            if chiffres_OK(G,i,j)[0]==L[0][1]:
                                G[i,j]=chiffres_OK(G,i,j)[1]
                            else:
                                G[i,j]=chiffres_OK(G,i,j)[0]


def un_tour(G):
    changement=False
    for i in range(0,9):
        for j in range(0,9):
            if G[i,j]==0:
                if nb_possible(G,i,j)==1:
                    G[i,j]=chiffres_OK(G,i,j)[0]
                    changement=True
                    break
                for k in chiffres_OK(G,i,j):
                    if occurrence_carre(G,i,j,k)==1:
                        G[i,j]=k
                        changement=True
                        break
                    if occurrence_ligne(G,i,k)==1:
                        G[i,j]=k
                        changement=True
                        break
                    if occurrence_colonne(G,j,k)==1:
                        G[i,j]=k
                        changement=True
                        break              
    return changement
#print(un_tour(G))


def complete(G):
    acc=0
    while un_tour(G)!=False or acc>10:
        un_tour(G)
        acc+=1
    return G
print(complete(G))



