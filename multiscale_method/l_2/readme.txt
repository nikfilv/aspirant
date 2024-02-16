0. Установить необходимые библиотеки

fenics 2019.1.0
perlin_numpy
numpy
scipy

1. Сгенерировать неоднородные коэффициент

python3 coefficients_generator.py

2. Решить задачу на мелкой сетке

python3 fine_solver.py

3. Вычислить эффективные свойства

python3 numerical_homogenization.py

4. Решить задачу на грубой сетке

python3 coarse_solver.py