from dolfin import *

mesh = Mesh('mesh.xml')
domains = MeshFunction('size_t', mesh, 'mesh_physical_region.xml')
boundaries = MeshFunction('size_t', mesh, 'mesh_facet_region.xml')

V = FunctionSpace(mesh, 'Lagrange', 1)

dx = Measure('dx')(subdomain_data=domains)
ds = Measure('ds')(subdomain_data=boundaries)

f = Constant(0.0)
g = Constant(150)
g_1 = Constant(-1)

u0_val = Constant(0)
u0 = interpolate(u0_val, V)

bc = DirichletBC(V, g, boundaries, 1)

k_1 = Constant(25)
k_2 = Constant(0.569)

alpha_1 = 0.1
alpha_2 = 100

C_1 = Constant(0.5)
C_2 = Constant(4.1806)

T = 60
N = 20
tau = T / N

u = TrialFunction(V)
v = TestFunction(V)

a = (C_1 / tau) * u * v * dx(1) + \
    (C_2 / tau) * u * v * dx(2) + \
    k_1 * inner(grad(u), grad(v)) * dx(1) + \
    k_2 * inner(grad(u), grad(v)) * dx(2) + \
    alpha_1 * u * v * ds(2) + \
    alpha_2 * u * v * ds(3)
L = (C_1 / tau) * u0 * v * dx(1) + \
    (C_2 / tau) * u0 * v * dx(2) + \
    f * v * dx(1) + \
    f * v * dx(2) + \
    alpha_1 * g_1 * v * ds(2) + \
    alpha_2 * g_1 * v * ds(3)

u = Function(V)
file = File('./results/time_dep.pvd')

t = 0
while t < T:
    t += tau
    solve(a == L, u, bc)
    file << u
    u0.assign(u)
