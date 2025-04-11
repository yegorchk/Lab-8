import time
import cv2

def video_processing():
    cap = cv2.VideoCapture(1)
    last_box = None
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (15, 15), 0)

        edges = cv2.Canny(gray, 10, 30)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 50:
                x, y, w, h = cv2.boundingRect(largest_contour)
                last_box = (x, y, w, h)

        if last_box:
            x, y, w, h = last_box
            if x > (frame.shape[1]) // 2:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('frame with box', frame)
        cv2.imshow('edges', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_processing()