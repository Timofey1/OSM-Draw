from mapFunc import *
import xml.etree.ElementTree as xxx
import matplotlib.pyplot as plt

mapName = "mapfull.xml" 


e = xxx.parse(mapName).getroot()
node_dict_tmp = {}


way_types = ["motorway", "trunk", "primary", "secondary", "tertiary", "unclassified", "residential", "service",
             "living_street", "building"]

for i in e:
    # Nodes.
    if i.tag == "node":
        node_dict_tmp[i.attrib["id"]] = [float(i.attrib["lat"]), float(i.attrib["lon"])]

print(node_dict_tmp)
print(getWays(mapName))
ways = getWays(mapName)

fig = []

for way in ways:
    smf = []
    for i in way["nd"]:
        smf.append(node_dict_tmp[i])
    fig.append(smf)

for points in fig:
    xs, ys = zip(*points)
    plt.plot(xs, ys, 'o')
    plt.plot(xs, ys, '-')

    automin, automax = plt.xlim()
    plt.xlim(automin-0.5, automax+0.5)
    automin, automax = plt.ylim()
    plt.ylim(automin-0.5, automax+0.5)
plt.show()