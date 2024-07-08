if __name__ == '__main__':
    from ultralytics import YOLO

    # Initialize model
    model = YOLO('runs/detect/train31/weights/best.pt')
    
    # Start training
    model.train(data='/home/fengrenxu/Dataset/行为识别/Yolo_train/dataset.yaml', epochs=50, imgsz=640,batch=48)
