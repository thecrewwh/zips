# -*- coding: utf-8 -*-

'''
    Genesis Add-on
    Copyright (C) 2015 lambda

    -Mofidied by The Crew
    -Copyright (C) 2019 The Crew


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import json
import os
import sys
import traceback

import xbmc
import xbmcplugin

from resources.lib.modules import control, log_utils

HOME = xbmc.translatePath('special://home/')
FILENAME = os.path.join(HOME, 'userdata/addon_data/plugin.video.thecrew/bookmarks.json')

defaults = {'Channels': {},
            'Documentaries': {},
            'Radio': {},
            'Podcasts': {}
            }


class jsonBookmarks(object):
    def __init__(self):
        if not os.path.exists(FILENAME):
            f = open(FILENAME, 'w')
            temp = json.dumps(defaults)
            f.write(temp)
            f.close()
            self.bookmarks = json.loads(temp)
        else:
            with open(FILENAME) as json_file:
                self.bookmarks = json.load(json_file)

    def add_channel(self, dbase):
        temp = dbase.decode('base64').split('|')
        name = temp[0]
        chan_id = temp[1]
        action = temp[2]
        icon = temp[3]
        url = temp[4]
        try:
            if action in self.bookmarks['Channels']:
                if chan_id not in self.bookmarks['Channels'][action]:
                    self.bookmarks['Channels'][action][chan_id] = {'name': name, 'id': chan_id, 'action': action, 'icon': icon, 'url': url}
                    self.save()
                    control.refresh()
            else:
                self.bookmarks['Channels'][action] = {}
                self.bookmarks['Channels'][action][chan_id] = {}
                self.bookmarks['Channels'][action][chan_id] = {'name': name, 'id': chan_id, 'action': action, 'icon': icon, 'url': url}
                self.save()
                control.refresh()
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('Bookmarks - Add Channel Exception: \n' + str(failure))

    def rem_channel(self, dbase):
        temp = dbase.decode('base64').split('|')
        chan_id = temp[1]
        action = temp[2]
        try:
            del self.bookmarks['Channels'][action][chan_id]
            self.save()
            control.refresh()
        except Exception:
            from resources.lib.dialogs import ok
            ok.load('Bookmarks Error', '[B]Error removing channel.[/B]')
            failure = traceback.format_exc()
            log_utils.log('Remove Channel Bookmark - Exception: \n' + str(failure))
            return

    def show_channels(self):
        items = []
        for action in self.bookmarks['Channels'].keys():
            for entry in self.bookmarks['Channels'][action].keys():
                try:
                    channel = self.bookmarks['Channels'][action][entry]
                    item = control.item(label=channel['name'])
                    item.setProperty("IsPlayable", "true")
                    item.setArt({"thumb": channel['icon'], "icon": channel['icon']})
                    item.setInfo(type="video", infoLabels={"Title": channel['name'], "mediatype": "video"})
                    url = '%s?action=%s&url=%s' % (sys.argv[0], channel['action'], channel['url'])

                    cm = self.build_cm('Channels', name=channel['name'], id=channel['id'], action=channel['action'], icon=channel['icon'], url=channel['url'])
                    item.addContextMenuItems(cm)

                    try:
                        item.setContentLookup(False)
                    except AttributeError:
                        pass
                    items.append((url, item, False))
                except Exception:
                    from resources.lib.dialogs import ok
                    ok.load('Bookmarks Error', '[B]Error loading bookmarks.[/B]')
                    failure = traceback.format_exc()
                    log_utils.log('Show Channel Bookmarks - Exception: \n' + str(failure))
                    return
        control.addItems(int(sys.argv[1]), items)
        self.endDirectory('files', xbmcplugin.SORT_METHOD_LABEL)

    def add_podcast(self, dbase):
        temp = dbase.decode('base64').split('|')
        name = temp[0]
        show_id = temp[1]
        action = temp[2]
        icon = temp[3]
        url = temp[4]
        try:
            if action in self.bookmarks['Podcasts']:
                if show_id not in self.bookmarks['Podcasts'][action]:
                    self.bookmarks['Podcasts'][action][show_id] = {'name': name, 'id': show_id, 'action': action, 'icon': icon, 'url': url}
                    self.save()
                    control.refresh()
            else:
                self.bookmarks['Podcasts'][action] = {}
                self.bookmarks['Podcasts'][action][show_id] = {}
                self.bookmarks['Podcasts'][action][show_id] = {'name': name, 'id': show_id, 'action': action, 'icon': icon, 'url': url}
                self.save()
                control.refresh()
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('Bookmarks - Add Podcast Exception: \n' + str(failure))
#TC 2/01/19 started
    def rem_podcast(self, dbase):
        temp = dbase.decode('base64').split('|')
        show_id = temp[1]
        action = temp[2]
        try:
            del self.bookmarks['Podcasts'][action][show_id]
            self.save()
            control.refresh()
        except Exception:
            from resources.lib.dialogs import ok
            ok.load('Bookmarks Error', '[B]Error removing podcast show.[/B]')
            failure = traceback.format_exc()
            log_utils.log('Remove Podcast Bookmark - Exception: \n' + str(failure))
            return

    def show_podcasts(self):
        items = []
        for action in self.bookmarks['Podcasts'].keys():
            for entry in self.bookmarks['Podcasts'][action].keys():
                try:
                    show = self.bookmarks['Podcasts'][action][entry]
                    item = control.item(label=show['name'])
                    item.setProperty("IsPlayable", "false")
                    item.setArt({"thumb": show['icon'], "icon": show['icon']})
                    url = '%s?action=%s&podcastshow=%s' % (sys.argv[0], show['action'], show['url'])

                    cm = self.build_cm('Podcasts', name=show['name'], id=show['id'], action=show['action'], icon=show['icon'], url=show['url'])
                    item.addContextMenuItems(cm)

                    try:
                        item.setContentLookup(False)
                    except AttributeError:
                        pass
                    items.append((url, item, True))
                except Exception:
                    from resources.lib.dialogs import ok
                    ok.load('Bookmarks Error', '[B]Error loading bookmarks.[/B]')
                    failure = traceback.format_exc()
                    log_utils.log('Show Podcast Bookmarks - Exception: \n' + str(failure))
                    return
        control.addItems(int(sys.argv[1]), items)
        self.endDirectory('files', xbmcplugin.SORT_METHOD_LABEL)

    def add_radio(self, dbase):
        temp = dbase.decode('base64').split('|')
        name = temp[0]
        station_id = temp[1]
        action = temp[2]
        icon = temp[3]
        url = temp[4]
        try:
            if action in self.bookmarks['Radio']:
                if station_id not in self.bookmarks['Radio'][action]:
                    self.bookmarks['Radio'][action][station_id] = {'name': name, 'id': station_id, 'action': action, 'icon': icon, 'url': url}
                    self.save()
                    control.refresh()
            else:
                self.bookmarks['Radio'][action] = {}
                self.bookmarks['Radio'][action][station_id] = {}
                self.bookmarks['Radio'][action][station_id] = {'name': name, 'id': station_id, 'action': action, 'icon': icon, 'url': url}
                self.save()
                control.refresh()
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('Bookmarks - Add Radio Exception: \n' + str(failure))

    def rem_radio(self, dbase):
        temp = dbase.decode('base64').split('|')
        station_id = temp[1]
        action = temp[2]
        try:
            del self.bookmarks['Radio'][action][station_id]
            self.save()
            control.refresh()
        except Exception:
            from resources.lib.dialogs import ok
            ok.load('Bookmarks Error', '[B]Error removing radio station.[/B]')
            failure = traceback.format_exc()
            log_utils.log('Remove Radio Bookmark - Exception: \n' + str(failure))
            return

    def show_radio(self):
        items = []
        for action in self.bookmarks['Radio'].keys():
            for entry in self.bookmarks['Radio'][action].keys():
                try:
                    station = self.bookmarks['Radio'][action][entry]
                    item = control.item(label=station['name'])
                    item.setProperty("IsPlayable", "true")
                    item.setArt({"thumb": station['icon'], "icon": station['icon']})
                    url = '%s?action=%s&url=%s' % (sys.argv[0], station['action'], station['url'])

                    cm = self.build_cm('Radio', name=station['name'], id=station['id'], action=station['action'], icon=station['icon'], url=station['url'])
                    item.addContextMenuItems(cm)

                    try:
                        item.setContentLookup(False)
                    except AttributeError:
                        pass
                    items.append((url, item, False))
                except Exception:
                    from resources.lib.dialogs import ok
                    ok.load('Bookmarks Error', '[B]Error loading bookmarks.[/B]')
                    failure = traceback.format_exc()
                    log_utils.log('Show Radio Bookmarks - Exception: \n' + str(failure))
                    return
        control.addItems(int(sys.argv[1]), items)
        self.endDirectory('files', xbmcplugin.SORT_METHOD_LABEL)

    def save(self):
        with open(FILENAME, 'w') as json_file:
            json.dump(self.bookmarks, json_file, sort_keys=True, indent=4)
            json_file.close()

    def build_cm(self, bmtype, **kwargs):
        try:
            cm = []
            name = kwargs.get('name')
            action = kwargs.get('action')
            icon = kwargs.get('icon')
            url = kwargs.get('url')
            if bmtype == 'Channels':
                chan_id = kwargs.get('id')
                dbase = name + '|' + chan_id + '|' + action + '|' + icon + '|' + url
                if action in self.bookmarks[bmtype]:
                    if chan_id in self.bookmarks[bmtype][action]:
                        cm.append(('Remove Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'remove_channel', dbase.encode('base64'))))
                    else:
                        cm.append(('Add Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'add_channel', dbase.encode('base64'))))
                else:
                    cm.append(('Add Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'add_channel', dbase.encode('base64'))))
            elif bmtype == 'Podcasts':
                show_id = kwargs.get('id')
                dbase = name + '|' + show_id + '|' + action + '|' + icon + '|' + url
                if action in self.bookmarks[bmtype]:
                    if show_id in self.bookmarks[bmtype][action]:
                        cm.append(('Remove Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'remove_podcast', dbase.encode('base64'))))
                    else:
                        cm.append(('Add Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'add_podcast', dbase.encode('base64'))))
                else:
                    cm.append(('Add Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'add_podcast', dbase.encode('base64'))))
            elif bmtype == 'Radio':
                station_id = kwargs.get('id')
                dbase = name + '|' + station_id + '|' + action + '|' + icon + '|' + url
                if action in self.bookmarks[bmtype]:
                    if station_id in self.bookmarks[bmtype][action]:
                        cm.append(('Remove Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'remove_radio', dbase.encode('base64'))))
                    else:
                        cm.append(('Add Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'add_radio', dbase.encode('base64'))))
                else:
                    cm.append(('Add Bookmark', 'RunPlugin(%s?action=%s&url=%s)' % (sys.argv[0], 'add_radio', dbase.encode('base64'))))
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('Bookmarks - Context Exception: \n' + str(failure))

        return cm

    def endDirectory(self, contentType='addons', sortMethod=xbmcplugin.SORT_METHOD_NONE):
        control.content(int(sys.argv[1]), contentType)
        control.sortMethod(int(sys.argv[1]), sortMethod)
        control.directory(int(sys.argv[1]), cacheToDisc=True)