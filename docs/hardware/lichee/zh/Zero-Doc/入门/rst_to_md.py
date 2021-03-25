import requests
import os

def md_to_rst(from_file, to_file):
    """
    将markdown格式转换为rst格式
    @param from_file: {str} markdown文件的路径
    @param to_file: {str} rst文件的路径
    """
    response = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'markdown', 'from': 'rst'},
        files={'input_files[]': open(from_file, 'rb')}
    )

    if response.ok:
        with open(to_file, "wb") as f:
            f.write(response.content)


if __name__ == '__main__':
    a = os.getcwd()
    list = os.listdir(a)
    list.remove("rst_to_md.py")
    for i in range(len(list)):

        md_to_rst(str(list[i]), str(list[i].replace("rst", "md")))
