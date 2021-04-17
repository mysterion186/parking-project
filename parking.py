from tkinter import *

##############################################################################################################################
# Infos en vrac                                                                                                              #
##############################################################################################################################
# - il faut 20 pixel d'écart selon y pour avoir de "jolie bouton"

##############################################################################################################################
# Déclaration des variables                                                                                                  #
##############################################################################################################################
place_occupe = 0   #nombre de place prise dans le parking
place_libre = 2    #nombre de place libre dans le parking
place_max = 2      #nopmbre de place dans le parking

##############################################################################################################################
# Déclaration de classe                                                                                                      #
##############################################################################################################################
class Parking :
    def __init__(self,frame,name,x,y):
        self.name = name
        self.name_var = StringVar() #permet de changer le texte qui se trouve sur le bouton de manière dynamique
        self.name_var.set(self.name)
        self.x = x 
        self.y = y 
        self.frame = frame
        #creation d'un bouton, on utilise highlightbackground à lla place de background car ça ne marche pas sur macos 
        self.button = Button(self.frame,textvariable = str(self.name_var),command = self.update_place,highlightbackground='green')

    #ajoute le bouton crée dans le fenêtre tkinter 
    def add(self):
        self.button.place(x = self.x,y = self.y)

    """#met à jour la valeur du bouton ("L si libre et P si prise ")
    def update_button_value(self):
        if self.name[0] == "L":
            temp = "P"+self.name[1:]
            self.name = temp
        else :
            temp = "L"+self.name[1:]
            self.name = temp
        self.name_var.set(self.name)"""
    
    #modifie la couleur de la place selon qu'elle est prise(red) ou non(green)
    def change_color(self):
        if self.button["highlightbackground"]=='red':
            self.button["highlightbackground"]= 'green'
        else :
            self.button["highlightbackground"]='red' 

    #met à jour le nombre de place libre/occupé dans le parking
    def update_place(self):
        global place_occupe,place_libre,place_max,place_libre

        #place de parking libre, on essaye de se garer
        if self.button["highlightbackground"]=="green" : #on regarde la couleur car elle nous indique l'état de la place (prise ou non)
            place_occupe+=1
            place_libre -=1
            print("Nombre de place Libre = {}, nombre de place occupée occupé = {}".format(place_libre,place_occupe))
            self.change_color()

        #place de parking prise, on essaye de sortir 
        elif self.button["highlightbackground"]=="red": #and place_occupe != 0 :
            place_libre +=1
            place_occupe -=1
            print("Nombre de place Libre = {}, nombre de place occupée occupé = {}".format(place_libre,place_occupe))
            self.change_color()
        else : 
            print("Action illégal")

        #mise à jour des valeur de place libre/occupe dans le parking
        place_libre_var.set("Nombre de place dispo dans le parking : "+str(place_libre)+"/"+str(place_max))
        place_occupe_var.set("Nombre de place occupé dans le parking : "+str(place_occupe)+"/"+str(place_max))

##############################################################################################################################
# Partie graphique                                                                                                           #
##############################################################################################################################


#################################### initialisation de la fenêtre  ####################################
fenetre = Tk()
fenetre.title("Parking Manager")
fenetre.geometry("500x500")

#################################### Initialisation des compteur de place ####################################
place_libre_var = StringVar()
place_occupe_var = StringVar()

place_libre_var.set("Nombre de place disponible dans le parking : {}".format(place_libre)+"/"+str(place_max))
place_occupe_var.set("Nombre de place occupé dans le parking    : "+str(place_occupe)+"/"+str(place_max))

place_libre_label = Label(fenetre,textvariable = place_libre_var).place(x=0,y = 0)
place_occupe_label = Label(fenetre,textvariable = place_occupe_var).place(x=0,y = 20)

#################################### Initialisation des places de parking #################################### 
#premier étage
etage_1 = Label(fenetre,text = "Etage n°1") .place(x=200,y = 50)
alle_1_1 = Label(fenetre,text = "Allé 1").place(x = 0,y=70)
p1 = Parking(fenetre,"place 1 ",0,90)
p1.add()
p2 = Parking(fenetre,"place 2 ",55,90)
p2.add()

#################################### Initialisation des places de parking #################################### 


fenetre.mainloop()
