from dolfin import *

mesh = UnitSquareMesh(32, 32)
V = FunctionSpace(mesh , "Lagrange", 1)

def boundary(x):
    return x[0] < DOLFIN_EPS or x[0] > 1.0 - DOLFIN_EPS or \
            x[1] < DOLFIN_EPS or x[1] > 1.0 - DOLFIN_EPS

g = Constant(0.0)
bc = DirichletBC(V, g, boundary)

u = TrialFunction(V)
v = TestFunction(V)

k = Constant(1.0)
f = Constant(1.0)

a = k * inner(grad(u), grad(v)) * dx
L = f * v * dx

u = Function(V)
solve(a == L, u, bc)

file = File("poisson.pvd")
file << u
