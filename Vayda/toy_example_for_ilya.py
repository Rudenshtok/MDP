import numpy as np
from vaidya_for_ilya import vaidya, get_init_polytope
import matplotlib.pyplot as plt


n = 5  # Размерность задачи = 5
np.random.seed(0)
x_0 = np.random.randn(n, 1)  # Начальное приближение (слабо влияет на работу алгоритма)
x_0 /= np.linalg.norm(x_0)

y_0 = np.array([1., 2.])  # это просто заглушка, так как пример с обычной оптимизацией, а не седловыми задачами

R = 10.  # Радиус множества, на котором будем минимизировать функцию, т.е. ||x|| <= 10
A_0, b_0 = get_init_polytope(n, R)  # Некоторые начальные параметры алгоритма, зависящие от радиуса множества

K = 100  # Число итераций

# Целевая функция f(x) = ||x||**2
class objective_function:
    def __init__(self):
        pass

    def func(self, x):
        return np.linalg.norm(x) ** 2

    def get_delta_grad(self, x, y):  # градиент. y - заглушка
        return 2 * x, y

objective = objective_function()
best_func_value = np.inf

# подбираем наилучшие параметры алгоритма eta, eps
for eta in [1e3, 1e2, 1e1]:
    for factor in [1e-3, 1e-4]:
        eps = eta * factor

        # Параметр stepsize, скорее всего, подойдёт такой, какой есть. Но если нет, можно менять от 0.01 до 1.
        trajectory, _ = vaidya(A_0, b_0, x_0, y_0, eps, eta, K, objective, stepsize=0.18, verbose=False)

        func_value = objective.func(trajectory[-1])
        if func_value < best_func_value:
            best_func_value = func_value
            best_params = (eta, eps)
            best_traj = trajectory
        print(f"eta = {eta:.0e}, eps = {eps:.0e}, конечное значение функции = {func_value:.3f}")

eta, eps = best_params
print(f"Наименьшее значение функции {best_func_value:.3f} достигается при параметрах eta = {eta:.0e}, eps = {eps:.0e}")
plt.plot([objective.func(x) for x in trajectory])

# Построение графика сходимости
fsize = 15
fig = plt.figure(figsize=(10, 7))
plt.plot([objective.func(x) for x in best_traj])

plt.xticks(fontsize=fsize)
plt.yticks(fontsize=fsize)
plt.yscale('log')
plt.xlabel(r"# of iterations", fontsize=fsize)
plt.ylabel(r"$f(x)$", fontsize=fsize)
plt.savefig(f"toy_example_for_ilya.png", bbox_inches='tight')