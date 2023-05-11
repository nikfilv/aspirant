from dolfin import *

meshname = "mesh"
mesh = Mesh(meshname + ".xml")
subdomains = MeshFunction("size_t", mesh, meshname + "_physical_region.xml")
boundaries = MeshFunction("size_t", mesh, meshname + "_facet_region.xml")

mu = 0.8*1.0e11
lmbda = 1.25*1.0e11
f2 = Constant((1.0e2, 0, 0))
f1 = Constant((0.0, 0, -1.0e8))
g = Constant(0.0)


def epsilon(u):
    return 0.5*(grad(u) + grad(u).T)


def sigma(u):
    return lmbda*div(u)*Identity(3) + 2*mu*epsilon(u)


V = VectorFunctionSpace(mesh, "CG", 1)

bc1 = DirichletBC(V.sub(0), g, boundaries, 3)
bc2 = DirichletBC(V.sub(1), g, boundaries, 3)
bc3 = DirichletBC(V.sub(2), g, boundaries, 3)
bcs = [bc1, bc2, bc3]

u = TrialFunction(V)
v = TestFunction(V)

dx = Measure('dx', domain=mesh, subdomain_data=subdomains)
ds = Measure('ds', domain=mesh, subdomain_data=boundaries)

a = inner(sigma(u), epsilon(v))*dx
L = inner(f1, v)*ds(1)+inner(f2, v)*ds(2)

u = Function(V)

solve(a == L, u, bcs)

print('u(%g, %g)' % (u.vector().min(), u.vector().max()))

u.rename('u', '0')
file = File("./results/u.pvd")
file << u

W = TensorFunctionSpace(mesh, "DG", 0)

stress = project(sigma(u), V=W)
stress.rename('u', '0')
File("./results/s.pvd") << stress
