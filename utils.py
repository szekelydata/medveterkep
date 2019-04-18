def text_processor(title,content):
    relevant=0
    severity=0
    deaths=0
    tamadas=[u'támad',u'sebes']
    for i in tamadas:
        if i in title+content:
            relevant=1
            severity=2
    tamadas=[u'halál',u'áldozat',u'ölt ',u'pusztít']
    for i in tamadas:
        if i in title+content:
            relevant=1
            severity=3
    tamadas=[u'medve',u'medvé']
    for i in tamadas:
        if i in title.replace(',',' ').replace('.',' ').lower():
            relevant=1
    for i in tamadas:
        if (u'medv' or u'nagyvad') not in title+content:
            relevant=-1
    tamadas=[u'medvegyev',u'medveczky',u'jegesmedvék',u'medvehagyma',u'aranymedve',u'szibéria',u' kupa',
             u'jégkorong',u'kosárlabda',u'labdarúgás',u'labdarúgó',u'steaua',
             u'c osztály',u'berlin',u'állatkert',u'medve-tó',u'oroszorsz',u' orosz ']
    for i in tamadas:
        if i in (title+content).replace(',',' ').replace('.',' ').lower():
            relevant=-1
    return relevant,severity,deaths