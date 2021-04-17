from tkinter import * 
import os 

print(os.name)
##############################################################################################################################
# Infos en vrac                                                                                                              #
##############################################################################################################################
# - il faut 20 pixel d'écart selon y pour avoir de "jolie bouton"
# - L = place de parking libre
# - P : place de parking prise

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
        Button(self.frame,textvariable = str(self.name_var),command = self.update_place ).place(x = self.x,y = self.y)

    #met à jour la valeur du bouton ("L si libre et P si prise ")
    def update_button_value(self):
        if self.name[0] == "L":
            temp = "P"+self.name[1:]
            self.name = temp
        else :
            temp = "L"+self.name[1:]
            self.name = temp
        self.name_var.set(self.name)


    #met à jour le nombre de place libre/occupé dans le parking
    def update_place(self):
        global place_occupe,place_libre,place_max,place_libre

        #place de parking libre, on essaye de se garer
        if self.name[0]=="L" : #and place_occupe != place_max and place_libre != 0:
            place_occupe+=1
            place_libre -=1
            print("Libre = {} occupé = {}".format(place_libre,place_occupe))
            self.update_button_value()

        #place de parking prise, on essaye de sortir 
        elif self.name[0] =="P": #and place_occupe != 0 :
            place_libre +=1
            place_occupe -=1
            print("Libre = {} occupé = {}".format(place_libre,place_occupe))
            self.update_button_value()
        else : 
            print("Action illégal")

        #mise à jour des valeur de place libre/occupe dans le parking
        place_libre_var.set("Nombre de place dispo dans le parking : {}".format(place_libre)+"/"+str(place_max))
        place_occupe_var.set("Nombre de place occupé dans le parking :  "+str(place_occupe)+"/"+str(place_max))

##############################################################################################################################
# Partie graphique                                                                                                           #
##############################################################################################################################

#initialisation de la fenêtre 
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
p1 = Parking(fenetre,"L-P1",0,50)
p2 = Parking(fenetre,"L-P2",0,70)
p3 = Button(fenetre,text = 'value').place(x = 0, y = 90)


#"boucle" while de tkinter
fenetre.mainloop()
