# Загрузка феникса
from dolfin import *

# делает нумерацию степней свободы равной нумерации вершин
# степени свободы - это искомые величины
parameters["reorder_dofs_serial"] = False

# разрешение экстраполяции
parameters["allow_extrapolation"] = True

import numpy as np

# генератор случайных функций
from perlin_numpy import generate_perlin_noise_2d


#------------------
#--- PROPERTIES ---
#------------------

#!--- CHECKING STATUS: CHECKED ---!#

# длины по x и y нашей области
L_x, L_y = 1.0, 1.0

# количество ячеек на мелкой (подробной) вычислительной сетке по x и y
n_x, n_y = 100, 100

# минимальная и максимальная пористости
min_phi = 0.05
max_phi = 0.2

# количество ячеек на мелкой (подробной) вычислительной сетке
N = n_x * n_y

# создаем левую нижеюю и правую верхнюю точки
p_0 = Point(0.0, 0.0)
p_1 = Point(L_x, L_y)

# создаем прямоугольную мелкую сетку с прямоугольными ячейками
mesh = RectangleMesh.create([p_0, p_1], [n_x, n_y], CellType.Type.quadrilateral)


# -----------------------------
# --- GENERATE COEFFICIENTS ---
# -----------------------------

#!--- CHECKING STATUS: CHECKED ---!#

#--- generate random fields ---

# генерируем с помощью шума Перлина случайную функцию
# (4, 4) - периодичность
# phi = \sum_i a_i * \psi_i
data_phi = generate_perlin_noise_2d((n_x, n_y), (4, 4))
data_phi = data_phi.flatten()

#--- generate porosity field ---

# масштабируем и получаем пористость

data_phi[:] = (data_phi[:] - data_phi.min()) / (data_phi.max() - data_phi.min())
data_phi[:] = data_phi[:] * (max_phi - min_phi) + min_phi

#--- generate coefficients ---

# генериурем коэффициент проницаемости как функцию от пористости

data_k = np.zeros(N)

for i in range(N):
    # берем значение пористости на ячейке
    val = data_phi[i]
    # вычисляем значение проницаемости
    data_k[i] = 1e-16 * np.exp(20 * val)

# ranges

print('\nphi: %.1e, %.1e' % (data_phi.min(), data_phi.max()))
print('\nk: %.1e, %.1e' % (data_k.min(), data_k.max()))


#-------------------------
#--- SAVE COEFFICIENTS ---
#-------------------------

#--- visualize ---

# директория сохранения
coefficients_dir = f"data/coefficients/"

def visualize_function(
                            name: str, 
                            directory: str,
                            mesh: Mesh,
                            arr: np.ndarray
                        ):
    # пространство кусочно-постоянных функций заданных на ячейках сетки
    # то есть в каждой ячейке постоянное значение
    DG0 = FunctionSpace(mesh, "DG", 0)
    # создаем функцию
    coefficient_function = Function(DG0)

    # записываем значения коэффициентов в функцию
    coefficient_function.vector()[:] = arr[:]

    # визуализируем в xdmf файл
    # можно открыть с помощью ParaView
    visualization = XDMFFile(directory + name + ".xdmf")
    visualization.write(coefficient_function)

# phi

visualize_function(
                        name="phi",
                        directory=coefficients_dir + "visualization/",
                        mesh=mesh,
                        arr=data_phi
)

# k

visualize_function(
                        name="k",
                        directory=coefficients_dir + "visualization/",
                        mesh=mesh,
                        arr=data_k
)

#--- save coefficients in target mesh ---

# сохраняем в виде текстовых файлов

file_phi = coefficients_dir + "phi"
file_k = coefficients_dir + "k"

np.save(file_phi, data_phi)
np.save(file_k, data_k)

print("\nDONE")