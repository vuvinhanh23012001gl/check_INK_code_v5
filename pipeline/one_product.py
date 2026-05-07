
from core.context.run_one_product import RunOneProduct as CtxOneProduct
from .macro import Macro as PipelineMacro
from models import Frame
from handler.frame_unet_convert_IAI import FrameUnetConvertIAI
from services import ModelUnet,MaskUnet
from config import UnetConfig
import time
import queue
import threading
import cv2 

task_queue = queue.Queue()
def producer():
    print("Đã vào luồng này")
    tasks = [
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture15.png", "command": (0,0)},
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture16.png", "command": (1,0)},
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture17.png", "command": (2,0)},
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture18.png", "command": (3,0)},
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture19.png", "command": (4,0)},
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture20.png", "command": (5,0)},
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture21.png", "command": (6,0)},
        {"image": r"C:\Users\anhuv\Desktop\code_v5\img\Picture22.png", "command": (7,0)},
    ]
    for task in tasks:
        print("push vao queue")
        task_queue.put(task)
        time.sleep(0.5)


class PipelineOneProduct():
    def __init__(self,ctxOneProduct:CtxOneProduct):
        
        t1 = threading.Thread(target=producer)
        t1.start()
        t1.join()
        print("Done!")






        self.ctxOneProduct = ctxOneProduct
        # Gia du lieu
        self.ctxOneProduct.machine.horizontal_ration = 300
        self.ctxOneProduct.machine.vertical_ration   =  300
        self.ctxOneProduct.machine.status = True
        self.ctxOneProduct.machine.org_machine_IAI =  (0,0)
        self.ctxOneProduct.machine.org_mul_product = (0,0)
        self.ctxOneProduct.machine.max_coordinate = (10,10)
        self.ctxOneProduct.machine.polygons_arr_one_product = []  # Mang lưu danh sách polygon
        self.ctxOneProduct.machine.width_of_the_inspection_area_px, self.ctxOneProduct.machine.height_of_the_inspection_area_px  =  self.ctxOneProduct.machine.calculate_width_height_total_frame()

        #setupxong ctx        
        
    
       
        
        

        config =  UnetConfig()
        model_unet = ModelUnet(config)
        modler_mask = MaskUnet(model_unet)
        self.handler_macro = PipelineMacro(modler_mask)
        # Gia du lieu
        # self.macro_pipeline.handler()
        

        
    def handler(self):
        pass
        # mask_grafting()
        

    def mask_grafting(self):
        while True:
            try:
                task = task_queue.get(timeout=0.1)
            except queue.Empty:
                continue
            print("queue đã nhận được")
            image = task["image"]
            img = cv2.imread(image)
            command = task["command"]
            print(f"Đang xử lý: {image} | command: {command}")
            time.sleep(0.1)
            _,polygon = self.handler_macro.handler(img)
            object_frame =  FrameUnetConvertIAI(self.ctxOneProduct.machine,polygon,img.shape[0],command)
            status,polygon_convert,msg = object_frame.convert_polygons_to_region_to_polygon()
            # print("status,polygon_convert,msg",status,polygon_convert,msg)
            if status :
                self.ctxOneProduct.machine.polygons_arr_one_product.append(polygon_convert)
                # object_frame.polygon_draw_mask(polygon_convert)
                object_frame.polygon_draw_mask(self.ctxOneProduct.machine.polygons_arr_one_product)
                
               





            # if self.ctxOneProduct.machine.polygons_arr_one_product is not None and len(self.ctxOneProduct.machine.polygons_arr_one_product) > 0:
            #         object_frame.show_img(self.ctxOneProduct.machine.polygons_arr_one_product)
     


 



from models.frame import Frame
from models.machine import Machine
frame = Frame()
machine = Machine()
ctx = CtxOneProduct(frame,machine)



p_line = PipelineOneProduct(ctx)
p_line.mask_grafting()

        
