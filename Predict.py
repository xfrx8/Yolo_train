if __name__ == '__main__':
    import csv # 导入CSV库，用于创建和操作CSV文件
    from ultralytics import YOLO # 从ultralytics库导入YOLO类，用于加载和使用YOLO模型

    # Initialize model
    model = YOLO('runs/detect/train27/weights/best.pt') # 初始化YOLO模型，加载预训练的模型文件'yolov8n.pt'
    results = model.track(source='视频1.mp4', imgsz=1280, conf=0.1, save=True)
    results = model.track(source='视频2.mp4', imgsz=1280, conf=0.1, save=True)
    results = model.track(source='视频3.mp4', imgsz=1280, conf=0.1, save=True)
    results = model.track(source='视频4.mp4', imgsz=1280, conf=0.1, save=True)
    results = model.track(source='视频5.mp4', imgsz=1280, conf=0.1, save=True)
    # # Define CSV file and write headers
    # csv_file = 'predictions.csv'
    # with open(csv_file, mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     # Write headers
    #     writer.writerow(['frame', 'object_class', 'confidence', 'xmin', 'ymin', 'xmax', 'ymax'])

    # # Perform testing on a video and save results
    # results = model.predict(source='/home/fengrenxu/Dataset/yolov8/白手套.mp4', imgsz=1280, conf=0.1, save=True, save_dir='runs/detect/predict23')
    
    # frame_number = 0
    # for result in results:
    #     frame_number += 1
    #     boxes = result.boxes
    #     for box in boxes:
    #         # Extract bbox details
    #         xyxy = box.xyxy[0]  # Extract the first (and only) array from xyxy
    #         xmin, ymin, xmax, ymax = xyxy
    #         obj_class = box.cls[0]  # Extract the first (and only) class from cls
    #         confidence = box.conf[0]  # Extract the first (and only) confidence from conf

    #         # Write prediction data to CSV file
    #         with open(csv_file, mode='a', newline='') as file:
    #             writer = csv.writer(file)
    #             writer.writerow([frame_number, obj_class, confidence, xmin, ymin, xmax, ymax])

