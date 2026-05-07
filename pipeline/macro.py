
from services import ModelUnet
class  Macro():
    def __init__(self,model:ModelUnet):
        self.model = model

    def handler(self,img):
       # ham nay tra ve mask va polygon 
       return self.model.get_mask(img)
        


    



    
    

        

        
        
