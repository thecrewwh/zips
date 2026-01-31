# -*- coding: utf-8 -*-
'''
***********************************************************
*
* @file addon.py
* @package script.module.thecrew
*
* Created on 2024-03-08.
* Copyright 2024 by The Crew. All rights reserved.
*
* @license GNU General Public License, version 3 (GPL-3.0)
*
********************************************************cm*
'''

import re
import os
import sys
import json
import html
import base64

from urllib.parse import urlencode, unquote, parse_qsl, quote_plus, urlparse, urljoin
from datetime import datetime, timezone

import requests
import xbmc
import xbmcvfs
import xbmcgui
import xbmcplugin
import xbmcaddon


addon_url = sys.argv[0]
addon_handle = int(sys.argv[1])
params = dict(parse_qsl(sys.argv[2][1:]))
addon = xbmcaddon.Addon(id='plugin.video.daddylive')
mode = addon.getSetting('mode')

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
FANART = addon.getAddonInfo('fanart')
ICON = addon.getAddonInfo('icon')

SEED_BASEURL = 'https://daddylive.sx/'

def log(msg):
    logpath = xbmcvfs.translatePath('special://logpath/')
    filename = 'daddylive.log'
    log_file = os.path.join(logpath, filename)
    try:
        if isinstance(msg, str):
            _msg = f'\n    {msg}'
        else:
            _msg = f'\n    {repr(msg)}'
        if not os.path.exists(log_file):
            with open(log_file, 'w', encoding='utf-8'):
                pass
        with open(log_file, 'a', encoding='utf-8') as f:
            line = ('[{} {}]: {}').format(datetime.now().date(), str(datetime.now().time())[:8], _msg)
            f.write(line.rstrip('\r\n') + '\n')
    except (TypeError, Exception) as e:
        try:
            xbmc.log(f'[ Daddylive ] Logging Failure: {e}', 2)
        except:
            pass

def normalize_origin(url):
    try:
        u = urlparse(url)
        return f'{u.scheme}://{u.netloc}/'
    except:
        return SEED_BASEURL

def resolve_active_baseurl(seed):
    try:
        s = requests.Session()
        headers = {'User-Agent': UA}
        resp = s.get(seed, headers=headers, timeout=10, allow_redirects=True)
        final = normalize_origin(resp.url if resp.url else seed)
        return final
    except Exception as e:
        log(f'Active base resolve failed, using seed. Error: {e}')
        return normalize_origin(seed)

def get_active_base():
    base = addon.getSetting('active_baseurl')
    if not base:
        base = resolve_active_baseurl(SEED_BASEURL)
        addon.setSetting('active_baseurl', base)
    if not base.endswith('/'):
        base += '/'
    return base

def set_active_base(new_base: str):
    if not new_base.endswith('/'):
        new_base += '/'
    addon.setSetting('active_baseurl', new_base)

def abs_url(path: str) -> str:
    return urljoin(get_active_base(), path.lstrip('/'))

def _sched_headers():
    base = get_active_base()
    return {'User-Agent': UA, 'Referer': base, 'Origin': base}

def get_local_time(utc_time_str):
    try:
        utc_now = datetime.utcnow()
        event_time_utc = datetime.strptime(utc_time_str, '%H:%M')
        event_time_utc = event_time_utc.replace(year=utc_now.year, month=utc_now.month, day=utc_now.day)
        event_time_utc = event_time_utc.replace(tzinfo=timezone.utc)
        local_time = event_time_utc.astimezone()
        time_format_pref = addon.getSetting('time_format')
        if time_format_pref == '1':
            local_time_str = local_time.strftime('%H:%M')
        else:
            local_time_str = local_time.strftime('%I:%M %p').lstrip('0')
        return local_time_str
    except Exception as e:
        log(f"Failed to convert time: {e}")
        return utc_time_str

def build_url(query):
    return addon_url + '?' + urlencode(query)

