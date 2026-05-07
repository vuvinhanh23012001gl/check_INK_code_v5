from services import ProductService
from path_structure import ProductPathData
from responsibility import ProductRepository
from config import ProductConfig
import webbrowser
import threading

class Container:
    def __init__(self):

        self.obj_product_path_data = ProductPathData(ProductConfig.path)
        self.obj_product_reponsitory = ProductRepository(self.obj_product_path_data)
        self.obj_product_service = ProductService(self.obj_product_reponsitory)




        
        def open_browser():
            webbrowser.open("http://127.0.0.1:8000")
        threading.Thread(target = open_browser).start()













        print("..--------------------------------.. init Complete ...----------------------------------.")
    def stop(self):
        print("....Stopping Service....")
        # Viết các hàm thoát ở đây


def create_container():
        return Container()
