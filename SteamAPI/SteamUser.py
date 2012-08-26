from SteamAPI.base import json_request

class SteamUser(json_request):

    def __init__(self, api_key):
        super().__init__(api_key)

    def getPlayerSummaries(self, steamids):
        base_url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
        steamids = ','.join(steamids)
        steamids = {'steamdids':steamids}
        self._compose_url(base_url, steamids)
        results = self._download()
