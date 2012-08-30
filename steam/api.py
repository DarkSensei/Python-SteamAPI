from steam.base import json_request

class SteamUser(json_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getPlayerSummaries(self, steamids, get_values = None):
        base_url = 'api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
        if type(steamids).__name__ == 'list' or type(steamids).__name__ == 'tuple':
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

class SteamApp(json_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getNewsForApp(self, appid, count, maxlength, get_values = None):
        base_url = 'api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'
        kwargs = {'appid':appid, 'count':count, 'maxlength':maxlength}
        self._compose_url(base_url, **kwargs)
        self._download()
        return self._get(get_values)

    def getGlobalAchievementPercentagesForApp(self, appid, get_values = None):
        base_url = 'api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/'
        kwargs = {'gameid':appid}
        self._compose_url(base_url, **kwargs)
        self._download()
        return self._get(get_values)


