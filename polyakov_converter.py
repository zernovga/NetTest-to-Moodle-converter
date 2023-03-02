file_name = '8.html'

qs = []

f = '\n'.join(open(file_name).readlines())
i1 = f.find('topicview')
while i1 > 0:
    q1 = {}

    ids = f.find('(№&nbsp;', i1) + len('(№&nbsp;')
    ide = f.find(')', ids)
    q1['id'] = f[ids:ide]

    ts = f.find('changeImageFilePath(', i1) + len('changeImageFilePath(') + 1 
    q1['stared'] = f[ts] == '*'

    if '(' in f[ts:ts+5]:
        ts = f.find(') ', ts) + len(') ')
    te = f.find("')", ts)
    q1['text'] = f[ts:te]

    ast = f.find('changeImageFilePath(', te) + len('changeImageFilePath(') + 1
    ae = f.find("')", ast)
    q1['valid_answer'] = f[ast:ae]
    qs.append(q1)

    print(q1)

    i1 = f.find('topicview', ae + 1)



cat = 'test'

moodle = open('moodle.xml', mode='w')
moodle.write('<?xml version="1.0" ?><quiz>\n')
moodle.write('''
    <question type="category">
        <category>
            <text>$course$/''' + cat + '''</text>
        </category>
    </question>''')
for i, q in enumerate(qs):
    qname = cat + '-' + str(i)
    moodle.write('''
    <question type="shortanswer">
        <tag>
            <text>NetTest</text>
        </tag>
        <name>
            <text>''' + qname + '''</text>
        </name>
        <questiontext format="html">
            <text>''' + qs[i]['text'] + '''</text>
        </questiontext>
        <answer fraction="100">
            <text>''' + qs[i]['valid_answer'] + '''</text>
            <feedback><text>Верно!</text></feedback>
        </answer>
    </question>
''')


moodle.write('</quiz>')
moodle.close()