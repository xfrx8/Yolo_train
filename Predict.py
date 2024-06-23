if __name__ == '__main__':
    import csv # 导入CSV库，用于创建和操作CSV文件
    from ultralytics import YOLO # 从ultralytics库导入YOLO类，用于加载和使用YOLO模型

    # Initialize model
    model = YOLO('runs/detect/train27/weights/best.pt') # 初始化YOLO模型，加载预训练的模型文件'yolov8n.pt'
    results = model.predict(source='videos/视频1.mp4', imgsz=1280, conf=0.7, save=True)

