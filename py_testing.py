"""
Condition 
"""

# condition if elif else


# a , b , c = 10 , 10, 13 



# print(" la valeur de a est : {}".format(a))
# print(f"la valeur de b est  : {b}")



# if a > b :
#     print("a supérieur à b")

# elif a < b :
#     print( "a est inférieur à b")

# else : 
#     print("a est égale à b ")


"""
boucle ( Loop)  : processus d'instruction tiana haverimberina 


"""


""" logique et / ou """

# "ET" est considéré comme : "and" ( * (multiplication))
# "OU" est considéré comme : "or" ( + ( addition))

# il y a deux logiques : 
# on les appeles : logique1 et logique2 ( c'est à dire  : true ou false)

"""
Formule : 
    avec ou : 
        true + true = true ( ou i.e  : true or true = true)
        true + false =  true (i.e : true or false = true)
        false + true = true ( ou i.e  : false or true = true)
        false + false =  false (i.e : true or false = false )

    avec et  : 
        true * true = true ( ou i.e  : true and true = true)
        true * false =  false (i.e : true  or false = false)
        false * true = false ( ou i.e  : false or true = false)
        false * false =  false (i.e : true or false = false )


"""


# a , b , c  = 1 , 2 , 3 


# if not a == 1: 
#     print("vraie")
# else :
#     print("diso")

## boucle while ( tant que )

""""

vérification de départ 
while condition à vérifier : 
    instruction(s)
"""

# exemple : 

# var = 99
# var = var + 1 
# var += 1 


# i = 1


# while  i <= 5 :
#     print(i)
#     if  i == 3 :
#         print("test pour i = {}".format(i))
#     i += 1


## boucle for ( pour )

# iterations : nombre d'instruction à repéter dans un loop 


""" first : chaine de caractère"""
# name = "Fitiavana"

# for letter in name: 
#     print(letter)


""" second : number"""


# import datetime

# nombre = 1000000000
# start_time = datetime.datetime.now()

# for i in range(nombre):
#     pass


# end_time = datetime.datetime.now()


# time  = end_time - start_time


# print("temps de comptage de nombre : {} est durant :{}".format(nombre, time))



"""
Autres types de variable 

list , tuple , dictionnary
"""

# tableau 
# formule : nom_de_variable = ["valeur1", valeur2 , valeur3, ..., valeurn]

# list_1 = []
# my_fisrt_list = ["Fitiavana", "Fandresena", 2025, True, ""]


# print(f"list_1 : {list_1}")
# print(f" premier liste avec des valeur : {my_fisrt_list}")

# get value of list per index 
# list[index]


# index0_value = my_fisrt_list[1]
# print(index0_value)

# for value in my_fisrt_list :
#     if value == "Fitiavana":
#         print(value)



# t1 = ("Fitiavana", "Fandresena", True)
# for t in t1 :
#     if t == True :
#         print("dernier valeur de mon tuple")



# mon_dico = {
#     "nom": "Fitiavana", 
#     "age": 30, 
#     "sexe": "M",
#     "taille": "2.3", 
#     "nationality": "american"
#     }

# # premier cas 
# for key in mon_dico :
#     print(key)

# value =  mon_dico["age"]

# print(value)

# # second case
# for key in mon_dico :
#     print(f"key :{key}  avec la valeur : {mon_dico[key]}")
#     print("key :{}  avec la valeur : {}".format(key, mon_dico[key]))



# third case
# for k, v in mon_dico.items() :
#     print(f"key :{k}  avec la valeur : {v}")



"""
méthode
"""

# méthode 1 : strip() : c'est pour effacer les espaces vides dans une chaine de caractère
#exemple 
# name = "      Fitiavana            "
# print(f"caractère avec des espaces:{name}")

# name_v2 = name.strip()
# print(f"caractère sans espaces:{name_v2}")



# méhtode 2 : split() : c'est pour séparer les valeurs d'une chaine de carcartère selon leur séparateur ( ex:  " ", "_", "-", ".", "()")


# paragraphe = " Nandeha tany an-tsean i Neny.  Nividy mofo izy. Tezitra i Fitahiana . Nisotro kafe i Anicet"

# filename = "prison_break_season_1_episode_1.mp4"
# filename_v2 = filename.split("_")
# for v in filename_v2:
#     print(v)

 
# para = paragraphe.split(".")
# print(para)


# methode 3 : append() : c'eest ajouter une valeur dans un tableau

# tableau = ["A", "B", "C"]
# tableau.append("Natacha")

# print(tableau)

# tableau = []

# for i in range (10):
#     tableau.append(i)

# print(tableau)


# print(tableau)

"""
fonction , class
"""


# Fonction 
"""
def function_name():
    instruction 1


    instruction n

    return
"""



# def addition():
#     a , b = 1, 2
#     c = a + b  
#     return c    


# add = addition()

# print(add)

# def addition():
#     a , b = 1, 2
#     c = a + b  
#     print(f" a +b = {c}")   


# addition()

# def addition(a, b):
#     c = a + b
#     return c 



# a = input("entréer la valeur de a : ")
# b = input( "entréer la valeur de b : ")


# print(f"type a avant : {type(a)}")
# print(f"type b avant : {type(b)}")
# ovaina entier ny type de a et b 

# a = int(a)
# b = int(b)

# print(f"type a après : {type(a)}")
# print(f"type b après : {type(b)}")


# if type(a) == int and type(b) == int: 
#     add = addition(a, b)
#     print(add)







# def eq_degree_1( a, b):
#     x = None
#     if a and b :
#         if a != 0:
#             x = - b / a  

#         else : 
#             if b == 0 :
#                 x = "R"
#             else : 
#                 x = "Impossible"


#     return x




# a = int(input("a  = "))
# b = int(input("b = "))



# print(f"Résolution de l'équation de premier degré y ={a}x + {b}")
# eq_d = eq_degree_1(a,b)
# print(eq_d)


    





""" 
créer un mini jeu qui demande à l'utilisateur de déviner un nombre 
si l'entréé de l'utisateur est inférieur au nombre à deviner : afficher : plus petit
sinon si l'entrée de l'utilisateur est supérieur à ce nombre, afficher : plus grand 
 sinon : afficher : bravo , vous avez trouvez le nombre ( valeur du nombre à donner) 
 
 nb : l'utilisateur peut quiter le jeu sans fin  """


import random
secret = random.randint(1, 20)


is_found = False

# print("Tape 'quitter' pour quitter le jeu")
while not is_found :
   
    input_user = input("Entre une valeur entre 1 et 20 : ")
    n = int(input_user)

    if secret == n :
        print("Bravo , vous avez trouvé le nombre ")
        is_found = True 
    elif n < secret :
        print("Trop petit")
    else: 
        print("Trop grand")




    


    





    




