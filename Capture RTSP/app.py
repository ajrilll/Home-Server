import cv2
import time
from datetime import datetime

rtsp_url = "rtsp://admin:otwpimnas36@192.168.0.99:554/"

def capture_frame(rtsp_url):
    try:
        cap = cv2.VideoCapture(rtsp_url)
        ret, frame = cap.read()
        if ret:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_file = f"capture_{timestamp}.jpg"
            cv2.imwrite(output_file, frame)
            print("Capture berhasil disimpan sebagai", output_file)
            return True
        else:
            print("Gagal membaca frame dari aliran video RTSP")
            return False
        cap.release()
    except Exception as e:
        print("Error:", e)
        return False

while True:
    capture_frame(rtsp_url)
    time.sleep(120)
