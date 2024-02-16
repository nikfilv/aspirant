from dolfin import *
parameters["reorder_dofs_serial"] = False
parameters["allow_extrapolation"] = True

import numpy as np
import os


#------------------ 
#--- PROPERTIES ---
#------------------

#!--- CHECKING STATUS: CHECKED ---!#

L_x, L_y = 1.0, 1.0

n_x, n_y = 100, 100

# количество ячеек на грубой сетке по x и y
N_x, N_y = 10, 10

# размеры ячейки на мелкой сетке по x и y
h_x, h_y = L_x / n_x, L_y / n_y

# размеры ячейки на грубой сетке по x и y
H_x, H_y = L_x / N_x, L_y / N_y

# площадь ячейки
volume_K = H_x * H_y

# количество мелкосеточных ячеек в грубой ячейке K по x
loc_n_x = n_x // N_x

# количество мелкосеточных ячеек в грубой ячейке K по y
loc_n_y = n_y // N_y

def boundary(x, on_boundary):
    return on_boundary


#----------------------------------------
#--- COMPUTING EFFECTIVE COEFFICIENTS ---
#----------------------------------------

# левая нижняя вершина
global_p_0 = Point(0, 0)

# правая верхняя вершина
global_p_1 = Point(L_x, L_y)

# создаем грубую сетка
coarse_mesh = RectangleMesh.create([global_p_0, global_p_1], [N_x, N_y], CellType.Type.quadrilateral)

# создаем пространство кусочно заданных функций
coarse_DG0 = FunctionSpace(coarse_mesh, "DG", 0)

# создаем функции эффективных коэффициентов
k_11 = Function(coarse_DG0)
k_12 = Function(coarse_DG0)
k_21 = Function(coarse_DG0)
k_22 = Function(coarse_DG0)

#--- load global fine-scale coefficient ---

coefficients_dir = f"data/coefficients/"

# загружаем проницаемость на мелкой сетке
k_arr = np.load(coefficients_dir + "k.npy")


#--- iterate coarse cells ---

# проходимся по y
for i in range(N_y):
    # проходимся по x
    for j in range(N_x):
        #--- create local mesh ---
        
        # вычисляем индекс грубой ячейки
        # каждой грубой ячейке задается идентификатор по естесственной нумерации
        K_id = i * N_x + j

        # координаты левой нижней вершины грубой ячейки
        x_0 = j * H_x
        y_0 = i * H_y

        # координаты правой верхней вершины грубой ячейки
        x_1 = (j + 1) * H_x
        y_1 = (i + 1) * H_y

        p_0 = Point(x_0, y_0)
        p_1 = Point(x_1, y_1)

        # грубая ячейка с мелкосеточными ячейками внутри
        loc_mesh = RectangleMesh.create([p_0, p_1], [loc_n_x, loc_n_y], CellType.Type.quadrilateral)

        #--- create local fine-scale coefficient ---

        loc_DG0 = FunctionSpace(loc_mesh, "DG", 0)

        # создаем функцию проницаемости на грубой ячейке с мелкосеточными ячейками внутри

        k_loc = Function(loc_DG0)

        # у глобальной мелкой сетки и мелкой сетки ограниченной грубой ячейкой разные нумерации вершин и разные размеры
        # нам нужно вычислить отображение из глобальной в локальную
        for c_i in range(loc_mesh.num_cells()):
            # узнаем порядок мелкой ячейки внутри грубой ячейки по y
            loc_i = c_i // loc_n_x
            # узнаем порядок мелкой ячейки внутри грубой ячейки по x
            loc_j = c_i % loc_n_x

            # узнаем порядок соответствующей глобальной мелкой ячейки по y
            global_i = loc_i + i * loc_n_y
            # узнаем порядок соответствующей глобальной мелкой ячейки по x
            global_j = loc_j + j * loc_n_x

            # глобальный индекс ячейки
            global_c_i = global_i * n_x + global_j

            # присваиваем
            k_loc.vector()[c_i] = k_arr[global_c_i]
        
        #--- local variational formulation ---
        
        # стандартные линейные базисные функции
        V_loc = FunctionSpace(loc_mesh, "P", 1)

        phi = TrialFunction(V_loc)
        v = TestFunction(V_loc)

        # вариационная постановка задачи на ячейке
        a = inner(k_loc * grad(phi), grad(v)) * dx
        L = Constant(0) * v * dx

        #--- first local problem ---

        # граничное условие первой задачи на ячейке phi_1
        g_1 = Expression("x[0]", degree=0)
        bc_1 = DirichletBC(V_loc, g_1, boundary)

        phi_1 = Function(V_loc)

        solve(a == L, phi_1, bc_1)

        #--- second local problem ---

        # граничное условие первой задачи на ячейке phi_2
        g_2 = Expression("x[1]", degree=0)
        bc_2 = DirichletBC(V_loc, g_2, boundary)

        phi_2 = Function(V_loc)

        solve(a == L, phi_2, bc_2)

        #--- effective coefficients ---

        # вычисляем эффективные свойства по формуле
        k_11.vector()[K_id] = assemble((1.0 / volume_K) * k_loc * phi_1.dx(0) * dx)
        k_12.vector()[K_id] = assemble((1.0 / volume_K) * k_loc * phi_2.dx(0) * dx)
        k_21.vector()[K_id] = assemble((1.0 / volume_K) * k_loc * phi_1.dx(1) * dx)
        k_22.vector()[K_id] = assemble((1.0 / volume_K) * k_loc * phi_2.dx(1) * dx)

#--- visualize effective coefficients ---
        
# визуализируем

effective_coefficients_dir = f"data/effective_coefficients/"

File(effective_coefficients_dir + "visualization/k_11.pvd") << k_11
File(effective_coefficients_dir + "visualization/k_12.pvd") << k_12
File(effective_coefficients_dir + "visualization/k_21.pvd") << k_21
File(effective_coefficients_dir + "visualization/k_22.pvd") << k_22

#--- saving effective coefficients ---

# сохраняем в текстовый файл

np.savetxt(effective_coefficients_dir + "k_11.txt", k_11.vector().get_local(), fmt="%g")
np.savetxt(effective_coefficients_dir + "k_12.txt", k_12.vector().get_local(), fmt="%g")
np.savetxt(effective_coefficients_dir + "k_21.txt", k_21.vector().get_local(), fmt="%g")
np.savetxt(effective_coefficients_dir + "k_22.txt", k_22.vector().get_local(), fmt="%g")