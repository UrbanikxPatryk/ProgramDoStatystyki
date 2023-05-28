import os
class Menu:
    def __init__(self,Boot,User_name_input) :
       self.User=User_name_input
       self.NBoot=Boot
    def przywitanie(self):

        print(f"{self.NBoot} > Witam cie w  Menu Glownym {self.User} ")   

    def menu_glowne(self):
          
          print("\t\t\t\t Menu \n"
                "1:Kalkulator\n"
                "2:Generatro Wykresow\n"
                "3:Generator Hasla \n"
                "0:Wyjscie z systemu")
          

    def button_key(self):
        try:
            button_input=int(input(f"{self.NBoot} > Wybierz co chcesz zrobic >  "))

        except ValueError:
            os.system("cls")
            print(f"{self.NBoot} >  hmm chyba ci sie pomylił klawisz  spprobuj jeszcze raz {self.User}")
            self.menu_glowne()
            self.button_key()

        else:
            match button_input:
                case 1 :
                    os.system("cls")
                    print("w Budowie")
