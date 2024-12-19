# image_processing.py
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import datetime

def get_datetime_from_filename(filename):
    """ファイル名から日時を取得する関数"""
    try:
        date_str = filename.split('.')[0]
        return datetime.strptime(date_str, "%Y%m%d_%H%M%S")
    except ValueError as e:
        print(f"日時情報の抽出に失敗しました: {filename} (エラー: {e})")
        return None

def find_most_recent_file(image_folder):
    """フォルダ内で最も新しい日時のファイルを特定する関数"""
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    datetime_dict = {}

    for img_file in image_files:
        dt = get_datetime_from_filename(img_file)
        if dt:
            datetime_dict[img_file] = dt

    if not datetime_dict:
        print("日時情報が取得できた画像がありません。")
        return None

    most_recent_file = max(datetime_dict, key=datetime_dict.get)
    return most_recent_file


def save_image(image, folder, filename):
    """画像を指定されたフォルダに保存"""
    filepath = os.path.join(folder, filename)
    cv2.imwrite(filepath, image)
    print(f"{filename} を保存しました")
    return filepath

def merge_images_horizontally(image_folder, image1, image2, output_filename):
    """2枚の画像を横に結合する関数"""
    img1 = cv2.imread(os.path.join(image_folder, image1))
    img2 = cv2.imread(os.path.join(image_folder, image2))

    if img1 is None or img2 is None:
        print(f"画像の読み込みに失敗しました: {image1}, {image2}")
        return

    # 高さを揃えるためにリサイズ
    min_height = min(img1.shape[0], img2.shape[0])
    img1_resized = cv2.resize(img1, (int(img1.shape[1] * (min_height / img1.shape[0])), min_height))
    img2_resized = cv2.resize(img2, (int(img2.shape[1] * (min_height / img2.shape[0])), min_height))

    # 横に結合
    combined_img = cv2.hconcat([img1_resized, img2_resized])
    output_path = os.path.join(image_folder, output_filename)
    cv2.imwrite(output_path, combined_img)
    print(f"画像を結合して保存しました: {output_filename}")
