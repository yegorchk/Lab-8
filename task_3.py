import cv2

def video_processing():
    last_box = None
    fly = cv2.imread('fly64.png')
    print(fly.shape)
    cap = cv2.VideoCapture(1)
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
            if cv2.contourArea(largest_contour) > 100:
                x, y, w, h = cv2.boundingRect(largest_contour)
                center_width = (x + (w//2))
                center_height = (y + (h//2))
                last_box = (center_width, center_height)

        if last_box:
            center_width, center_height = last_box
            x1 = int(center_width - 32)
            x2 = int(center_width + 32)
            y1 = int(center_height - 32)
            y2 = int(center_height + 32)
            frame[y1:y2, x1:x2] = fly

        cv2.imshow('frame with box', frame)
        cv2.imshow('edges', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_processing()
    