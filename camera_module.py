# カメラモジュール
import cv2
import time
from datetime import datetime

class Camera:
    def __init__(self, width=480, height=480):
        self.width = width
        self.height = height
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.start_time = None

    def capture_image(self):
        """画像をキャプチャして返す"""
        ret, image = self.cap.read()
        if not ret:
            return None
        return image

    def start_timer(self, current_time, wait_time=3.0):
        """スペースキー押した後、3秒経過したらTrueを返す"""
        if self.start_time is not None and current_time - self.start_time >= wait_time:
            self.start_time = None  # タイマーリセット
            return True
        return False

    def wait_for_keypress(self):
        """キー入力を待機し、特定のキーでアクションをトリガー"""
        key = cv2.waitKey(10)
        if key == 27:  # ESCキーで終了
            return "exit"
        elif key == 32:  # スペースキーでタイマー開始
            self.start_time = time.time()
            return "start"
        return None

    def release(self):
        """カメラリソースを解放"""
        self.cap.release()
        cv2.destroyAllWindows()
