#PRACTICA 8
class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementa_xz(self):
        self.x += 1
        self.z += 1

    def incrementa_z(self):
        self.z += 1

    def get_x(self):
        return self.x

    def get_z(self):
        return self.z


class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def incrementa_yz(self):
        self.y += 1
        self.z += 1

    def incrementa_z(self):
        self.z += 1

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


class D:
    def __init__(self, x, z, y):
        self.a = A(x, z)
        self.b = B(y, z)

    def incrementa_xz(self):
        self.a.incrementa_xz()
        self.b.incrementa_z()

    def get_a_x(self):
        return self.a.get_x()

    def get_a_z(self):
        return self.a.get_z()

    def get_b_y(self):
        return self.b.get_y()

    def get_b_z(self):
        return self.b.get_z()


if __name__ == "__main__":
    d = D(1, 2, 3)

    print("Valores iniciales:")
    print("A.x:", d.get_a_x())
    print("A.z:", d.get_a_z())
    print("B.y:", d.get_b_y())
    print("B.z:", d.get_b_z())

    d.incrementa_xz()
    print("---------------------------------")
    print("Valores después de incrementa_xz:")
    print("A.x:", d.get_a_x())
    print("A.z:", d.get_a_z())
    print("B.y:", d.get_b_y())
    print("B.z:", d.get_b_z())