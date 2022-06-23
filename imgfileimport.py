import os
import pprint
import pandas as pd
from PIL import Image
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
root_dir = 'c:/PythonWorkspace/read_img/couponimg1' # 디렉토리
resultcoupon = ''
img_path_list =  [[],[]]
possible_img_extension = ['.jpg'] # 이미지 확장자들

for (root, dirs, files) in os.walk(root_dir):
    
    if len(files) > 0:
        i=0
        for file_name in files:
               
            if os.path.splitext(file_name)[1] in possible_img_extension:
                
                img_path = root + '/' + file_name
                # 경로에서 \를 모두 /로 바꿔줘야함
                img_path = img_path.replace('\\', '/') # \는 \\로 나타내야함
                img = Image.open(img_path)
                text = pytesseract.image_to_string(img)
                text_format = ['202111','202112','202201','202202','202203']
                for format in text_format:
                    if format in text:
                        index = text.find(format)
                        resultcoupon = text[index:index+14]
                        break
                    else:
                        resultcoupon = ''

                result =img_path.replace("c:/PythonWorkspace/read_img/couponimg1/", "")
                img_path_list.append((result,resultcoupon.replace("\n","").replace(".","").replace(",","").strip()))
                
                raw_data = pd.DataFrame(img_path_list)
                print(raw_data.index,' ',result,' : ',resultcoupon.replace("\n","").replace(".","").replace(",","").strip())
   

    raw_data.to_excel(excel_writer='coupon1.xlsx')

