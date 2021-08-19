"""
Demonstrate creation of a custom graphic (a candlestick plot)
"""
#import initExample ## Add path to library (just for examples; you do not need this)

import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see QGraphicsItem documentation)
class BlockItem(pg.GraphicsObject):
	def __init__(self, data):
		pg.GraphicsObject.__init__(self)
		self.data = data  ## data must have fields: time, open, close, min, max
		self.generatePicture()
	def generatePicture(self):
		## pre-computing a QPicture object allows paint() to run much more quickly, 
		## rather than re-drawing the shapes every time.
		self.picture = QtGui.QPicture()
		p = QtGui.QPainter(self.picture)
		for (xl, xh, yl, yh,color) in self.data:
			p.setPen(pg.mkPen(color))
			p.setBrush(pg.mkBrush((255, 0, 0, 20)))
			x = xl
			y = yl
			w = xh - xl
			h = yh - yl
			p.drawRect(QtCore.QRectF(x, y, w, h)) # fields are (x,y,w,h)
		p.end()
	def paint(self, p, *args):
		p.drawPicture(0, 0, self.picture)
    
	def boundingRect(self):
		## boundingRect _must_ indicate the entire area that will be drawn on
		## or else we will get artifacts and possibly crashing.
		## (in this case, QPicture does all the work of computing the bouning rect for us)
		return QtCore.QRectF(self.picture.boundingRect())

data = [  ## fields are (time, open, close, min, max).
    (3, 10, 13,15, 'g'),
    (2, 13, 17,20,'r'),
    (3., 17, 14,23,'c')
]
item = BlockItem(data)
plt = pg.plot()
plt.addItem(item)
plt.setWindowTitle('pyqtgraph example: customGraphicsItem')

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
