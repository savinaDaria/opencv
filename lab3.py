
import cv2

img1 = cv2.imread("balls/1.png")
img2 = cv2.imread("balls/3.png")
scale_percent = 100  # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
resized2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

added = cv2.add(resized1,resized2)
subtracted = cv2.subtract(added,resized1)

cv2.imshow("Original_img",img1)
cv2.imshow("Added",added)
cv2.imshow("subtracted",subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()