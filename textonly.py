import numpy as np

from Game_Khelne_Thalo import Game_Board




class Goat_ko_hisabkitab(Game_Board):
    
    

    def __init__(self) -> None:
         self.bakhra_on_board=np.empty((1,2))
         


         
    def update(self,row,col,flag):
        
        if flag!=1:
          self.flag=flag
          self.bakhra_on_board=np.append(self.bakhra_on_board, [[row,col]], axis=0)
          
        #else:
            
        print(self.bakhra_on_board)
        #print(self.bakhra_on_board[0])

         
    
    
          
    
    
    dead_bakhra=0
    total_bakhra_on_hand=20- dead_bakhra
         
         
         
    def datas(self):
         print("Total bakhra left in hand: ", self.total_bakhra_on_hand) 

    
    


     

class Baagh_ko_hisabkitab():
     
     pass    
     
          



base=Game_Board()
Goat=Goat_ko_hisabkitab()
game_over=False
turn=0


while not game_over:
        
        
        success=False
        if turn == 0:
              
              print(base.get_board())
              print()
              print("Bakhra ko Paalo")
              print()

              move_type=int(input("DO YOU WANT TO DROP PIECES(1) OR MOVE EXISTING PIECE ON THE BOARD(2)? : "))
              if move_type==1:
                
                while success==False:
                    
                    r_bakhra_to_place=int(input("Row to place bakhra (0-4): "))
                    
                    c_bakhra_to_place=int(input("Column to place bakhra (0-4): "))
                    
                    success=base.bakhra_placement(r_bakhra_to_place, c_bakhra_to_place)

                    
                Goat.update(r_bakhra_to_place,c_bakhra_to_place,base.bakhra_on_board)
                

              if move_type==2:

                while success==False:
                    r_bakhra_to_move=int(input("Row location of Bakhra(0-4): "))
                    c_bakhra_to_move=int(input("Column location of Bakhra (0-4): "))
                    if base.check_if_bakhra_exists(r_bakhra_to_move,c_bakhra_to_move):
                      
                      print()
                      
                      print()
                      r_bakhra_destination=int(input("Row destination of Bakhra (0-4): "))
                      c_bakhra_destination=int(input("Column Destination of Bakhra (0-4): "))
                      
                      print(base.available_spaces_filtering_blocks(True, False, r_bakhra_to_move,c_bakhra_to_move,r_bakhra_destination,c_bakhra_destination))
                      if base.available_spaces_filtering_blocks(True, False, r_bakhra_to_move,c_bakhra_to_move,r_bakhra_destination,c_bakhra_destination)==True:
                      
                        base.Bakhra_movement(r_bakhra_to_move,c_bakhra_to_move,r_bakhra_destination,c_bakhra_destination)
                        
                      else:
                        success=False
                        print("Invalid")
                        print(base.get_board())
                        
                    else:
                        print("Bakhrai chhaina")

              print("Total Bakhra on Board: ", base.bakhra_on_board)  
        else:
              
              print()
              print(base.get_board())
              print()
              
              print("Baagh ko Paalo")

              while success==False:
                    
                r_baagh_to_move=int(input("Row location of Baagh (0-4): "))
                c_baagh_to_move=int(input("Column location of Baagh (0-4): "))
                print()
                if base.check_bagh_exists(r_baagh_to_move,c_baagh_to_move):
                  
                
                  r_baagh_destination=int(input("Row destination of Baagh (0-4): "))
                  c_baagh_destination=int(input("Column Destination of Baagh (0-4): "))
                  base.available_spaces_filtering_blocks(False,True,r_baagh_to_move,c_baagh_to_move,r_baagh_destination,c_baagh_destination)
                  
                  success=base.baagh_movement(r_baagh_to_move,c_baagh_to_move,r_baagh_destination,c_baagh_destination)
                else:
                    print("Baagh nai chhaina")

              
        
        print()
        turn+=1
        turn=turn%2

              