import os

# 定义要处理的目录
directory = '标注数据/第四次增强2/annotations'

# 定义列的分隔符（根据你的文件格式进行调整，例如使用空格或逗号）
separator = ' '  # 假设列是用空格分隔的

# 遍历目录下的所有文件
for filename in os.listdir(directory):
    # 检查文件扩展名是否为 .txt
    if filename.endswith('.txt'):
        # 构建文件的完整路径
        file_path = os.path.join(directory, filename)
        
        # 尝试使用 'latin1' 编码读取文件内容
        try:
            with open(file_path, 'r', encoding='latin1') as file:
                lines = file.readlines()
        except UnicodeDecodeError as e:
            print(f"Error decoding {file_path}: {e}")
            continue  # 跳过无法解码的文件
        
        # 替换第一列中的 15 为 0
        modified_lines = []
        for line in lines:
            columns = line.strip().split(separator)
            if columns[0] == '15':
                columns[0] = '0'
            modified_line = separator.join(columns)
            modified_lines.append(modified_line)
        
        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='latin1') as file:
            file.write('\n'.join(modified_lines) + '\n')

print("All .txt files have been modified.")
