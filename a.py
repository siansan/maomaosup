import cv2
from matplotlib import pyplot as plt
for i in range(0,4):
    image = cv2.imread(f"C:/Users/sian/Desktop/test/new_mem_nobg/arrow_pic/{i}.jpg")
    img1 = cv2.resize(image, (96, 96), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(f'C:/Users/sian/Desktop/test/new_mem_nobg/arrow_pic/{i}.jpg', img1)