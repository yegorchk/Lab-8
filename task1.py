import matplotlib.pyplot as plt
import numpy as np
import cv2
import pylab 

pylab.rcParams['figure.figsize'] = (10.0, 8.0)

input_image = cv2.imread('variant-4.jpeg')

b, g, r = cv2.split(input_image)

zero = np.zeros_like(b)
blue_only = cv2.merge([b, zero, zero])

plt.imshow(cv2.cvtColor(blue_only, cv2.COLOR_BGR2RGB))
plt.title('Blue Channel Only')
plt.axis('off')
plt.show()