def addDir(title, dir_url, is_folder=True):
    li = xbmcgui.ListItem(title)
    clean_plot = re.sub(r'<[^>]+>', '', title)
    labels = {'title': title, 'plot': clean_plot, 'mediatype': 'video'}
    kodiversion = getKodiversion()
    if kodiversion < 20:
        li.setInfo("video", labels)
    else:
        infotag = li.getVideoInfoTag()
        infotag.setMediaType(labels.get("mediatype", "video"))
        infotag.setTitle(labels.get("title", "Daddylive"))
        infotag.setPlot(labels.get("plot", labels.get("title", "Daddylive")))
    li.setArt({'thumb': '', 'poster': '', 'banner': '', 'icon': ICON, 'fanart': FANART})
    li.setProperty("IsPlayable", 'false' if is_folder else 'true')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=dir_url, listitem=li, isFolder=is_folder)

def closeDir():
    xbmcplugin.endOfDirectory(addon_handle)

def getKodiversion():
    try:
        return int(xbmc.getInfoLabel("System.BuildVersion")[:2])
    except:
        return 18

def Main_Menu():
    menu = [
        ['[B][COLOR gold]LIVE SPORTS SCHEDULE[/COLOR][/B]', 'sched'],
        ['[B][COLOR gold]LIVE TV CHANNELS[/COLOR][/B]', 'live_tv'],
        ['[B][COLOR gold]SEARCH EVENTS SCHEDULE[/COLOR][/B]', 'search'],
        ['[B][COLOR gold]SEARCH LIVE TV CHANNELS[/COLOR][/B]', 'search_channels'],
        ['[B][COLOR gold]REFRESH CATEGORIES[/COLOR][/B]', 'refresh_sched'],
        ['[B][COLOR gold]SET ACTIVE DOMAIN (AUTO)[/COLOR][/B]', 'resolve_base_now'],
    ]
    for m in menu:
        addDir(m[0], build_url({'mode': 'menu', 'serv_type': m[1]}))
    closeDir()

def getCategTrans():
    schedule_url = abs_url('index.php')
    try:
        headers = {'User-Agent': UA, 'Referer': get_active_base()}
        html_text = requests.get(schedule_url, headers=headers, timeout=10).text

        m = re.search(r'<div[^>]+class="filters"[^>]*>(.*?)</div>', html_text, re.IGNORECASE | re.DOTALL)
        if not m:
            log("getCategTrans(): filters block not found")
            return []

        block = m.group(1)
        anchors = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.IGNORECASE | re.DOTALL)
        if not anchors:
            log("getCategTrans(): no <a> items in filters block")
            return []

        categs = []
        seen = set()

        for href, text_content in anchors:
            name = html.unescape(re.sub(r'\s+', ' ', text_content)).strip()
            if not name or name.lower() == 'all':
                continue
            if name in seen:
                continue
            seen.add(name)
            categs.append((name, '[]'))

        return categs

    except Exception as e:
        xbmcgui.Dialog().ok("Error", f"Error fetching category data: {e}")
        log(f'index parse fail: url={schedule_url} err={e}')
        return []

def Menu_Trans():
    categs = getCategTrans()
    if not categs:
        return
    for categ_name, _events_list in categs:
        addDir(categ_name, build_url({'mode': 'showChannels', 'trType': categ_name}))
    closeDir()

def ShowChannels(categ, channels_list):
    for item in channels_list:
        title = item.get('title')
        addDir(title, build_url({'mode': 'trList', 'trType': categ, 'channels': json.dumps(item.get('channels'))}), True)
    closeDir()

