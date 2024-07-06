import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random
from sklearn.linear_model import LinearRegression
def split_on_intervals(min_val, max_val, n):
  step = (max_val - min_val)/n
  intervals = [min_val+(step*x) for x in range(n+1)]
  return intervals
def create_groups(x_intervals, y_intervals):
  groups = {}
  x_intervals = np.concatenate([[-np.inf], x_intervals, [np.inf]])
  y_intervals = np.concatenate([[-np.inf], y_intervals, [np.inf]])

  for x_i in range(len(x_intervals)-1):
    for y_i in range(len(y_intervals)-1):
      groups[f'x : {x_intervals[x_i]} - {x_intervals[x_i+1]} | y : {y_intervals[y_i]} - {y_intervals[y_i+1]}'] = 0
  return groups
def sort_on_groups(x_vals, y_vals, x_intervals, y_intervals, groups, only_vals = False):

  for x, y in zip(x_vals, y_vals):
    for x_i in range(len(x_intervals)-1):
      for y_i in range(len(y_intervals)-1):
        if ((x_intervals[x_i] <= x < x_intervals[x_i+1]) and (y_intervals[y_i] <= y < y_intervals[y_i+1])):
          groups[f'x : {x_intervals[x_i]} - {x_intervals[x_i+1]} | y : {y_intervals[y_i]} - {y_intervals[y_i+1]}'] += 1


  if only_vals:
    return list(groups.values())
  return groups
def create_dataset(config, df):
  x_intervals = split_on_intervals(config['min_xval'], config['max_xval'], config['x_ngroups'])
  y_intervals = split_on_intervals(config['min_yval'], config['max_yval'], config['y_ngroups'])

  groups = create_groups(x_intervals, y_intervals)

  groups_values=[]

  for i in range(len(df)):
    g = df.iloc[i]
    points = np.array([[float(x['lat']), float(x['lon'])] for x in g['points']])


    group_values = sort_on_groups(points[:,0], points[:,1], x_intervals, y_intervals, groups.copy(), only_vals = True)
    groups_values.append(group_values)


  groups_values = np.array(groups_values)
  for i in range(len(groups.keys())):
    groups[list(groups.keys())[i]]=groups_values[:,i]
  return groups
def calc_grad_on_batch(X, Y, w, batch_size):
    sample = np.random.choice(X.shape[0], size=batch_size, replace=False)
    return 2 * np.dot(X[sample].T, np.dot(X[sample], w) - Y[sample]) / batch_size
df=pd.read_json('C:\\Users\\USER\\Downloads\\train_dataset_train_data_Mediawise\\train_data_Mediawise\\train_data.json')
df=pd.concat([df,pd.json_normalize(df['targetAudience'])], axis=1)
df=df.drop(['targetAudience','id'], axis=1)
config = {'min_xval':55.55, 'max_xval':55.95, 'min_yval':37.3, 'max_yval':37.9, 'x_ngroups': 18, 'y_ngroups': 18}
dataset = pd.DataFrame(create_dataset(config, df))
x = dataset.to_numpy()
y = df.to_numpy()
anss = np.ones(0)
indik = np.zeros((len(y), 436))
a = set()
b = set()
c = set()
d = set()
for i in y:
    a.add(i[-4])
    b.add(i[-3])
    c.add(i[-2])
    d.add(i[-1])
a = sorted(a)
b = sorted(b)
c = sorted(c)
d = sorted(d)
g = int(len(y)*0.7)
X = np.zeros((g, 436))
Y = np.ones(g)
for i in range(len(y)):
    for j in range(400):
        indik[i][j] = x[i][j]
    anss = np.append(anss, y[i][2])
    for j in range(3):
        indik[i][400 + j] = (y[i][-4] == a[j])
    for j in range(11):
        indik[i][403 + j] = (y[i][-3] == b[j])
    for j in range(16):
        indik[i][414 + j] = (y[i][-2] == c[j])
    for j in range(5):
        indik[i][430 + j] = (y[i][-1] == d[j])
    indik[i][-1] = 1
    if(i < g):
        X[i] = indik[i]
        Y[i] = anss[i]
ww = np.ones(436)
ans = 1000000000
for _ in range(1):
    w_0 = np.ones(436)
    for i in range(436):
        w_0[i] = random.randint(1, 200000) / 100000
    w = w_0.copy()
    step_size = 1e-3
    num_steps = 4200
    for i in range(num_steps):
        h = 2 * step_size * np.dot(X.T, np.dot(X, w) - Y) / Y.shape[0]
        w = w - h
    ans1 = 0
    for i in range(g, len(anss)):
        ans1 += (anss[i]- np.dot(w, indik[i]))**2
    if(ans1 < ans):
        ans = ans1
        ww = w
print(ww)
print(ans)
print((1-(ans/(int(len(Y)*0.3)))**0.5/30)**4)
