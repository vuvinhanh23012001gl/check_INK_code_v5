
from services.vision.detect.egde.unet_plus.mask_and_polygon import Mask as model_unet
class  Macro():
    def __init__(self,model:model_unet):
        self.model = model

    def handler(self,img):
       # ham nay tra ve mask va polygon 
       return self.model.get_mask(img)
        


    



    
    

        

        
        
