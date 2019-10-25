import time
import requests
import webbrowser

def count_down(m, url):
    '''Count down to open a website'''
    for m in range(m, 0, -1):
        minute = m - 1
        if minute < 10:
            minute = '0' + str(minute)
        for s in range(59, 0, -1):
            if s < 10:
                s = '0' + str(s)
            print(f'{minute}:{s}', end=' \r')
            time.sleep(1)

    webbrowser.open(url)

def main():
    
    while True:
        m = input('请输入倒计时的分钟数: ')
        if m == '' or m.count(' ') >= 1:
            continue
        try:
            m = int(m)
        except Exception:
            print('请输入分钟数(正整数)')
            continue
        break    
    while True:    
        url = input('请输入到计时结束后要开启的网站: ')
        if url == '' or url.count(' ') >= 1:
            continue
        if url[:7] != 'http://' or url[:8] != 'https://':
            url = 'http://' + url
        try:
            requests.get(url)
        except Exception:
            print('您输入的url无法访问，请在输入有效的url!')
            continue
        break

    count_down(m, url)

if __name__ == '__main__':
    main()
