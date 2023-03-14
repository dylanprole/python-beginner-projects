import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

try:
    plt.close('all')
    print('Closing figures...')
except:
    print('No figures open. Continuing...')

class Image(object):
    def __init__(self, png):
        self.png = cv.imread(png)
        self.dimensions = [len(self.png), len(self.png[0])]

    def size(self):
        return self.dimensions
    
    def image(self):
        return self.png
    
    def grayscale(self):
        greyscale_img = self.png.copy()
        for row in range(self.dimensions[0]):
            for col in range(self.dimensions[1]):
                average = sum(self.png[row][col])//3
                greyscale_img[row][col] = [average]*3
        return greyscale_img
    
    def channel(self, channel_colour):
        try:
            channel_dict = {'b':0, 'g':1, 'r':2}
            channel_number = channel_dict[channel_colour]
            new_image = self.png.copy()
            channels = [0,1,2]
            channels.remove(channel_number)
            for row in range(self.dimensions[0]):
                for col in range(self.dimensions[1]):
                    for channel in channels:
                        new_image[row][col][channel] = 0
            return new_image
        except:
            print('Incorrect colour channel entered')
            return False
        
    def edge_detect(self):
        edges = self.png.copy()
        x_mult = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        # y_mult = [-2, -2, -1, 0, 0, 0, 1, 2, 1]
        # Change the first and last columns/rows to black
        black_row = [0, 1, self.dimensions[0] - 2, self.dimensions[0] - 1]
        black_col = [0, 1, self.dimensions[1] - 2, self.dimensions[1] - 1]
        for row in range(self.dimensions[0]):
            for col in range(self.dimensions[1]):
                if row in black_row or col in black_col:
                    edges[row][col] = [0]*3
                else:
                    x_kernel = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                    for kernel_row in range(3):
                        for kernel_col in range(3):
                            x_kernel[kernel_row][kernel_col] = sum(self.png[row + (kernel_row - 1)][col + (kernel_col - 1)])//3
                    x_value = sum(sum(np.multiply(x_mult,x_kernel)))
                    edges[row][col] = [x_value]*3
        return edges
    
cat = Image('cats.png')
cat_image = cat.image()
cat_edges = cat.edge_detect()
print(cat_edges)

fig, ax = plt.subplots(1, 2, figsize=(16, 8))
fig.tight_layout()

img_1 = ax[0]
img_1.imshow(cv.cvtColor(cat_image, cv.COLOR_BGR2RGB))
img_1.set_title("Original")
img_1.axis('off')

img_2 = ax[1]
img_2.imshow(cv.cvtColor(cat_edges, cv.COLOR_BGR2RGB))
img_2.set_title("Edges")
img_2.axis('off')

plt.show()

# cat_gray = cat.grayscale()
# cat_red = cat.channel('r')
# cat_green = cat.channel('g')

# fig, ax = plt.subplots(2, 2, figsize=(16, 8))
# fig.tight_layout()

# img_1 = ax[0][0]
# img_1.imshow(cv.cvtColor(cat_image, cv.COLOR_BGR2RGB))
# img_1.set_title("Original")
# img_1.axis('off')

# img_2 = ax[0][1]
# img_2.imshow(cv.cvtColor(cat_red, cv.COLOR_BGR2RGB))
# img_2.set_title("Red")
# img_2.axis('off')

# img_3 = ax[1][0]
# img_3.imshow(cv.cvtColor(cat_green, cv.COLOR_BGR2RGB))
# img_3.set_title("Green")
# img_3.axis('off')

# img_4 = ax[1][1]
# img_4.imshow(cv.cvtColor(cat_image, cv.COLOR_BGR2RGB))
# img_4.set_title("Grayscale")
# img_4.axis('off')

# plt.show()