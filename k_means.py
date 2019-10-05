import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df_raw = pd.read_json(r"data.json")

## Count photos by age

data = df_raw[['photo','age']]
colmap = {1: 'red', 2: 'green', 3: 'blue',4:'yellow',5:'black',6:'orange',7:'purple'}


df = pd.DataFrame(data)
df = df[df['age'] != 0]
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['photo'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 50000)

plt.xlabel("Age")
plt.ylabel("Count Photos")

plt.show(block = False)



##5
kmeans = KMeans(n_clusters=5)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['photo'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])


plt.xlim(-10, 200)
plt.ylim(0, 50000)

plt.xlabel("Age")
plt.ylabel("Count Photos")

plt.show(block = False)


##7
kmeans = KMeans(n_clusters=7)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['photo'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 50000)

plt.xlabel("Age")
plt.ylabel("Count Photos")

plt.show(block = False)




##Count videos by age

data = df_raw[['countVideo','age']]
colmap = {1: 'red', 2: 'green', 3: 'blue',4:'yellow',5:'black',6:'orange',7:'purple'}


df = pd.DataFrame(data)
df = df[df['age'] != 0]
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countVideo'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 2000)

plt.xlabel("Age")
plt.ylabel("Count Videos")

plt.show(block = False)



##5
kmeans = KMeans(n_clusters=5)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countVideo'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])


plt.xlim(-10, 200)
plt.ylim(0, 2000)

plt.xlabel("Age")
plt.ylabel("Count Videos")

plt.show(block = False)


##7
kmeans = KMeans(n_clusters=7)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countVideo'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 2000)

plt.xlabel("Age")
plt.ylabel("Count Videos")

plt.show(block = False)


##Count Notes by age

data = df_raw[['countNotes','age']]
colmap = {1: 'red', 2: 'green', 3: 'blue',4:'yellow',5:'black',6:'orange',7:'purple'}


df = pd.DataFrame(data)
df = df[df['age'] != 0]
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countNotes'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 2000)

plt.xlabel("Age")
plt.ylabel("Count Notes")

plt.show(block = False)



##5
kmeans = KMeans(n_clusters=5)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countNotes'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])


plt.xlim(-10, 200)
plt.ylim(0, 2000)

plt.xlabel("Age")
plt.ylabel("Count Notes")

plt.show(block = False)


##7
kmeans = KMeans(n_clusters=7)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countNotes'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 2000)

plt.xlabel("Age")
plt.ylabel("Count Notes")

plt.show(block = False)


##Count Groups by age

data = df_raw[['countGroups','age']]
colmap = {1: 'red', 2: 'green', 3: 'blue',4:'yellow',5:'black',6:'orange',7:'purple'}


df = pd.DataFrame(data)
df = df[df['age'] != 0]
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countGroups'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 1500)

plt.xlabel("Age")
plt.ylabel("Count Groups")

plt.show(block = False)



##5
kmeans = KMeans(n_clusters=5)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countGroups'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])


plt.xlim(-10, 200)
plt.ylim(0, 1500)

plt.xlabel("Age")
plt.ylabel("Count Groups")

plt.show(block = False)


##7
kmeans = KMeans(n_clusters=7)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(5, 5))

colors_map = map(lambda x: colmap[x+1], labels)
colors = list(colors_map)

plt.scatter(df['age'], df['countGroups'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(-10, 200)
plt.ylim(0, 1500)

plt.xlabel("Age")
plt.ylabel("Count Groups")

plt.show()




