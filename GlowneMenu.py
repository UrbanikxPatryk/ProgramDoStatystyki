class Menu:
    def __init__(self,Boot,User_name_input) :
       self.User=User_name_input
       self.NBoot=Boot

    def menu_glowne(self):
          print(f"\t\t{self.NBoot} > Witam cie w  Menu Glownym {self.User} ")   