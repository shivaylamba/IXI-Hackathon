Type Markdown and LaTeX:  𝛼2 
Type Markdown and LaTeX: 𝛼2
import json
import requests
import numpy as np
import pandas as pd

import requests
from requests.auth import HTTPBasicAuth
import json
import requests
import numpy as np
import pandas as pd
​
import requests
from requests.auth import HTTPBasicAuth
Type Markdown and LaTeX: 𝛼2
​
credentials = json.loads(open('credentials.json').read())
authentication = HTTPBasicAuth(credentials['username'], credentials['password'])
Type Markdown and LaTeX: 𝛼2
data = requests.get('https://api.github.com/users/' + 'rahulgarg28071998',
                    auth = authentication)
data = data.json()
data
{'login': 'rahulgarg28071998',
 'id': 25707781,
 'node_id': 'MDQ6VXNlcjI1NzA3Nzgx',
 'avatar_url': 'https://avatars2.githubusercontent.com/u/25707781?v=4',
 'gravatar_id': '',
 'url': 'https://api.github.com/users/rahulgarg28071998',
 'html_url': 'https://github.com/rahulgarg28071998',
 'followers_url': 'https://api.github.com/users/rahulgarg28071998/followers',
 'following_url': 'https://api.github.com/users/rahulgarg28071998/following{/other_user}',
 'gists_url': 'https://api.github.com/users/rahulgarg28071998/gists{/gist_id}',
 'starred_url': 'https://api.github.com/users/rahulgarg28071998/starred{/owner}{/repo}',
 'subscriptions_url': 'https://api.github.com/users/rahulgarg28071998/subscriptions',
 'organizations_url': 'https://api.github.com/users/rahulgarg28071998/orgs',
 'repos_url': 'https://api.github.com/users/rahulgarg28071998/repos',
 'events_url': 'https://api.github.com/users/rahulgarg28071998/events{/privacy}',
 'received_events_url': 'https://api.github.com/users/rahulgarg28071998/received_events',
 'type': 'User',
 'site_admin': False,
 'name': None,
 'company': None,
 'blog': '',
 'location': None,
 'email': None,
 'hireable': None,
 'bio': None,
 'public_repos': 21,
 'public_gists': 0,
 'followers': 7,
 'following': 9,
 'created_at': '2017-02-11T15:10:14Z',
 'updated_at': '2019-12-01T11:44:36Z'}
From the json output above, I'll try to extract basic information such as name, location, email, bio, public_repos, and public gists. I'll also keep some of the urls handy inluding repos_url, gists_url and blog.

print("Information about user {}:\n".format('rahulgarg28071998'))
print("Name: {}".format(data['name']))
print("Email: {}".format(data['email']))
print("Location: {}".format(data['location']))
print("Public repos: {}".format(data['public_repos']))
print("Public gists: {}".format(data['public_gists']))
print("About: {}".format(data['bio']))
Information about user rahulgarg28071998:

Name: None
Email: None
Location: None
Public repos: 21
Public gists: 0
About: None
Type Markdown and LaTeX: 𝛼2
url = data['repos_url']
page_no = 1
repos_data = []
while (True):
    response = requests.get(url, auth = authentication)
    response = response.json()
    repos_data = repos_data + response
    repos_fetched = len(response)
    print("Total repositories fetched: {}".format(repos_fetched))
    if (repos_fetched == 30):
        page_no = page_no + 1
        url = data['repos_url'] + '?page=' + str(page_no)
    else:
        break
Total repositories fetched: 21
I'll first explore only one repository information and take a look at all the information I can keep.