def getTransData(categ):
    try:
        url = abs_url('index.php?cat=' + quote_plus(categ))
        headers = {'User-Agent': UA, 'Referer': get_active_base()}
        html_text = requests.get(url, headers=headers, timeout=10).text

        cut = re.search(r'<h2\s+class="collapsible-header\b', html_text, re.IGNORECASE)
        if cut:
            html_text = html_text[:cut.start()]

        events = re.findall(
            r'<div\s+class="schedule__event">.*?'
            r'<div\s+class="schedule__eventHeader"[^>]*?>\s*'
            r'(?:<[^>]+>)*?'
            r'<span\s+class="schedule__time"[^>]*data-time="([^"]+)"[^>]*>.*?</span>\s*'
            r'<span\s+class="schedule__eventTitle">\s*([^<]+)\s*</span>.*?'
            r'</div>\s*'
            r'<div\s+class="schedule__channels">(.*?)</div>',
            html_text, re.IGNORECASE | re.DOTALL
        )

        trns = []
        for time_str, event_title, channels_block in events:
            event_time_local = get_local_time(time_str.strip())
            title = f'[COLOR gold]{event_time_local}[/COLOR] {html.unescape(event_title.strip())}'

            chans = []
            for href, title_attr, link_text in re.findall(
                r'<a[^>]+href="([^"]+)"[^>]*title="([^"]*)"[^>]*>(.*?)</a>',
                channels_block, re.IGNORECASE | re.DOTALL
            ):
                try:
                    u = urlparse(href)
                    qs = dict(parse_qsl(u.query))
                    cid = qs.get('id') or ''
                except Exception:
                    cid = ''
                name = html.unescape((title_attr or link_text).strip())
                if cid:
                    chans.append({'channel_name': name, 'channel_id': cid})

            if chans:
                trns.append({'title': title, 'channels': chans})

        return trns

    except Exception as e:
        log(f'getTransData error for categ={categ}: {e}')
        return []

def TransList(categ, channels):
    for channel in channels:
        channel_title = html.unescape(channel.get('channel_name'))
        channel_id = str(channel.get('channel_id', '')).strip()
        if not channel_id:
            continue
        addDir(channel_title, build_url({'mode': 'trLinks', 'trData': json.dumps({'channels': [{'channel_name': channel_title, 'channel_id': channel_id}]})}), False)
    closeDir()

def getSource(trData):
    try:
        data = json.loads(unquote(trData))
        channels_data = data.get('channels')
        if channels_data and isinstance(channels_data, list):
            cid = str(channels_data[0].get('channel_id', '')).strip()
            if not cid:
                return
            if '%7C' in cid or '|' in cid:
                url_stream = abs_url('watchs2watch.php?id=' + cid)
            else:
                url_stream = abs_url('watch.php?id=' + cid)
            xbmcplugin.setContent(addon_handle, 'videos')
            PlayStream(url_stream)
    except Exception as e:
        log(f'getSource failed: {e}')

def list_gen():
    chData = channels()
    for c in chData:
        addDir(c[1], build_url({'mode': 'play', 'url': abs_url(c[0])}), False)
    closeDir()

def channels():
    url = abs_url('24-7-channels.php')
    allow_adult = xbmcaddon.Addon().getSetting('adult_pw') == 'lol'
    headers = {'Referer': get_active_base(), 'User-Agent': UA}

    try:
        resp = requests.post(url, headers=headers, timeout=10).text
    except Exception as e:
        log(f"[DADDYLIVE] channels(): request failed: {e}")
        return []

    card_rx = re.compile(
        r'<a\s+class="card"[^>]*?href="(?P<href>[^"]+)"[^>]*?data-title="(?P<data_title>[^"]*)"[^>]*>'
        r'.*?<div\s+class="card__title">\s*(?P<title>.*?)\s*</div>'
        r'.*?ID:\s*(?P<id>\d+)\s*</div>'
        r'.*?</a>',
        re.IGNORECASE | re.DOTALL
    )

    items = []
    for m in card_rx.finditer(resp):
        href_rel = m.group('href').strip()
        title_dom = html.unescape(m.group('title').strip())
        title_attr = html.unescape(m.group('data_title').strip())
        name = title_dom or title_attr

        is_adult = ('18+' in name) or ('18+' in title_attr) or name.lower().startswith('18+')
        if is_adult and not allow_adult:
            continue

        name = re.sub(r'^\s*\d+(?=[A-Za-z])', '', name).strip()

        items.append([href_rel, name])

    if not items:
        log("[DADDYLIVE] channels(): Site may have changed.")

    return items

