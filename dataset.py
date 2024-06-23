import os
import shutil
import random

# 定义数据集路径
dataset_path = '白手套/第二次'
images_path = os.path.join(dataset_path, 'image')
labels_path = os.path.join(dataset_path, 'annotation')

# 定义输出路径
output_path = 'output_dataset1'
train_images_path = os.path.join(output_path, 'images', 'train')
val_images_path = os.path.join(output_path, 'images', 'val')
test_images_path = os.path.join(output_path, 'images', 'test')
train_labels_path = os.path.join(output_path, 'labels', 'train')
val_labels_path = os.path.join(output_path, 'labels', 'val')
test_labels_path = os.path.join(output_path, 'labels', 'test')

# 创建输出文件夹
os.makedirs(train_images_path, exist_ok=True)
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(test_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)
os.makedirs(test_labels_path, exist_ok=True)

# 获取所有图片文件
all_images = [f for f in os.listdir(images_path) if f.endswith('.jpg')]
random.shuffle(all_images)

# 划分比例
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# 计算每个集合的数量
total_images = len(all_images)
train_count = int(total_images * train_ratio)
val_count = int(total_images * val_ratio)
test_count = total_images - train_count - val_count

# 划分数据集
train_images = all_images[:train_count]
val_images = all_images[train_count:train_count + val_count]
test_images = all_images[train_count + val_count:]

# 函数：复制文件
def copy_files(images, src_images_path, src_labels_path, dest_images_path, dest_labels_path):
    for image in images:
        # 复制图片
        shutil.copy(os.path.join(src_images_path, image), os.path.join(dest_images_path, image))
        # 复制标签
        label = image.replace('.jpg', '.txt')
        shutil.copy(os.path.join(src_labels_path, label), os.path.join(dest_labels_path, label))

# 复制文件到相应的文件夹
copy_files(train_images, images_path, labels_path, train_images_path, train_labels_path)
copy_files(val_images, images_path, labels_path, val_images_path, val_labels_path)
copy_files(test_images, images_path, labels_path, test_images_path, test_labels_path)

print(f"训练集数量: {train_count}")
print(f"验证集数量: {val_count}")
print(f"测试集数量: {test_count}")
