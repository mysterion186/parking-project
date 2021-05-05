from tkinter import *

##############################################################################################################################
# Infos en vrac                                                                                                              #
##############################################################################################################################
""" 
RAPPEL: background ne fonctionne pas sur macos d'où l'utilisation de highlightbackground => pb si on quitte la fenêtre tkinter
on aura que les bordures qui auront une couleur sinon toutes les places seront coloriées normalement 

Configuration : 
niveau 0 : 2 allées de 5 places et 4 places 
niveau 1 : 2 allées de 5 places et 4 places 
niveau 2 : 2 allées de 5 places et 4 places 
"""

##############################################################################################################################
# Déclaration des variables                                                                                                  #
##############################################################################################################################
place_occupe = 0   #nombre de place prise dans le parking
place_libre = 0    #nombre de place libre dans le parking
place_max = 0      #nombre de place maximal dans le parking
place_0 = 0        #nombre de place libre par niveau
place_1 = 0
place_2 = 0


##############################################################################################################################
# Déclaration de classe                                                                                                      #
##############################################################################################################################

#va nous permettre de créer des boutons plus facilement et gérer plein de fonctionnalité dessus comme le changement de couleur
#quand on clique dessus ou bien la mise à jour du nombre de place dispo/prise 
class Parking :
    def __init__(self,frame,name,x,y):
        global place_libre,place_max

        self.name = name #nom de la place 
        self.x = x #coordonnée x du bouton
        self.y = y #coordonnée y du bouton
        self.frame = frame #nom de le fenêtre tkinter
        #creation d'un bouton, on utilise highlightbackground à la place de background car ça ne marche pas sur macos 
        self.button = Button(self.frame,text = str(self.name),command = self.update_place,highlightbackground='green',background = 'green')

        #on met à jour le nombre de place libre et maximal à la création de chaque place de parking
        # place_libre +=1 
        # place_max +=1
        update_place_value(self.name[0],"init")

    #ajoute le bouton crée dans la fenêtre tkinter 
    def add(self):
        self.button.place(x = self.x,y = self.y)
    
    #modifie la couleur de la place selon qu'elle est prise(red) ou non(green)
    def change_color(self):
        #on teste highlightbackground et non background à cause des pb sur macos et pour être sûr qu'il y ait un changement de couleur
        if self.button["highlightbackground"]=='red':
            self.button["highlightbackground"]= 'green'
            self.button["background"]= 'green'
        else :
            self.button["highlightbackground"]='red'
            self.button["background"]='red' 

    #met à jour le nombre de place libre/occupé dans le parking
    def update_place(self):
        global place_occupe,place_libre,place_max,place_libre

        #place de parking libre, on essaye de se garer
        if self.button["highlightbackground"]=="green" : #on regarde la couleur car elle nous indique l'état de la place (prise ou non)
            # place_occupe+=1
            # place_libre -=1
            print("Nombre de place Libre = {}, nombre de place occupée occupé = {}".format(place_libre,place_occupe))
            self.change_color()
            update_place_value(self.name[0],"partir")
            print("place 0 {} place 1 {} place 2 {}".format(place_0,place_1,place_2))
        #place de parking prise, on essaye de sortir 
        elif self.button["highlightbackground"]=="red": 
            # place_libre +=1
            # place_occupe -=1
            print("Nombre de place Libre = {}, nombre de place occupée occupé = {}".format(place_libre,place_occupe))
            self.change_color()
            update_place_value(self.name[0],"garer")
            print("place 0 {} place 1 {} place 2 {}".format(place_0,place_1,place_2))
        else : 
            print("Action illégal")

        #mise à jour des valeur de place libre/occupe dans le parking et dans les différents niveaux
        place_libre_var.set("Nombre de place dispo dans le parking : "+str(place_libre)+"/"+str(place_max))
        place_occupe_var.set("Nombre de place occupé dans le parking : "+str(place_occupe)+"/"+str(place_max))
        niveau_0_var.set("Niveau n°0 "+str(place_0)+"/9")
        niveau_1_var.set("Niveau n°1 "+str(place_1)+"/9")
        niveau_2_var.set("Niveau n°2 "+str(place_2)+"/9")

##############################################################################################################################
# Déclaration de fonction                                                                                                    #
##############################################################################################################################

