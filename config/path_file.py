# Thư mục gốc
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
PATH_STORAGE = "storage"
# Tạo một biến gốc cho storage để các biến sau nối đuôi vào
BASE_PATH_STORAGE = BASE_DIR / PATH_STORAGE
# # --- ĐỊNH NGHĨA THỦ CÔNG CÁC ĐƯỜNG DẪN ---
# # 1. Các Folder (Đường dẫn tuyệt đối)
# PATH_PRODUCT_IMG = str(BASE_PATH_STORAGE / "manager_product_images")
# PATH_PRODUCT_ROI_PRODUCT_IMG = str(BASE_PATH_STORAGE / "manager_product_roi_images")

# # 2. Các File (Đường dẫn tuyệt đối)
# PATH_PRODUCT_DATA = str(BASE_PATH_STORAGE / "manager_product_data.json")
# PATH_PRODUCT_CHOOSE_PRODUCT = str(BASE_PATH_STORAGE / "choose_product_select.json")
# PATH_PRODUCT_MODEL = str(BASE_PATH_STORAGE / "unetpp.pth")
# PATH_FEATUERES_CFG_CAM = str(BASE_PATH_STORAGE / "features.cfg")
# PATH_INFORMATION_SOFTWARE = str(BASE_PATH_STORAGE / "information_software.json")
# PATH_CONFIG_SOFTWARE = str(BASE_PATH_STORAGE / "config_software.json")
# PATH_CONFIG_CALIBRATION = str(BASE_PATH_STORAGE / "config_calibration.json")
# # --- ĐỊNH NGHĨA ĐƯỜNG DẪN TƯƠNG ĐỐI (Dùng cho Frontend hoặc lưu JSON) ---
# # Nếu bạn muốn lưu vào JSON mà không có ổ đĩa (C:\...)
# REL_PATH_PRODUCT_IMG = f"{PATH_STORAGE}/manager_product_images"

#---------------------
NAME_FOLDER_AI = "model_AI"
NAME_FOLDER_DETECT_EGDE = "detect_egde"
NAME_FOLDER_UNET = "unetpp.pth"  # Cai  nay su dung mo hinh chung de nhan dien canh khong dung mo hinh rieng cho tung anh
PATH_FILE_UNET_DETECT = BASE_PATH_STORAGE/NAME_FOLDER_AI/NAME_FOLDER_DETECT_EGDE/NAME_FOLDER_UNET   # Lam dai de cho do nham voi yolo
# print("PATH_FOLDER_UNET_DETECT",PATH_FILE_UNET_DETECT)
NAME_FOLDER_DETECT_ABNORMAL ="detect_abnormal"  # Cai nay dung mo hinh rieng cho moi vi tri anh can xu ly 
NAME_FOLDER_PATCHCORE =  "patch_core"
PATH_FOLDER_PATCHCORE_ABNORMAL_DETECT =   BASE_PATH_STORAGE/NAME_FOLDER_AI/NAME_FOLDER_DETECT_ABNORMAL/NAME_FOLDER_PATCHCORE
# print("PATH_FOLDER_PATCHCORE_ABNORMAL_DETECT",PATH_FOLDER_PATCHCORE_ABNORMAL_DETECT)








