import json
from urllib.request import urlopen

class json_request(object):

    def __init__(self, api_key):
        """Creates the object and sets the Steam API Key"""
        self.api_key = api_key

    def _compose_url(self, base_url, **kwargs):
        """Composes a url used to download data"""
        if not base_url[-1] == '/':
            base_url += '/'
        api_key = '?key=' + self.api_key
        url_list = [base_url, api_key]
        for k, v in kwargs:
            url_list.append(str('&' + k + '=' + v))
        self.url = ''.join(url_list)
        return self.url

    def _download(self, url = None):
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

