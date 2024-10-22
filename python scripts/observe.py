from ultralytics import YOLO
import cv2

model = YOLO("best_custom.pt")

stream = cv2.VideoCapture(0)
if not stream.isOpened():
    print("No stream found")
    exit()
  
while (True):
    ret, frame = stream.read()
    if not ret:
        print("No more stream")
        break
    
    model.predict(source= frame,
     show = True,
     save = True,
     conf = 0.6)
 
    
    #cv2.imshow("Webcamera",frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
stream.release()
cv2.destroyAllWindows()
    


#model = YOLO("best_custom.pt")

#model.predict(source= "Birds eye view dolly slow motion people walk steps from _ to underground entrance.100-25p super slom.mp4",
# show = True,
# save = True,
# conf = 0.6)
 