#! /bin/usr/python3

# Fonction "cree_reseau" (question 1) :

def cree_reseau(t):
    '''
    Crée un réseau de relations à partir d'une liste représentant les relations entre individus.
    Par exemple, t = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"] indique que :
    - Alice est en relation avec Bob et Charlie.
    - Bob est en relation avec Denis.
    
    Paramètre :
    "t" qui est un tableau de relations entre individus.
    
    Retourne :
    un dictionnaire qui représente le réseau.
    '''
    dico_reseau = {}
    i = 0
    while i < len(t) - 1:
        couple_amis = (t[i], t[i + 1])  # Permet de créer un couple d'amis
        
        if couple_amis[0] not in dico_reseau:  # Si la première personne du couple d'amis n'est pas dans le dico
            dico_reseau[couple_amis[0]] = []  # On initialise un tableau vide dont la clé est la première personne du couple
        
        if couple_amis[1] not in dico_reseau:  # Pareil pour la seconde personne
            dico_reseau[couple_amis[1]] = []
        
        # On ajoute chaque personne dans la liste d'amis de l'autre
        dico_reseau[couple_amis[0]].append(couple_amis[1])
        dico_reseau[couple_amis[1]].append(couple_amis[0])
        
        i += 2  # On incrémente de deux pour passer au couple suivant
    
    return dico_reseau


# Fonction "liste_personne" (question 3)
def liste_personne(reseau):
    '''
    Renvoie la liste des personnes du réseau.
    
    Paramètre :
    dictionnaire qui représente le réseau.
    
    Retourne :
    un tableau contenant tous les noms des personnes du réseau.
    '''
    t_personne = []
    for personne in reseau.keys():
        t_personne.append(personne)
    return t_personne


# Fonction "sont_amis" (question 4)
def sont_amis(reseau, personne_1, personne_2):
    '''
    Permet de vérifier si deux membre du reseau sont amis .
   
    Paramètre :
    - un dictionnaire qui représente le réseau (reseau)
    - chaine caractère qui symbolyse le nom d'une des deux personne dont on veut vérifier l'amitié (personne_1)
    - chaine caractère qui symbolyse le nom d'une des deux personne dont on veut vérifier l'amitié (personne_2)
   
    Retourne :
    - Une valeur booléen (True , False )
    '''
    for personne in reseau[personne_1]:  # Parcourt la liste d'amis de la première personne
        if personne == personne_2:  # Si la deuxième personne est trouvée
            return True
    return False


# Fonction "sont_amis_de" (question 5)
def sont_amis_de(personne, groupe, reseau):
    '''
    Permet de voir si une personne est amis avec tout les membres du groupe .
	
    Paramètre :
    - chaine caractère qui symbolyse le nom de personne dont on veut vérifier si oui ou non elle est amis avec tout
      les autre personne du groupe (personne)
	   
    - tableau qui représente un groupe de personne faisant partie du même réseau mais pas forcément amis (groupe)
	  
    - dictionnaire qui représente le reseau reseau 
	
    Retourne :
    - Un boolèen (True,False)
    '''
    for gens in groupe:
        if gens not in reseau[personne]:
            return False
    return True


# Fonction "est_comu" (question 6)
def est_comu(reseau, groupe):
    '''
    Permet de déterminer si un groupe est une communauté ou non .
    
    Paramètre :
    - dictionnaire qui représente le reseau reseau (reseau)
    - tableau qui représente un groupe de personne faisant partie du même réseau (groupe)
    
    Retourne :
    - Une valeur booléen (True , False )
    '''
    for personne in groupe:
        for individu in groupe:
            if personne != individu:
                # Ici je vérifie si individu est ami avec personne
                if personne not in reseau or individu not in reseau[personne]:
                    return False
    return True


# Fonction "comu" (question 7)
def comu(groupe, reseau):
    '''
    Crée une communauté maximal à partir du groupe , le reseau permet de voir qui est 
    en relation avec qui .
    
    Paramètre :
    - dictionnaire qui représente le reseau reseau (reseau)
    - tableau qui représente un groupe de personne faisant partie du même réseau (groupe)
    
    Retourne:
    - le tableau représentant la communauté (comu)
    '''
    comu = []
    comu.append(groupe[0])  # On rajoute a personne qui déterminera la construction de la communauté
    for personne in groupe:
        if sont_amis_de(personne, comu, reseau):  # cette fonction permet de determiner si personne st ammis avec tous les membre de comu
            comu.append(personne)
    return comu


