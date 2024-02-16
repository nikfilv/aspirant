from dolfin import *
parameters["reorder_dofs_serial"] = False
parameters["allow_extrapolation"] = True

import numpy as np

# линейная интерполяция, так как феникс не поддерживает интерполяцию с использование прямоугольных ячеек
from scipy.interpolate import RegularGridInterpolator


#------------------ 
#--- PROPERTIES ---
#------------------

#!--- CHECKING STATUS: CHECKED ---!#

L_x, L_y = 1.0, 1.0

n_x, n_y = 100, 100
N_x, N_y = 10, 10

loc_n_x = n_x // N_x
loc_n_y = n_y // N_y

p_0 = Point(0.0, 0.0)
p_1 = Point(L_x, L_y)

fine_mesh = RectangleMesh.create([p_0, p_1], [n_x, n_y], CellType.Type.quadrilateral)
coarse_mesh = RectangleMesh.create([p_0, p_1], [N_x, N_y], CellType.Type.quadrilateral)


#---------------------------
#--- PROBLEM FORMULATION ---
#---------------------------

#--- set coefficients ---

effective_coefficients_dir = f"data/effective_coefficients/"

# загружаем массивы эффективных свойств
k_11_arr = np.loadtxt(effective_coefficients_dir + "k_11.txt")
k_12_arr = np.loadtxt(effective_coefficients_dir + "k_12.txt")
k_21_arr = np.loadtxt(effective_coefficients_dir + "k_21.txt")
k_22_arr = np.loadtxt(effective_coefficients_dir + "k_22.txt")

coarse_DG0 = FunctionSpace(coarse_mesh, "DG", 0)

# инициализуем функции эффективных свойств

k_11 = Function(coarse_DG0)
k_11.vector()[:] = k_11_arr[:]

k_12 = Function(coarse_DG0)
k_12.vector()[:] = k_12_arr[:]

k_21 = Function(coarse_DG0)
k_21.vector()[:] = k_21_arr[:]

k_22 = Function(coarse_DG0)
k_22.vector()[:] = k_22_arr[:]

# представляем эффективное свойство в виде матрицы

k_eff = as_matrix(((k_11, k_12), (k_21, k_22)))

f = Constant(1e-6)

#--- variational formulations ---

# стандртные базисные функции на грубой сетке

V_c = FunctionSpace(coarse_mesh, "P", 1)

u_c = TrialFunction(V_c)
v_c = TestFunction(V_c)

def boundary(x, on_boundary):
    return on_boundary

u_zero = Constant(1e-6)
bc_c = DirichletBC(V_c, u_zero, boundary)

a_c = inner(k_eff * grad(u_c), grad(v_c)) * dx
L_c = f * v_c * dx

u_c = Function(V_c)

#--- solving ---

solve(a_c == L_c, u_c, bc_c)

file = File("data/results/coarse/u_c.pvd")
file << u_c

np.savetxt("data/results/coarse/u_c.txt", u_c.vector().get_local(), fmt="%g")

#-----------------------
#--- COMPUTING ERROR ---
#-----------------------

# L2 норма погрешности - погрешность решения
# H1 норма погрешности - погрешность градиента решения
# для H1 нормы будем использовать k как вес

#--- load fine-scale coefficient ---

# загружаем k

coefficients_dir = f"data/coefficients/"

k_arr = np.load(coefficients_dir + "k.npy")

DG0 = FunctionSpace(fine_mesh, "DG", 0)

k = Function(DG0)
k.vector()[:] = k_arr[:]

#--- load fine-scale solution ---

V_f = FunctionSpace(fine_mesh, "P", 1)

# загружаем решение на мелкой сетке
u_f_arr = np.loadtxt("data/results/fine/u_f.txt")

u_f = Function(V_f)
u_f.vector()[:] = u_f_arr[:]

#--- interpolate coarse-scale solution ---

# интерполируем решение на грубой сетке в мелкую сетку

# по x и y задаем начало, конец, количество вершин
x = np.linspace(0, L_x, N_x + 1)
y = np.linspace(0, L_y, N_y + 1)

# представляем массив решения на грубой сетке в виде матрицы
u_c_matrix = np.reshape(u_c.vector().get_local(), (N_x + 1, N_y + 1)).T

# получаем интерполятор
u_c_interp = RegularGridInterpolator((x, y), u_c_matrix)

u_c = Function(V_f)

# создаем интерполированную функцию решения на грубой сетке
for v_i in range(fine_mesh.num_vertices()):
    v = Vertex(fine_mesh, v_i)
    p = v.point()
    u_c.vector()[v_i] = u_c_interp((p.x(), p.y()))

# визуализируем на мелкой сетке
file = File("data/results/coarse_interp/u_c_interp.pvd")
file << u_c

#--- L2 error ---

# разница между решением на мелкой и грубой сетках
u_error = u_f - u_c

# относительная L2 норма погрешности
# \int_{\Omega} (u_f - u_c)^2 dx / \int_{\Omega} u_f^2 dx
L2_error = np.sqrt(assemble(u_error * u_error * dx))
L2_norm = np.sqrt(assemble(u_f * u_f * dx))

L2_relative_error = L2_error / L2_norm * 100.0

print(F"L2 relative error = {L2_relative_error} %")

#--- H1 error ---

# относительная H1 норма погрешности
# \int_{\Omega} (k * grad(u_f) \cdot grad(u_c)) dx / \int_{\Omega} (k * grad(u_f))^2 dx
H1_error = np.sqrt(assemble(inner(k * grad(u_error), grad(u_error)) * dx))
H1_norm = np.sqrt(assemble(inner(k * grad(u_f), grad(u_f)) * dx))

H1_relative_error = H1_error / H1_norm * 100.0

print(F"H1 relative error = {H1_relative_error} %")