#fonction pour ajouter des boutons/places de parking dans la fenêtre tkinter
#frame = nom de la fenêtre tkinter; x/y_base = coordonnées du premier élément, allee_num = numéro de l'allée, num_max = nb de place par allée
def add_places(frame,x_base,y_base,allee_num,num_max,niveau_num,count):
    allee = Label(frame,text = f"Allé {allee_num}").place(x = x_base,y=y_base)
    for k in range(1,num_max+1):
        #seulement pour avoir un jolie rendu
        if count <10:
            spot = Parking(fenetre,f"{str(niveau_num)}-place 0{str(count)}",(x_base+(k-1)*75),y_base+20)
        else :
            spot = Parking(fenetre,f"{str(niveau_num)}-place {str(count)}",(x_base+(k-1)*75),y_base+20)
        spot.add()
        count+=1
    return count

#met à jour le nombre de place dans le niveau considéré [place disponible]
#niveau_num = numéro du niveau, action = bouléen, True si on quitte la place False sinon
def update_place_value(niveau_num,action="garer"):
    global place_0,place_1,place_2, place_libre, place_occupe,place_max
    #on met à jour le nombre de place dans le niveau
    if action == "garer":
        place_libre +=1
        place_occupe -=1
        if niveau_num == "0":
            place_0 +=1
        elif niveau_num =="1" :
            place_1 +=1
        elif niveau_num == "2":
            place_2 +=1
    elif action == 'partir' :
        place_occupe+=1
        place_libre -=1
        if niveau_num == "0":
            place_0 -=1
        elif niveau_num =="1" :
            place_1 -=1
        elif niveau_num == "2":
            place_2 -=1
    else :
        place_libre +=1 
        place_max +=1 
        if niveau_num == "0":
            place_0 +=1
        elif niveau_num =="1" :
            place_1 +=1
        elif niveau_num == "2":
            place_2 +=1
    return True
##############################################################################################################################
# Partie graphique                                                                                                           #
##############################################################################################################################


#################################### initialisation de la fenêtre  ############################################################
fenetre = Tk()
#nom de la fenêtre tkinter
fenetre.title("Parking Manager")
#dimension de départ de la fenêtre tkinter
fenetre.geometry("500x500")

#################################### Initialisation des places de parking ######################################################
#coordonées y de départ, qu'on va ensuite modifier dans la boucle pour avoir les différents éléments à la bonne place
y = 50 
count = 1
#on utilise une boucle pour ne pas répeter 3 fois les mêmes lignes de codes
for k in range(0,3):
    #allée 1 du niveau k 
    y+=10
    allee_k_1 = add_places(frame=fenetre,x_base=0, y_base=y,allee_num = 1,num_max=5,niveau_num = k,count = count)
    y+=50
    #allée 2 du niveau k 
    allee_k_2 = add_places(frame=fenetre,x_base=0, y_base=y,allee_num = 2,num_max=4,niveau_num = k,count = allee_k_1)
    y+=60
    count = allee_k_2


#################################### Initialisation des compteur de place ######################################################
#création de 2 variables qui peuvent être modifiées dynamiquement
place_libre_var = StringVar()
place_occupe_var = StringVar()

niveau_0_var = StringVar()
niveau_1_var = StringVar()
niveau_2_var = StringVar()

#on indique quoi mettre dans les  variables
place_libre_var.set("Nombre de place disponible dans le parking : "+str(place_libre)+"/"+str(place_max))
place_occupe_var.set("Nombre de place occupé dans le parking     : "+str(place_occupe)+"/"+str(place_max))
niveau_0_var.set("Niveau n°0 "+str(place_0)+"/9")
niveau_1_var.set("Niveau n°1 "+str(place_1)+"/9")
niveau_2_var.set("Niveau n°2 "+str(place_2)+"/9")

#on affiche les variables (et leurs contenus dans la fenêtre tkinter)
place_libre_label = Label(fenetre,textvariable = place_libre_var).place(x=0,y = 0)
place_occupe_label = Label(fenetre,textvariable = place_occupe_var).place(x=0,y = 20)
niveau_0_label = Label(fenetre,textvariable = niveau_0_var).place(x=200,y = 50)
niveau_1_label = Label(fenetre,textvariable = niveau_1_var).place(x=200,y = 170)
niveau_2_label = Label(fenetre,textvariable = niveau_2_var).place(x=200,y = 290)

#bouton pour fermer la fenêtre tkinter
fermer = Button(fenetre,text = "quitter" ,command = fenetre.quit,highlightbackground='blue',background = 'blue')
fermer.place(x=200,y=460)
fenetre.mainloop()