def PlayStream(link):
    try:
        base = get_active_base()
        session = requests.Session()

        def _origin(u):
            try:
                p = urlparse(u)
                return f'{p.scheme}://{p.netloc}'
            except:
                return ''

        def _fetch(u, ref=None, note=''):
            headers = {
                'User-Agent': UA,
                'Referer': base,
                'Origin': _origin(base),
            }
            if ref:
                headers['Referer'] = ref
                headers['Origin'] = _origin(ref)
            log(f'[PlayStream] GET {u}  (ref={headers.get("Referer")}) {note}')
            r = session.get(u, headers=headers, timeout=10)
            r.raise_for_status()
            return r.text, r.url

        html1, url1 = _fetch(link, ref=base, note='entry')

        m = re.search(r'data-url="([^"]+)"\s+title="PLAYER 2"', html1, re.I)
        if m:
            url2 = urljoin(url1, m.group(1).replace('//cast', '/cast'))
        else:
            m = re.search(r'iframe\s+src="([^"]+)"', html1, re.I)
            if not m:
                log('[PlayStream] No iframe found after entry page.')
                return
            url2 = urljoin(url1, m.group(1))

        html2, url2_final = _fetch(url2, ref=url1, note='player2/outer iframe')
        m_if = re.search(r'iframe\s+src="([^"]+)"', html2, re.I)
        if m_if:
            url3 = urljoin(url2_final, m_if.group(1))
            html3, url3_final = _fetch(url3, ref=url2_final, note='inner iframe')
            page = html3
            page_url = url3_final
        else:
            page = html2
            page_url = url2_final

        ck_rx = re.compile(
            r'const\s+(?:CHANNEL_KEY|CHANNEL_ID|CH(?:ANNEL)?_?KEY?)\s*=\s*["\']([^"\']+)["\']',
            re.I
        )
        m_ck = ck_rx.search(page)
        if not m_ck:
            log('[PlayStream] CHANNEL_KEY not found.')
            return
        channel_key = m_ck.group(1).strip()
        log(f'[PlayStream] CHANNEL_KEY = {channel_key}')

        auth_token = ''
        auth_country = ''
        auth_ts = ''
        base_domain = 'giokko.ru'

        try:
            m_tok = re.search(r'const\s+AUTH_TOKEN\s*=\s*"([^"]+)"', page)
            if m_tok:
                auth_token = m_tok.group(1).strip()
                log(f'[PlayStream] AUTH_TOKEN found (len={len(auth_token)})')

            m_cty = re.search(r'const\s+AUTH_COUNTRY\s*=\s*"([^"]+)"', page)
            if m_cty:
                auth_country = m_cty.group(1).strip()
                log(f'[PlayStream] AUTH_COUNTRY = {auth_country}')

            m_ts = re.search(r'const\s+AUTH_TS\s*=\s*"([^"]+)"', page)
            if m_ts:
                auth_ts = m_ts.group(1).strip()
                log(f'[PlayStream] AUTH_TS = {auth_ts}')

            m_hb = re.search(r"https://([^/]+)/heartbeat", page)
            if m_hb:
                heartbeat_host = m_hb.group(1).strip()
                m_dom = re.search(r"\.([A-Za-z0-9-]+\.[A-Za-z]{2,})$", heartbeat_host)
                if m_dom:
                    base_domain = m_dom.group(1).lower()
                log(f'[PlayStream] heartbeat host: {heartbeat_host}, base_domain: {base_domain}')
            else:
                log('[PlayStream] heartbeat URL not found; using legacy base_domain.')
        except Exception as e:
            log(f'[PlayStream] AUTH/heartbeat parse error: {e}')

        client_token = ''
        try:
            if auth_country and auth_ts:
                try:
                    lang = xbmc.getLanguage(xbmc.ISO_639_1) or 'en'
                except Exception:
                    lang = 'en'

                screen = '1920x1080'
                tz = 'UTC'

                fingerprint = f'{UA}|{screen}|{tz}|{lang}'
                sign_data = f'{channel_key}|{auth_country}|{auth_ts}|{UA}|{fingerprint}'
                client_token = base64.b64encode(sign_data.encode('utf-8')).decode('ascii')
                log(f'[PlayStream] CLIENT_TOKEN generated (len={len(client_token)})')
            else:
                log('[PlayStream] Missing AUTH_COUNTRY/AUTH_TS, skipping CLIENT_TOKEN.')
        except Exception as e:
            log(f'[PlayStream] CLIENT_TOKEN generation error: {e}')
            client_token = ''

        if auth_token:
            try:
                if 'heartbeat_host' in locals():
                    heartbeat_url = f'https://{heartbeat_host}/heartbeat'
                    hb_headers = {
                        'User-Agent': UA,
                        'Authorization': f'Bearer {auth_token}',
                        'X-Channel-Key': channel_key,
                        'Referer': page_url,
                        'Origin': _origin(page_url)
                    }
                    if client_token:
                        hb_headers['X-Client-Token'] = client_token
                    hb_headers['X-User-Agent'] = UA

                    session.get(heartbeat_url, headers=hb_headers, timeout=10)
                    log(f'[PlayStream] Heartbeat called: {heartbeat_url}')
            except Exception as e:
                log(f'[PlayStream] Heartbeat call failed: {e}')

        try:
            if 'giokko.ru' in page:
                try:
                    cookie_headers = {
                        'User-Agent': UA,
                        'Referer': page_url,
                        'Origin': _origin(page_url)
                    }
                    session.get('https://security.giokko.ru/cookie.php', headers=cookie_headers, timeout=10)
                    session.cookies.set('access', 'true', domain='giokko.ru')
                    session.cookies.set('access', 'true', domain='security.giokko.ru')
                    log('[PlayStream] cookie.php called and access cookie set in session (legacy giokko).')
                except Exception as e:
                    log(f'[PlayStream] cookie.php / cookie set failed: {e}')

            bundle_rx = re.compile(r'const\s+(?:BUNDLE|IJXX|XKZK)\s*=\s*["\']([^"\']+)["\']', re.I)
            m_b = bundle_rx.search(page)
            if m_b:
                log('[PlayStream] BUNDLE found, using legacy auth flow.')

                try:
                    bundle_raw = base64.b64decode(m_b.group(1)).decode('utf-8', 'ignore')
                    parts = json.loads(bundle_raw)
                    for k, v in list(parts.items()):
                        try:
                            parts[k] = base64.b64decode(v).decode('utf-8', 'ignore')
                        except:
                            pass
                except Exception as e:
                    log(f'[PlayStream] Failed to decode BUNDLE: {e}')
                    parts = {}

                b_host   = (parts.get('b_host') or '').strip()
                b_script = (parts.get('b_script') or '').strip()
                b_ts     = (parts.get('b_ts') or '').strip()
                b_rnd    = (parts.get('b_rnd') or '').strip()
                b_sig    = (parts.get('b_sig') or '').strip()

                if b_script and re.search(r'(?i)\ba\.php$', b_script):
                    b_script = re.sub(r'(?i)\ba\.php$', 'auth.php', b_script)

                if b_host and b_script and b_ts and b_rnd and b_sig:
                    auth_base = urljoin(b_host if b_host.startswith('http') else _origin(page_url), b_script)
                    auth_url = (
                        f'{auth_base}?channel_id={quote_plus(channel_key)}'
                        f'&ts={quote_plus(b_ts)}&rnd={quote_plus(b_rnd)}&sig={quote_plus(b_sig)}'
                    )
                    try:
                        session.get(
                            auth_url,
                            headers={'User-Agent': UA, 'Referer': page_url, 'Origin': _origin(page_url)},
                            timeout=10
                        )
                        log(f'[PlayStream] Legacy auth called: {auth_url}')
                    except Exception as e:
                        log(f'[PlayStream] Legacy auth failed: {e}')
            else:
                log('[PlayStream] BUNDLE not found, trying AUTH2.')
        except Exception as e:
            log(f'[PlayStream] BUNDLE block error: {e}')

        try:
            fields = dict(
                re.findall(
                    r"formData\.append\('([^']+)'\s*,\s*(var_[A-Za-z0-9]+)\)",
                    page
                )
            )
            values = dict(
                re.findall(
                    r"const\s+(var_[A-Za-z0-9]+)\s*=\s*\"([^\"]+)\"",
                    page
                )
            )
            final = {field: values.get(varname, '') for field, varname in fields.items()}

            if final:
                auth2_url = 'https://security.giokko.ru/auth2.php'
                log(f'[PlayStream] AUTH2 URL = {auth2_url}')
                log(f'[PlayStream] AUTH2 payload keys = {list(final.keys())}')

                files = {k: (None, v) for k, v in final.items()}

                auth_headers = {
                    'User-Agent': UA,
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Origin': _origin(page_url),
                    'Referer': page_url,
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                }

                auth_headers['Cookie'] = 'access=true'

                r_auth = session.post(
                    auth2_url,
                    headers=auth_headers,
                    files=files,
                    timeout=10
                )
                log(f'[PlayStream] auth2.php status={r_auth.status_code}')
                log(f'[PlayStream] auth2.php body={r_auth.text[:150]}')

                if r_auth.status_code != 200:
                    log('[PlayStream] auth2.php did not return 200; stream may be blocked.')
            else:
                log('[PlayStream] AUTH2: no formData/var_* pattern found.')
        except Exception as e:
            log(f'[PlayStream] AUTH2 error: {e}')

        host_raw = _origin(page_url)

        server_lookup_url = None
        try:
            m_srv = re.search(r"fetchWithRetry\('([^']*server_lookup[^']*)", page)
            if m_srv:
                base_srv = m_srv.group(1)
                if not base_srv.startswith('http'):
                    base_srv = urljoin(host_raw + '/', base_srv)

                if 'channel_id=' in base_srv:
                    if base_srv.endswith('='):
                        server_lookup_url = base_srv + quote_plus(channel_key)
                    else:
                        server_lookup_url = base_srv
                else:
                    sep = '&' if '?' in base_srv else '?'
                    server_lookup_url = f'{base_srv}{sep}channel_id={quote_plus(channel_key)}'
        except Exception as e:
            log(f'[PlayStream] server_lookup parse error: {e}')

        if not server_lookup_url:
            server_lookup_url = f'{host_raw}/server_lookup.js?channel_id={quote_plus(channel_key)}'

        log(f'[PlayStream] Server lookup: {server_lookup_url}')

        lookup_headers = {
            'User-Agent': UA,
            'Referer': page_url,
            'Origin': host_raw
        }
        if auth_token:
            lookup_headers['Authorization'] = f'Bearer {auth_token}'
            lookup_headers['X-Channel-Key'] = channel_key
        if client_token:
            lookup_headers['X-Client-Token'] = client_token
        lookup_headers['X-User-Agent'] = UA

        lookup_resp = session.get(server_lookup_url, headers=lookup_headers, timeout=10)
        lookup_resp.raise_for_status()

        try:
            data = lookup_resp.json()
        except Exception as e:
            log(f'[PlayStream] server_lookup JSON decode failed: {e}  body={lookup_resp.text[:200]}')
            return

        server_key = (data.get('server_key') or '').strip()
        log(f'[PlayStream] server_key from lookup: {server_key}')
        if not server_key:
            return

        if server_key == 'top1/cdn':
            hls_url = f'https://top1.{base_domain}/top1/cdn/{channel_key}/mono.css'
        else:
            hls_url = f'https://{server_key}new.{base_domain}/{server_key}/{channel_key}/mono.css'

        cookie_val = 'access=true'
        if auth_token:
            cookie_val = f'access=true; eplayer_session={auth_token}'

        header_dict = {
            'Referer': f'{host_raw}/',
            'Origin': host_raw,
            'Connection': 'Keep-Alive',
            'User-Agent': UA,
            'Cookie': cookie_val,
        }
        if auth_token:
            header_dict['Authorization'] = f'Bearer {auth_token}'
            header_dict['X-Channel-Key'] = channel_key
        if client_token:
            header_dict['X-Client-Token'] = client_token
        header_dict['X-User-Agent'] = UA

        header_str = '&'.join(f'{k}={quote_plus(v)}' for k, v in header_dict.items())

        m3u8 = f'{hls_url}|{header_str}'
        log(f'[PlayStream] Final HLS = {m3u8}')

        liz = xbmcgui.ListItem('Daddylive', path=m3u8)
        liz.setProperty('inputstream', 'inputstream.ffmpegdirect')
        liz.setMimeType('application/x-mpegURL')
        liz.setProperty('inputstream.ffmpegdirect.is_realtime_stream', 'true')
        liz.setProperty('inputstream.ffmpegdirect.stream_mode', 'timeshift')
        liz.setProperty('inputstream.ffmpegdirect.manifest_type', 'hls')

        xbmcplugin.setResolvedUrl(addon_handle, True, liz)

    except Exception as e:
        import traceback
        log(f"[PlayStream] Exception: {e}\n{traceback.format_exc()}")

