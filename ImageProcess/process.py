from Filter import EdgeDetector ,Filter
# from plot import plot3D , plot2D
from plot import plot2D
from IM_classical import Image_classical

'''
class ImageProcess(EdgeDetector , plot2D ,plot3D  ,Filter , Image_classical) :
    def __init__(self):
        EdgeDetector.__init__(self)
        plot2D.__init__(self)
        plot3D.__init__(self)
        Filter.__init__(self)
        Image_classical.__init__(self)
'''

class ImageProcess(EdgeDetector, plot2D, Filter, Image_classical):
    def __init__(self):
        EdgeDetector.__init__(self)
        plot2D.__init__(self)
        Filter.__init__(self)
        Image_classical.__init__(self)
        
