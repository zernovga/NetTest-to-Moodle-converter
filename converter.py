import xml.etree.cElementTree as ET

cat = 'ЕГЭ/11'
file_name = '11.xml'

tree = ET.parse(file_name)
questions = tree.findall('question')

qs = []

for i, q in enumerate(questions):
    q1 = {}
    q1['text'] = q.find('text').text[1:]
    q1['type'] = q.find('type').text
    q1['valid_answer'] = q.find('answers/answer[@valid="1"]').text
    qs.append(q1)


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
            <text>''' + qs[0]['text'] + '''</text>
        </questiontext>
        <answer fraction="100">
            <text>''' + qs[0]['valid_answer'] + '''</text>
            <feedback><text>Верно!</text></feedback>
        </answer>
    </question>
''')

moodle.write('</quiz>')
moodle.close()
