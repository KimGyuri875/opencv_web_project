import sys
import cv2

# 카메라, 비디오 파일에서 frame 을 받아오는 클래스, 카메라 오픈
# cap = cv2.VideoCapture(0), 내 카메라 frame이 출력
cap = cv2.VideoCapture('vtest.avi')

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break
    #if frame is None:
    #    break

    edge = cv2.Canny(frame, 50, 150) # 영상 numpy 형태로 만들어진다.

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    # cv2.waitKey(1) 속 숫자는 영상의 속도를 제어하기도 한다. 영상마다 고유의 fps가 있다. 1로 하면 너무 빨라
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
