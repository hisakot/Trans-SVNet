import cv2
import numpy as np

labels = np.loadtxt("result_6ch_1tensor_6class_re.csv", delimiter=",", usecols=[0])
labels = labels.tolist()
preds6 = np.loadtxt("result_6ch_re_tp.csv", delimiter=",", usecols=[1])
preds6 = preds6.tolist()

c = [(255, 127, 255), (0, 60, 255), (0, 127, 255), (0, 255, 0), (255, 127, 0), (127, 127, 127)]

img_l = np.zeros((30, len(labels) * 1, 3), np.uint8)
img_p6 = np.zeros((30, len(labels) * 1, 3), np.uint8)

for i, label in enumerate(labels):
    cv2.rectangle(img_l, (int(i*1), 0, 1, 30), c[int(label)], thickness=-1)

cv2.imshow("img", img_l)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("test_labels_bar.png", img_l)

for i, pred in enumerate(preds6):
    cv2.rectangle(img_p6, (int(i*1), 0, 1, 30), c[int(pred)], thickness=-1)

cv2.imshow("img", img_p6)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("test_preds6_tp_bar.png", img_p6)

