import torch 
from matplotlib import pyplot as plt
import numpy as np
import cv2


model = torch.hub.load('ultralytics/yolov5', 'yolov5s') # load pretained torchub model
image = '/content/daddy_trudeau.jpeg'
results = model(image)
results.print()

class FaceDetection:
    def __init__(self) -> None:
        pass

# shows 
%matplotlib inline
plt.imshow(np.squeeze(results.render()))
plt.show

"""""""