from dolfin import *

mesh = Mesh('mesh.xml')
domains = MeshFunction('size_t', mesh, 'mesh_physical_region.xml')
boundaries = MeshFunction('size_t', mesh, 'mesh_facet_region.xml')

V = FunctionSpace(mesh, 'Lagrange', 1)

dx = Measure('dx')(subdomain_data=domains)
ds = Measure('ds')(subdomain_data=boundaries)

f = Constant(0.0)
g = Constant(1)

u0_val = Constant(5.0)
u0 = interpolate(u0_val, V)

bc = DirichletBC(V, g, boundaries, 360)

k_1 = Constant(0.1)
k_2 = Constant(0.01)
k_3 = Constant(100)

C_1 = Constant(1)
C_2 = Constant(10)
C_3 = Constant(100)

T = 60.0
N = 10
tau = T / N

u = TrialFunction(V)
v = TestFunction(V)

a = (C_1 / tau) * u * v * dx(1) + \
    (C_2 / tau) * u * v * dx(2) + \
    (C_3 / tau) * u * v * dx(3) + \
    k_1 * inner(grad(u), grad(v)) * dx(1) + \
    k_2 * inner(grad(u), grad(v)) * dx(2) + \
    k_3 * inner(grad(u), grad(v)) * dx(3)
L = (C_1 / tau) * u0 * v * dx(1) + \
    (C_2 / tau) * u0 * v * dx(2) + \
    (C_3 / tau) * u0 * v * dx(3) + \
    f * v * dx(1) + \
    f * v * dx(2) + \
    f * v * dx(3)

u = Function(V)
file = File('./results/time_dep.pvd')

t = 0
while t < T:
    t += tau
    solve(a == L, u, bc)
    file << u
    u0.assign(u)
