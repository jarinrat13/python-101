class Calcutate_area:

    def rectangle_area(self, w, h):
        return w * h

    @classmethod
    def triangle_ares(cls, b, h):
        return 0.5 * b * h

    @staticmethod
    def circle_area(r):
        return 3.14 * r * r

cal = Calcutate_area()
cal_rec = cal.rectangle_area(4, 5)
cal_tri = cal.triangle_ares(4, 5)
cal_circle = cal.circle_area(5)

print('Rectangle Ares = ', cal_rec)
print('Triangle Area = ', cal_tri)
print('Circle Area = ', cal_circle)

#print('Test Triangle Area', Calculate.triangle_area(5, 6))
#print('Test Circle Area', Calculate.circle_area(5))
#print('Test Rectangle Area', Calculate.rectangle_area(5, 6))