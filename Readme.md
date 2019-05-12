# GRPH

Generate a python client code from graphql spec. It allows clients to define the structure of the data required, and exactly the same structure of the data is returned from the server. It is a strongly typed runtime which allows clients to dictate what data is needed.

### Usage

```python
python -m grph examples/github.json > examples/github_lib.py
```

### Sample of generated code

```python
class Repository(node):
    """
    A repository contains the content for a project.
    """

    codeOfConduct: CodeOfConduct = None
    createdAt: DateTime = None
    databaseId: int = None
    defaultBranchRef: Ref = None
    description: str = None
    descriptionHTML: HTML = None
    diskUsage: int = None
    forkCount: int = None
    hasIssuesEnabled: bool = None
    hasWikiEnabled: bool = None
    homepageUrl: URI = None
    id: ID = None
    isArchived: bool = None
    isFork: bool = None
    isLocked: bool = None
    isMirror: bool = None
    isPrivate: bool = None
    license: str = None
    licenseInfo: License = None
    lockReason: RepositoryLockReason = None
    mirrorUrl: URI = None
    name: str = None
    nameWithOwner: str = None
    owner: RepositoryOwner = None
    parent: Repository = None
    primaryLanguage: Language = None
    projectsResourcePath: URI = None
    projectsUrl: URI = None
    pushedAt: DateTime = None
    resourcePath: URI = None
    sshUrl: GitSSHRemote = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanAdminister: bool = None
    viewerCanCreateProjects: bool = None
    viewerCanSubscribe: bool = None
    viewerCanUpdateTopics: bool = None
    viewerHasStarred: bool = None
    viewerPermission: RepositoryPermission = None
    viewerSubscription: SubscriptionState = None

    def assignableUsers(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of users that can be assigned to issues in this repository.
        """
        tmpl = "assignableUsers(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())
...
class Query(Node):
    ....
    def repository(self, owner:str, name:str) -> Repository:
        """
        Lookup a given repository by the owner and repository name.
        """
        tmpl = "repository(owner:%(owner)s, name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, owner=owner, name=name, ret=Repository.F())


```

### Sample of request

```python
from grph.http import guery

import examples.github_lib as gh


def endpoint(q):
    return guery(q, port=443, sufix="/beta/betausers")


def test_gh():
    q = gh.query.repository(owner="foo", repo="bar")
    print(endpoint(q))

    q = gh.query.user(name="bar")
    print(endpoint(q))

test_gh()
```
