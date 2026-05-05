# Nếu muốn lấy mas thì chạy file này
# Nếu muốn lấy polyon thì chạy cái này

from .model import ModelUnet
import numpy as np
import cv2


class Mask:
    def __init__(self,model:ModelUnet):
        self.model = model

    def get_mask(self,img):
        mask = self.model.predict(img)
        mask_clean = self.clean_mask_opening(mask,self.model.config.kernel) # Loc nhieu xung quanh
        polygon  = self.find_largest_external_polygon(mask_clean,self.model.config.epsilon_ratio,self.model.config.min_area)
        # self.draw_polygon(img,polygon)
        # self.show_img(img)
        # self.show_mask(mask_clean)
        return mask_clean,polygon


    def clean_mask_opening(self, mask, kernel_size=3, iterations=1):
            """
            Làm sạch mask bằng phép Morphology Opening (Erosion + Dilation)

            Parameters:
                mask (np.ndarray): Ảnh mask nhị phân (0 hoặc 255)
                kernel_size (int): Kích thước kernel (ví dụ: 3 → kernel 3x3)
                iterations (int): Số lần lặp phép morphology

            Returns:
                np.ndarray: Mask đã được làm sạch
            """
            # Đảm bảo mask là uint8
            mask = mask.astype(np.uint8)

            # Tạo kernel
            kernel = np.ones((kernel_size, kernel_size), np.uint8)

            # Morphology Opening
            mask_clean = cv2.morphologyEx(
                mask,
                cv2.MORPH_OPEN,
                kernel,
                iterations=iterations
            )
            return mask_clean
    

    def show_mask(self, mask , window_name="Mask"):
        """
        Hiển thị mask đơn giản
        """
        mask = mask.astype(np.uint8)
        cv2.imshow(window_name, mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_img(self, image, window_name="Image"):
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def find_largest_external_polygon(self, mask, Approx_value,min_area=100):
        """
        Tìm contour ngoài cùng, lọc theo diện tích và xấp xỉ polygon
        Parameters:
            mask (np.ndarray): Mask nhị phân (0 hoặc 255)
            min_area (int): Diện tích tối thiểu để giữ contour

        Returns:
            poly (np.ndarray | None): Polygon xấp xỉ contour lớn nhất
        """
        mask = mask.astype(np.uint8)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if not contours:
            return None

        # 🔹 Lọc contour theo diện tích
        valid_contours = [
            cnt for cnt in contours
            if cv2.contourArea(cnt) >= min_area
        ]

        if not valid_contours:
            return None
    
        # 🔹 Lấy contour lớn nhất
        cnt = max(valid_contours, key=cv2.contourArea)

        # 🔹 Approx polygon (chuẩn hình học)
        epsilon = Approx_value * cv2.arcLength(cnt, True)
        #         epsilon = 0.002 * cv2.arcLength(cnt, True)   cung ok
        poly = cv2.approxPolyDP(cnt, epsilon, True)

        return poly
    

    def draw_polygon(self, image, poly, color=(0, 255, 0), thickness=2):
        """
        Vẽ polygon lên ảnh gốc.
        
        Parameters:
            image (np.ndarray): Ảnh gốc (BGR) để vẽ lên.
            poly (np.ndarray): Kết quả trả về từ hàm find_largest_external_polygon.
            color (tuple): Màu sắc của đường vẽ (B, G, R). Mặc định là màu xanh lá.
            thickness (int): Độ dày của đường vẽ.
            
        Returns:
            image (np.ndarray): Ảnh đã được vẽ polygon.
        """
        if poly is not None:
            # cv2.polylines yêu cầu một list các arrays [poly]
            # isClosed=True để đóng kín điểm đầu và điểm cuối
            cv2.polylines(image, [poly], isClosed=True, color=color, thickness=thickness)
        
        return image
    





# img = cv2.imread(r"C:\Disk D\Project\Python_Detect_Width_Line\dataset\data_28_img\img\Picture2.png")
# from config.AI import Unet
# test = Unet()            
# h1  = ModelUnet(test)
# mask  = Mask(h1)
# mask.get_mask(img)
