if __name__ == '__main__':
    from ultralytics import YOLO

    # 初始化模型
    model = YOLO('runs/detect/train36/weights/best.pt')
    
    # 开始训练
    model.train(data='/home/fengrenxu/Dataset/行为识别/Yolo_train/dataset.yaml', epochs=100, imgsz=640, batch=64)


