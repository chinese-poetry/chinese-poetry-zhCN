# -*- coding: utf-8 -*-
import six, os
from zhconv import convert_for_mw


if six.PY2:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

POETRY_DIRECTORY = './chinese-poetry/json/'


def trans(name):
    file_path = os.path.join(POETRY_DIRECTORY, name)

    raw = open(file_path, 'r').read()

    content = convert_for_mw(unicode(raw), 'zh-cn')

    output_path = os.path.join('./poetry/', name)

    with open(output_path, 'w') as f:
        f.write(content)
    
    


map(trans, os.listdir(POETRY_DIRECTORY))
