from typing import Optional,Tuple

class Machine:
    def __init__(self):
        self.org_machine_IAI:Optional[tuple[int,list]] =  None
        self.org_mul_product:Optional[tuple[int,list]]=  None
        self.max_coordinate :Optional[tuple[int,list]]  = None  # toa do vung mask chay
        self.horizontal_ration:float = 0
        self.vertical_ration:float = 0
        self.polygons_arr_one_product = []
        self.status:bool = False
        
        self.height_of_the_inspection_area_px  = 0 #  chiều cao khung đang xet 
        self.width_of_the_inspection_area_px  = 0 #  chiều ngang khung đang xet 

    def calculate_width_height_total_frame(self) -> Tuple:
        """
        Input: org_coordinate, max_coordinate, h_ratio, v_ratio
        Output: (width_px, height_px)
        Chức năng: tính kích thước frame (unit → pixel)
        Lỗi:None
        """
        #  self.width_of_the_inspection_area_px:int = 0
        #  self.height_of_the_inspection_area_px:int = 0
        ox, oy = self.org_mul_product[:2]
        mx, my = self.max_coordinate[:2]
        # tính theo unit
        width_unit = mx - ox
        height_unit = my - oy
        # convert sang pixel
        width_px = width_unit * self.horizontal_ration
        height_px = height_unit * self.vertical_ration
        return width_px, height_px
    
