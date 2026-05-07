# Lớp này để tối ưu code sao cho gọn trong pipe line
from typing import Optional,Tuple
import numpy as np
import copy 
from models import Machine
import cv2


class FrameUnetConvertIAI:
    # Lớp này để tính toán mask bằng Unet trong pipeline

    def __init__(self,ctx_machine:Machine,polygon,height_frame_img:int,coordinate_current:Optional[Tuple[int,list]]):  #machine:Machine la kieu ctx 
        
        self.ctx_machine =  ctx_machine
        self.polygon = polygon
        self.height_frame_img = height_frame_img
        self.coordinate_current = coordinate_current



    def convert_polygons_to_region_to_polygon(self):
        """
        Đầu ra: 
            status: trạng thái chuyển đổi xử lý (True/False
            polygon_convert_px: chuyển tọa độ của polygon vào hệ trục tọa độ của máy
            msg: thông báo lỗi hoặc trạng thái lỗi
        Chức năng:
        """
        if self.polygon is not None and len(self.polygon) > 0:
            polygon_convert_botom_left = self.convert_coodinate_top_left_to_bottom_left()  # đổi hệ trục tọa độ polygon tuwf top left sang bottom left
            return self.convert_pixel_system_polygons(polygon_convert_botom_left) # chuyển tọa độ polygon sang hệ trục tọa độ chính của hệ px

    
    def convert_polygons_to_region_to_mask(self):
        """
        Đầu ra: 
            status: trạng thái chuyển đổi xử lý (True/False
            polygon_convert_px: chuyển tọa độ của polygon vào hệ trục tọa độ của máy
            msg: thông báo lỗi hoặc trạng thái lỗi
        Chức năng:
        """
        if self.polygon is not None and len(self.polygon) > 0:
            polygon_convert_botom_left = self.convert_coodinate_top_left_to_bottom_left()  # đổi hệ trục tọa độ polygon tuwf top left sang bottom left
            return self.polygons_to_mask(polygon_convert_botom_left) # chuyển tọa độ polygon sang hệ trục tọa độ chính của hệ px
    

   
    def show_img(self,img, win_name="Image", wait=0):
            cv2.imshow(win_name, img)
            cv2.waitKey(wait)
            cv2.destroyAllWindows()



    def convert_coodinate_top_left_to_bottom_left(self):

        """Đầu vào:  polygons: mảng/list tọa độ (shape: (M,N,1,2) hoặc (N,1,2) hoặc (N,2))img_height: chiều cao ảnh
        Đầu ra: polygons_copy: tọa độ mới (gốc dưới bên trái)
        Chức năng: Đổi hệ tọa độ từ gốc trên trái → gốc dưới trái bằng cách đảo trục Y
        Lỗi có thể gặp: Shape không đúng → raise lỗi, img_height sai → tọa độ bị lệch,Input không phải numpy/list hợp lệ"""
        polygons_copy = np.array(self.polygon, copy = True)  # copy toàn bộ
        if polygons_copy.ndim == 4:      # (M, N, 1, 2)
            polygons_copy[:, :, :, 1] = self.height_frame_img - polygons_copy[:, :, :, 1]
        elif polygons_copy.ndim == 3:    # (N, 1, 2)
            polygons_copy[:, :, 1] = self.height_frame_img - polygons_copy[:, :, 1]
        elif polygons_copy.ndim == 2:    # (N, 2)
            polygons_copy[:, 1] = self.height_frame_img - polygons_copy[:, 1]
        else:
            raise (f"Shape không hợp lệ: {polygons_copy.shape}")
        return polygons_copy
    



    def convert_pixel_system_polygons(self,polygon_convert):
        """
        Input: polygon_convert
        Output: polygon_convert_copy đã xoay pixel
        Chức năng: chuyển tọa độ phán định lên tọa độ của gốc của vùng xét
        """
        polygon_convert_copy = copy.deepcopy(polygon_convert)
        ok, delta, msg = self.compare_the_original_command_coordinates()
        if not ok:
            return False, None, msg
        dx, dy =  delta
        dx_pixel = dx * self.ctx_machine.horizontal_ration
        dy_pixel = dy * self.ctx_machine.vertical_ration
        print("dx_pixel",dx_pixel , dy_pixel)
        for contour in polygon_convert_copy:
            contour[0][0] = contour[0][0] + dx_pixel
            contour[0][1] = contour[0][1] + dy_pixel
        return True,polygon_convert_copy,"OK"
    


    def polygons_to_mask(self,image_shape, polygons):
        """
        Chuyển danh sách polygons thành mask nhị phân.

        Args:
            image_shape: (height, width)
            polygons: list các polygon, mỗi polygon là list điểm [(x1,y1), (x2,y2), ...]

        Returns:
            mask: numpy array shape (H, W), giá trị 0 hoặc 255
        """
        h, w = image_shape
        mask = np.zeros((h, w), dtype=np.uint8)

        for poly in polygons:
            pts = np.array(poly, dtype=np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(mask, [pts], color=255)
        return mask


    def compare_the_original_command_coordinates(self):
        """
        Input: coordinate_current (list/tuple 2 giá trị)
        Output: (True/False, (dx, dy) hoặc None, status)
        Chức năng: so sánh tọa độ hiện tại với org_coordinate và tính độ lệch (dx, dy)
        Lỗi: sai type / sai length coordinate_current / không ép int được
        """

        if not isinstance(self.coordinate_current, (list, tuple)) or len(self.coordinate_current) != 2:
            return False, None, "ERROR_COORDINATE_NOT_TYPE"
        x, y  = map(int, self.coordinate_current)
        x_org, y_org = map(int, self.ctx_machine.org_mul_product)
        distance_x = x - x_org
        distance_y = y - y_org
        if distance_x >= 0 and distance_y >= 0:
            return True, (distance_x,distance_y), "OK"
        return False, (distance_x,distance_y), "ERRO_Tọa độ điểm ở quá gốc"        
           


    def polygon_draw_mask(self, polygon_convert):
        """Hàm này vẽ được cả polygon_convert và arr polygon_convert"""
        # ===== CASE 1: single polygon (N,2) =====
        if isinstance(polygon_convert, np.ndarray) and polygon_convert.ndim == 2:
            arr_polygons = [polygon_convert]

        # ===== CASE 2: (N,1,2) or (N,2,1) =====
        elif isinstance(polygon_convert, np.ndarray) and polygon_convert.ndim == 3:
            arr_polygons = [polygon_convert]

        # ===== CASE 3: list of polygons =====
        elif isinstance(polygon_convert, (list, tuple)):
            arr_polygons = polygon_convert

        else:
            print("❌ Unsupported polygon format")
            return

        mark = self.convert_polygon_mask_bottom_left(
            self.ctx_machine.width_of_the_inspection_area_px,
            self.ctx_machine.height_of_the_inspection_area_px,
            arr_polygons
        )

        self.show_img(mark)



    def convert_polygon_mask_bottom_left(self, w, h, arr_polygons, out_size=(1344, 840)):
        w, h = int(w), int(h)
        mask = np.zeros((h, w), dtype=np.uint8)

        # đảm bảo luôn là list
        if isinstance(arr_polygons, np.ndarray) and arr_polygons.dtype == object:
            arr_polygons = list(arr_polygons)

        for poly in arr_polygons:
            poly = np.asarray(poly)

            # ===== chuẩn hoá về (N,2) =====
            if poly.ndim == 3:
                poly = poly.reshape(-1, 2)
            elif poly.ndim != 2 or poly.shape[-1] != 2:
                continue

            poly = poly.copy()

            # ===== flip Y (bottom-left origin) =====
            poly[:, 1] = h - 1 - poly[:, 1]

            poly = poly.astype(np.int32).reshape(-1, 1, 2)
            cv2.fillPoly(mask, [poly], 255)

        # resize output
        out_w, out_h = out_size
        mask = cv2.resize(mask, (out_w, out_h), interpolation=cv2.INTER_NEAREST)

        return mask
    






