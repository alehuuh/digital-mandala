from sp2_mandala import *

if __name__ == '__main__':

    mandala = Mandala(size=(1000,1000), bgcolor=(0,0,0))

    mandala.draw_diamond((500,500), 700, 0, (121,75,196))
    mandala.draw_diamond((500,500), 700, 45, (121,75,196))

    for n in range(20):
        mandala.draw_diamond((500,500), 660+n, 0, (121,75,196))
        mandala.draw_diamond((500,500), 660+n, 45, (121,75,196))
        mandala.draw_diamond((500,500), 675, n*5, (121,75,196))
        mandala.draw_diamond((500,500), 450, n*5, (29,161,242))
        mandala.draw_diamond((500,500), 300, n*5, (23,191,99))
        mandala.draw_diamond((500,500), 200, n*5, (224,36,94))


    sec_angle = 0
    for x in range(0,4):
        for n in range(10):
            mandala.draw_diamond((500,500), 300+n, sec_angle, (23,191,99))
            mandala.draw_diamond((500,500), 450+n, sec_angle, (29,161,242))
        sec_angle += 22.5

    for n in range(10):
        mandala.draw_sunrays((500, 500), 100, n*10, (243,93,34))

    length = 50
    for x in range(0,4):
        for n in range(10):
            mandala.draw_sunrays((500, 500), length+n, 0, (255,173,31))
        length += 25


    center = (95,500)
    angle = 0
    for n in range(0,8):
        mandala.draw_circles(center, 50, angle, (255,255,255))
        mandala.draw_triangle(center, 70, angle, (255,215,0))
        mandala.draw_triangle(center, 70, 180+angle, (211,211,211))
        center = mandala.rotate_point(center, (500,500), 45)
        angle += -90


    mandala.draw_circles((500, 500), 75, 0, (224,36,94))
    mandala.draw_circles((500, 500), 10, 90, (255,173,31))

    mandala.show()
    mandala.save("sp2_output.png")
