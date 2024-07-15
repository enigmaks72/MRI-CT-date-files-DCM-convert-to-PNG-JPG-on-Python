import os
import pydicom
from PIL import Image
import numpy as np

def convert_dcm_to_image(dcm_folder, output_folder, output_format='png'):
    for root, _, files in os.walk(dcm_folder):
        for file in files:
            if file.endswith(".dcm"):
                dcm_path = os.path.join(root, file)
                print(f"Converting: {dcm_path}")
                ds = pydicom.dcmread(dcm_path)
                pixel_array = ds.pixel_array

                # 원본 폴더 구조를 유지하기 위해 상대 경로 계산
                relative_path = os.path.relpath(root, dcm_folder)
                output_dir = os.path.join(output_folder, relative_path)

                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                image = Image.fromarray(pixel_array.astype(np.uint8))
                output_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.{output_format}")
                image.save(output_path)
                print(f"Saved to: {output_path}")

dcm_folder = r'C:\down\MRI\MRI\DCMData\00147804\20240712'  # DCM 파일이 있는 폴더 경로
output_folder = r'C:\down\MRI\PNG'  # 변환된 이미지를 저장할 폴더 경로
convert_dcm_to_image(dcm_folder, output_folder, output_format='png')