repos_data[0]
{'id': 110245773,
 'node_id': 'MDEwOlJlcG9zaXRvcnkxMTAyNDU3NzM=',
 'name': 'ACM-MAIT-Website',
 'full_name': 'rahulgarg28071998/ACM-MAIT-Website',
 'private': False,
 'owner': {'login': 'rahulgarg28071998',
  'id': 25707781,
  'node_id': 'MDQ6VXNlcjI1NzA3Nzgx',
  'avatar_url': 'https://avatars2.githubusercontent.com/u/25707781?v=4',
  'gravatar_id': '',
  'url': 'https://api.github.com/users/rahulgarg28071998',
  'html_url': 'https://github.com/rahulgarg28071998',
  'followers_url': 'https://api.github.com/users/rahulgarg28071998/followers',
  'following_url': 'https://api.github.com/users/rahulgarg28071998/following{/other_user}',
  'gists_url': 'https://api.github.com/users/rahulgarg28071998/gists{/gist_id}',
  'starred_url': 'https://api.github.com/users/rahulgarg28071998/starred{/owner}{/repo}',
  'subscriptions_url': 'https://api.github.com/users/rahulgarg28071998/subscriptions',
  'organizations_url': 'https://api.github.com/users/rahulgarg28071998/orgs',
  'repos_url': 'https://api.github.com/users/rahulgarg28071998/repos',
  'events_url': 'https://api.github.com/users/rahulgarg28071998/events{/privacy}',
  'received_events_url': 'https://api.github.com/users/rahulgarg28071998/received_events',
  'type': 'User',
  'site_admin': False},
 'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website',
 'description': 'Website for ACM MAIT Student Chapter',
 'fork': True,
 'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website',
 'forks_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/forks',
 'keys_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/keys{/key_id}',
 'collaborators_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/collaborators{/collaborator}',
 'teams_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/teams',
 'hooks_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/hooks',
 'issue_events_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/issues/events{/number}',
 'events_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/events',
 'assignees_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/assignees{/user}',
 'branches_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/branches{/branch}',
 'tags_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/tags',
 'blobs_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/blobs{/sha}',
 'git_tags_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/tags{/sha}',
 'git_refs_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/refs{/sha}',
 'trees_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/trees{/sha}',
 'statuses_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/statuses/{sha}',
 'languages_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/languages',
 'stargazers_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/stargazers',
 'contributors_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/contributors',
 'subscribers_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/subscribers',
 'subscription_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/subscription',
 'commits_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits{/sha}',
 'git_commits_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/commits{/sha}',
 'comments_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/comments{/number}',
 'issue_comment_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/issues/comments{/number}',
 'contents_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/contents/{+path}',
 'compare_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/compare/{base}...{head}',
 'merges_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/merges',
 'archive_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/{archive_format}{/ref}',
 'downloads_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/downloads',
 'issues_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/issues{/number}',
 'pulls_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/pulls{/number}',
 'milestones_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/milestones{/number}',
 'notifications_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/notifications{?since,all,participating}',
 'labels_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/labels{/name}',
 'releases_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/releases{/id}',
 'deployments_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/deployments',
 'created_at': '2017-11-10T12:41:51Z',
 'updated_at': '2017-11-10T12:41:52Z',
 'pushed_at': '2017-10-20T12:15:44Z',
 'git_url': 'git://github.com/rahulgarg28071998/ACM-MAIT-Website.git',
 'ssh_url': 'git@github.com:rahulgarg28071998/ACM-MAIT-Website.git',
 'clone_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website.git',
 'svn_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website',
 'homepage': '',
 'size': 1926,
 'stargazers_count': 0,
 'watchers_count': 0,
 'language': 'CSS',
 'has_issues': False,
 'has_projects': True,
 'has_downloads': True,
 'has_wiki': True,
 'has_pages': False,
 'forks_count': 0,
 'mirror_url': None,
 'archived': False,
 'disabled': False,
 'open_issues_count': 0,
 'license': None,
 'forks': 0,
 'open_issues': 0,
 'watchers': 0,
 'default_branch': 'master',
 'permissions': {'admin': False, 'push': False, 'pull': True}}
