# -*- coding: utf-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
#  As long as you retain this notice you can do whatever you want with this
# stuff. Just please ask before copying. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Atreides
# Addon id: plugin.video.atreides
# Addon Provider: House Atreides

import time
import traceback

from resources.lib.modules import client, control, log_utils


class webform(object):
    def __init__(self, key=''):
        self.bugs_url = 'aHR0cHM6Ly90ZWFtLWNyZXcuMDAwd2ViaG9zdGFwcC5jb20vYnVncy9idWdfcmVwb3J0LnBocA=='.decode('base64')
        self.bugs_get_url = 'aHR0cHM6Ly90ZWFtLWNyZXcuMDAwd2ViaG9zdGFwcC5jb20vYnVncy9idWdfcmVwb3J0X3B1bGwucGhw'.decode('base64')
        #self.features_url = 'http://request.php'.decode('base64')
        self.user_agent = {'User-Agent': 'Paul/1.0 (Whatever; U; Want; en-GB; rv:1.0.0.0) MoonRat/2008092417 Atreides/1.0.0'}

    def bug_report(self, addonFor, bugReport):
        try:
            expires_at = control.setting('BR_EXPIRES_AT')
            if expires_at == '':
                expires_at = 1
            else:
                expires_at = int(float(expires_at))
            if time.time() < expires_at:
                return None

            # Payload is the variables for the form, dipshit
            payload = {'bug_report': bugReport, 'submit': 'Submit'}

            req = client.request(self.bugs_url, post=payload, headers=self.user_agent)
            expires_at = time.time() + 60
            control.setSetting('BR_EXPIRES_AT', str(expires_at))
            if req is None:
                return False
            return True
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('Webform - Exception: \n' + str(failure))
            return False


    def get_bugs(self):
        try:
            expires_at = control.setting('BR_EXPIRES_AT')
            if expires_at == '':
                expires_at = 1
            else:
                expires_at = int(float(expires_at))
            if time.time() < expires_at:
                return None

            req = client.request(self.bugs_get_url, headers=self.user_agent)
            expires_at = time.time() + 10
            control.setSetting('BR_EXPIRES_AT', str(expires_at))
            if req is None:
                return False
            return req
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('Webform - Exception: \n' + str(failure))
            return False

    def feature_request(self):
        # Payload is the variables for the form, dipshit
        payload = {'you_suck': 'this_sucks'}
        # Not yet implemented, and payload form is not yet made
