from steam.base import json_request

class SteamApp(json_request):

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
