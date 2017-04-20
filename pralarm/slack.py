from slackclient import SlackClient


class SlackIntegration:
    def __init__(self, slack_token):
        self.slack_token = slack_token

    def send_message(self, channel_name, message):
        client = self._get_client()
        self._auth(client)

        try:
            channel = self._get_channel_id(client, channel_name)
            result = client.api_call(
                "chat.postMessage",
                channel=channel,
                text=message,
                username='pr-alarm-bot',
                icon_emoji=':robot_face:'
            )
            if result.get('ok'):
                print("Success! Your message has been sent")
        except Exception as exception:
            print("Channel {} not found".format(str(exception)))

    def _get_client(self):
        return SlackClient(self.slack_token)

    def _auth(self, client):
        client.api_call("api.test")
        client.api_call("auth.test")

    def _get_channel_id(self, client, channel_name):
        channels_call = client.api_call("channels.list")
        if channels_call.get('ok'):
            channels = channels_call['channels']
            for channel in channels:
                if channel['name'] == channel_name:
                    return channel['id']
            raise Exception(channel_name)
        else:
            raise Exception(channels_call)
