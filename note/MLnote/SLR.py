# 簡單線性回歸，透過ML達成
import wget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import fontManager

wget.download("https://github.com/GrandmaCan/ML/raw/main/Resgression/ChineseFont.ttf")
fontManager.addfont("ChineseFont.ttf")
mpl.rc('font', family="ChineseFont")

url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"
data = pd.read_csv(url)
x = data["YearsExperience"]
y = data["Salary"]

def compute_cost(x, y, w, b):
  cost = (w * x + b - y) ** 2
  cost = cost.mean()
  return cost

# 方法一:窮舉所有一定範圍的w, b，利用numpy的功能找到最小的cost
ws = np.arange(-100, 101)
bs = np.arange(-100, 101)
costs = np.zeros((201, 201))

i = 0
for w in ws:
  j = 0
  for b in bs:
    cost = compute_cost(x, y, w, b)
    costs[i,j] = cost
    j = j+1
  i = i+1

plt.figure(figsize=(7, 7))
ax = plt.axes(projection="3d")
ax.view_init(0, 45)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0))

b_grid, w_grid = np.meshgrid(bs, ws)
# https://wangyeming.github.io/2018/11/12/numpy-meshgrid/

ax.plot_surface(w_grid, b_grid, costs, cmap="Spectral_r", alpha=0.7)
ax.plot_wireframe(w_grid, b_grid, costs, color="black", alpha=0.1)

ax.set_title("w b 對應的 cost")
ax.set_xlabel("w")
ax.set_ylabel("b")
ax.set_zlabel("cost")

w_index, b_index = np.where(costs == np.min(costs))
ax.scatter(ws[w_index], bs[b_index], costs[w_index, b_index], color="red", s=40)

plt.show()

print(f"當w={ws[w_index]}, b={bs[b_index]} 會有最小cost:{costs[w_index, b_index]}")
# 方法二:透過cost對w, b偏微分，得出斜率，並設定學習率透過迴圈讓機器學習，一步步逼近微分等於0的位置，也就是最小值
# 此方法稱為gradient descent。
def compute_gradient(x, y, w, b):
  w_gradient = (2*(w * x + b -y)*x).mean()
  b_gradient = (2*(w * x + b - y)).mean()
  return w_gradient, b_gradient

def gradient_descent(x, y, w_init, b_init, learning_rate, cost_function, gradient_function, iter_time, per_iter=1000):
  
  c_hist = []
  w_hist = []
  b_hist = []
  
  w = w_init
  b = b_init

  for i in range(iter_time):
    w_gradient, b_gradient = gradient_function(x, y, w, b)
    w = w - w_gradient*learning_rate
    b = b - b_gradient*learning_rate
    cost = cost_function(x, y, w, b)

    w_hist.append(w)
    b_hist.append(b)
    c_hist.append(cost)

    if (i % per_iter) == 0:
      print(f"Iteration {i:5}: Cost{cost: .4e}, where w={w: .2e}, b={b: .2e}, w_gradient={w_gradient: .2e}, b_gradient={b_gradient: .2e}")

  return w, b, w_hist, b_hist, c_hist

w_init = 0
b_init = 0
learning_rate = 0.001
iter_time = 20001

w_final, b_final, w_hist, b_hist, c_hist = gradient_descent(x, y, w_init, b_init, learning_rate, compute_cost, compute_gradient, iter_time, per_iter=1000)
print(f"最終w={w_final:2f}, b={b_final:2f}")

ex = int(input("經歷:"))
salary = w_final * ex + b_final
print(salary)