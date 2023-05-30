import os 
class Kalkulaotr:
    def __init__(self,NBoot,User):
        self.NBoot=NBoot
        self.User=User
        
        
    def menu_kalkulatora(self):
        print(f"{self.NBoot} > Witam cie w Kalkulatorze  {self.User} \n"
              "wybierz jaki kalkulator cie interesuje ")
        print("1 : Kalkulator Statystyczny \n"
              "2 : Kalkulator Matematyczny \n"
              "3 : Kalkulator Wynagrodzen \n "
              "4 : Kalkulatro Podatku ") 

    def button_key(self):

       try: 
           button_input=int(input(f"{self.NBoot} > wpisz co chcesz zrobic : "))
       except ValueError:
           print(f"{self.NBoot} > upss chyba nie ten klawisz jeżeli masz problem lub potrzebujesz pomocy  wejdzi w dział pomoc")
           self.help_button()
       else:
           match button_input:
               case 1 : 
                   os.system("cls")
                   print("W budowie")               
               case 2 :
                   os.system("cls")            #Przyciski nawigacyjne 
                   print("w Budowei ")
               case _ :
                   os.system("cls") 
                   print(f"{self.NBoot} > nie rozpoznalem przycisku :/ potrzebujesze pomocy ?  ")
                   self.help_button()

                            
     
          
    def help_button(self):
        
        
        try:
         hellp_button_input=int(input("1 : pomoc \n"))   # centrum pomocy 
        except ValueError:
            print("uu nie ten przycisk ")

        else:
            match hellp_button_input:
                case 1 : 
                    print("Centrum pomocy")    
