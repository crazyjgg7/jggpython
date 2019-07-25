from smb.SMBConnection import *
import os
class SMBClient(object):
    '''
    smb连接客户端
    '''
    user_name = ''
    passwd = ''
    ip = ''
    prot = None

    status = False
    samba = None

    def __init__(self, user_name, passwd, ip, port=445):
        self.user_name = user_name
        self.passwd = passwd
        self.ip = ip
        self.port = port

    def connect(self):
        try:
            self.samba = SMBConnection(self.user_name, self.passwd, '', '', use_ntlm_v2=True)
            self.samba.connect(self.ip, self.port)
            self.status = self.samba.auth_result
        except:
            self.samba.close()
         

    def disconnect(self):
        if self.status:
            self.samba.close()

    def all_file_names_in_dir(self, service_name, dir_name):
        '''
        列出文件夹内所有文件名
        :param service_name:
        :param dir_name:
        :return:
        '''
        f_names = list()
        for e in self.samba.listPath(service_name, dir_name):

            if e.filename[0] != '.':
                f_names.append(e.filename)
            return f_names    

   
            #if len(e.filename) > 3: （会返回一些.的文件，需要过滤）　　　　　　　
                
        

    def download(self, f_names, service_name, smb_dir, local_dir):
        '''
        下载文件
        :param f_names:文件名
        :param service_name:服务名（smb中的文件夹名）
        :param smb_dir: smb文件夹
        :param local_dir: 本地文件夹
        :return:
        '''
        assert isinstance(f_names, list)
        for f_name in f_names:
            f = open(os.path.join(local_dir, f_name), 'w')
            self.samba.retrieveFile(service_name, os.path.join(smb_dir, f_name), f)
            f.close()
    def upload(self, service_name, smb_dir, file_name):
        self.samba.storeFile(service_name, smb_dir, file_name)

    # '''
    # 上传文件
    # :param f_names:文件名
    # :param service_name:服务名（smb中的文件夹名）
    # :param smb_dir: smb文件夹
    # :param local_dir: 本地文件夹
    # :return:    
    # '''
    

    def createDir(self, service_name, path):
        # """
        # 创建文件夹
        # :param service_name:
        # :param path:
        # :return:
        # """
        try:
            self.samba.createDirectory(service_name, path)
            print('创建文件成功')

        except OperationFailure:
            pass
            
if __name__ == '__main__':

    smbf=SMBClient('crazyjgg','jgg171891','172.16.0.15',port=445)
    smbf.connect()
    result=smbf.all_file_names_in_dir('VocLog','dir_name')
    #smbf.createDir('testfile','\\VocLog') 
    print(result)
    smbf.disconnect()           
