# import the necessary packages
from skimage.measure import compare_ssim as ssim
from skimage.transform import resize
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import os




# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True,
	help="folder of images to compar")
ap.add_argument("-s", "--image", required=True,
	help="image to compare")
args = vars(ap.parse_args())



path = args["folder"] + "/"
comparing_image = cv2.imread(path + args["image"])
comparing_image = cv2.cvtColor(comparing_image, cv2.COLOR_BGR2GRAY)
closest_image = cv2.imread(path + "boom.png")
closest_image_number = 0.0

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title, currentssim):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)

	if currentssim < s and s != 1:
		global closest_image_number
		closest_image_number = s
		closest_image_number = s
		global closest_image
		closest_image = imageB




for image_path in os.listdir(path):
	im2comp = cv2.imread(path + image_path)
	im2comp = cv2.cvtColor(im2comp, cv2.COLOR_BGR2GRAY)
	im2comp = cv2.resize(im2comp,dsize=(64,64), interpolation=cv2.INTER_CUBIC)
	compare_images(comparing_image,im2comp,"compared", closest_image_number)


title = "Closest image"
fig = plt.figure(title)
plt.suptitle("SSIM: %.2f" % (closest_image_number))

# show first image
ax = fig.add_subplot(1, 2, 1)
plt.imshow(comparing_image, cmap = plt.cm.gray)
plt.axis("off")

# show the closest image
ax = fig.add_subplot(1, 2, 2)
plt.imshow(closest_image, cmap = plt.cm.gray)
plt.axis("off")

# show the images
plt.show()
