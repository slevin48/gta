import pandas as pd
import xml.etree.ElementTree as ET

def read_controller(XMLfile):
    # XMLfile = 'test.xml'
    tree = ET.parse(XMLfile)
    root = tree.getroot()
    states = [child for child in root]

    state0 = states[0].getchildren()
    headers = [i.tag for i in state0]

    rows = []
    for i in states:
        state_i = i.getchildren()
        rows.append([j.text for j in state_i])

    df = pd.DataFrame(rows,columns = headers)
    return df 