import numpy as np


class Game_Board():
    def __init__(self):
        self.board = np.zeros((5, 5))
        self.board[0, 0] = 1
        self.board[4, 0] = 1
        self.board[0, 4] = 1
        self.board[4, 4] = 1
        self.bakhra_on_board=0
        
    def get_board(self):
        return self.board
    
    def available_moves(self,row,column):
         av_spaces=[]
         for x in (-1,0,1):
              for j in (-1,0,1):
                   if row+x>=0 and column+j>=0 and (row+x!=row or column+j!=column):
                    av_spaces.append((row+x,column+j))
         #print(av_spaces)

         items=len(av_spaces)           
         if (row+column)%2!=0:
            to_del=[]
            for x in range(items):
                 #print(x)
                 if av_spaces[x][0]!=row and av_spaces[x][1]!=column:
                      to_del.append((av_spaces[x][0],av_spaces[x][1]))
            #print(to_del) 
            final_av_spaces=[x for x in av_spaces if x not in to_del]
                 
         else:
              final_av_spaces=av_spaces             
         
         #print(final_av_spaces) 
         array_of_available_moves=np.array(final_av_spaces)
         #print("Available vertices on board: ", array_of_available_moves)
         return(array_of_available_moves)
    
    def available_spaces_filtering_blocks(self,Goat,Tiger,row,col,row2,col2):
        block_filtered_spaces=[]
        position=np.array([[row,col]])
        
        if Goat==True:
            moves=self.available_moves(row,col)
            print(moves)
            for x in moves:
                
                r=x[0]
                c=x[1]
                
                if self.board[r,c]==0:
                  block_filtered_spaces.append(x)
            array_block_filtered_spaces= np.array(block_filtered_spaces)      
            print("Available spaces after filtering the blocks: ", array_block_filtered_spaces )      
            x=self.check_if_dest_in_available_moves(row2,col2,array_block_filtered_spaces)
            return x
        if Tiger==True:
            moves=self.available_moves(row,col)
            print(moves)
            for x in moves:
                
                r=x[0]
                c=x[1]
                
                if self.board[r,c]==0:
                  block_filtered_spaces.append(x)
                if self.board[r,c]==2:
                    vec=[(r-row,c-col)]
                    array_vec=np.array(vec)
                    disp_array=2*array_vec
                    potential_space=position+disp_array
                    if self.board[(potential_space[0][0]),(potential_space[0][1])]==0:
                        block_filtered_spaces.append(x)
                        
                        #to run kill function
                            
            array_block_filtered_spaces= np.array(block_filtered_spaces)
            print(array_block_filtered_spaces)
            pass
    
    
    def bakhra_placement(self, row, column):
        
        if self.board[row, column] == 0:
            self.board[row, column] = 2
            self.bakhra_on_board+=1
            
            return True
        else:
            print("Unable to place Bakhra")
            return False
    
    
    def Bakhra_movement(self,row,col,row2,col2):
        self.board[row,col]=0
        self.board[row2,col2]=2
        
            
                
            
            

     
    def baagh_movement(self,row1,column1,row2,column2):
         
        
            
                
                if self.board[row2,column2]==0:
                    self.board[row2,column2]=1
                    self.board[row1,column1]=0
                    return True
                
                
            
                else:
                    print("Unable to move")
                    return False
        
    
    def check_if_bakhra_exists(self,row,column):
         return self.board[row,column]==2
    
    def check_bagh_exists(self,row,col):
        return self.board[row,col]==1
         
    
      
                    
       

    def check_if_dest_in_available_moves(self,row_to_move,col_to_move,array,):

         
         
         to_move=np.array((row_to_move,col_to_move))
         to_move_array=to_move.reshape(1,2)
         return to_move_array
         c=False
         for x in array:
             while c==False:
                if array[x]==to_move_array:
                    c=True
         return c 
        
    
         
    
    

        
         