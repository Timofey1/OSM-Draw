import xml.dom.minidom as minidom


def getDoc(name):
    doc = minidom.parse(name)
    return doc


def getNodes(name):
    doc = getDoc(name)
    # node = doc.documentElement
    nodes = doc.getElementsByTagName("node")
    # print(len(nodes))
    # print(nodes[0].attributes["id"].value)

    DATA = []

    for node in nodes:
        jsdata = {"id": "", "lat": "", "lon": "", "tag": []}
        id = node.attributes['id'].value
        lat = node.attributes['lat'].value
        lon = node.attributes['lon'].value
        # print(id, lat, lon)
        jsdata["id"] = id
        jsdata["lat"] = lat
        jsdata["lon"] = lon
        tags = node.getElementsByTagName("tag")
        for tag in tags:
            t = {"k": "", "v": ""}
            # print(tag.attributes['k'].value, tag.attributes['v'].value)
            t["k"] = tag.attributes['k'].value
            t["v"] = tag.attributes['v'].value
            jsdata["tag"].append(t)
        DATA.append(jsdata)
    return DATA


def getWays(name):
    doc = getDoc(name)
    ways = doc.getElementsByTagName("way")

    DATA = []

    for way in ways:
        jsdata = {"id": "", "nd": [], "tag": []}
        id = way.attributes["id"].value
        jsdata["id"] = id
        nds = way.getElementsByTagName("nd")
        for nd in nds:
            ref = nd.attributes["ref"].value
            jsdata["nd"].append(ref)
        tags = way.getElementsByTagName("tag")
        for tag in tags:
            t = {"k": "", "v": ""}
            # print(tag.attributes['k'].value, tag.attributes['v'].value)
            t["k"] = tag.attributes['k'].value
            t["v"] = tag.attributes['v'].value
            jsdata["tag"].append(t)
        DATA.append(jsdata)
    return DATA


def getRel(name):
    doc = getDoc(name)
    relations = doc.getElementsByTagName("relation")

    DATA = []

    for rel in relations:
        jsdata = {"id": "", "mem": [], "tag": []}
        jsdata["id"] = rel.attributes["id"].value
        members = rel.getElementsByTagName("member")
        for mem in members:
            m = {"type": "", "ref": "", "role": ""}
            m['type'] = mem.attributes["type"].value
            m['ref'] = mem.attributes["ref"].value
            m['role'] = mem.attributes["role"].value
            jsdata["mem"].append(m)
        tags = rel.getElementsByTagName("tag")
        for tag in tags:
            t = {"k": "", "v": ""}
            # print(tag.attributes['k'].value, tag.attributes['v'].value)
            t["k"] = tag.attributes['k'].value
            t["v"] = tag.attributes['v'].value
            jsdata["tag"].append(t)

        DATA.append(jsdata)

    return DATA