# Fonction "tri_popul" (question 8)
def ech(t, i, j):  # Fonction d'echange qui facilite le trie par sélection
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp


def nb_amis(personne, reseau):  # Fonction qui compte le nombre d'amis de personne
    compteur = 0
    for amis in reseau[personne]:
        compteur += 1
    return compteur


def tri_popul(groupe, reseau):
    '''
    Trie une liste de personnes(groupe) en ordre décroissant du nombre d'amis dans le réseau,
    en utilisant un algorithme de tri par sélection adapté.

    Paramètres :
    - groupe : liste des noms des personnes à trier.
    - reseau : dictionnaire représentant le réseau social.

    Retourne :
    - La liste triée des personnes par nombre d'amis décroissant.
    '''
    n = len(groupe)  # longeur du tableau a trié
    nt = 0  # nombre d'élément trié
    while nt < n:
        nnt = n - nt  # nombre d'élément non trié
        imin = 0
        i = 1
        while i < nnt:
            if nb_amis(groupe[i], reseau) < nb_amis(groupe[imin], reseau):  # appel de nb_amis pour comparer les nombres d'amis de imax et i
                imin = i
            i += 1
        ech(groupe, imin, nnt - 1)  # appel a la fonction ech pour échanger la place de deux personne
        nt += 1
    return groupe


# Fonction "comu_dans_reseau" (question 9)
def comu_dans_reseau(reseau):
    '''
    Construit une communauté maximale en commençant par trier les individus du réseau
    selon leur nombre d'amis (ordre décroissant). La personne la plus populaire est placée
    au début du tableau.
    
    Paramètres :
    - reseau : dictionnaire représentant le réseau social.

    Retourne :
    - Une tableau représentant la communauté maximale.
    '''
    groupe_nt = liste_personne(reseau)  # liste des personne du reseau
    
    groupe = tri_popul(groupe_nt, reseau)  # on trie les personne du reseau par ordre décroissant 
                                           # par rapport a leur nombre d'amis
    
    # puis on applique l'alghorithme de construction de la question 7 (la fonction comu)
    comu = []
    comu.append(groupe[0])
    for personne in groupe:
        if sont_amis_de(personne, comu, reseau):
            comu.append(personne)
    return comu


# Fonction "comu_dans_amis" (question 10)
def comu_dans_amis(personne, reseau):
    '''
    Construit une communauté maximale de la personne indiquer en paramètre
    . Cette personne est ajoutée à la communauté en premier.

    Ensuite, les amis de cette personne sont examinés dans l'ordre décroissant
    de leur popularité (du plus grand au plus petit) pour vérifier s'ils peuvent intégrer la communauté.

    Paramètres :
    - reseau : dictionnaire représentant le réseau.

    Retourne :
    - Un tableau représentant la communauté maximale.
    '''
    comu = [personne]  # initialisation de la communauté
    amis_trier = tri_popul(reseau[personne], reseau)  # trie de la liste des amis de personne avec tri_popul
    for amis in amis_trier:
        if sont_amis_de(amis, comu, reseau):
            comu.append(amis)
    return comu


# Fonction "comu_max" (question 12)
def comu_max(reseau):
    '''
    Fonction qui renvoie la communauté la plus grande possible en appliquant la 
    fonction comu_dans_amis à chaque membre du groupe est compare les communauté 
    obtenue pour déterminer la plus grande communauté .
    
    Paramètres :
    - reseau : dictionnaire représentant le réseau.

    Retourne :
    - Un tableau représentant la communauté la plus grande du réseau.
    '''
    comu_max = []  # initialisation de comu_max avec un tableau vide essentiel pour déterminer la véritable comu_max
    for amis in reseau.keys():
        comu = comu_dans_amis(amis, reseau)  # création des différente communauté en fonction de amis
        if len(comu) > len(comu_max):  # comparaison des taille crée et de comu_max pour déterminer la plus grande
            comu_max = comu
    return comu_max

