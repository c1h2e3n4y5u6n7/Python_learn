import yaml
import ruamel
from ruamel import yaml
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)


##一个文件中包含一个文档
## 打开yaml文件
file=open('./test.yaml','r',encoding="utf-8")
data=file.read()
file.close()
## yaml打开的文件，内容的类型是str
data_dict=yaml.load(data)
print(data_dict)
print(data_dict['usr'])

##一个文件中包含多个文档
file = open('./test1.yaml', 'r', encoding="utf-8")
file_data = file.read()
file.close()
all_data = yaml.load_all(file_data)
for data in all_data:
    print(data)


## 将yaml写入yaml文件中
py_object = {'school': 'zhang','students': ['a', 'b']}
file = open('./Generation.yaml','w',encoding='utf-8')
yaml.dump(py_object, file)
file.close()

## 使用ruamel写入yaml文件
py_object = {'school': 'zhang',
             'students': ['a', 'b']}
file = open('./Generation1.yaml', 'w', encoding='utf-8')
yaml.dump(py_object, file, Dumper=yaml.RoundTripDumper)

## 使用ruamel读取yaml文件
file = open('./test.yaml', 'r', encoding='utf-8')
data = yaml.load(file.read(),Loader=ruamel.yaml.Loader)
file.close()
print(data)