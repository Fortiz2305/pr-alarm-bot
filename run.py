from config import (
    GITHUB_USERNAME,
    GITHUB_PASSWORD,
    GITHUB_ORGANIZATION,
    SLACK_CHANNEL,
    SLACK_TOKEN
)

from githubslackbot.github import GitHubIntegration
from githubslackbot.slack import SlackIntegration

if __name__ == '__main__':
    github_integration = GitHubIntegration(GITHUB_USERNAME, GITHUB_PASSWORD)
    pr = github_integration.get_org_pull_requests_older_than_num_days(GITHUB_ORGANIZATION, 3)

    slack_integration = SlackIntegration(SLACK_TOKEN)
    message = "Repos with PR older than 3 days\n" + '\n'.join(pr)
    print("sending {} to channel {}".format(message, SLACK_CHANNEL))
    slack_integration.send_message(SLACK_CHANNEL, message)
