import requests


class GetHomePage:

    def GetHomePage(self):
        response = requests.get("https://zoho.com")
        return response.content
