from steam.base import json_request

class SteamUser(json_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getPlayerSummaries(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
        self._compose_url(base_url, params)
        self._download()
        return self._get(get_vals)

    def getPlayerAchievements(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/'
        self._compose_url(base_url, params)
        self._download()
        return self._get(get_vals)

    def getFriendList(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUser/GetFriendList/v0001/'
        self._compose_url(base_url, params)
        self._download()
        return self._get(get_vals)

class SteamApp(json_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getNewsForApp(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'
        self._compose_url(base_url, params)
        self._download()
        return self._get(get_vals)

    def getGlobalAchievementPercentagesForApp(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/'
        self._compose_url(base_url, params)
        self._download()
        return self._get(get_vals)

class DotaUser(json_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getMatchHistory(self, params, get_vals = None):
        base_url = 'api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/'
        self._compose_url(base_url, params)
        self._download()
        return self._get(get_vals)

    def getMatch(self, params, get_vals = None):
        base_url = 'api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001'
        self._compose_url(base_url, params)
        self._download()
        return self._get(get_vals)



