from blessed import Terminal
from TUIUtilities import *
import random as rd

def add_IntParam(menu):
    #fonctions pour ajouter a menu les choix venant des intégrales a paramètres
    #les données viennent de reflexion.md
    menu.add("CPM de la variable d'integration et integrabilité","CPM_var_int")
    menu.add("CPM de la variable principale","CPM_var_princ")
    menu.add("CPM de la variable d'integration sur la dérivée","CPM_var_int_der")
    menu.add("CPM de la variable principale sur la dérivée","CPM_var_princ_der")
    menu.add("CTE de la variable d'integration","CTE_var_int")
    menu.add("CTE de la variable principale","CTE_var_princ")
    menu.add("CTE de la variable principale sur la dérivée","CTE_var_princ_der")
    menu.add("CTE de la variable d'integration sur la dérivée","CTE_var_int_der")
    menu.add("Domination","DOM")
    menu.add("Domination de la dérivée","DOM_der")

def add_SuiteFonction(menu):
    menu.add("CVS des f_n (de la limite et/ou de la serie)","CVS_fn")
    menu.add("CVS de f (par limite ou par serie)","CVS_f")
    menu.add("CPM des f_n","CPM_fn")
    menu.add("CPM de f (par limite ou par serie)","CPM_f")
    menu.add("continuité des f_n","CTE_fn")
    menu.add("continuité de f (par limite ou par serie)","CTE_f")
    menu.add("CVU des f_n","CVU_fn")
    menu.add("CVU de f (par limite ou par serie)","CVU_f")
    menu.add("convergence forte de la serie des integrales","CVF")
    menu.add("Domination des f_n","DOM_fn")
    menu.add("Domination de f (par limite ou par serie)","DOM_f")
    menu.add("C1 des f_n","C1_fn")
    menu.add("C1 de f (par limite ou par serie)","C1_f")

dico_IntParam = {
    "CPM_var_int" : "CPM de la variable d'integration et integrabilité",
    "CPM_var_princ" : "CPM de la variable principale",
    "CPM_var_int_der" : "CPM de la variable d'integration sur la dérivée",
    "CPM_var_princ_der" : "CPM de la variable principale sur la dérivée",
    "CTE_var_int" : "CTE de la variable d'integration",
    "CTE_var_princ" : "CTE de la variable principale",
    "CTE_var_princ_der" : "CTE de la variable principale sur la dérivée",
    "CTE_var_int_der" : "CTE de la variable d'integration sur la dérivée",
    "DOM" : "Domination",
    "DOM_der" : "Domination de la dérivée"
}

dico_SuiteFonction = {
    "CVS_fn" : "CVS des f_n (de la limite et/ou de la serie)",
    "CVS_f" : "CVS de f (par limite ou par serie)",
    "CPM_fn" : "CPM des f_n",
    "CPM_f" : "CPM de f (par limite ou par serie)",
    "CTE_fn" : "continuité des f_n",
    "CTE_f" : "continuité de f (par limite ou par serie)",
    "CVU_fn" : "CVU des f_n",
    "CVU_f" : "CVU de f (par limite ou par serie)",
    "CVF" : "convergence forte de la serie des integrales",
    "DOM_fn" : "Domination des f_n",
    "DOM_f" : "Domination de f (par limite ou par serie)",
    "C1_fn" : "C1 des f_n",
    "C1_f" : "C1 de f (par limite ou par serie)"
}

def setParams_intParam(title,keys):
    def test(data):
        #on test si le tableau de data sont egaux a keys
        full = True
        
        if len(data) != len(keys):
            full = False
        else:
            for i in range(len(data)):
                #en utilisant in
                if data[i] not in keys[i]:
                    full = False
                    break
        clearScreen()
        print(["vous avez reussi !","vous avez echoué"][int(not full)])
        
    menu = CheckboxMenu(title,test)
    add_IntParam(menu)
    menu.execute()

def setParams_suiteFonction(title,keys):
    def test(data):
        #on test si le tableau de data sont egaux a keys
        full = True
        
        if len(data) != len(keys):
            full = False
        else:
            for i in range(len(data)):
                #en utilisant in
                if data[i] not in keys[i]:
                    full = False
                    break
        clearScreen()
        print(["vous avez reussi !","vous avez echoué"][int(not full)])
        if not full :
            #on imprime les bonnes réponses dans le cas ou on a échoué
            print("les bonnes réponses sont :")
            for i in range(len(keys)):
                print(dico_SuiteFonction[keys[i]])
        
    menu = CheckboxMenu(title,test)
    add_SuiteFonction(menu)
    menu.execute()



while True:
    r = rd.randint(0,100000) % 7
    if r == 0:
        setParams_intParam("Thm 1 : continuité des integrales de fonctions à paramètres",["CPM_var_int","CTE_var_princ","DOM"])
    elif r == 1:
        setParams_intParam("Thm 2 : C1 des integrales de fonctions a parametres",["CPM_var_int","CPM_var_int_der","CTE_var_princ_der","DOM_der"])
    elif r ==2:
        setParams_suiteFonction("Thm 5 : interversion limite integrale",["CVS_fn","CPM_f","DOM_fn"])
    elif r == 3:
        setParams_suiteFonction("Thm 7 : interversion serie integrale",["CVS_fn","CPM_fn","CVF"])
    elif r == 4:
        setParams_suiteFonction("Thm 8-9 : interversion limite limite / limite serie",["CVU_fn"])
    elif r == 5:
        setParams_suiteFonction("Thm 10 : continuité d'une série",["CTE_fn","CVU_fn"])
    elif r == 6:
        setParams_suiteFonction("Thm 11 : C1 d'une série",["CVS_fn","CVU_fn","C1_fn"])