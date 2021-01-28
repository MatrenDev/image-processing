# Packages
from PIL import Image, ImageFilter 
import cv2 
import numpy as np 

# Load Images
image_default = Image.open(r'images/default.png') 
img_default_2 = cv2.imread('images/default.png', 0)    
documentation = Image.open(r'images/documentation.png')
# Input Data
lang = int(input("Type Language - Polish - 1, English - 2 | Podaj jezyk - Polski - 1, Angielski - 2"))

if lang == 1:
    value = int(input("Podaj 'kernel size', np. 3 da nam 3x3: "))
else:
    value = int(input("Type 'kernel size', for example 3 is 3x3: "))

# Max & Min filter
max_image = image_default.filter(ImageFilter.MaxFilter(size = value)) 
min_image = image_default.filter(ImageFilter.MinFilter(size = value)) 
   
# Image - Average processing
m, n = img_default_2.shape 

print(m)
print(n)

mk = np.ones([value, value], dtype = int) 
mk = mk / 9

img_gen = np.zeros([m, n]) 
img_gen2 = img_gen
for i in range(1, m-1): 
    for j in range(1, n-1): 
        data = img_default_2[i-1, j-1]*mk[0, 0]
        data += img_default_2[i-1, j]*mk[0, 1]
        data += img_default_2[i-1, j+1]*mk[0, 2]
        data += img_default_2[i, j-1]*mk[1, 0]
        data += img_default_2[i, j]*mk[1, 1]
        data += img_default_2[i, j + 1]*mk[1, 2]
        data += img_default_2[i + 1, j-1]*mk[2, 0]
        data += img_default_2[i + 1, j]*mk[2, 1]
        data += img_default_2[i + 1, j + 1]*mk[2, 2]
    
        img_gen[i, j]= data 
          
img_gen = img_gen.astype(np.uint8)

# Image - Median
for i in range(1, m-1): 
    for j in range(1, n-1): 
        data_v2 = [img_default_2[i-1, j-1], 
               img_default_2[i-1, j], 
               img_default_2[i-1, j + 1], 
               img_default_2[i, j-1], 
               img_default_2[i, j], 
               img_default_2[i, j + 1], 
               img_default_2[i + 1, j-1], 
               img_default_2[i + 1, j], 
               img_default_2[i + 1, j + 1]] 
          
        data_v2 = sorted(data_v2) 
        img_gen2[i, j]= data_v2[4] 
  
img_gen2 = img_gen2.astype(np.uint8) 

# Results
cv2.imwrite('results/average.png', img_gen) 
cv2.imwrite('results/median.png', img_gen2) 
max_image.show() 
min_image.show()
documentation.show()
