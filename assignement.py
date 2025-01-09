import cv2  


image = cv2.imread('assignment-001-given.jpg')



cv2.rectangle(image, (260, 190), (985, 925), (0, 255, 0), 8)
cv2.addWeighted(cv2.rectangle(image.copy(), (800, 85), (1230, 175), (0, 0, 0), -1), 0.5, image, 1 - 0.5, 0, dst=image)
cv2.putText(image, 'RAH972U', (800, 160), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)


cv2.imshow('Image', image)


cv2.waitKey(0)


cv2.imwrite('assignment_01.jpg', image)


cv2.destroyAllWindows()