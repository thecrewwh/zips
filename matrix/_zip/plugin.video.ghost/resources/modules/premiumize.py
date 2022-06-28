# -*- coding: utf-8 -*-

import time

from resources.modules import log
import  json, re, logging,sys,xbmcgui,xbmc,os

from resources.modules import tools

import xbmcaddon

Addon = xbmcaddon.Addon()
from  resources.modules.client import get_html
try:
    resuaddon=xbmcaddon.Addon('script.module.resolveurl')
   
except Exception as e:
    
    pass
def copy2clip(txt):
    import subprocess
    platform = sys.platform

    if platform == 'win32':
        try:
            cmd = 'echo ' + txt.strip() + '|clip'
            return subprocess.check_call(cmd, shell=True)
            pass
        except:
            pass
    elif platform == 'linux2':
        try:
            from subprocess import Popen, PIPE

            p = Popen(['xsel', '-pi'], stdin=PIPE)
            p.communicate(input=txt)
        except:
            pass
    else:
        pass
    pass
def colorString(text, color=None):
    

    if color == 'default' or color == '' or color == None:
        color = ''
        if color == '':
            color = 'deepskyblue'

    try:
        return '[COLOR ' + str(color) + ']' + text + '[/COLOR]'
    except:
        return '[COLOR ' + str(color) + ']' + text   + '[/COLOR]'


