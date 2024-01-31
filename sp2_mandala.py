import PIL.Image, PIL.ImageDraw
import math

class Mandala:

    def __init__(self, size, bgcolor):
        self.size = size
        self.bgcolor = bgcolor
        self.canvas = PIL.Image.new("RGB", self.size, self.bgcolor)
        self.draw = PIL.ImageDraw.Draw(self.canvas)

    def show(self):
        self.canvas.show()

    def save(self, filename):
        self.canvas.save(filename)

    def rotate_point(self, point, pivot, angle):

        self.poi_x, self.poi_y = point
        self.piv_x, self.piv_y = pivot
        self.angle = math.radians(angle)

        rot_point_x = self.piv_x + math.cos(self.angle) * (self.poi_x - self.piv_x) - math.sin(self.angle) * (self.poi_y - self.piv_y) #https://academo.org/demos/rotation-about-point/
        rot_point_y = self.piv_y + math.sin(self.angle) * (self.poi_x - self.piv_x) + math.cos(self.angle) * (self.poi_y - self.piv_y)

        return float(rot_point_x), float(rot_point_y)

    def draw_triangle(self, center, side_length, rotation, color):
        height = ((3**0.5)/2) * side_length #http://www.treenshop.com/Treenshop/ArticlesPages/FiguresOfInterest_Article/The%20Equilateral%20Triangle.htm
        cent_to_vert = (2/3) * height
        half_line = (center[0] + cent_to_vert, center[1])
        first_point = self.rotate_point(half_line, center, 30)
        second_point = (first_point[0] - side_length, first_point[1])
        third_point = self.rotate_point(first_point, second_point, -60)

        triangle_points = [(first_point), (second_point), (third_point)]

        for index, points in enumerate(triangle_points):
            triangle_points[index] = self.rotate_point(points, center, rotation)

        self.draw.line([triangle_points[0], triangle_points[1]], fill=color, width=2)
        self.draw.line([triangle_points[1], triangle_points[2]], fill=color, width=2)
        self.draw.line([triangle_points[0], triangle_points[2]], fill=color, width=2)


    def draw_diamond(self, center, side_length, rotation, color):
        half_side = side_length / 2
        right_point = (center[0] + half_side, center[1])
        down_point = self.rotate_point(right_point, center, 90)
        left_point = self.rotate_point(down_point, center, 90)
        up_point = self.rotate_point(left_point, center, 90)

        diagonal_points = [(right_point), (down_point), (left_point), (up_point)]

        for index, points in enumerate(diagonal_points):
            diagonal_points[index] = self.rotate_point(points, center, rotation)

        self.draw.line([diagonal_points[0], diagonal_points[1]], fill=color, width=2)
        self.draw.line([diagonal_points[1], diagonal_points[2]], fill=color, width=2)
        self.draw.line([diagonal_points[2], diagonal_points[3]], fill=color, width=2)
        self.draw.line([diagonal_points[3], diagonal_points[0]], fill=color, width=2)


    def draw_circles(self, pivot, size, rotation, color):
        up_point = (pivot[0], pivot[1] - size)
        up_left = (up_point[0] - size, up_point[1])
        down_point = (pivot[0], pivot[1] + size)
        lower_right = (down_point[0] + size, down_point[1])

        radius1 = size - 10
        up_point1 = (pivot[0], pivot[1] - radius1)
        down_point1 = (pivot[0], pivot[1]+ radius1)
        up_left1 = (up_point1[0] - radius1, up_point1[1])
        lower_right1 = (down_point1[0] + radius1, down_point1[1])

        radius2 = size + 5
        up_point2 = (pivot[0], pivot[1] - radius2)
        down_point2 = (pivot[0], pivot[1]+ radius2)
        up_left2 = (up_point2[0] - radius2, up_point2[1])
        lower_right2 = (down_point2[0] + radius2, down_point2[1])

        circles_points = [(up_left), (lower_right), (up_left1), (lower_right1), (up_left2), (lower_right2)]

        for index, points in enumerate(circles_points):
            circles_points[index] = self.rotate_point(points, pivot, rotation)

        self.draw.arc([(up_left) , (lower_right)], 0, 360, fill=color, width=5)
        self.draw.arc([(up_left1) , (lower_right1)], 0, 360, fill=color, width=2)
        self.draw.arc([(up_left2) , (lower_right2)], 0, 360, fill=color, width=2)


    def draw_sunrays(self, pivot, size, rotation, color):
        first_half = size/2
        sun_points = []

        p1 = (pivot[0], pivot[1] - first_half)
        sun_points.append(p1)

        for point in range(0,8):
            point = self.rotate_point(p1, pivot, 45)
            sun_points.append(point)
            p1 = point

        for index, points in enumerate(sun_points):
            sun_points[index] = self.rotate_point(points, pivot, rotation)

        second_half = first_half/2
        sun_points1 = []
        p11 = self.rotate_point((pivot[0], pivot[1] - second_half), pivot, 22.5)
        sun_points1.append(p11)

        for point1 in range(0,8):
            point1 = self.rotate_point(p11, pivot, 45)
            sun_points1.append(point1)
            p11 = point1

        for index1, points1 in enumerate(sun_points1):
            sun_points1[index1] = self.rotate_point(points1, pivot, rotation)

        for n in range(0,8):
            self.draw.line([sun_points[n], sun_points1[n]], fill=color, width=2)
            self.draw.line([sun_points1[n], sun_points[n+1]], fill=color, width=2)







