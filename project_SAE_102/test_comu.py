#! /bin/usr/python3
from comu import cree_reseau,liste_personne,sont_amis,sont_amis_de,est_comu,comu,tri_popul,comu_dans_reseau,comu_dans_amis,comu_max


# test unitaire cree_reseau
def test_cree_reseau():
    tab_amis_test = [
        "Alice", "Bob", 
        "Alice", "Charlie", 
        "Bob", "David", 
        "Charlie", "Emma", 
        "Emma", "Frank", 
        "David", "Frank"
    ]
    assert cree_reseau(tab_amis_test) == {
        'Alice': ['Bob', 'Charlie'],
        'Bob': ['Alice', 'David'],
        'Charlie': ['Alice', 'Emma'],
        'David': ['Bob', 'Frank'],
        'Emma': ['Charlie', 'Frank'],
        'Frank': ['Emma', 'David']
    }
    print("La fonction cree_reseau fonctionne correctement")

# test unitaire liste_personne 
def test_liste_personne():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
  

    assert liste_personne(reseau_test)  == ["Alice","Bob","Carl","Dan"] 
    print("La fonction liste_personne fonctionne correctement")

# test unitaire sont_amis 
def test_sont_amis():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }

    assert sont_amis(reseau_test, "Alice", "Bob") == True
    assert sont_amis(reseau_test, "Alice", "Carl") == False
    assert sont_amis(reseau_test, "Bob", "Carl") == True
    print("La fonction sont_amis fonctionne correctement")

# test unitaire sont_amis_de 
def test_sont_amis_de():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }

    assert sont_amis_de("Alice", ["Bob", "Dan"], reseau_test) == True
    assert sont_amis_de("Alice", ["Bob", "Carl"], reseau_test) == False
    assert sont_amis_de("Bob", ["Alice", "Dan"], reseau_test) == True

    print("La fonction sont_amis_de fonctionne correctement")

# test unitaire est_comu
def test_est_comu():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    groupe_test1 = ["Alice","Bob","Dan"]
    assert est_comu(reseau_test,groupe_test1) == True
    groupe_test2 =["Alice","Bob","Carl"]
    assert est_comu(reseau_test,groupe_test2) == False
    print("La fonction est_comu fonctionne correctement")


# test unitaire comu 
def test_comu():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }

    groupe_test1 = ["Alice", "Bob", "Carl", "Dan"]
    resultat_attendu1 = ["Alice", "Bob", "Dan"]
    assert comu(groupe_test1, reseau_test) == resultat_attendu1
    groupe_test2 = ["Carl", "Alice", "Bob", "Dan"]
    resultat_attendu2 = ["Carl", "Bob"]
    assert comu(groupe_test2, reseau_test) == resultat_attendu2
    groupe_test3 = ["Carl", "Alice", "Dan"]
    resultat_attendu3 = ["Carl"]
    assert comu(groupe_test3, reseau_test) == resultat_attendu3
    print("La fonction comu fonctionne correctement")
    
# test unitaire trie_popul
from comu import est_comu
def test_tri_popul():
    reseau_test_1 = {
        'Alice': ['Franck'],
        'Franck': ['Alice', 'Bob', 'Sam'],
        'Bob': ['Franck'],
        'Ali': ['Sam'],
        'Sam': ['Ali', 'Franck']
    }
    reseau_test_2 = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    
    assert tri_popul(["Alice", "Franck", "Bob", "Ali", "Sam"], reseau_test_1) == ['Franck', 'Sam', 'Ali', 'Bob', 'Alice']
    assert tri_popul(["Alice", "Bob", "Carl"], reseau_test_2) == ["Bob", "Alice", "Carl"]
    print("La fonction tri_popul fonctionne correctement")

# test unitaire comu_dans_reseau
def test_comu_dans_reseau():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    
    communaute=comu_dans_reseau(reseau_test)
    
    assert "Alice" in communaute
    assert "Bob" in communaute
    assert "Dan" in communaute
    assert len(communaute) == 3  #On vérifie qu'il n'y a pas d'autre personne
    print("la fonction com_dans_reseau fonctionne correctement")
    
# test unitaire comu_dans_amis
def test_comu_dans_amis():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    personne1="Alice"
    assert comu_dans_amis(personne1,reseau_test) == ["Alice", "Bob", "Dan"]
    personne2="Carl"
    assert comu_dans_amis(personne2,reseau_test) == ["Carl","Bob"]
    print("la fonction com_dans_amis fonctionne correctement")
    
#test unitaire comu_max
def test_comu_max():
    reseau_test = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    communaute_max=comu_max(reseau_test)
    
    assert "Alice" in communaute_max
    assert "Bob" in communaute_max
    assert "Dan" in communaute_max
    assert len(communaute_max) == 3  #On vérifie qu'il n'y a pas d'autre personne
    print("la fonction com_dans_reseau fonctionne correctement")

