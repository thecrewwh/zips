#coding: utf-8
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
#Vidcloud / vcstream.to
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.hosters.hoster import iHoster
import urllib
class cHoster(iHoster):

    def __init__(self):
        self.__sDisplayName = 'VidCloud'
        self.__sFileName = self.__sDisplayName

    def getDisplayName(self):
        return  self.__sDisplayName

    def setDisplayName(self, sDisplayName):
        self.__sDisplayName = sDisplayName + ' [COLOR skyblue]' + self.__sDisplayName + '[/COLOR]'

    def setFileName(self, sFileName):
        self.__sFileName = sFileName

    def getFileName(self):
        return self.__sFileName

    def getPluginIdentifier(self):
        return 'vidcloud'

    def isDownloadable(self):
        return True

    def isJDownloaderable(self):
        return True

    def getPattern(self):
        return ''

    def __getIdFromUrl(self, sUrl):
        #https://vcstream.to/embed/5bcf5b4c39aff/The.Spy.Who.Dumped.Me.mp4
        sPattern = 'vcstream.to/embed/([^<]+)/'
        oParser = cParser()
        aResult = oParser.parse(sUrl, sPattern)
        if (aResult[0]):
            return aResult[1][0]
        return ''

    def __getKey(self):
        return ''

    def setUrl(self, sUrl):
        self.__sUrl = str(sUrl)

    def checkUrl(self, sUrl):
        return True

    def getUrl(self):
        return self.__sUrl

    def getMediaLink(self):
        return self.__getMediaLinkForGuest()

    def __getMediaLinkForGuest(self):
        api_call = False

        sId = self.__getIdFromUrl(self.__sUrl)
        if '/embed5' not in self.__sUrl:
            url = 'https://vcstream.to/player?fid=%s&page=embed' % sId
        else:
            url=self.__sUrl
        sPattern = 'file.+?\\"([^<]+)\\"\}'
        oRequest = cRequestHandler(url)
        sHtmlContent = oRequest.request()

        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://vidcloud.pro',
            'Connection': 'keep-alive',
            'Referer': url,
        }
        
        if (aResult[0]):
            api_call = aResult[1][0].replace('\\\\', '').replace(':\\"', '').split('"')[0]
            head=urllib.urlencode(headers)
            api_call=api_call#+"|"+head
        if (api_call):
            return True, api_call

        return False, False

