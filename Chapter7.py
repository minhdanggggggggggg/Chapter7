import numpy as np

class AddGate:
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        return x + y
    def backward(self, d_out):
        return d_out, d_out

class MultiplyGate:
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        return x * y
    def backward(self, d_out):
        dx = d_out * self.y
        dy = d_out * self.x
        return dx, dy

class PowerGate:
    def __init__(self, power):
        self.x = None
        self.power = power
    def forward(self, x):
        self.x = x
        return x ** self.power
    def backward(self, d_out):
        return d_out * self.power * (self.x ** (self.power - 1))

# Inputs
w, b, x, y = 2, 8, -2, 2

# Gates 
multiply_1 = MultiplyGate()
multiply_2 = MultiplyGate()
add_1 = AddGate()
add_2 = AddGate()
power = PowerGate(2)

# Compute forward
# Node 1
c = multiply_1.forward(w , x)

# Node 2
a = add_1.forward(c , b)

# Node 3
d = add_2.forward(a , -y)

# Node 4
e = power.forward(d)

# Node 5
J = multiply_2.forward(0.5 , e)

print(f"Loss: {J}")

# Compute backward
# Node 5
_ , A = multiply_2.backward(1)
print("A = ",A)

# Node 4
B = power.backward(A)
print("B = ",B)

# Node 3
C, _ = add_2.backward(B)
print("C = ",C)

# Node 2
D, E = add_1.backward(C)

print("D = ",D)
print("E = ",E)

# Node 1
F, _ = multiply_1.backward(D)

print("F = ",F)
