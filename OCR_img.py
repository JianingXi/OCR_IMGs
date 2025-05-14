import os
import glob
import re  # 导入正则表达式模块
from PIL import Image
import pytesseract


# 设置Tesseract的路径（如果需要）
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    # 打开图片
    image = Image.open(image_path)

    # 使用Tesseract进行OCR
    text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用中文语言包

    return text


def detect_columns(text):
    # 通过正则表达式判断是否有明显的双栏特征
    # 这里假设双栏文档中会有明显的空白区域
    lines = text.split('\n')
    blank_line_count = 0

    for line in lines:
        if re.match(r'^\s*$', line):  # 判断是否为空行
            blank_line_count += 1

    # 如果空行数量较多，可能是双栏文档
    if blank_line_count > len(lines) * 0.2:  # 假设空行超过20%为双栏
        return "双栏"
    else:
        return "单栏"


def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)


def process_image(image_path, output_txt_path):
    # 提取文本
    text = ocr_image(image_path)

    # 判断单栏或双栏
    column_type = detect_columns(text)
    print(f"文档类型: {column_type}")

    # 保存文本到文件
    save_text_to_file(text, output_txt_path)
    print(f"文本已保存到: {output_txt_path}")


def process_all_images_in_directory(directory):
    # 支持的图片格式
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff', '*.gif']

    # 遍历所有支持的图片文件
    for extension in image_extensions:
        # 使用 glob 查找匹配的文件
        for image_path in glob.glob(os.path.join(directory, extension)):
            # 生成对应的输出文本文件路径
            output_txt_path = os.path.splitext(image_path)[0] + '.txt'

            # 处理图片
            print(f"正在处理图片: {image_path}")
            try:
                process_image(image_path, output_txt_path)
            except Exception as e:
                print(f"处理图片 {image_path} 时出错: {e}")


# 示例使用
directory_path = r'C:\MyPython\OCR_IMGs\img'  # 替换为你的图片文件夹路径
process_all_images_in_directory(directory_path)