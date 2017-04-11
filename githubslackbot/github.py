import datetime

from github import Github


class GitHubIntegration:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.github_service = github_service

    def get_org_pull_requests_older_than_num_days(self, organization_name, num_days):
        client = self._get_client()
        organization = client.get_organization(organization_name)
        repos = organization.get_repos()
        return self._get_older_pull_requests(repos, num_days)

    def _get_older_pull_requests(self, repos, num_days):
        old_pulls = []
        for repo in repos:
            pulls = repo.get_pulls()
            for pull in pulls:
                if pull.created_at < datetime.datetime.now() - datetime.timedelta(days=num_days):
                    old_pulls.append(pull.html_url)

        return old_pulls

    def _get_client(self):
        return Github(self.username, self.password)





