"""import excel2img
excel2img.export_img("test.xlsx", "test.png")"""



import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('test.png')
imgplot = plt.imshow(img)
plt.show()



"""
import os
os.startfile("show.xlsx", "print")
"""