def Search_Events():
    keyboard = xbmcgui.Dialog().input("Enter search term", type=xbmcgui.INPUT_ALPHANUM)
    if not keyboard or keyboard.strip() == '':
        return
    term = keyboard.lower().strip()

    try:
        base = get_active_base()
        headers = {'User-Agent': UA, 'Referer': base}
        html_text = requests.get(abs_url('index.php'), headers=headers, timeout=10).text

        events = re.findall(
            r"<div\s+class=\"schedule__event\">.*?"
            r"<div\s+class=\"schedule__eventHeader\"[^>]*?>\s*"
            r"(?:<[^>]+>)*?"
            r"<span\s+class=\"schedule__time\"[^>]*data-time=\"([^\"]+)\"[^>]*>.*?</span>\s*"
            r"<span\s+class=\"schedule__eventTitle\">\s*([^<]+)\s*</span>.*?"
            r"</div>\s*"
            r"<div\s+class=\"schedule__channels\">(.*?)</div>",
            html_text, re.IGNORECASE | re.DOTALL
        )

        rows = {}
        seen = set()
        for time_str, raw_title, channels_block in events:
            title_clean = html.unescape(raw_title.strip())
            if term not in title_clean.lower():
                continue

            local_ts = get_local_time(time_str.strip())
            row_title = f"[COLOR gold]{local_ts}[/COLOR] {title_clean}"

            for href, title_attr, link_text in re.findall(
                r"<a[^>]+href=\"([^\"]+)\"[^>]*title=\"([^\"]*)\"[^>]*>(.*?)</a>",
                channels_block, re.IGNORECASE | re.DOTALL
            ):
                try:
                    u = urlparse(href)
                    qs = dict(parse_qsl(u.query))
                    cid = (qs.get('id') or '').strip()
                except Exception:
                    cid = ''
                if not cid:
                    continue

                sig = (title_clean.lower(), time_str.strip(), cid)
                if sig in seen:
                    continue
                seen.add(sig)

                ch_name = html.unescape((title_attr or link_text or '').strip()) or 'Channel'
                rows.setdefault(row_title, [])
                if all(cid != c['channel_id'] for c in rows[row_title]):
                    rows[row_title].append({'channel_name': ch_name, 'channel_id': cid})

        if not rows:
            xbmcgui.Dialog().ok("Search", "No matching events found.")
            return

        for row_title, chans in rows.items():
            addDir(row_title, build_url({'mode': 'trList', 'trType': 'search', 'channels': json.dumps(chans)}), True)
        closeDir()

    except Exception as e:
        log(f"Search_Events (fast) error: {e}")
        xbmcgui.Dialog().ok("Search", "Search failed. Check log.")

