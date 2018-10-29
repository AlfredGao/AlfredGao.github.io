import  urllib
# import urllib3
import urllib2, os, re, time, sys, httplib, errno
from bs4 import BeautifulSoup
logType = {1:'INFO', 2:'ERROR', 3:'WARINING'}
INFO = 1
ERROR = 2
WARN = 3
TARGET = "/Users/AlfredGao/Desktop/AlfredGao.github.io/whatTravel/upload/travel"
TARGET2 = "/Users/AlfredGao/Desktop/AlfredGao.github.io/whatTravel/upload/pictures"

def setupReq(url):
    values = {'name' : 'Michael Foord',

                'location' : 'Los Angeles',

                'language' : 'Python' }

    headers = { 'User-Agent' : 'Custom User-Agent' }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    req.add_unredirected_header('User-Agent', 'Custom User-Agent')
    return req


def log4P(id, type, info):
    timeStr = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
    print timeStr + " [" + str(logType[type]) + "]: " + str(id) + " " + str(info)

 
def parser(url):
    log4P(0, INFO, 'Start to download the img')
    urllib2.socket.setdefaulttimeout(60)
    null_proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    log4P(1, INFO, 'After install opener')


def getDivImg(url):
    urlStr = "Start down loading " + str(url)
    log4P(2, INFO, urlStr)
    try:
        req = setupReq(url)
        content  = urllib2.urlopen(req)
        soup = BeautifulSoup(content)
        my_img = soup.find_all('div', attrs={'class': 'img'})
        log4P(16, INFO, my_img)
        for img in my_img:
            img_link = img.get('style')
            # log4P(INFO, img_link)
            if img_link is not None:
                imgName = img_link[img_link.find('(')+1 : img_link.find(')')]
                dirName = TARGET2 + "/" + imgName.split('/')[3]
                log4P(3, INFO, dirName)
                fileSaveName = dirName + "/" + imgName.split('/')[4]
                log4P(4, INFO, fileSaveName)
                urlLink = "http://m.100.travel" + imgName
                # if not os.path.exists(dirName):
                #     try:
                #         os.mkdir(dirName)
                #         log4P(INFO, "Scuessfully create dir: " + dirName)
                #     except:
                #         log4P(ERROR, "Cannot create dir" + dirName)
                # log4P(INFO, "Save pic to dir: " + dirName)
                try:
                    os.makedirs(dirName)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
                try:
                    urllib.urlretrieve(urlLink, fileSaveName)
                except Exception as e:
                    print e
                    log4P(5, ERROR, "Cannot download the file: " + urlLink)
                log4P(6, INFO, "Successfully Download: " + fileSaveName)
    except urllib2.HTTPError, e:
        log4P(14, ERROR, 'HTTPError = ' + str(e.code))
    except urllib2.URLError, e:
        log4P(14, ERROR, 'URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
        log4P(14, ERROR, 'HTTPException')
    except Exception:
        import traceback
        log4P(14, ERROR, 'generic exception: ' + traceback.format_exc())


def getImg(url):
    urlStr = "Start down loading " + str(url)
    log4P(8, INFO, urlStr)
    try:
        req = setupReq(url)
        content  = urllib2.urlopen(req)
        soup = BeautifulSoup(content)
        my_img = soup.find_all('img')
        for img in my_img:
            img_link = img.get('src')
            if "/Public" not in img_link and "0.jpg" not in img_link:
                # log4P(INFO, img_link)
                urlLink = "http://m.100.travel" + img_link
                log4P(10, INFO, "Downloading " + img_link)
                filedir = img_link.split('/')[3]
                fileName = img_link.split('/')[4]
                log4P(11, INFO, fileName)
                fileSave = TARGET + "/" + filedir + "/" + fileName
                fileSaveDir = TARGET + "/" + filedir
                # if not os.path.exists(fileSaveDir):
                #     try:
                #         os.mkdir(fileSaveDir)
                #         log4P(INFO, "Scuessfully create dir: " + fileSaveDir)
                #     except:
                #         log4P(ERROR, "Cannot create file dir!!!" + fileSaveDir)
                # log4P(INFO, "Saving pic to dir: " + filedir)
                try:
                    os.makedirs(fileSaveDir)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
                try:
                    urllib.urlretrieve(urlLink, fileSave)
                except:
                    log4P(12, ERROR, "Cannot download the file: " + fileSave)
                log4P(13, INFO, "Successfully Download: " + fileSave)
    except urllib2.HTTPError, e:
        log4P(15, ERROR, 'HTTPError = ' + str(e.code))
    except urllib2.URLError, e:
        log4P(15, ERROR, 'URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
        log4P(15, ERROR, 'HTTPException')
    except Exception:
        import traceback
        log4P(15, ERROR, 'generic exception: ' + traceback.format_exc())

uurlList = ['http://m.100.travel/t35', 'http://m.100.travel/t151', 'http://m.100.travel/t37', 'http://m.100.travel/t150', 'http://m.100.travel/t141', 'http://m.100.travel/t153', 'http://m.100.travel/t149', 'http://m.100.travel/t12', 'http://m.100.travel/t11', 'http://m.100.travel/t136']
# uurlList = ['http://m.100.travel/t129']
for uurl in uurlList:
    parser(uurl)
    getImg(uurl)
    getDivImg(uurl)