class Premiumize:

    def __init__(self):
        self.client_id = "723798446"
        self.client_secret = "c2dnzt55hc7qw9zqbe"
        self.headers = {
            'Authorization': 'Bearer {}'.format(Addon.getSetting('premiumize.token'))
        }
        if Addon.getSetting('premiumize.token')=='':
            self.auth()
        self.headers = {
            'Authorization': 'Bearer {}'.format(Addon.getSetting('premiumize.token'))
        }

    def auth(self):
        
        data = {'client_id': self.client_id, 'response_type': 'device_code'}
        token = get_html('https://www.premiumize.me/token', data=data).json()
        expiry = token['expires_in']
        token_ttl = token['expires_in']
        poll_again = True
        success = False
        copy2clip(token['user_code'])
        tools.progressDialog.create(tools.addonName,
                                    'Open this link in a browser: {}'.format(colorString(token['verification_uri']))+'\n'+
                                    'Enter the code: {}'.format(colorString(token['user_code'])))
        tools.progressDialog.update(0)
        log.warning(token)
        while poll_again and not token_ttl <= 0 and not tools.progressDialog.iscanceled():
            poll_again, success = self.poll_token(token['device_code'])
            progress_percent = 100 - int((float((expiry - token_ttl) / expiry) * 100))
            tools.progressDialog.update(progress_percent)
            time.sleep(token['interval'])
            token_ttl -= int(token['interval'])
            
        tools.progressDialog.close()

        if success:
            tools.showDialog.ok(tools.addonName, 'Authentication is completed')

    def poll_token(self, device_code):
      
        data = {'client_id': self.client_id, 'code': device_code, 'grant_type': 'device_code'}
        token = get_html('https://www.premiumize.me/token', data=data).json()
        
        if 'error_code' in token:
            return True, False
        if 'error' in token:
            if token['error'] == "access_denied":
                return False, False
            return True, False

        tools.setSetting('premiumize.token', token['access_token'])
        self.headers['Authorization'] = 'Bearer {}'.format(token['access_token'])

        account_info = self.account_info()
        tools.setSetting('premiumize.username', account_info['customer_id'])

        return False, True

    def get_url(self, url):
       
        if self.headers['Authorization'] == 'Bearer ':
            tools.log('User is not authorised to make PM requests')
            return None
        url = "https://www.premiumize.me/api{}".format(url)
        req = get_html(url, timeout=10, headers=self.headers).json()
        log.warning('f_url')
        log.warning(url)
        return req

    def post_url(self, url, data):
       
        
        if self.headers['Authorization'] == 'Bearer ':
            tools.log('User is not authorised to make PM requests')
            xbmc.executebuiltin((u'Notification(%s,%s)' % ('Error', 'User is not authorised to make PM requests')))
            return None
        url = "https://www.premiumize.me/api{}".format(url)
        log.warning('f_url')
        log.warning(url)
        req = get_html(url, headers=self.headers, data=data, timeout=10).json()
        log.warning(req)
        return req

    def account_info(self):
        url = "/account/info"
        response = self.get_url(url)
        return response

    def list_folder(self, folderID):
        url = "/folder/list"
        postData = {'id': folderID}
        response = self.post_url(url, postData)
        return response['content']

    def list_folder_all(self, folderID):
        url = "/item/listall"
        response = self.get_url(url)
        return response['files']

    def hash_check(self, hashList):
        url = '/cache/check'
        #postData = {'items[]': hashList}
        #response = self.post_url(url, postData)
        all_mag=[]
        for itt in hashList:
            all_mag.append(itt)
            
        response =self.get_url(url+'?items%5B%5D='+'&items%5B%5D='.join(all_mag))
       
        return response

    def item_details(self, itemID):
        url = "/item/details"
        postData = {'id': itemID}
        return self.post_url(url, postData)

    def create_transfer(self, src, folderID=0):
        postData = {'src': src, 'folder_id': folderID}
        url = "/transfer/create"
        return self.post_url(url, postData)

    def direct_download(self, src):
        postData = {'src': src}
        url = '/transfer/directdl'
        log.warning(postData)
        log.warning(url)
        return self.post_url(url, postData)

    def list_transfers(self):
        url = "/transfer/list"
        postData = {}
        return self.post_url(url, postData)

    def delete_transfer(self, id):
        url = "/transfer/delete"
        postData = {'id': id}
        return self.post_url(url, postData)

    def get_used_space(self):
        info = self.account_info()
        used_space = int(((info['space_used'] / 1024) / 1024) / 1024)
        return used_space

    def hosterCacheCheck(self, source_list):
        post_data = {'items[]': source_list}
        return self.post_url('/cache/check', data=post_data)

    def updateRelevantHosters(self):
        hoster_list = database.get(self.post_url, 1, '/services/list', {})
        return hoster_list

    def resolve_hoster(self, source):

        directLink = self.direct_download(source)
        if directLink['status'] == 'success':
            stream_link = directLink['location']
        else:
            stream_link = None

        return stream_link

    def folder_streams(self, folderID):
        from resources.modules import source_utils
        files = self.list_folder(folderID)
        returnFiles = []
        for i in files:
            if i['type'] == 'file':
                if i['transcode_status'] == 'finished':
                    returnFiles.append({'name': i['name'], 'link': i['stream_link'], 'type': 'file'})
                else:
                    for extension in source_utils.COMMON_VIDEO_EXTENSIONS:
                        if i['link'].endswith(extension):
                            returnFiles.append({'name': i['name'], 'link': i['link'], 'type': 'file'})
                            break
        return returnFiles

    def internal_folders(self, folderID):
        folders = self.list_folder(folderID)
        returnFolders = []
        for i in folders:
            if i['type'] == 'folder':
                returnFolders.append({'name': i['name'], 'id': i['id'], 'type': 'folder'})
        return returnFolders

    def _single_magnet_resolve(self, magnet, pack_select=False):
        import logging
        from resources.modules import source_utils
       
        response=(self.direct_download(magnet))
        if response['status']=='error':
            tools.showDialog.ok(tools.addonName, response['message'])
            return '0'
        folder_details = response['content']
        folder_details = sorted(folder_details, key=lambda i: int(i['size']), reverse=True)
        folder_details = [i for i in folder_details if source_utils.is_file_ext_valid(i['link'])]
        
        return folder_details[0]['stream_link'] if tools.getSetting('premiumize.transcoded') == 'true' else folder_details[0]['link']
        '''
        filter_list = [i for i in folder_details if source_utils.filter_movie_title(i['path'].split('/')[-1],
                                                                                    args['info']['title'],
                                                                                    args['info']['year'])]
        '''
        if len(filter_list) == 1:
            stream_link = self._fetch_transcode_or_standard(filter_list[0])
            self._handle_add_to_cloud(magnet)
            return stream_link

        filter_list = [tfile for tfile in folder_details if 'sample' not in tfile['path'].lower()]
        filter_list = [tfile for tfile in filter_list if source_utils.cleanTitle(args['info']['title'])
                          in source_utils.cleanTitle(tfile['path'].lower())]

        if len(filter_list) == 1:
            stream_link = self._fetch_transcode_or_standard(filter_list[0])
            self._handle_add_to_cloud(magnet)
            return stream_link


    def resolve_magnet(self, magnet, args, torrent, pack_select):
        from resources.modules import source_utils
        if 'showInfo' not in args:
            return self._single_magnet_resolve(magnet, args)

        try:

            folder_details = self.direct_download(magnet)['content']

            if pack_select != False and pack_select != None:
                return self.user_select(folder_details)

            folder_details = source_utils.clear_extras_by_string(args, 'extras', folder_details)
            folder_details = source_utils.clear_extras_by_string(args, 'specials', folder_details)
            folder_details = source_utils.clear_extras_by_string(args, 'featurettes', folder_details)
            folder_details = source_utils.clear_extras_by_string(args, 'deleted scenes', folder_details)
            folder_details = source_utils.clear_extras_by_string(args, 'sample', folder_details)

            folder_details = [i for i in folder_details if source_utils.is_file_ext_valid(i['link'])]

            identified_file = source_utils.get_best_match('path', folder_details, args)

            stream_link = self._fetch_transcode_or_standard(identified_file)

        except:
            import traceback
            traceback.print_exc()
            return

        if stream_link != None:
            self._handle_add_to_cloud(magnet)

        return stream_link

    def _handle_add_to_cloud(self, magnet):
       
        if tools.getSetting('premiumize.addToCloud') == 'true':
            transfer = self.create_transfer(magnet)
            database.add_premiumize_transfer(transfer['id'])

    def _fetch_transcode_or_standard(self, file_object):
       
        if tools.getSetting('premiumize.transcoded') == 'true' and \
                file_object['transcode_status'] == 'finished':
            return file_object['stream_link']
        else:
            return file_object['link']

    def user_select(self, content):
        from resources.modules import source_utils
       
        display_list = []
        for i in content:
            if any(i['path'].endswith(ext) for ext in source_utils.COMMON_VIDEO_EXTENSIONS):
                display_list.append(i)

        selection = tools.showDialog.select('{}: {}'.format(tools.addonName,'Torrent File Picker'),
                                            [i['path'] for i in display_list])
        if selection == -1:
            return None

        selection = content[selection]

        if tools.getSetting('premiumize.transcoded') == 'true':
            if selection['transcode_status'] == 'finished':

                return selection['stream_link']
            else:
                pass

        return selection['link']

    def get_hosters(self, hosters):

        host_list = database.get(self.updateRelevantHosters, 1)
        if host_list==None:
            host_list = self.updateRelevantHosters()

        if host_list != None:
            hosters['premium']['premiumize'] = [(i, i.split('.')[0]) for i in host_list['directdl']]
        else:
            hosters['premium']['premiumize'] = []
