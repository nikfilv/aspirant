from dolfin import *

mesh = Mesh('mesh.xml')
domains = MeshFunction('size_t' , mesh , 'mesh_physical_region.xml')
boundaries = MeshFunction('size_t' , mesh , 'mesh_facet_region.xml')

V = FunctionSpace(mesh, 'Lagrange', 1)

dx = Measure('dx')(subdomain_data=domains)
ds = Measure('ds')(subdomain_data=boundaries)

f = Constant(1.0)
g_1 = Constant(70.0)
g_2 = Constant(20.0)
g_3 = Constant(-30.0)
g_4 = Constant (10000.0)
alpha = Constant (150.0)

bc_1 = DirichletBC(V, g_1, boundaries , 1)
bc_2 = DirichletBC(V, g_2, boundaries , 2)

bcs = [bc_1 , bc_2]

k_1 = Constant(1)
k_2 = Constant(420)

u = TrialFunction(V)
v = TestFunction(V)

a = k_1 * inner(grad(u), grad(v)) * dx(1) \
        + k_2 * inner(grad(u), grad(v)) * dx(2) + alpha * u * v * ds(3)
L = f * v * dx(1) + f * v * dx(2) + alpha * g_3 * v * ds(3) \
        - g_4 * v * ds(4)

u = Function(V)

solve(a == L, u, bcs)

file = File('./poisson.pvd')
file << u
