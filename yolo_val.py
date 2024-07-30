from ultralytics import YOLO

if __name__ == '__main__':
    # 初始化模型
    model = YOLO('runs/detect/train37/weights/best.pt')
    
    # 训练完成后进行验证并保存结果
    results = model.val(data='/home/fengrenxu/Dataset/行为识别/Yolo_train/dataset.yaml', split='test', save=True, save_json=True)
    
    # 输出验证结果保存路径
    print("Validation results saved.")
