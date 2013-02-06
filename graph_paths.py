#
# In the repository "PathAlgs" I have a big algorithm written that does what
# the two of these do separately, but PathAlgs algorithm does both of their
# functionalities in one call.




def paths_by_weight_real(graph, start, paths_dict):
    open_list = [start]
    paths_dict[start] = {}
    paths_dict[start][start] = 0
    while len(open_list) > 0:
            current = open_list[0]
            del open_list[0]
            for comic in graph[current]:
                    for hero in graph.keys():
                            if comic in graph[hero]:
                                    if hero not in paths_dict[start]:
                                            paths_dict[start][hero] = paths_dict[start][current] + weight(graph, current, hero)
                                            open_list.append(hero)
    return "Weighted paths for ", start, " completed."

# modeled after Dutch Computer Scientist Edsgar Dijkstra's algorithm

def dijkstra(G, v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    while len(final_dist) < len(G):
            w = shortest_dist_node(dist_so_far)
            final_dist[w] = dist_so_far[w]
            del dist_so_far[w]
            for x in G[w]:
                    if x not in final_dist:
                            if x not in dist_so_far:
                                    dist_so_far[x] = final_dist[w] + G[w][x]
                            elif final_dist[w] + G[w][x] < dist_so_far[x]:
                                    dist_so_far[x] = final_dist[w] + G[w][x]
    return final_dist

