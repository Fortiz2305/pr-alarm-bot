from slackclient import SlackClient


class SlackIntegration:
    def __init__(self, slack_token):
        self.slack_token = slack_token

    def send_message(self, channel_id, message):
        client = self._get_client()
        self._auth(client)
        result = client.api_call(
            "chat.postMessage",
            channel_id=channel_id,
            text=message,
            username='github-slack-bot',
            icon_emoji=':robot_face:'
        )
        print(result)

    def _get_client(self):
        return SlackClient(self.slack_token)

    def _auth(self, client):
        auth1 = client.api_call("api.test")
        auth2 = client.api_call("auth.test")
        print(auth1)
        print(auth2)
