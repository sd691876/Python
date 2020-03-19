class Rectangle:
    width=1
    height=2
    def getArea(width,height):
        print("The area of the rectangle is ",(width*height))
    def getPerimeter(width,height):
        print("The perimeter of the rechangle is",(2*(width+height)))
while(True):
    width=float(input("The width of the rectangle is "))
    height=float(input("The height of the rectangle is "))
    Rectangle.getArea(width,height)
    Rectangle.getPerimeter(width,height)
