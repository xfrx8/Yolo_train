def calculate_box_loss(pred_box, true_box):
    """
    计算预测框和真值框之间的损失。
    这里的计算方法需要根据具体的YOLO实现来确定。
    """
    # 例如，可以使用L1损失或IoU损失等
    loss = abs(pred_box - true_box).sum()
    return loss

if __name__ == '__main__':
    from ultralytics import YOLO

    # 初始化模型
    model = YOLO('runs/detect/train37/weights/best.pt')
    
    # 训练完成后进行验证
    results = model.val(data='/home/fengrenxu/Dataset/行为识别/Yolo_train/dataset.yaml', split='test')
    
    # 输出验证结果
    print(results)

    

