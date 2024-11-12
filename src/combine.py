import networkx as nx
import matplotlib.pyplot as plt

# 创建一个有向图
directed_graph = nx.DiGraph()
# 添加带权重的边
directed_graph.add_weighted_edges_from([
    ('A', 'B', 5),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('C', 'D', 4),
    ('D', 'A', 1),
    ('D', 'E', 7),
    ('E', 'B', 6)
])

# directed_graph.add_edges_from
# directed_graph.add_nodes_from
# directed_graph.add_node
# directed_graph.add_edge

# 创建一个无向图
undirected_graph = nx.Graph()
# 添加带权重的边
undirected_graph.add_weighted_edges_from([
    ('A', 'B', 5),
    ('A', 'C', 3),
    ('B', 'C', 2),
    ('C', 'D', 4),
    ('D', 'E', 7),
    ('E', 'B', 6)
])

# 有向图和无向图的绘制
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos = nx.spring_layout(directed_graph)
nx.draw(directed_graph, pos, with_labels=True, node_color='skyblue', node_size=700, arrows=True)
nx.draw_networkx_edge_labels(directed_graph, pos, edge_labels=nx.get_edge_attributes(directed_graph, 'weight'))
plt.title("有向图")

plt.subplot(1, 2, 2)
pos = nx.spring_layout(undirected_graph)
nx.draw(undirected_graph, pos, with_labels=True, node_color='lightgreen', node_size=700)
nx.draw_networkx_edge_labels(undirected_graph, pos, edge_labels=nx.get_edge_attributes(undirected_graph, 'weight'))
plt.title("无向图")

plt.show()

# **计算中心性度量**
# 度中心性
print("有向图的度中心性:", nx.degree_centrality(directed_graph))
print("无向图的度中心性:", nx.degree_centrality(undirected_graph))

# 介数中心性
print("有向图的介数中心性:", nx.betweenness_centrality(directed_graph, weight='weight'))
print("无向图的介数中心性:", nx.betweenness_centrality(undirected_graph, weight='weight'))

# 接近中心性
print("有向图的接近中心性:", nx.closeness_centrality(directed_graph))
print("无向图的接近中心性:", nx.closeness_centrality(undirected_graph))

# 特征向量中心性
print("有向图的特征向量中心性:", nx.eigenvector_centrality(directed_graph, max_iter=1000))
print("无向图的特征向量中心性:", nx.eigenvector_centrality(undirected_graph, max_iter=1000))

# **计算聚类系数**
print("有向图的聚类系数:", nx.clustering(directed_graph.to_undirected()))  # 转换为无向图计算聚类系数
print("无向图的聚类系数:", nx.clustering(undirected_graph))

# **计算平均聚类系数**
print("有向图的平均聚类系数:", nx.average_clustering(directed_graph.to_undirected()))
print("无向图的平均聚类系数:", nx.average_clustering(undirected_graph))


'''
get max and min
'''
# import networkx as nx
# import matplotlib.pyplot as plt

# # 创建有向图
# directed_graph = nx.DiGraph()
# directed_graph.add_weighted_edges_from([
#     ('A', 'B', 5),
#     ('A', 'C', 3),
#     ('B', 'C', 2),
#     ('C', 'D', 4),
#     ('D', 'A', 1),
#     ('D', 'E', 7),
#     ('E', 'B', 6)
# ])

# # 创建无向图
# undirected_graph = nx.Graph()
# undirected_graph.add_weighted_edges_from([
#     ('A', 'B', 5),
#     ('A', 'C', 3),
#     ('B', 'C', 2),
#     ('C', 'D', 4),
#     ('D', 'E', 7),
#     ('E', 'B', 6)
# ])

# # 中心性度量计算
# # 度中心性
# directed_degree_centrality = nx.degree_centrality(directed_graph)
# undirected_degree_centrality = nx.degree_centrality(undirected_graph)

# # 介数中心性
# directed_betweenness_centrality = nx.betweenness_centrality(directed_graph, weight='weight')
# undirected_betweenness_centrality = nx.betweenness_centrality(undirected_graph, weight='weight')

# # 接近中心性
# directed_closeness_centrality = nx.closeness_centrality(directed_graph)
# undirected_closeness_centrality = nx.closeness_centrality(undirected_graph)

# # 特征向量中心性
# directed_eigenvector_centrality = nx.eigenvector_centrality(directed_graph, max_iter=1000)
# undirected_eigenvector_centrality = nx.eigenvector_centrality(undirected_graph, max_iter=1000)

# # 聚类系数
# directed_clustering = nx.clustering(directed_graph.to_undirected())
# undirected_clustering = nx.clustering(undirected_graph)

# # 平均聚类系数
# directed_avg_clustering = nx.average_clustering(directed_graph.to_undirected())
# undirected_avg_clustering = nx.average_clustering(undirected_graph)

# # 输出每个测量的最大值和最小值
# print("有向图的度中心性 - 最大值:", max(directed_degree_centrality.values()), "最小值:", min(directed_degree_centrality.values()))
# print("无向图的度中心性 - 最大值:", max(undirected_degree_centrality.values()), "最小值:", min(undirected_degree_centrality.values()))

# print("有向图的介数中心性 - 最大值:", max(directed_betweenness_centrality.values()), "最小值:", min(directed_betweenness_centrality.values()))
# print("无向图的介数中心性 - 最大值:", max(undirected_betweenness_centrality.values()), "最小值:", min(undirected_betweenness_centrality.values()))

# print("有向图的接近中心性 - 最大值:", max(directed_closeness_centrality.values()), "最小值:", min(directed_closeness_centrality.values()))
# print("无向图的接近中心性 - 最大值:", max(undirected_closeness_centrality.values()), "最小值:", min(undirected_closeness_centrality.values()))

# print("有向图的特征向量中心性 - 最大值:", max(directed_eigenvector_centrality.values()), "最小值:", min(directed_eigenvector_centrality.values()))
# print("无向图的特征向量中心性 - 最大值:", max(undirected_eigenvector_centrality.values()), "最小值:", min(undirected_eigenvector_centrality.values()))

# print("有向图的聚类系数 - 最大值:", max(directed_clustering.values()), "最小值:", min(directed_clustering.values()))
# print("无向图的聚类系数 - 最大值:", max(undirected_clustering.values()), "最小值:", min(undirected_clustering.values()))

# print("有向图的平均聚类系数:", directed_avg_clustering)
# print("无向图的平均聚类系数:", undirected_avg_clustering)

