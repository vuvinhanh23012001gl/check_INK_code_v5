# Thư mục gốc
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
PATH_STORAGE = "storage"
# Tạo một biến gốc cho storage để các biến sau nối đuôi vào
BASE_PATH_STORAGE = BASE_DIR / PATH_STORAGE

NAME_FOLDER_AI = "model_AI"
NAME_FOLDER_DETECT_EGDE = "detect_egde"
NAME_FOLDER_UNET = "unetpp.pth"  # Cai  nay su dung mo hinh chung de nhan dien canh khong dung mo hinh rieng cho tung anh
PATH_FILE_UNET_DETECT = BASE_PATH_STORAGE/NAME_FOLDER_AI/NAME_FOLDER_DETECT_EGDE/NAME_FOLDER_UNET   # Lam dai de cho do nham voi yolo
# print("PATH_FOLDER_UNET_DETECT",PATH_FILE_UNET_DETECT)
NAME_FOLDER_DETECT_ABNORMAL ="detect_abnormal"  # Cai nay dung mo hinh rieng cho moi vi tri anh can xu ly 
NAME_FOLDER_PATCHCORE =  "patch_core"
PATH_FOLDER_PATCHCORE_ABNORMAL_DETECT =  BASE_PATH_STORAGE/NAME_FOLDER_AI/NAME_FOLDER_DETECT_ABNORMAL/NAME_FOLDER_PATCHCORE
# print("PATH_FOLDER_PATCHCORE_ABNORMAL_DETECT",PATH_FOLDER_PATCHCORE_ABNORMAL_DETECT)

NAME_FOLER_DATA = "data"
PATH_FOLDER_DATA = BASE_PATH_STORAGE / NAME_FOLER_DATA
#print("PATH_FOLDER_DATA",PATH_FOLDER_DATA)








