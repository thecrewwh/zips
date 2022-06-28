'''
    Copyright (C) 2013 Sean Poyser (seanpoyser@gmail.com)

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


def get():

        import xbmc,xbmcgui,xbmcaddon,xbmcvfs,os
        addonInfo = xbmcaddon.Addon().getAddonInfo
        addonPath = xbmc.translatePath(addonInfo('path'))
        changelogfile = os.path.join(addonPath, 'changelog.txt')
        r = open(changelogfile)
        text = r.read()

        id = 10147
        xbmc.executebuiltin('ActivateWindow(%d)' % id)
        xbmc.sleep(500)
        win = xbmcgui.Window(id)
        retry = 50
        while (retry > 0):
            try:
                xbmc.sleep(10)
                retry -= 1
                win.getControl(1).setLabel('THE CREW PROJECT TEST VERSION: %s' %(xbmcaddon.Addon().getAddonInfo('version')))
                win.getControl(5).setText(text)
                return
            except:
                pass
