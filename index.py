from flask import Flask
import cv2
import threading

app = Flask(__name__)

# Global variables to control the video capture
video_capture = None
is_capturing = False
capture_thread = None

def capture_video():
    global video_capture, is_capturing
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))
    
    while is_capturing:
        ret, frame = video_capture.read()
        if ret:
            out.write(frame)
        else:
            break
    
    out.release()

@app.route('/start', methods=['POST'])
def start_capture():
    global video_capture, is_capturing, capture_thread
    if not is_capturing:
        video_capture = cv2.VideoCapture(0)  # 0 for default camera
        is_capturing = True
        capture_thread = threading.Thread(target=capture_video)
        capture_thread.start()
        return "Video capture started"
    else:
        return "Video capture already in progress"

@app.route('/stop', methods=['POST'])
def stop_capture():
    global video_capture, is_capturing
    if is_capturing:
        is_capturing = False
        capture_thread.join()
        video_capture.release()
        video_capture = None
        return "Video capture stopped and saved"
    else:
        return "Video capture not in progress"

if __name__ == '__main__':
    app.run(debug=True)
