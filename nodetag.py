
import xml.etree.ElementTree as xxx
import matplotlib.pyplot as plt

e = xxx.parse("map.xml").getroot()
node_dict_tmp = {}


way_types = ["motorway", "trunk", "primary", "secondary", "tertiary", "unclassified", "residential", "service",
             "living_street", "building"]

for i in e:
    # Nodes.
    if i.tag == "node":
        node_dict_tmp[i.attrib["id"]] = [i.attrib["lat"], i.attrib["lon"]]

    if i.tag == "way":
        insert = False
        directed = False
        max_speed_v = None
        way_tmp = []
        for j in i:
            if j.tag == "nd":
                way_tmp.append(j.attrib["ref"])
            if j.tag == "tag":
                if j.attrib["k"] == "highway" and j.attrib["v"] in way_types:
                    insert = True
                if j.attrib["k"] == "building" and j.attrib["v"] == "yes":
                    insert = True

print(node_dict_tmp)
print(way_tmp)

nodes = []
for i in way_tmp:
    nodes.append(node_dict_tmp[i])

for i in nodes:
    c = 0
    i[c] = float(i[c])
    i[c+1] = float(i[c+1])
    # plt.plot(int(float(i[c])*10000000), int(float(i[c+1])*10000000), "o")

# plt.show()
print(nodes)

for points in [nodes]:
    xs, ys = zip(*points)
    plt.plot(xs, ys, 'o')
    plt.plot(xs, ys, '-')

    automin, automax = plt.xlim()
    plt.xlim(automin-0.5, automax+0.5)
    automin, automax = plt.ylim()
    plt.ylim(automin-0.5, automax+0.5)
plt.show()









# network_nodes = G.nodes()
# print(network_nodes)
# nx.draw_networkx_nodes(G, nx.spring_layout(G))
