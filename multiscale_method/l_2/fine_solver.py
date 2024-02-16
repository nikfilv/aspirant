from dolfin import *
parameters["reorder_dofs_serial"] = False
parameters["allow_extrapolation"] = True

import numpy as np


#------------------ 
#--- PROPERTIES ---
#------------------

#!--- CHECKING STATUS: CHECKED ---!#

L_x, L_y = 1.0, 1.0
n_x, n_y = 100, 100

p_0 = Point(0.0, 0.0)
p_1 = Point(L_x, L_y)

mesh = RectangleMesh.create([p_0, p_1], [n_x, n_y], CellType.Type.quadrilateral)


#---------------------------
#--- PROBLEM FORMULATION ---
#---------------------------

#--- set coefficients ---

coefficients_dir = f"data/coefficients/"

# загружаем проницаемость из файла
k_arr = np.load(coefficients_dir + "k.npy")

DG0 = FunctionSpace(mesh, "DG", 0)

# создаем и инициализируем функцию проницаемости
k = Function(DG0)
k.vector()[:] = k_arr[:]

# задаем правую часть
f = Constant(1e-6)

#--- variational formulations ---

# создаем функциональное пространство со стандартными линейными базисными функциями
# степени свободы = индексы вершин
V = FunctionSpace(mesh, "P", 1)

# создаем триальную и тестовые функции
u = TrialFunction(V)
v = TestFunction(V)

# функция которая возврщает True на границе области
def boundary(x, on_boundary):
    return on_boundary

# значение на границе
u_zero = Constant(1e-6)

# задаем граничное условие Дирихле на границе
bc = DirichletBC(V, u_zero, boundary)

# билинейная форма вариционной постановки
a = inner(k * grad(u), grad(v)) * dx

# линейная форма
L = f * v * dx

u = Function(V)

#--- solving ---

# решаем
solve(a == L, u, bc)

# визуализируем сохранив в pvd
# его можно на ParaView
file = File("data/results/fine/u_f.pvd")
file << u

# сохраняем в текстовый файл массив значений на узлах мелкой сетки
np.savetxt("data/results/fine/u_f.txt", u.vector().get_local(), fmt="%g")