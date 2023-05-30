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
       else:
           match button_input:
               case 1 : 
                   os.system("cls")
                   print("W budowie")               
               case 2 :
                   os.system("cls") 
                   print("w Budowei ")
               case _ : 
                   print(f"{self.NBoot} > nie rozpoznalem przycisku :/ potrzebujesze pomocy ?  ")
                            