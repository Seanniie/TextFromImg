import os
import pprint
import pandas as pd
from PIL import Image
import pytesseract 

#pytesseract 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

root_dir = 'c:/PythonWorkspace/text_from_img/imgtest' # 디렉토리

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

                #문자열중 해당 숫자로 시작하는 코드가 있는지 검색
                text_format = ['202111','202112','202201','202202','202203']
                for format in text_format:
                    if format in text:
                        index = text.find(format)

                        #존재한다면 그 index부터 13자리까지
                        resultcoupon = text[index:index+14]
                        break
                    else:
                        resultcoupon = ''

                result =img_path.replace("c:/PythonWorkspace/text_from_img/imgtest12/", "")
                img_path_list.append((result,resultcoupon.replace("\n","").replace(".","").replace(",","").strip()))
                
                raw_data = pd.DataFrame(img_path_list)
                print(raw_data.index,' ',result,' : ',resultcoupon.replace("\n","").replace(".","").replace(",","").strip())
   

    raw_data.to_excel(excel_writer='imgtest.xlsx')