Type Markdown and LaTeX: 𝛼2
Type Markdown and LaTeX: 𝛼2
repos_information = []
for i, repo in enumerate(repos_data):
    data = []
    data.append(repo['id'])
    data.append(repo['name'])
    data.append(repo['description'])
    data.append(repo['created_at'])
    data.append(repo['updated_at'])
    data.append(repo['owner']['login'])
    data.append(repo['license']['name'] if repo['license'] != None else None)
    data.append(repo['has_wiki'])
    data.append(repo['forks_count'])
    data.append(repo['open_issues_count'])
    data.append(repo['stargazers_count'])
    data.append(repo['watchers_count'])
    data.append(repo['url'])
    data.append(repo['commits_url'].split("{")[0])
    data.append(repo['url'] + '/languages')
    repos_information.append(data)
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
repos_df = pd.DataFrame(repos_information, columns = ['Id', 'Name', 'Description', 'Created on', 'Updated on', 
                                                      'Owner', 'License', 'Includes wiki', 'Forks count', 
                                                      'Issues count', 'Stars count', 'Watchers count',
                                                      'Repo URL', 'Commits URL', 'Languages URL'])
repos_df.head(10)
Id	Name	Description	Created on	Updated on	Owner	License	Includes wiki	Forks count	Issues count	Stars count	Watchers count	Repo URL	Commits URL	Languages URL
0	110245773	ACM-MAIT-Website	Website for ACM MAIT Student Chapter	2017-11-10T12:41:51Z	2017-11-10T12:41:52Z	rahulgarg28071998	None	True	0	0	0	0	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
1	194601024	AllMachineLearning-DeepLearning	contains all ML Projects	2019-07-01T04:43:57Z	2019-07-04T00:54:23Z	rahulgarg28071998	None	True	0	0	1	1	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
2	194501594	Artificail-Intelligence-RL	Artificail-Intelligence-RL	2019-06-30T10:08:39Z	2019-07-02T17:51:31Z	rahulgarg28071998	None	True	0	0	0	0	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
3	216314165	BatteryLife	None	2019-10-20T05:49:40Z	2019-10-24T10:40:48Z	rahulgarg28071998	None	True	1	0	0	0	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
4	108022563	computer-graphics	college lab code	2017-10-23T18:28:29Z	2017-10-23T18:44:27Z	rahulgarg28071998	None	True	0	0	1	1	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
5	107039363	data	None	2017-10-15T18:47:20Z	2017-10-24T13:39:47Z	rahulgarg28071998	None	True	0	0	1	1	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
6	128235503	eclipse-workspace-niit-project	None	2018-04-05T16:45:05Z	2018-04-05T16:49:56Z	rahulgarg28071998	None	True	0	0	0	0	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
7	88462367	Ecommerce-Project	None	2017-04-17T03:04:20Z	2017-04-17T03:04:22Z	rahulgarg28071998	None	True	0	0	0	0	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
8	222180630	HackK	None	2019-11-17T01:17:08Z	2019-11-17T01:17:08Z	rahulgarg28071998	None	True	0	0	0	0	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
9	222180655	hacknight	None	2019-11-17T01:17:22Z	2019-11-17T01:17:25Z	rahulgarg28071998	None	True	0	0	0	0	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...	https://api.github.com/repos/rahulgarg28071998...
Type Markdown and LaTeX: 𝛼2
for i in range(repos_df.shape[0]):
    response = requests.get(repos_df.loc[i, 'Languages URL'], auth = authentication)
    response = response.json()
    print(i, response)
    if response != {}:
        languages = []
        for key, value in response.items():
            languages.append(key)
        languages = ', '.join(languages)
        repos_df.loc[i, 'Languages'] = languages
    else:
        repos_df.loc[i, 'Languages'] = ""
