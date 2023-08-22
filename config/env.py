# env
class Env:
    HOST = 'xxx'
    MAINPAGE ='xxx'
    HEADLESS_FLAG = False
    BROWSER = 'chrome'
    PAGE_LOAD_TIMEOUT = 20
    POLL_FREQUENCY = 0.5
    TIMEOUT = 5

if __name__ == '__main__':
    a =Env()
    print(type(a.TIMEOUT))