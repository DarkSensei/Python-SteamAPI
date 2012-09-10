import json
try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

class api_request(object):

    def __init__(self, api_key = None):
        self.api_key = api_key

    def _if_key_assigned(self):
        if self.api_key:
            return True
        return False

    def _compose_url(self, base_url, params, use_ssl = True):
        """Composes a url used to download data"""
        api_key = '?key=' + str(self.api_key)
        url_list = [base_url, api_key]
        if not base_url[-1] == '/':
            base_url += '/'
        if not base_url[:8] == 'https://' or base_url[:7] == 'http://':
            temp_list = []
            if use_ssl:
                temp_list.append('https://')
            else:
                temp_list.append('http://')
            url_list = temp_list + url_list
        for k, v in params.items():
            url_list.append('&' + str(k) + '=' + str(v))
        self.url = ''.join(url_list)
        return self.url

    def _download_json(self, url = None):
        """Downloads json data of the passed url, or uses self.url"""
        if not url:
            url = self.url
        contents = urlopen(url).read()
        self.results = json.loads(contents.decode('utf-8'))
        return self.results

    def _get(self, values = None):
        """Gets passed values in results, if any. Otherwise returns the whole json object"""
        if not values:
            return self.results
        return_vals = []
        for value in values:
            vals = None
            for arg in value:
                if not vals:
                    vals = self.results[arg]
                else:
                    vals = vals[arg]
            return_vals.append(vals)
        return return_vals

    def json_request(self, base_url, params, get_vals = None):
        self._compose_url(base_url, params)
        self._download_json()
        return self._get(get_vals)

    def _get_replay_location(self, cluster, match_id, replay_salt):
        replay_url = "http://replay" + cluster + ".valve.net/570/" + match_id + "_" + replay_salt + ".dem.bz2"


