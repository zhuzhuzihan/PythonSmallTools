

class NewConfigToCS:
    def __init__(self, listen_port,):
        self.ServerListenPort = listen_port
        self.ClientListenPort = listen_port

    def server_config(self):
        pass


if __name__ == '__main__':
    sip = input('请输入服务端的ip地址（如11.22.33.44）： ')
    Spl = input('请输入服务端的端口（为空默认29900，可以使用多端口如（2000-3000）： ')
    st = input('请输入需要转发的端口（格式为IP:Port，为空默认为127.0.0.1:12948：')
    preKey = input('请输入预共享密钥（为空默认为\"it\'s a secrcet\"）')
    SCrypt = input('请请填写加密方式(aes, aes-128, aes-192, salsa20, blowfish, twofish, cast5, 3des, tea, xtea, xor, sm4, '
                   'none, null)：')
    mode = input('请输入加速模式（fast3, fast2, fast, normal, manual，为空默认fast）：')
    Qpp = input('是否使用QPP(使加密更安全,填ture或者false):').lower()
    if Qpp == 'ture':
        Qpp = True
        Qppc = input('请输入\'垫\'值以提高安全性，值越高越安全（为空默认为61：')
    else:
        Qpp = False
        Qppc = None
    conn = input('请输入并发数（为空默认为1）')
    autoexpire = input('请输入自动过期时间（当活动在指定时间内未活动，自动断开链接，以秒为单位，为空或设0为自动禁用）：')

