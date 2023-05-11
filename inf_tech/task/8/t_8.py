from dolfin import *

# Define the domain and create the mesh
mesh = UnitSquareMesh(32, 32)
V = FunctionSpace(mesh, "Lagrange", 1)

# Define the boundary conditions
def boundary(x):
    return x[0] < DOLFIN_EPS or x[0] > 1.0 - DOLFIN_EPS or \
        x[1] < DOLFIN_EPS or x[1] > 1.0 - DOLFIN_EPS

g = Constant(0.0)
bc = DirichletBC(V, g, boundary)

# Define the initial condition
p_0 = Constant(0.0)

# Define the parameters
k = Constant(1.0)
a_x = Constant(1.0)

# Define the source term
f = Expression("sin(pi*x[0])*cos(pi*x[1])", degree=2)

# Define the time-stepping parameters
T = 1.0
num_steps = 1
dt = T / num_steps

# Define the variational problem
p_n = interpolate(p_0, V)
p = TrialFunction(V)
v = TestFunction(V)

a = (p - p_n) / dt * v * dx \
    + dot(k * p_n * grad(p), grad(v)) * dx
L = f * v * dx

# Define the Picard iterations
tol = 1e-6
diff = 1.0
while diff > tol:
    solve(a == L, p, bc)
    diff = norm(p.vector() - p_n.vector(), 'l2')
    p_n.assign(p)

# Output the solution
File("solution.pvd") << p

