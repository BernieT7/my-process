# 多元線性回歸，利用ML達成
import wget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import fontManager
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def compute_cost(x, y, w, b):
  y_pred = (x*w).sum(axis=1) + b
  cost = ((y_pred - y)**2).mean()
  return cost


def compute_gradient(x, y, w, b):
  y_pred = (x*w).sum(axis=1) + b
  ws_grad = np.zeros(x.shape[1])
  b_grad = (y_pred - y).mean()
  for i in range(x.shape[1]):
    ws_grad[i] = (x[:, i]*(y_pred - y)).mean()
  

  return ws_grad, b_grad


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
      print(f"Iteration {i:5}: Cost{cost: .4e}, where w={w}, b={b: .2e}, w_gradient={w_gradient}, b_gradient={b_gradient: .2e}")

  return w, b, w_hist, b_hist, c_hist


wget.download("https://github.com/GrandmaCan/ML/raw/main/Resgression/ChineseFont.ttf")
fontManager.addfont("ChineseFont.ttf")
mpl.rc('font', family="ChineseFont")

url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data2.csv"
data = pd.read_csv(url)

onehot_encoder = OneHotEncoder()
onehot_encoder.fit(data[["City"]])
city_num = onehot_encoder.transform(data[["City"]]).toarray()
data[["CityA", "CityB", "CityC"]] = city_num
data = data.drop(["City", "CityC"], axis=1)

x = data[["YearsExperience", "EducationLevel", "CityA", "CityB"]]
y = data["Salary"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=87)
x_train = x_train.to_numpy()
x_test = x_test.to_numpy()

scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

np.set_printoptions(formatter={'float': '{: .2e}'})

w_init = np.array([1, 2, 2, 4])
b_init = 1
learning_rate = 0.01
iter_time = 20001

w_final, b_final, w_hist, b_hist, c_hist = gradient_descent(x_train, y_train, w_init, b_init, learning_rate, compute_cost, compute_gradient, iter_time, per_iter=1000)

y_pred = (w_final*x_test).sum(axis=1) + b_final
pd.DataFrame({
    "y_pred": y_pred,
    "y_test": y_test
})
