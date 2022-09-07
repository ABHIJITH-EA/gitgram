from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QBrush, QImage, QPainter, QPixmap, QWindow

def roundImage(imgdata, imgtype='jpg', size=120):
    image = QImage.fromData(imgdata, imgtype)
    image.convertToFormat(QImage.Format_ARGB32)

    imgsize = min(image.width(), image.height())
    
    rect = QRect(
        (image.width() - imgsize) // 2,
        (image.height() - imgsize) // 2,
        imgsize,
        imgsize,
    )
  
    image = image.copy(rect)

    output_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
    output_img.fill(Qt.transparent)

    brush = QBrush(image)       
    painter = QPainter(output_img)
    painter.setBrush(brush)
    painter.setPen(Qt.NoPen)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.drawEllipse(0, 0, imgsize, imgsize)
    painter.end()

    
    pr = QWindow().devicePixelRatio()
    pm = QPixmap.fromImage(output_img)
    
    pm.setDevicePixelRatio(pr)
    size *= pr

    pm = pm.scaled(int(size), int(size), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
    return pm