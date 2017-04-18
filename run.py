from config import (
    GITHUB_USERNAME,
    GITHUB_PASSWORD,
    GITHUB_ORGANIZATION,
    SLACK_CHANNEL,
    SLACK_TOKEN
)

from pralarm.github import GitHubIntegration
from pralarm.slack import SlackIntegration

if __name__ == '__main__':
    github_integration = GitHubIntegration(GITHUB_USERNAME, GITHUB_PASSWORD)
    slack_integration = SlackIntegration(SLACK_TOKEN)

    older_pr = github_integration.get_org_pull_requests_older_than_num_days(GITHUB_ORGANIZATION, 3)
    if older_pr:
        message = "Badgers! These PR's are older than 3 days\n" + '\n'.join(older_pr)
    else:
        message = "Yeah! We don't have any PR older than 3 days"
    slack_integration.send_message(SLACK_CHANNEL, message)
