import os
import GlowneMenu
Boot="Marks"
System="Mxrs"
def menu():
    os.system("cls")
    print(f"\t\t\t\t\t\tWitam w oprogramowaniu statystycznym {System} \n"
           "\t\t\t\tKtóry ma za zadanie pomoć ci w twojej pracy i rozwiaywać twoje problemy\n "
          f"\t\t\t\t\tProgram tez zawiera pomocnika który nazywa sie {Boot}\n"
          f"\n{Boot} > Witam cie Uzytkowniku nazywam sie {Boot} a ty jak masz na imie ? ")
    User_name_input=input("Podaj swoje imie: ")    
    odpowiedzi(User_name_input,Boot)

def kotrola(User_name_input):
   
   if len(User_name_input)==0:
       return False  

   elif len(User_name_input) < 2 :
       return False

   else :
      return True


def odpowiedzi(User_name_input,Boot):
   
   if kotrola(User_name_input)==True:
       print(f"{Boot} > Witam cie {User_name_input} zapraszam cie do programu i zycze ci milego uzywania tego oprogramownia\n")
       przejscie(User_name_input,Boot)

   else:
       print(f"{Boot} > Przytkor mi bardzo ze nie poznalem towojego imienia moze :( lecz licze  ze podasz go  nastepnym razem )")

def przejscie(User_name_input,Boot):
    try: 
        Button_Input=int(input(f"{Boot} > Kliknij Key 1 By wejść do Menu: "))
    except ValueError :
        os.system("cls")
        print(f"{Boot} > Coś poszło nie tak sproboj jeszcze raz {User_name_input} ")
        przejscie(User_name_input,Boot)
         
    else:
        match Button_Input : 
            case 1 : 
                os.system("cls")
                M=GlowneMenu.Menu(Boot,User_name_input)
                M.przywitanie()
                M.menu_glowne()
                M.button_key()

            case _ : 
                os.system("cls")
                print(f"{Boot} > Ups Chyba  nie ma takiego klawisza nic nie szkodzi {User_name_input} zdarza sie sproboj jeszcze raz ")
                przejscie(User_name_input,Boot)

menu()    