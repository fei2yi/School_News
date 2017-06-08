
import os
from School_News.lib.environment import env


def write_file(filename,text):
    file_path = os.path.join(env.file_path, filename)
    f = open(file_path, 'a', encoding='UTF-8')
    f.write(text)

def transport(filename, key):
    file_path = os.path.join(env.file_path, filename)
    f = open(file_path, 'r', encoding='UTF-8')
    content = f.read()
    l = eval(content)
    webaddress = [d[key] for d in l if key in d.keys()]

    return webaddress