0 {'CSS': 64172, 'HTML': 28319, 'JavaScript': 9328}
1 {'Jupyter Notebook': 317979}
2 {'Jupyter Notebook': 115318}
3 {'Jupyter Notebook': 300580, 'Python': 4994, 'HTML': 4042}
4 {}
5 {}
6 {'Java': 34645}
7 {'Java': 1492}
8 {}
9 {}
10 {'Python': 84798, 'R': 41696}
11 {'Scilab': 6239}
12 {}
13 {'C++': 17964}
14 {'C++': 19845}
15 {'Jupyter Notebook': 643831, 'Java': 357690, 'JavaScript': 113731, 'CSS': 14595, 'HTML': 14242}
16 {'Python': 282808}
17 {}
18 {'Java': 34645}
19 {'Java': 91751, 'CSS': 13653}
20 {}
Type Markdown and LaTeX: 𝛼2
repos_df.to_csv('repos_info.csv', index = False)
Type Markdown and LaTeX: 𝛼2
response = requests.get(repos_df.loc[0, 'Commits URL'], auth = authentication)
response.json()
[{'sha': 'ef0f181ff33adfc80e1605396a16238f397f14c9',
  'node_id': 'MDY6Q29tbWl0MTEwMjQ1NzczOmVmMGYxODFmZjMzYWRmYzgwZTE2MDUzOTZhMTYyMzhmMzk3ZjE0Yzk=',
  'commit': {'author': {'name': 'Savitoj Singh',
    'email': '31477126+phoenix157@users.noreply.github.com',
    'date': '2017-10-20T12:15:43Z'},
   'committer': {'name': 'GitHub',
    'email': 'noreply@github.com',
    'date': '2017-10-20T12:15:43Z'},
   'message': 'Merge pull request #1 from meghansh36/meghansh-changes\n\nfixed gallery',
   'tree': {'sha': '6015a11f0f6f9d00e5675255e31354966e3f2abb',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/trees/6015a11f0f6f9d00e5675255e31354966e3f2abb'},
   'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/commits/ef0f181ff33adfc80e1605396a16238f397f14c9',
   'comment_count': 0,
   'verification': {'verified': False,
    'reason': 'unsigned',
    'signature': None,
    'payload': None}},
  'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/ef0f181ff33adfc80e1605396a16238f397f14c9',
  'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/ef0f181ff33adfc80e1605396a16238f397f14c9',
  'comments_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/ef0f181ff33adfc80e1605396a16238f397f14c9/comments',
  'author': {'login': 'savitoj98',
   'id': 31477126,
   'node_id': 'MDQ6VXNlcjMxNDc3MTI2',
   'avatar_url': 'https://avatars1.githubusercontent.com/u/31477126?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/savitoj98',
   'html_url': 'https://github.com/savitoj98',
   'followers_url': 'https://api.github.com/users/savitoj98/followers',
   'following_url': 'https://api.github.com/users/savitoj98/following{/other_user}',
   'gists_url': 'https://api.github.com/users/savitoj98/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/savitoj98/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/savitoj98/subscriptions',
   'organizations_url': 'https://api.github.com/users/savitoj98/orgs',
   'repos_url': 'https://api.github.com/users/savitoj98/repos',
   'events_url': 'https://api.github.com/users/savitoj98/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/savitoj98/received_events',
   'type': 'User',
   'site_admin': False},
  'committer': {'login': 'web-flow',
   'id': 19864447,
   'node_id': 'MDQ6VXNlcjE5ODY0NDQ3',
   'avatar_url': 'https://avatars3.githubusercontent.com/u/19864447?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/web-flow',
   'html_url': 'https://github.com/web-flow',
   'followers_url': 'https://api.github.com/users/web-flow/followers',
   'following_url': 'https://api.github.com/users/web-flow/following{/other_user}',
   'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions',
   'organizations_url': 'https://api.github.com/users/web-flow/orgs',
   'repos_url': 'https://api.github.com/users/web-flow/repos',
   'events_url': 'https://api.github.com/users/web-flow/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/web-flow/received_events',
   'type': 'User',
   'site_admin': False},
  'parents': [{'sha': 'c654f698945bface53a4d8343b7abe5697d776f0',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/c654f698945bface53a4d8343b7abe5697d776f0',
    'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/c654f698945bface53a4d8343b7abe5697d776f0'},
   {'sha': '1883befe45bc52afccce4a62c446156ba8f9fda4',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/1883befe45bc52afccce4a62c446156ba8f9fda4',
    'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/1883befe45bc52afccce4a62c446156ba8f9fda4'}]},
 {'sha': '1883befe45bc52afccce4a62c446156ba8f9fda4',
  'node_id': 'MDY6Q29tbWl0MTEwMjQ1NzczOjE4ODNiZWZlNDViYzUyYWZjY2NlNGE2MmM0NDYxNTZiYThmOWZkYTQ=',
  'commit': {'author': {'name': 'meghansh36',
    'email': 'meghansh.work@gmail.com',
    'date': '2017-10-17T21:33:53Z'},
   'committer': {'name': 'meghansh36',
    'email': 'meghansh.work@gmail.com',
    'date': '2017-10-17T21:33:53Z'},
   'message': 'fixed gallery',
   'tree': {'sha': '6015a11f0f6f9d00e5675255e31354966e3f2abb',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/trees/6015a11f0f6f9d00e5675255e31354966e3f2abb'},
   'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/commits/1883befe45bc52afccce4a62c446156ba8f9fda4',
   'comment_count': 0,
   'verification': {'verified': False,
    'reason': 'unsigned',
    'signature': None,
    'payload': None}},
  'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/1883befe45bc52afccce4a62c446156ba8f9fda4',
  'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/1883befe45bc52afccce4a62c446156ba8f9fda4',
  'comments_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/1883befe45bc52afccce4a62c446156ba8f9fda4/comments',
  'author': {'login': 'meghansh36',
   'id': 32713974,
   'node_id': 'MDQ6VXNlcjMyNzEzOTc0',
   'avatar_url': 'https://avatars3.githubusercontent.com/u/32713974?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/meghansh36',
   'html_url': 'https://github.com/meghansh36',
   'followers_url': 'https://api.github.com/users/meghansh36/followers',
   'following_url': 'https://api.github.com/users/meghansh36/following{/other_user}',
   'gists_url': 'https://api.github.com/users/meghansh36/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/meghansh36/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/meghansh36/subscriptions',
   'organizations_url': 'https://api.github.com/users/meghansh36/orgs',
   'repos_url': 'https://api.github.com/users/meghansh36/repos',
   'events_url': 'https://api.github.com/users/meghansh36/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/meghansh36/received_events',
   'type': 'User',
   'site_admin': False},
  'committer': {'login': 'meghansh36',
   'id': 32713974,
   'node_id': 'MDQ6VXNlcjMyNzEzOTc0',
   'avatar_url': 'https://avatars3.githubusercontent.com/u/32713974?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/meghansh36',
   'html_url': 'https://github.com/meghansh36',
   'followers_url': 'https://api.github.com/users/meghansh36/followers',
   'following_url': 'https://api.github.com/users/meghansh36/following{/other_user}',
   'gists_url': 'https://api.github.com/users/meghansh36/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/meghansh36/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/meghansh36/subscriptions',
   'organizations_url': 'https://api.github.com/users/meghansh36/orgs',
   'repos_url': 'https://api.github.com/users/meghansh36/repos',
   'events_url': 'https://api.github.com/users/meghansh36/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/meghansh36/received_events',
   'type': 'User',
   'site_admin': False},
  'parents': [{'sha': 'c654f698945bface53a4d8343b7abe5697d776f0',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/c654f698945bface53a4d8343b7abe5697d776f0',
    'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/c654f698945bface53a4d8343b7abe5697d776f0'}]},
 {'sha': 'c654f698945bface53a4d8343b7abe5697d776f0',
  'node_id': 'MDY6Q29tbWl0MTEwMjQ1NzczOmM2NTRmNjk4OTQ1YmZhY2U1M2E0ZDgzNDNiN2FiZTU2OTdkNzc2ZjA=',
  'commit': {'author': {'name': 'Savitoj Singh',
    'email': '31477126+phoenix157@users.noreply.github.com',
    'date': '2017-10-11T08:46:41Z'},
   'committer': {'name': 'GitHub',
    'email': 'noreply@github.com',
    'date': '2017-10-11T08:46:41Z'},
   'message': 'Removed template.html',
   'tree': {'sha': '0e45f195cca7c3b322f19d41af193fa06a6a4e8a',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/trees/0e45f195cca7c3b322f19d41af193fa06a6a4e8a'},
   'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/commits/c654f698945bface53a4d8343b7abe5697d776f0',
   'comment_count': 0,
   'verification': {'verified': False,
    'reason': 'unsigned',
    'signature': None,
    'payload': None}},
  'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/c654f698945bface53a4d8343b7abe5697d776f0',
  'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/c654f698945bface53a4d8343b7abe5697d776f0',
  'comments_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/c654f698945bface53a4d8343b7abe5697d776f0/comments',
  'author': {'login': 'savitoj98',
   'id': 31477126,
   'node_id': 'MDQ6VXNlcjMxNDc3MTI2',
   'avatar_url': 'https://avatars1.githubusercontent.com/u/31477126?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/savitoj98',
   'html_url': 'https://github.com/savitoj98',
   'followers_url': 'https://api.github.com/users/savitoj98/followers',
   'following_url': 'https://api.github.com/users/savitoj98/following{/other_user}',
   'gists_url': 'https://api.github.com/users/savitoj98/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/savitoj98/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/savitoj98/subscriptions',
   'organizations_url': 'https://api.github.com/users/savitoj98/orgs',
   'repos_url': 'https://api.github.com/users/savitoj98/repos',
   'events_url': 'https://api.github.com/users/savitoj98/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/savitoj98/received_events',
   'type': 'User',
   'site_admin': False},
  'committer': {'login': 'web-flow',
   'id': 19864447,
   'node_id': 'MDQ6VXNlcjE5ODY0NDQ3',
   'avatar_url': 'https://avatars3.githubusercontent.com/u/19864447?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/web-flow',
   'html_url': 'https://github.com/web-flow',
   'followers_url': 'https://api.github.com/users/web-flow/followers',
   'following_url': 'https://api.github.com/users/web-flow/following{/other_user}',
   'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions',
   'organizations_url': 'https://api.github.com/users/web-flow/orgs',
   'repos_url': 'https://api.github.com/users/web-flow/repos',
   'events_url': 'https://api.github.com/users/web-flow/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/web-flow/received_events',
   'type': 'User',
   'site_admin': False},
  'parents': [{'sha': 'd6c4d98d9996e3280140eabff0195f8e1f627e88',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/d6c4d98d9996e3280140eabff0195f8e1f627e88',
    'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/d6c4d98d9996e3280140eabff0195f8e1f627e88'}]},
 {'sha': 'd6c4d98d9996e3280140eabff0195f8e1f627e88',
  'node_id': 'MDY6Q29tbWl0MTEwMjQ1NzczOmQ2YzRkOThkOTk5NmUzMjgwMTQwZWFiZmYwMTk1ZjhlMWY2MjdlODg=',
  'commit': {'author': {'name': 'Savitoj Singh',
    'email': '31477126+phoenix157@users.noreply.github.com',
    'date': '2017-10-11T08:39:27Z'},
   'committer': {'name': 'GitHub',
    'email': 'noreply@github.com',
    'date': '2017-10-11T08:39:27Z'},
   'message': 'Added README.md',
   'tree': {'sha': 'bd48d5523c358388c7d5465368756379412db503',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/trees/bd48d5523c358388c7d5465368756379412db503'},
   'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/commits/d6c4d98d9996e3280140eabff0195f8e1f627e88',
   'comment_count': 0,
   'verification': {'verified': False,
    'reason': 'unsigned',
    'signature': None,
    'payload': None}},
  'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/d6c4d98d9996e3280140eabff0195f8e1f627e88',
  'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/d6c4d98d9996e3280140eabff0195f8e1f627e88',
  'comments_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/d6c4d98d9996e3280140eabff0195f8e1f627e88/comments',
  'author': {'login': 'savitoj98',
   'id': 31477126,
   'node_id': 'MDQ6VXNlcjMxNDc3MTI2',
   'avatar_url': 'https://avatars1.githubusercontent.com/u/31477126?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/savitoj98',
   'html_url': 'https://github.com/savitoj98',
   'followers_url': 'https://api.github.com/users/savitoj98/followers',
   'following_url': 'https://api.github.com/users/savitoj98/following{/other_user}',
   'gists_url': 'https://api.github.com/users/savitoj98/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/savitoj98/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/savitoj98/subscriptions',
   'organizations_url': 'https://api.github.com/users/savitoj98/orgs',
   'repos_url': 'https://api.github.com/users/savitoj98/repos',
   'events_url': 'https://api.github.com/users/savitoj98/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/savitoj98/received_events',
   'type': 'User',
   'site_admin': False},
  'committer': {'login': 'web-flow',
   'id': 19864447,
   'node_id': 'MDQ6VXNlcjE5ODY0NDQ3',
   'avatar_url': 'https://avatars3.githubusercontent.com/u/19864447?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/web-flow',
   'html_url': 'https://github.com/web-flow',
   'followers_url': 'https://api.github.com/users/web-flow/followers',
   'following_url': 'https://api.github.com/users/web-flow/following{/other_user}',
   'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions',
   'organizations_url': 'https://api.github.com/users/web-flow/orgs',
   'repos_url': 'https://api.github.com/users/web-flow/repos',
   'events_url': 'https://api.github.com/users/web-flow/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/web-flow/received_events',
   'type': 'User',
   'site_admin': False},
  'parents': [{'sha': 'a50da02d330b872d3489b6197cdece5fdb2cdbc8',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/a50da02d330b872d3489b6197cdece5fdb2cdbc8',
    'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/a50da02d330b872d3489b6197cdece5fdb2cdbc8'}]},
 {'sha': 'a50da02d330b872d3489b6197cdece5fdb2cdbc8',
  'node_id': 'MDY6Q29tbWl0MTEwMjQ1NzczOmE1MGRhMDJkMzMwYjg3MmQzNDg5YjYxOTdjZGVjZTVmZGIyY2RiYzg=',
  'commit': {'author': {'name': 'savitoj',
    'email': 'savitojsingh15@gmail.com',
    'date': '2017-10-11T08:36:33Z'},
   'committer': {'name': 'savitoj',
    'email': 'savitojsingh15@gmail.com',
    'date': '2017-10-11T08:36:33Z'},
   'message': 'first commit',
   'tree': {'sha': '1f89476388e00a100e81eff2b0c56c18cd9286ba',
    'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/trees/1f89476388e00a100e81eff2b0c56c18cd9286ba'},
   'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/git/commits/a50da02d330b872d3489b6197cdece5fdb2cdbc8',
   'comment_count': 0,
   'verification': {'verified': False,
    'reason': 'unsigned',
    'signature': None,
    'payload': None}},
  'url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/a50da02d330b872d3489b6197cdece5fdb2cdbc8',
  'html_url': 'https://github.com/rahulgarg28071998/ACM-MAIT-Website/commit/a50da02d330b872d3489b6197cdece5fdb2cdbc8',
  'comments_url': 'https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits/a50da02d330b872d3489b6197cdece5fdb2cdbc8/comments',
  'author': {'login': 'savitoj98',
   'id': 31477126,
   'node_id': 'MDQ6VXNlcjMxNDc3MTI2',
   'avatar_url': 'https://avatars1.githubusercontent.com/u/31477126?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/savitoj98',
   'html_url': 'https://github.com/savitoj98',
   'followers_url': 'https://api.github.com/users/savitoj98/followers',
   'following_url': 'https://api.github.com/users/savitoj98/following{/other_user}',
   'gists_url': 'https://api.github.com/users/savitoj98/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/savitoj98/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/savitoj98/subscriptions',
   'organizations_url': 'https://api.github.com/users/savitoj98/orgs',
   'repos_url': 'https://api.github.com/users/savitoj98/repos',
   'events_url': 'https://api.github.com/users/savitoj98/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/savitoj98/received_events',
   'type': 'User',
   'site_admin': False},
  'committer': {'login': 'savitoj98',
   'id': 31477126,
   'node_id': 'MDQ6VXNlcjMxNDc3MTI2',
   'avatar_url': 'https://avatars1.githubusercontent.com/u/31477126?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/savitoj98',
   'html_url': 'https://github.com/savitoj98',
   'followers_url': 'https://api.github.com/users/savitoj98/followers',
   'following_url': 'https://api.github.com/users/savitoj98/following{/other_user}',
   'gists_url': 'https://api.github.com/users/savitoj98/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/savitoj98/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/savitoj98/subscriptions',
   'organizations_url': 'https://api.github.com/users/savitoj98/orgs',
   'repos_url': 'https://api.github.com/users/savitoj98/repos',
   'events_url': 'https://api.github.com/users/savitoj98/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/savitoj98/received_events',
   'type': 'User',
   'site_admin': False},
  'parents': []}]
Type Markdown and LaTeX: 𝛼2
commits_information = []
for i in range(repos_df.shape[0]):
    url = repos_df.loc[i, 'Commits URL']
    page_no = 1
    while (True):
        response = requests.get(url, auth = authentication)
        response = response.json()
        print("URL: {}, commits: {}".format(url, len(response)))
        for commit in response:
            try:
                commit_data = []
                commit_data.append(repos_df.loc[i, 'Id'])
                commit_data.append(commit['sha'])
                commit_data.append(commit['commit']['committer']['date'])
                commit_data.append(commit['commit']['message'])
                commits_information.append(commit_data)
            except: 
                pass
        if (len(response) == 30):
            page_no = page_no + 1
            url = repos_df.loc[i, 'Commits URL'] + '?page=' + str(page_no)
        else:
            break
URL: https://api.github.com/repos/rahulgarg28071998/ACM-MAIT-Website/commits, commits: 5
URL: https://api.github.com/repos/rahulgarg28071998/AllMachineLearning-DeepLearning/commits, commits: 2
URL: https://api.github.com/repos/rahulgarg28071998/Artificail-Intelligence-RL/commits, commits: 5
URL: https://api.github.com/repos/rahulgarg28071998/BatteryLife/commits, commits: 7
URL: https://api.github.com/repos/rahulgarg28071998/computer-graphics/commits, commits: 3
URL: https://api.github.com/repos/rahulgarg28071998/data/commits, commits: 5
URL: https://api.github.com/repos/rahulgarg28071998/eclipse-workspace-niit-project/commits, commits: 2
URL: https://api.github.com/repos/rahulgarg28071998/Ecommerce-Project/commits, commits: 29
URL: https://api.github.com/repos/rahulgarg28071998/HackK/commits, commits: 2
URL: https://api.github.com/repos/rahulgarg28071998/hacknight/commits, commits: 1
URL: https://api.github.com/repos/rahulgarg28071998/Machine-learning-A-Z/commits, commits: 3
URL: https://api.github.com/repos/rahulgarg28071998/mathlab-practical-scilab/commits, commits: 2
URL: https://api.github.com/repos/rahulgarg28071998/NiitDtKrishnaPackersWorkspace/commits, commits: 1
URL: https://api.github.com/repos/rahulgarg28071998/object-oriented-programmind/commits, commits: 3
URL: https://api.github.com/repos/rahulgarg28071998/OperatingSystemLab/commits, commits: 2
URL: https://api.github.com/repos/rahulgarg28071998/PepCoding/commits, commits: 13
URL: https://api.github.com/repos/rahulgarg28071998/Python-games-really-fun/commits, commits: 8
URL: https://api.github.com/repos/rahulgarg28071998/react-skeleton/commits, commits: 2
URL: https://api.github.com/repos/rahulgarg28071998/ShoppingCartBackend/commits, commits: 2
URL: https://api.github.com/repos/rahulgarg28071998/ShoppingCartFrontend/commits, commits: 3
URL: https://api.github.com/repos/rahulgarg28071998/webapp1/commits, commits: 8
commits_df = pd.DataFrame(commits_information, columns = ['Repo Id', 'Commit Id', 'Date', 'Message'])
commits_df.head(5)
Repo Id	Commit Id	Date	Message
0	110245773	ef0f181ff33adfc80e1605396a16238f397f14c9	2017-10-20T12:15:43Z	Merge pull request #1 from meghansh36/meghansh...
1	110245773	1883befe45bc52afccce4a62c446156ba8f9fda4	2017-10-17T21:33:53Z	fixed gallery
2	110245773	c654f698945bface53a4d8343b7abe5697d776f0	2017-10-11T08:46:41Z	Removed template.html
3	110245773	d6c4d98d9996e3280140eabff0195f8e1f627e88	2017-10-11T08:39:27Z	Added README.md
4	110245773	a50da02d330b872d3489b6197cdece5fdb2cdbc8	2017-10-11T08:36:33Z	first commit
​
Type Markdown and LaTeX: 𝛼2
commits_df.to_csv('commits_info.csv', index = False)
