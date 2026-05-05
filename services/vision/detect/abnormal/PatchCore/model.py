from services.vision.base_AI import BaseAI
from dataclasses import dataclass
import torchvision.transforms as T
from torchvision.models import resnet18, ResNet18_Weights
from sklearn.neighbors import NearestNeighbors
import numpy as np
import cv2
import torch

@dataclass
class PatchCore:
    path:str = r"C:\Users\anhuv\Desktop\code_v5\storage\model_AI\detect_abnormal\patch_core\features.npy"    # Gia lap du lieu

class ModelPatchCore(BaseAI):
    def __init__(self,config:PatchCore):
        self.config  = config
        self.load_model()

        
    def load_model(self):
        print("load model")
        features = np.load(self.config.path) 
        nbrs = NearestNeighbors(n_neighbors=1).fit(features)
        model = resnet18(weights=ResNet18_Weights.DEFAULT)
        model = torch.nn.Sequential(*list(model.children())[:-2])  # remove FC + avgpool
        model.eval()
        
    def preprocess(self):
        # tiền xử lý
        pass
    def predict(self):
        # du doan
        pass
    def unload(self):
        # giai phong mo hinh tren ram
        pass
    def warmup(self):
        # chạy trước mô hình 1 lần
        pass
        
P1_Config = PatchCore()
M_Patch_Core = ModelPatchCore(P1_Config)
