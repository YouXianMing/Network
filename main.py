from networking import *


def get():
    """
    Get请求基本使用
    :return: None
    """

    web_text = Networking("http://www.cnblogs.com/").get().response.text
    print(web_text)


def post():
    """
    Post请求基本使用
    :return: None
    """

    web_text = Networking("http://www.cnblogs.com/").post().response.text
    print(web_text)


def download():
    """
    下载数据以及回调
    :return: None
    """

    def download_report(block_num, block_size, size):

        per = 100.0 * block_num * block_size / size
        print("%2.2f%%" % per)

    network = Networking(url="http://hiphotos.baidu.com/mgzcalice/pic/item/ed96859676e2607dd0135ee4.jpg",
                         download_file_path='/Users/YouXianMing/Desktop/ed96859676e2607dd0135ee4.jpg',
                         reporthook=download_report).download()

    print(network.message)
    print(network.file_path)


get()
post()
download()