def Search_Channels():
    keyboard = xbmcgui.Dialog().input("Enter channel name", type=xbmcgui.INPUT_ALPHANUM)
    if not keyboard or keyboard.strip() == '':
        return
    term = keyboard.lower().strip()

    try:
        base = get_active_base()
        headers = {'User-Agent': UA, 'Referer': base}
        html_text = requests.get(abs_url('index.php'), headers=headers, timeout=10).text

        channel_blocks = re.findall(
            r"<div\s+class=\"schedule__event\">.*?"
            r"<div\s+class=\"schedule__eventHeader\"[^>]*?>.*?</div>\s*"
            r"<div\s+class=\"schedule__channels\">(.*?)</div>",
            html_text, re.IGNORECASE | re.DOTALL
        )

        results = []
        seen = set()
        for block in channel_blocks:
            for href, title_attr, link_text in re.findall(
                r"<a[^>]+href=\"([^\"]+)\"[^>]*title=\"([^\"]*)\"[^>]*>(.*?)</a>",
                block, re.IGNORECASE | re.DOTALL
            ):
                display = html.unescape((title_attr or link_text or '').strip())
                if term not in display.lower():
                    continue

                try:
                    u = urlparse(href)
                    qs = dict(parse_qsl(u.query))
                    cid = (qs.get('id') or '').strip()
                except Exception:
                    cid = ''
                if not cid:
                    continue

                sig = (display.lower(), cid)
                if sig in seen:
                    continue
                seen.add(sig)

                results.append({'title': display, 'channel_id': cid})

        if not results:
            xbmcgui.Dialog().ok("Search", "No matching channels found.")
            return

        for result in results:
            addDir(result['title'], build_url({
                'mode': 'trLinks',
                'trData': json.dumps({'channels': [{'channel_name': result["title"], 'channel_id': result["channel_id"]}]})
            }), False)
        closeDir()

    except Exception as e:
        log(f"Search_Channels (fast) error: {e}")
        xbmcgui.Dialog().ok("Search", "Search failed. Check log.")

def refresh_active_base():
    new_base = resolve_active_baseurl(SEED_BASEURL)
    set_active_base(new_base)
    xbmcgui.Dialog().ok("Daddylive", f"Active domain set to:\n{new_base}")
    xbmc.executebuiltin('Container.Refresh')

kodiversion = getKodiversion()
mode = params.get('mode', None)

if not mode:
    Main_Menu()
else:
    if mode == 'menu':
        servType = params.get('serv_type')
        if servType == 'sched':
            Menu_Trans()
        elif servType == 'live_tv':
            list_gen()
        elif servType == 'search':
            Search_Events()
        elif servType == 'search_channels':
            Search_Channels()
        elif servType == 'refresh_sched':
            xbmc.executebuiltin('Container.Refresh')

    elif mode == 'showChannels':
        transType = params.get('trType')
        channels = getTransData(transType)
        ShowChannels(transType, channels)

    elif mode == 'trList':
        transType = params.get('trType')
        channels = json.loads(params.get('channels'))
        TransList(transType, channels)

    elif mode == 'trLinks':
        trData = params.get('trData')
        getSource(trData)

    elif mode == 'play':
        link = params.get('url')
        PlayStream(link)

    elif mode == 'resolve_base_now':
        refresh_active_base()

