# pr-alarm-bot
Slack bot which sends notifications with organization's PR older than a number of days

## Requirements

* Install python 3.X: [here](https://www.python.org/downloads/)

* Install pralarm:

   ```
   pip3 install pralarm==0.1
   ```

* Create a Slack token: [https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens)


## How to use

You have to add the following environment variables with your GitHub and Slack credentials:

* GITHUB_USERNAME
* GITHUB_PASSWORD
* GITHUB_ORGANIZATION
* SLACK_CHANNEL
* SLACK_TOKEN

NOTE: If you have set [Two Factor Authentication](https://github.com/blog/1614-two-factor-authentication) in GitHub, you have to access to the api through an authentication token instead of using username & password. This is possible following the steps below:

    * Create a personal token: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/

    * Set the environment variable `GITHUB_OAUTH_TOKEN` to the token value.

It is algo possible to add these variables in the `config.py` file.

Then, it is only necessary to add a file, for instance `run.py` with the following information:

```python
from pralarm.github import GitHubIntegration
from pralarm.slack import SlackIntegration

github_client = GitHubIntegration(GITHUB_USERNAME, GITHUB_PASSWORD)
slack_client = SlackIntegration(SLACK_TOKEN)

older_pr = github_client.get_org_pull_requests_older_than_num_days(GITHUB_ORGANIZATION, num_days)

slack_client.send_message(SLACK_CHANNEL, your_message)
```

With two factor authentication:

```python
github_client = GitHubIntegration(GITHUB_OAUTH_TOKEN)
```

## Run the program

Open the command line and execute:

```
python3 run.py
```

This will send your message to your slack channel.
