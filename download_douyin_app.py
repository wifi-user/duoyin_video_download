import requests #用于获取页面代码
import urllib #用于解码
from pyquery import PyQuery as PQ #用于解析html
import os

def download(download_author,title,url):
    # print(url)
    # print(os.listdir('抖音/'))
    if download_author not in str(os.listdir()):
        print('创建文件夹：'+ download_author)
        os.mkdir(download_author)
    response_video = requests.get(url)
    with open(download_author+'/'+title+'.mp4','wb') as file:
        file.write(response_video.content)
        print(title,'下载完成！')

def main(url_douyin):
    #输入快手url
    response =requests.get(url_douyin,headers=headers)
    # print(response.text)
    # with open('html.txt','w') as file:
    #     file.write(response.text)
    data = PQ(response.text)
    title = data('title').text()#获取title标签
    print(title)
    script = data('script#RENDER_DATA').text()
    script_js = urllib.parse.unquote(script)#解码url编码
    # response_video = requests.get(url)
    with open('抖音文本.txt','w',encoding='utf-8') as file:
        file.write(script_js)
        print('下载完成！')
    # print(script_js)
    # "nickname":"𝑎𝑛𝑔𝑒𝑙马斯","remarkName"
    title1 = script_js.find('"nickname":"')
    title2 = script_js.find('","remarkName"')
    author = script_js[title1+12:title2]
    print('title: ',author,'\n\n',title1,'\n\n',title2,'\n\n')
    url1 = script_js.find('"playApi":"')
    url2 = script_js.find('","bitRateList"')
    url = 'http:'+script_js[url1+11:url2]#视频url
    # print(url,'\n\n',url1,'\n\n',url2)
    print('url: ',url)
    #下载函数
    download(author,title,url)
    
def get_douyin_url(url):
    #获取抖音直接分享URL解析跳转url
    # url = ' https://v.douyin.com/N99yx29/'#抖音分享视频链接
    if 'douyin.com/video/' in url :
        return url
    response =requests.get(url,allow_redirects=False)
    # print(response.text)
    get_url= response.headers['Location']#获取跳转链接
    # 001 : https://www.douyin.com/video/7080057739212328199
    # 002 : https://www.iesdouyin.com/share/video/7080057739212328199/?region=CN&mid=7080057762964589349&u_code=3a4m3e9g&did=MS4wLjABAAAAM4XbPhZRlgfJgDdt3OeORApKzVwyoAv5nwJWNjxJS1NZXfG6xU8kSv_pTG-ftklc&iid=MS4wLjABAAAAz38WqdXfS9Ei0YF_iFqm_1y3pYzDpsrDa0Kr2j3ScuOBseFrDyjZGuZVzaBhhURv&with_sec_did=1&titleType=title&utm_source=copy&utm_campaign=client_share&utm_medium=android&app=aweme
    # 001跳转002
    if 'douyin.com/share/video/' in get_url:
        get_url = get_douyin_url(get_url)
    print('\n\nget_douyin_url: '+get_url)
    return get_url#返回跳转url该跳转url含义视频链接



if __name__ == "__main__":
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'douyin.com; ttwid=1%7CLG-ZDqoaIpKHaK_ig5CJtsQ3NSECnPsDKNtWHiJCS2Q%7C1648304726%7Ce3d263df7af720b8d8757ef995c662c845d33971f6089f04edb72377d5ed7207; _tea_utm_cache_6383=undefined; douyin.com; strategyABtestKey=1648304730.553; passport_csrf_token=f4ffc11fdf4fd50ffc6b06dc77f7ba99; passport_csrf_token_default=f4ffc11fdf4fd50ffc6b06dc77f7ba99; AB_LOGIN_GUIDE_TIMESTAMP=1648304730402; s_v_web_id=verify_l17y2v7o_79heVmmv_EXg1_4VJe_BzYC_mvOGNBg61G3z; _tea_utm_cache_1300=undefined; MONITOR_WEB_ID=b2e68619-37e7-4565-b5f6-63e4668ada4a; ttcid=9488d287c65d433fa41c3753a3a54f6c22; _tea_utm_cache_2285=undefined; THEME_STAY_TIME=299118; IS_HIDE_THEME_CHANGE=1; msToken=_UnTOf72o6ZrksrgepvuXjvRmmhs3OMVutpDSsNtfTS8C3JfFNJKB2FCY2hkcIrj4uaixl5jIIb_UNSeIMlLTVhTpVgItmI7XLaDcg71NMJPWp8xBa1Cfw==; pwa_guide_count=3; home_can_add_dy_2_desktop=1; tt_scid=tacQWhuRV4FExaVFHJ-rgIVy9kSGNkon1RofoCSY9H80NjtxFxe5rxUTV-Yo175P31ac; msToken=nFNQXZFARrRDW_sUVPXj6eA06ax9k88xyT6qnE62FCupj7kUlZg5BbW2AEZYsW2upeoA9AZCmQ4aeHa-HJbPAAmq2DDgHNJP8YxRpBKwN5mX_6qqVB80Fw==; __ac_nonce=0623f342f008b1a036e50; __ac_signature=_02B4Z6wo00f01NQ3XiAAAIDBCkEGhXfd1fDUF1qAAFc4Jix9iz7xUepFTlU1gMjk4UESvn0pzdOSHJqw8ivxA5ed9atU6WvWpn-Em3pgb62SyDQYxDxLksD7nQifTnYHeY7PkYFn57h9szrZfb; __ac_referer=__ac_blank',
    'referer': 'https://www.douyin.com/video/7075484290640923937',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    
    
    def app():
        try:
            URL_home = input("输入抖音链接：")
            URL = get_douyin_url(URL_home)
            #https://www.douyin.com/discover?modal_id=7075484290640923937
            url = URL.replace('discover?modal_id=', 'video/')
            print(url)
            main(url)#运行主函数
        except:
            print('error\n\n')
        app()
    app()








