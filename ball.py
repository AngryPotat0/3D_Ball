import numpy as np
from numpy import linalg

def rotate(a, b, ang):
    a1 = np.dot(a, b) / np.dot(b, b) * b
    a2 = a - a1
    w = np.cross(a2, b)
    d = np.cos(ang) * a2 / linalg.norm(a2) + np.sin(ang) * w / linalg.norm(w)
    a3 = linalg.norm(a2) * d
    return a1 + a3

def generate(r, n):
    points = []
    k = (np.sqrt(5) - 1) / 2
    for i in range(1, n + 1):
        z = (2 * i - 1) / n - 1
        p = np.sqrt(1 - z**2)
        ang = 2 * np.pi * i * k
        x = p * np.cos(ang)
        y = p * np.sin(ang)
        points.append([x, y, z,1])
    return np.array(points) * r

class MyBall():
    def __init__(self, r, n):
        self.radius = r
        xVectors = generate(r, n)
        self.X = np.matrix(xVectors.T)
        # self.X = generate(r,n)

    def rotate(self, angle):
        Y = np.matrix([[np.cos(angle),0,np.sin(angle),0],[0,1,0,0],[-np.sin(angle),0,np.cos(angle),0],[0,0,0,1]])
        self.X = Y * self.X

    def camera(self):
        # print('*****************')
        # print(self.X.T)
        # print('\n')
        lis = self.X.T.tolist()
        # print(lis)
        # print('****************')
        for idx in range(len(lis)):
            lis[idx][2] += 30
        res = np.matrix(np.array(lis).T)
        # print(res)
        return res

    def image(self,f):
        I = np.matrix([[f,0,0,0],[0,f,0,0],[0,0,1,0]])
        # print('|||||||||||||||||||||||')
        # print(self.X.T)
        Cam = self.camera()
        image = (I * Cam)# / self.X[2]
        # print('|||||||||||||||||||||||')
        # print(image.T)
        return image

    def screen(self,f,dx,dy,u0,v0):
        S = np.matrix([[1 / dx,0,u0],[0,1 / dy,v0],[0,0,1]])
        image = self.image(f)
        # screen = S * image
        screen = image
        return screen.T
        # return image.T

    def points(self):
        return self.X
        # return (self.X).T

class Ball:
    def __init__(self, r, n):
        self.radius = r
        self.A = np.identity(3)
        xVectors = generate(r, n)
        self.X = np.matrix(xVectors.T)

    def rotate(self, direction, angle):
        dirVector = np.array([0, np.cos(direction), np.sin(direction)])
        for i in range(3):
            self.A[:,i] = rotate(self.A[:,i], dirVector, angle)

    def points(self):
        return (self.A * self.X).T
        # return (self.X).T

if __name__ == '__main__':
    b = MyBall(10, 10)
    # b = Ball(10, 10)
    # b.rotate(1,1)
    print(b.points())
    print(b.image(10).T)