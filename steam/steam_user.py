from steam.base import json_request

class SteamUser(json_request):

    def getPlayerSummaries(self, steamids, get_values = None):
        base_url = 'api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
        steamids = ','.join(steamids)
        kwargs = {'steamids':steamids}
        self._compose_url(base_url, **kwargs)
        self._download()
        return self._get(get_values)

    def getPlayerAchievements(self, steamid, appid, lang, get_values = None):
        base_url = 'api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/'
        kwargs = {'appid':appid, 'steamid':steamid, 'l':lang}
        self._compose_url(base_url, **kwargs)
        self._download()
        return self._get(get_values)

    def getFriendList(self, steamid, rel = 'friend', get_values = None):
        base_url = 'api.steampowered.com/ISteamUser/GetFriendList/v0001/'
        kwargs = {'steamid':steamid, 'relationship':rel}
        self._compose_url(base_url, **kwargs)
        self._download()
        return self._get(get_values)



