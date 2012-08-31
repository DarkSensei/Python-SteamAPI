from steam.base import api_request

class SteamUser(api_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getPlayerSummaries(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
        self.json_request(base_url, params, get_vals)

    def getPlayerAchievements(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/'
        self.json_request(base_url, params, get_vals)

    def getFriendList(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUser/GetFriendList/v0001/'
        self.json_request(base_url, params, get_vals)

class SteamApp(api_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getNewsForApp(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamNews/GetNewsForApp/v0002/'
        self.json_request(base_url, params, get_vals)

    def getGlobalAchievementPercentagesForApp(self, params, get_vals = None):
        base_url = 'api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/'
        self.json_request(base_url, params, get_vals)

class DotaUser(api_request):

    def __init__(self, api_key = None):
        super().__init__(api_key)

    def getMatchHistory(self, params, get_vals = None):
        base_url = 'api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/'
        self.json_request(base_url, params, get_vals)

    def getMatch(self, match_id, get_vals = None):
        base_url = 'api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/'
        params = {"match_id":match_id}
        self.json_request(base_url, params, get_vals)

    def _getReplayLocation(self, cluster, match_id, replay_salt):
        return self._get_replay_location(cluster, match_id, replay_salt)

    def getMatchReplayLocation(self, match_id):
        get_vals = (
            ()
        )
        self.getMatch(match_id)




