# main.py
import cv2
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import time
from datetime import datetime
from camera_module import Camera 
from image_processing import save_image, merge_images_horizontally, get_datetime_from_filename, find_most_recent_file 

# フォルダのパス設定
image_folder = r"C:/Users/narra/Documents_kosen/zemi2/R4_4Iseminar/image_folder"
merged_folder = r"C:/Users/narra/Documents_kosen/zemi2/R4_4Iseminar/merged_folder"


if __name__ == "__main__":
    camera = Camera()
    most_recent_file = find_most_recent_file(image_folder)

    if most_recent_file:
        print(f"最も新しいファイル: {most_recent_file}")
    else:
        print("新しいファイルは見つかりませんでした。")

    while True:
        image = camera.capture_image()
        if image is None:
            break

        current_time = time.time()
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        action = camera.wait_for_keypress()

        if action == "exit":
            break
        elif action == "start":
            print("タイマー開始")

        if camera.start_timer(current_time):
            filename = f"{current_datetime}.jpg"
            save_image(image, image_folder, filename)

            if most_recent_file:
                merge_images_horizontally(image_folder, filename, most_recent_file, f"merged_{filename}")

        # 画面にシルエットを描画
        cv2.circle(image, (315, 120), 100, (237, 216, 130), 5)
        cv2.rectangle(image, (170, 220), (450, 960), (237, 216, 130), 5)

        cv2.imshow('image', image)

    camera.release()
