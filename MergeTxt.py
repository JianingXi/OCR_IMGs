import os


def concatenate_txt_files(directory, output_file):
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 遍历目录中的所有文件
        for filename in os.listdir(directory):
            # 检查文件是否为 .txt 文件
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                print(f"正在处理文件: {file_path}")

                # 打开并读取当前 .txt 文件
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # 将当前文件内容写入输出文件
                    outfile.write(infile.read())
                    # 可选：在每个文件之间添加一个换行符
                    outfile.write('\n')

    print(f"所有文件已拼接完成，结果保存到: {output_file}")


# 示例使用
directory_path = r'D:\Alpha\StoreLatestYears\Store2024\B教学_教学与人才培养_A04_教改社科论文\D20240705_EI教学会议_ISAIE_2024\D20241201_封面封底目录\aaa'  # 替换为你的 txt 文件文件夹路径
output_file_path = r'D:\Alpha\StoreLatestYears\Store2024\B教学_教学与人才培养_A04_教改社科论文\D20240705_EI教学会议_ISAIE_2024\D20241201_封面封底目录\aaa.txt'  # 替换为输出文件的路径
concatenate_txt_files(directory_path, output_file_path)