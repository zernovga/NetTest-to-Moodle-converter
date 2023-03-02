file_name = '8 - Анализ списка слов заданной длины.html'
first_n_tasks = 100
cat = 'ЕГЭ/8/Анализ списка слов заданной длины'

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

    # print(q1)

    i1 = f.find('topicview', ae + 1)

moodle = open('moodle.xml', mode='w')
moodle.write('<?xml version="1.0" ?><quiz>\n')
moodle.write('''
    <question type="category">
        <category>
            <text>$course$/''' + cat + '''</text>
        </category>
    </question>''')
for i, q in enumerate(qs[:min(len(qs), first_n_tasks)]):
    qname = cat.replace('/', ' ') + ' ' + str(i)
    stared = ''
    if q['stared']:
        stared = 'Со звездочкой'
    else:
        stared = 'Базовая'
    moodle.write('''
    <question type="shortanswer">
        <tags>
            <tag>
                <text>Поляков</text>
            </tag>
            <tag>
                <text>''' + stared + '''</text>
            </tag>
        </tags>
        <name>
            <text>''' + qname + '''</text>
        </name>
        <questiontext format="html">
            <text><![CDATA[''' + qs[i]['text'] + ''']]></text>
        </questiontext>
        <answer fraction="100">
            <text>''' + qs[i]['valid_answer'] + '''</text>
            <feedback><text>Верно!</text></feedback>
        </answer>
    </question>
''')


moodle.write('</quiz>')
moodle.close()