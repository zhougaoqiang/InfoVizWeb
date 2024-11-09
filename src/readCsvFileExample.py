import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# 从CSV文件中读取边数据
df = pd.read_csv("data/edges.csv")  # 读取 CSV 文件

# 创建无向图对象
G = nx.Graph()

# 从DataFrame中添加边到图中
G.add_edges_from(df.values)  # 将每一行作为一条边添加到图中

# 计算聚类系数
local_clustering_node = nx.clustering(G)  # 计算每个节点的局部聚类系数，返回字典
local_clustering_node_a = nx.clustering(G, 'a')  # 计算节点 'a' 的局部聚类系数
print("Local Clustering: " + str(local_clustering_node))  # 打印所有节点的局部聚类系数
print("Local Clustering for node a: " + str(local_clustering_node_a))  # 打印节点 'a' 的局部聚类系数

# 计算平均聚类系数
avg_clustering = nx.average_clustering(G)  # 计算图的平均聚类系数
print("Average Clustering: " + str(avg_clustering))  # 打印平均聚类系数

# 生成节点位置，使用 spring 布局
pos = nx.spring_layout(G)

# 定义节点和边的绘制属性
nodes = nx.draw_networkx_nodes(G, pos, alpha=0.5, node_size=700, node_color='blue')  # 绘制节点，设置透明度、大小和颜色
edges = nx.draw_networkx_edges(G, pos, edge_color='green', width=0.5)  # 绘制边，设置颜色和宽度

# 添加节点标签
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')  # 设置标签字体大小和样式

# 获取当前的绘图轴，并关闭坐标轴显示
ax = plt.gca()
ax.set_axis_off()  # 关闭坐标轴

# 显示绘制的图形
plt.show()
