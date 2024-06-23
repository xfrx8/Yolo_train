if __name__ == '__main__':
    from ultralytics import YOLO

    # Initialize model
    model = YOLO('yolov8n.pt')
    
    # Start training
    model.train(data='dataset.yaml', epochs=100, imgsz=1280,batch=48)
