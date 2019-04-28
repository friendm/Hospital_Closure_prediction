st="Baldwin County, Alabama: Summary level: 050, state:01> county:003"

def normalize_index(x):
    prt1=x.split('>')
    prt2=prt1[0].split(':')
    print(prt2[3])
    return str(int(prt2[3]))+prt1[1].split(':')[1]

print(normalize_index(st))
