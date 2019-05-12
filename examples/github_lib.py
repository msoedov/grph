from grph.util import *

define(__name__, [
    "Actor",
    "Assignable",
    "AssignedEvent",
    "AddedToProjectEvent",
    "AddReactionPayload",
    "AddReactionInput",
    "AddCommentPayload",
    "AddCommentInput",
    "AddProjectColumnPayload",
    "AddProjectColumnInput",
    "AddProjectCardPayload",
    "AddProjectCardInput",
    "AddPullRequestReviewPayload",
    "AddPullRequestReviewInput",
    "AddPullRequestReviewCommentPayload",
    "AddPullRequestReviewCommentInput",
    "AddStarPayload",
    "AddStarInput",
    "AcceptTopicSuggestionPayload",
    "AcceptTopicSuggestionInput",
    "Blob",
    "Blame",
    "BlameRange",
    "Bot",
    "BaseRefForcePushedEvent",
    "BaseRefChangedEvent",
    "Closable",
    "Comment",
    "CommentAuthorAssociation",
    "CommentCannotUpdateReason",
    "Commit",
    "CommitConnection",
    "CommitEdge",
    "CommitHistoryConnection",
    "CommitAuthor",
    "CommitCommentConnection",
    "CommitCommentEdge",
    "CommitComment",
    "CommitCommentThread",
    "ClosedEvent",
    "Closer",
    "CrossReferencedEvent",
    "CommentDeletedEvent",
    "ConvertedNoteToIssueEvent",
    "CollaboratorAffiliation",
    "CodeOfConduct",
    "CollectionItemContent",
    "CreateProjectPayload",
    "CreateProjectInput",
    "DateTime",
    "Deletable",
    "Date",
    "DefaultRepositoryPermissionField",
    "DemilestonedEvent",
    "DeployedEvent",
    "Deployment",
    "DeploymentStatusConnection",
    "DeploymentStatusEdge",
    "DeploymentStatus",
    "DeploymentStatusState",
    "DeploymentState",
    "DeployKeyConnection",
    "DeployKeyEdge",
    "DeployKey",
    "DeploymentConnection",
    "DeploymentEdge",
    "DeleteProjectPayload",
    "DeleteProjectInput",
    "DeleteProjectColumnPayload",
    "DeleteProjectColumnInput",
    "DeleteProjectCardPayload",
    "DeleteProjectCardInput",
    "DraftPullRequestReviewComment",
    "DismissPullRequestReviewPayload",
    "DismissPullRequestReviewInput",
    "DeletePullRequestReviewPayload",
    "DeletePullRequestReviewInput",
    "DeclineTopicSuggestionPayload",
    "DeclineTopicSuggestionInput",
    "ExternalIdentityConnection",
    "ExternalIdentityEdge",
    "ExternalIdentity",
    "ExternalIdentitySamlAttributes",
    "ExternalIdentityScimAttributes",
    "FollowingConnection",
    "FollowerConnection",
    "GitObject",
    "GitObjectID",
    "GitActor",
    "GitTimestamp",
    "GitSignature",
    "GitSignatureState",
    "GistConnection",
    "GistEdge",
    "Gist",
    "GistCommentConnection",
    "GistCommentEdge",
    "GistComment",
    "GistPrivacy",
    "GistOrder",
    "GistOrderField",
    "GitSSHRemote",
    "GitHubMetadata",
    "GpgSignature",
    "HTML",
    "HeadRefDeletedEvent",
    "HeadRefRestoredEvent",
    "HeadRefForcePushedEvent",
    "Issue",
    "IssueConnection",
    "IssueEdge",
    "IssueOrder",
    "IssueOrderField",
    "IssueState",
    "IssueCommentConnection",
    "IssueCommentEdge",
    "IssueComment",
    "IssuePubSubTopic",
    "IssueOrPullRequest",
    "IssueTimelineConnection",
    "IssueTimelineItemEdge",
    "IssueTimelineItem",
    "Labelable",
    "LabelConnection",
    "LabelEdge",
    "Label",
    "Lockable",
    "LockReason",
    "LanguageConnection",
    "LanguageEdge",
    "Language",
    "License",
    "LicenseRule",
    "LabeledEvent",
    "LockedEvent",
    "LanguageOrder",
    "LanguageOrderField",
    "LockLockablePayload",
    "LockLockableInput",
    "Milestone",
    "MilestoneState",
    "MergeableState",
    "MarketplaceListing",
    "MarketplaceCategory",
    "MergedEvent",
    "MilestonedEvent",
    "MilestoneItem",
    "MentionedEvent",
    "MovedColumnsInProjectEvent",
    "MilestoneConnection",
    "MilestoneEdge",
    "MilestoneOrder",
    "MilestoneOrderField",
    "MarketplaceListingConnection",
    "MarketplaceListingEdge",
    "Mutation",
    "MoveProjectColumnPayload",
    "MoveProjectColumnInput",
    "MoveProjectCardPayload",
    "MoveProjectCardInput",
    "Node",
    "OrderDirection",
    "OrganizationInvitationConnection",
    "OrganizationInvitationEdge",
    "OrganizationInvitation",
    "Organization",
    "OrganizationConnection",
    "OrganizationEdge",
    "OrganizationIdentityProvider",
    "OrganizationInvitationType",
    "OrganizationInvitationRole",
    "ProjectOwner",
    "Project",
    "ProjectState",
    "ProjectColumnConnection",
    "ProjectColumnEdge",
    "ProjectColumn",
    "ProjectCardConnection",
    "ProjectCardEdge",
    "ProjectCard",
    "ProjectCardState",
    "ProjectCardItem",
    "PageInfo",
    "PullRequestConnection",
    "PullRequestEdge",
    "PullRequest",
    "PullRequestState",
    "PullRequestReviewConnection",
    "PullRequestReviewEdge",
    "PullRequestReview",
    "PullRequestReviewState",
    "PullRequestReviewCommentConnection",
    "PullRequestReviewCommentEdge",
    "PullRequestReviewComment",
    "PullRequestPubSubTopic",
    "PullRequestReviewThread",
    "ProjectConnection",
    "ProjectEdge",
    "ProjectOrder",
    "ProjectOrderField",
    "PullRequestCommitConnection",
    "PullRequestCommitEdge",
    "PullRequestCommit",
    "PullRequestTimelineConnection",
    "PullRequestTimelineItemEdge",
    "PullRequestTimelineItem",
    "ProtectedBranchConnection",
    "ProtectedBranchEdge",
    "ProtectedBranch",
    "PushAllowanceConnection",
    "PushAllowanceEdge",
    "PushAllowance",
    "PushAllowanceActor",
    "PublicKeyConnection",
    "PublicKeyEdge",
    "PublicKey",
    "PullRequestReviewEvent",
    "Query",
    "Repository",
    "Reactable",
    "ReactionGroup",
    "ReactionContent",
    "ReactingUserConnection",
    "ReactingUserEdge",
    "ReactionConnection",
    "ReactionEdge",
    "Reaction",
    "ReactionOrder",
    "ReactionOrderField",
    "RepositoryNode",
    "Ref",
    "RepositoryOwner",
    "RepositoryConnection",
    "RepositoryEdge",
    "RepositoryPrivacy",
    "RepositoryOrder",
    "RepositoryOrderField",
    "RepositoryAffiliation",
    "RepositoryPermission",
    "RepositoryInvitation",
    "RepositoryInvitationRepository",
    "RepositoryInfo",
    "RepositoryLockReason",
    "ReviewRequestConnection",
    "ReviewRequestEdge",
    "ReviewRequest",
    "RequestedReviewer",
    "ReopenedEvent",
    "ReferencedEvent",
    "ReferencedSubject",
    "RenamedTitleEvent",
    "RenamedTitleSubject",
    "ReviewRequestedEvent",
    "ReviewRequestRemovedEvent",
    "ReviewDismissedEvent",
    "RemovedFromProjectEvent",
    "RepositoryCollaboratorAffiliation",
    "RepositoryTopicConnection",
    "RepositoryTopicEdge",
    "RepositoryTopic",
    "Release",
    "ReleaseAssetConnection",
    "ReleaseAssetEdge",
    "ReleaseAsset",
    "ReviewDismissalAllowanceConnection",
    "ReviewDismissalAllowanceEdge",
    "ReviewDismissalAllowance",
    "ReviewDismissalAllowanceActor",
    "RepositoryCollaboratorConnection",
    "RepositoryCollaboratorEdge",
    "RefConnection",
    "RefEdge",
    "RefOrder",
    "RefOrderField",
    "ReleaseConnection",
    "ReleaseEdge",
    "ReleaseOrder",
    "ReleaseOrderField",
    "RepositoryContributionType",
    "RateLimit",
    "RemoveReactionPayload",
    "RemoveReactionInput",
    "RemoveOutsideCollaboratorPayload",
    "RemoveOutsideCollaboratorInput",
    "RequestReviewsPayload",
    "RequestReviewsInput",
    "RemoveStarPayload",
    "RemoveStarInput",
    "Subscribable",
    "SubscriptionState",
    "Status",
    "StatusState",
    "StatusContext",
    "Starrable",
    "StargazerConnection",
    "StargazerEdge",
    "StarOrder",
    "StarOrderField",
    "SubscribedEvent",
    "SuggestedReviewer",
    "StarredRepositoryConnection",
    "StarredRepositoryEdge",
    "SearchResultItemConnection",
    "SearchResultItemEdge",
    "SearchResultItem",
    "SearchType",
    "SubmitPullRequestReviewPayload",
    "SubmitPullRequestReviewInput",
    "SmimeSignature",
    "Tree",
    "TreeEntry",
    "TeamConnection",
    "TeamEdge",
    "Team",
    "TeamPrivacy",
    "TeamMemberConnection",
    "TeamMemberEdge",
    "TeamMemberRole",
    "TeamMembershipType",
    "TeamRepositoryConnection",
    "TeamRepositoryEdge",
    "TeamRepositoryOrder",
    "TeamRepositoryOrderField",
    "TeamRole",
    "TeamOrder",
    "TeamOrderField",
    "Topic",
    "TopicConnection",
    "TopicEdge",
    "TextMatch",
    "TextMatchHighlight",
    "TopicSuggestionDeclineReason",
    "Tag",
    "UniformResourceLocatable",
    "URI",
    "User",
    "Updatable",
    "UserConnection",
    "UserEdge",
    "UserContentEditConnection",
    "UserContentEditEdge",
    "UserContentEdit",
    "UpdatableComment",
    "UnsubscribedEvent",
    "UnassignedEvent",
    "UnlabeledEvent",
    "UnlockedEvent",
    "UpdateSubscriptionPayload",
    "UpdateSubscriptionInput",
    "UpdateProjectPayload",
    "UpdateProjectInput",
    "UpdateProjectColumnPayload",
    "UpdateProjectColumnInput",
    "UpdateProjectCardPayload",
    "UpdateProjectCardInput",
    "UpdatePullRequestReviewPayload",
    "UpdatePullRequestReviewInput",
    "UpdatePullRequestReviewCommentPayload",
    "UpdatePullRequestReviewCommentInput",
    "UpdateTopicsPayload",
    "UpdateTopicsInput",
    "UnknownSignature",
    "X509Certificate",
])

class Query(node):
    """
    The query root of GitHub's GraphQL interface.
    """

    codesOfConduct: CodeOfConduct = None
    licenses: None = None
    meta: GitHubMetadata = None
    relay: Query = None
    viewer: User = None

    def codeOfConduct(self, key:str) -> CodeOfConduct:
        """
        Look up a code of conduct by its key
        """
        tmpl = "codeOfConduct(key:%(key)s) %(ret)s"
        return self.wrap(tmpl, fn=True, key=key, ret=CodeOfConduct.F())

    def license(self, key:str) -> License:
        """
        Look up an open source license by its key
        """
        tmpl = "license(key:%(key)s) %(ret)s"
        return self.wrap(tmpl, fn=True, key=key, ret=License.F())

    def marketplaceCategories(self, excludeEmpty:bool) -> MarketplaceCategory:
        """
        Get alphabetically sorted list of Marketplace categories
        """
        tmpl = "marketplaceCategories(excludeEmpty:%(excludeEmpty)s) %(ret)s"
        return self.wrap(tmpl, fn=True, excludeEmpty=excludeEmpty, ret=MarketplaceCategory.F())

    def marketplaceCategory(self, slug:str) -> MarketplaceCategory:
        """
        Look up a Marketplace category by its slug.
        """
        tmpl = "marketplaceCategory(slug:%(slug)s) %(ret)s"
        return self.wrap(tmpl, fn=True, slug=slug, ret=MarketplaceCategory.F())

    def marketplaceListing(self, slug:str) -> MarketplaceListing:
        """
        Look up a single Marketplace listing
        """
        tmpl = "marketplaceListing(slug:%(slug)s) %(ret)s"
        return self.wrap(tmpl, fn=True, slug=slug, ret=MarketplaceListing.F())

    def marketplaceListings(self, first:int, after:str, last:int, before:str, categorySlug:str, viewerCanAdmin:bool, adminId:ID, organizationId:ID, allStates:bool, slugs:str, primaryCategoryOnly:bool, withFreeTrialsOnly:bool) -> MarketplaceListingConnection:
        """
        Look up Marketplace listings
        """
        tmpl = "marketplaceListings(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, categorySlug:%(categorySlug)s, viewerCanAdmin:%(viewerCanAdmin)s, adminId:%(adminId)s, organizationId:%(organizationId)s, allStates:%(allStates)s, slugs:%(slugs)s, primaryCategoryOnly:%(primaryCategoryOnly)s, withFreeTrialsOnly:%(withFreeTrialsOnly)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, categorySlug=categorySlug, viewerCanAdmin=viewerCanAdmin, adminId=adminId, organizationId=organizationId, allStates=allStates, slugs=slugs, primaryCategoryOnly=primaryCategoryOnly, withFreeTrialsOnly=withFreeTrialsOnly, ret=MarketplaceListingConnection.F())

    def node(self, id:ID) -> Node:
        """
        Fetches an object given its ID.
        """
        tmpl = "node(id:%(id)s) %(ret)s"
        return self.wrap(tmpl, fn=True, id=id, ret=Node.F())

    def nodes(self, ids:ID) -> Node:
        """
        Lookup nodes by a list of IDs.
        """
        tmpl = "nodes(ids:%(ids)s) %(ret)s"
        return self.wrap(tmpl, fn=True, ids=ids, ret=Node.F())

    def organization(self, login:str) -> Organization:
        """
        Lookup a organization by login.
        """
        tmpl = "organization(login:%(login)s) %(ret)s"
        return self.wrap(tmpl, fn=True, login=login, ret=Organization.F())

    def rateLimit(self, dryRun:bool) -> RateLimit:
        """
        The client's rate limit information.
        """
        tmpl = "rateLimit(dryRun:%(dryRun)s) %(ret)s"
        return self.wrap(tmpl, fn=True, dryRun=dryRun, ret=RateLimit.F())

    def repository(self, owner:str, name:str) -> Repository:
        """
        Lookup a given repository by the owner and repository name.
        """
        tmpl = "repository(owner:%(owner)s, name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, owner=owner, name=name, ret=Repository.F())

    def repositoryOwner(self, login:str) -> RepositoryOwner:
        """
        Lookup a repository owner (ie. either a User or an Organization) by login.
        """
        tmpl = "repositoryOwner(login:%(login)s) %(ret)s"
        return self.wrap(tmpl, fn=True, login=login, ret=RepositoryOwner.F())

    def resource(self, url:URI) -> UniformResourceLocatable:
        """
        Lookup resource by a URL.
        """
        tmpl = "resource(url:%(url)s) %(ret)s"
        return self.wrap(tmpl, fn=True, url=url, ret=UniformResourceLocatable.F())

    def search(self, first:int, after:str, last:int, before:str, query:str, type:SearchType) -> SearchResultItemConnection:
        """
        Perform a search across resources.
        """
        tmpl = "search(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, query:%(query)s, type:%(type)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, query=query, type=type, ret=SearchResultItemConnection.F())

    def topic(self, name:str) -> Topic:
        """
        Look up a topic by name.
        """
        tmpl = "topic(name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, name=name, ret=Topic.F())

    def user(self, login:str) -> User:
        """
        Lookup a user by login.
        """
        tmpl = "user(login:%(login)s) %(ret)s"
        return self.wrap(tmpl, fn=True, login=login, ret=User.F())

    def render(self):
        return dict(codesOfConduct=self.codesOfConduct, licenses=self.licenses, meta=self.meta, relay=self.relay, viewer=self.viewer)



class Node(node):
    """
    An object with an ID.
    """

    id: ID = None

    def render(self):
        return dict(id=self.id)



class UniformResourceLocatable(node):
    """
    Represents a type that can be retrieved by a URL.
    """

    resourcePath: URI = None
    url: URI = None

    def render(self):
        return dict(resourcePath=self.resourcePath, url=self.url)



class URI(str):
    """
    An RFC 3986, RFC 3987, and RFC 6570 (level 4) compliant URI string.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "URI"


class User(node):
    """
    A user is an individual's account on GitHub that owns repositories and can make new content.
    """

    bio: str = None
    bioHTML: HTML = None
    company: str = None
    companyHTML: HTML = None
    createdAt: DateTime = None
    databaseId: int = None
    email: str = None
    id: ID = None
    isBountyHunter: bool = None
    isCampusExpert: bool = None
    isDeveloperProgramMember: bool = None
    isEmployee: bool = None
    isHireable: bool = None
    isSiteAdmin: bool = None
    isViewer: bool = None
    location: str = None
    login: str = None
    name: str = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanFollow: bool = None
    viewerIsFollowing: bool = None
    websiteUrl: URI = None

    def avatarUrl(self, size:int) -> URI:
        """
        A URL pointing to the user's public avatar.
        """
        tmpl = "avatarUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def commitComments(self, first:int, after:str, last:int, before:str) -> CommitCommentConnection:
        """
        A list of commit comments made by this user.
        """
        tmpl = "commitComments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=CommitCommentConnection.F())

    def contributedRepositories(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool) -> RepositoryConnection:
        """
        A list of repositories that the user recently contributed to.
        """
        tmpl = "contributedRepositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, ret=RepositoryConnection.F())

    def followers(self, first:int, after:str, last:int, before:str) -> FollowerConnection:
        """
        A list of users the given user is followed by.
        """
        tmpl = "followers(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=FollowerConnection.F())

    def following(self, first:int, after:str, last:int, before:str) -> FollowingConnection:
        """
        A list of users the given user is following.
        """
        tmpl = "following(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=FollowingConnection.F())

    def gist(self, name:str) -> Gist:
        """
        Find gist by repo name.
        """
        tmpl = "gist(name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, name=name, ret=Gist.F())

    def gistComments(self, first:int, after:str, last:int, before:str) -> GistCommentConnection:
        """
        A list of gist comments made by this user.
        """
        tmpl = "gistComments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=GistCommentConnection.F())

    def gists(self, first:int, after:str, last:int, before:str, privacy:GistPrivacy, orderBy:GistOrder) -> GistConnection:
        """
        A list of the Gists the user has created.
        """
        tmpl = "gists(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, ret=GistConnection.F())

    def issueComments(self, first:int, after:str, last:int, before:str) -> IssueCommentConnection:
        """
        A list of issue comments made by this user.
        """
        tmpl = "issueComments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=IssueCommentConnection.F())

    def issues(self, first:int, after:str, last:int, before:str, labels:str, orderBy:IssueOrder, states:IssueState) -> IssueConnection:
        """
        A list of issues assocated with this user.
        """
        tmpl = "issues(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, labels:%(labels)s, orderBy:%(orderBy)s, states:%(states)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, labels=labels, orderBy=orderBy, states=states, ret=IssueConnection.F())

    def organization(self, login:str) -> Organization:
        """
        Find an organization by its login that the user belongs to.
        """
        tmpl = "organization(login:%(login)s) %(ret)s"
        return self.wrap(tmpl, fn=True, login=login, ret=Organization.F())

    def organizations(self, first:int, after:str, last:int, before:str) -> OrganizationConnection:
        """
        A list of organizations the user belongs to.
        """
        tmpl = "organizations(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=OrganizationConnection.F())

    def pinnedRepositories(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool) -> RepositoryConnection:
        """
        A list of repositories this user has pinned to their profile
        """
        tmpl = "pinnedRepositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, ret=RepositoryConnection.F())

    def publicKeys(self, first:int, after:str, last:int, before:str) -> PublicKeyConnection:
        """
        A list of public keys associated with this user.
        """
        tmpl = "publicKeys(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=PublicKeyConnection.F())

    def pullRequests(self, first:int, after:str, last:int, before:str, states:PullRequestState, labels:str, headRefName:str, baseRefName:str, orderBy:IssueOrder) -> PullRequestConnection:
        """
        A list of pull requests assocated with this user.
        """
        tmpl = "pullRequests(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, states:%(states)s, labels:%(labels)s, headRefName:%(headRefName)s, baseRefName:%(baseRefName)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, states=states, labels=labels, headRefName=headRefName, baseRefName=baseRefName, orderBy=orderBy, ret=PullRequestConnection.F())

    def repositories(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool, isFork:bool) -> RepositoryConnection:
        """
        A list of repositories that the user owns.
        """
        tmpl = "repositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s, isFork:%(isFork)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, isFork=isFork, ret=RepositoryConnection.F())

    def repositoriesContributedTo(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, isLocked:bool, includeUserRepositories:bool, contributionTypes:RepositoryContributionType) -> RepositoryConnection:
        """
        A list of repositories that the user recently contributed to.
        """
        tmpl = "repositoriesContributedTo(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, isLocked:%(isLocked)s, includeUserRepositories:%(includeUserRepositories)s, contributionTypes:%(contributionTypes)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, isLocked=isLocked, includeUserRepositories=includeUserRepositories, contributionTypes=contributionTypes, ret=RepositoryConnection.F())

    def repository(self, name:str) -> Repository:
        """
        Find Repository.
        """
        tmpl = "repository(name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, name=name, ret=Repository.F())

    def starredRepositories(self, first:int, after:str, last:int, before:str, ownedByViewer:bool, orderBy:StarOrder) -> StarredRepositoryConnection:
        """
        Repositories the user has starred.
        """
        tmpl = "starredRepositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, ownedByViewer:%(ownedByViewer)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ownedByViewer=ownedByViewer, orderBy=orderBy, ret=StarredRepositoryConnection.F())

    def watching(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool) -> RepositoryConnection:
        """
        A list of repositories the given user is watching.
        """
        tmpl = "watching(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, ret=RepositoryConnection.F())

    def render(self):
        return dict(bio=self.bio, bioHTML=self.bioHTML, company=self.company, companyHTML=self.companyHTML, createdAt=self.createdAt, databaseId=self.databaseId, email=self.email, id=self.id, isBountyHunter=self.isBountyHunter, isCampusExpert=self.isCampusExpert, isDeveloperProgramMember=self.isDeveloperProgramMember, isEmployee=self.isEmployee, isHireable=self.isHireable, isSiteAdmin=self.isSiteAdmin, isViewer=self.isViewer, location=self.location, login=self.login, name=self.name, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url, viewerCanFollow=self.viewerCanFollow, viewerIsFollowing=self.viewerIsFollowing, websiteUrl=self.websiteUrl)



class Actor(node):
    """
    Represents an object which can take actions on GitHub. Typically a User or Bot.
    """

    login: str = None
    resourcePath: URI = None
    url: URI = None

    def avatarUrl(self, size:int) -> URI:
        """
        A URL pointing to the actor's public avatar.
        """
        tmpl = "avatarUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def render(self):
        return dict(login=self.login, resourcePath=self.resourcePath, url=self.url)



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

    def collaborators(self, first:int, after:str, last:int, before:str, affiliation:CollaboratorAffiliation) -> RepositoryCollaboratorConnection:
        """
        A list of collaborators associated with the repository.
        """
        tmpl = "collaborators(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, affiliation:%(affiliation)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, affiliation=affiliation, ret=RepositoryCollaboratorConnection.F())

    def commitComments(self, first:int, after:str, last:int, before:str) -> CommitCommentConnection:
        """
        A list of commit comments associated with the repository.
        """
        tmpl = "commitComments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=CommitCommentConnection.F())

    def deployKeys(self, first:int, after:str, last:int, before:str) -> DeployKeyConnection:
        """
        A list of deploy keys that are on this repository.
        """
        tmpl = "deployKeys(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=DeployKeyConnection.F())

    def deployments(self, first:int, after:str, last:int, before:str, environments:str) -> DeploymentConnection:
        """
        Deployments associated with the repository
        """
        tmpl = "deployments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, environments:%(environments)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, environments=environments, ret=DeploymentConnection.F())

    def forks(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool) -> RepositoryConnection:
        """
        A list of direct forked repositories.
        """
        tmpl = "forks(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, ret=RepositoryConnection.F())

    def issue(self, number:int) -> Issue:
        """
        Returns a single issue from the current repository by number.
        """
        tmpl = "issue(number:%(number)s) %(ret)s"
        return self.wrap(tmpl, fn=True, number=number, ret=Issue.F())

    def issueOrPullRequest(self, number:int) -> IssueOrPullRequest:
        """
        Returns a single issue-like object from the current repository by number.
        """
        tmpl = "issueOrPullRequest(number:%(number)s) %(ret)s"
        return self.wrap(tmpl, fn=True, number=number, ret=IssueOrPullRequest.F())

    def issues(self, first:int, after:str, last:int, before:str, labels:str, orderBy:IssueOrder, states:IssueState) -> IssueConnection:
        """
        A list of issues that have been opened in the repository.
        """
        tmpl = "issues(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, labels:%(labels)s, orderBy:%(orderBy)s, states:%(states)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, labels=labels, orderBy=orderBy, states=states, ret=IssueConnection.F())

    def label(self, name:str) -> Label:
        """
        Returns a single label by name
        """
        tmpl = "label(name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, name=name, ret=Label.F())

    def labels(self, first:int, after:str, last:int, before:str, query:str) -> LabelConnection:
        """
        A list of labels associated with the repository.
        """
        tmpl = "labels(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, query:%(query)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, query=query, ret=LabelConnection.F())

    def languages(self, first:int, after:str, last:int, before:str, orderBy:LanguageOrder) -> LanguageConnection:
        """
        A list containing a breakdown of the language composition of the repository.
        """
        tmpl = "languages(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, ret=LanguageConnection.F())

    def mentionableUsers(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of Users that can be mentioned in the context of the repository.
        """
        tmpl = "mentionableUsers(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def milestone(self, number:int) -> Milestone:
        """
        Returns a single milestone from the current repository by number.
        """
        tmpl = "milestone(number:%(number)s) %(ret)s"
        return self.wrap(tmpl, fn=True, number=number, ret=Milestone.F())

    def milestones(self, first:int, after:str, last:int, before:str, states:MilestoneState, orderBy:MilestoneOrder) -> MilestoneConnection:
        """
        A list of milestones associated with the repository.
        """
        tmpl = "milestones(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, states:%(states)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, states=states, orderBy=orderBy, ret=MilestoneConnection.F())

    def object(self, oid:GitObjectID, expression:str) -> GitObject:
        """
        A Git object in the repository
        """
        tmpl = "object(oid:%(oid)s, expression:%(expression)s) %(ret)s"
        return self.wrap(tmpl, fn=True, oid=oid, expression=expression, ret=GitObject.F())

    def project(self, number:int) -> Project:
        """
        Find project by number.
        """
        tmpl = "project(number:%(number)s) %(ret)s"
        return self.wrap(tmpl, fn=True, number=number, ret=Project.F())

    def projects(self, first:int, after:str, last:int, before:str, orderBy:ProjectOrder, search:str, states:ProjectState) -> ProjectConnection:
        """
        A list of projects under the owner.
        """
        tmpl = "projects(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s, search:%(search)s, states:%(states)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, search=search, states=states, ret=ProjectConnection.F())

    def protectedBranches(self, first:int, after:str, last:int, before:str) -> ProtectedBranchConnection:
        """
        A list of protected branches that are on this repository.
        """
        tmpl = "protectedBranches(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ProtectedBranchConnection.F())

    def pullRequest(self, number:int) -> PullRequest:
        """
        Returns a single pull request from the current repository by number.
        """
        tmpl = "pullRequest(number:%(number)s) %(ret)s"
        return self.wrap(tmpl, fn=True, number=number, ret=PullRequest.F())

    def pullRequests(self, first:int, after:str, last:int, before:str, states:PullRequestState, labels:str, headRefName:str, baseRefName:str, orderBy:IssueOrder) -> PullRequestConnection:
        """
        A list of pull requests that have been opened in the repository.
        """
        tmpl = "pullRequests(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, states:%(states)s, labels:%(labels)s, headRefName:%(headRefName)s, baseRefName:%(baseRefName)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, states=states, labels=labels, headRefName=headRefName, baseRefName=baseRefName, orderBy=orderBy, ret=PullRequestConnection.F())

    def ref(self, qualifiedName:str) -> Ref:
        """
        Fetch a given ref from the repository
        """
        tmpl = "ref(qualifiedName:%(qualifiedName)s) %(ret)s"
        return self.wrap(tmpl, fn=True, qualifiedName=qualifiedName, ret=Ref.F())

    def refs(self, first:int, after:str, last:int, before:str, refPrefix:str, direction:OrderDirection, orderBy:RefOrder) -> RefConnection:
        """
        Fetch a list of refs from the repository
        """
        tmpl = "refs(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, refPrefix:%(refPrefix)s, direction:%(direction)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, refPrefix=refPrefix, direction=direction, orderBy=orderBy, ret=RefConnection.F())

    def release(self, tagName:str) -> Release:
        """
        Lookup a single release given various criteria.
        """
        tmpl = "release(tagName:%(tagName)s) %(ret)s"
        return self.wrap(tmpl, fn=True, tagName=tagName, ret=Release.F())

    def releases(self, first:int, after:str, last:int, before:str, orderBy:ReleaseOrder) -> ReleaseConnection:
        """
        List of releases which are dependent on this repository.
        """
        tmpl = "releases(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, ret=ReleaseConnection.F())

    def repositoryTopics(self, first:int, after:str, last:int, before:str) -> RepositoryTopicConnection:
        """
        A list of applied repository-topic associations for this repository.
        """
        tmpl = "repositoryTopics(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=RepositoryTopicConnection.F())

    def shortDescriptionHTML(self, limit:int) -> HTML:
        """
        A description of the repository, rendered to HTML without any links in it.
        """
        tmpl = "shortDescriptionHTML(limit:%(limit)s) %(ret)s"
        return self.wrap(tmpl, fn=True, limit=limit, ret=HTML.F())

    def stargazers(self, first:int, after:str, last:int, before:str, orderBy:StarOrder) -> StargazerConnection:
        """
        A list of users who have starred this starrable.
        """
        tmpl = "stargazers(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, ret=StargazerConnection.F())

    def watchers(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of users watching the repository.
        """
        tmpl = "watchers(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def render(self):
        return dict(codeOfConduct=self.codeOfConduct, createdAt=self.createdAt, databaseId=self.databaseId, defaultBranchRef=self.defaultBranchRef, description=self.description, descriptionHTML=self.descriptionHTML, diskUsage=self.diskUsage, forkCount=self.forkCount, hasIssuesEnabled=self.hasIssuesEnabled, hasWikiEnabled=self.hasWikiEnabled, homepageUrl=self.homepageUrl, id=self.id, isArchived=self.isArchived, isFork=self.isFork, isLocked=self.isLocked, isMirror=self.isMirror, isPrivate=self.isPrivate, license=self.license, licenseInfo=self.licenseInfo, lockReason=self.lockReason, mirrorUrl=self.mirrorUrl, name=self.name, nameWithOwner=self.nameWithOwner, owner=self.owner, parent=self.parent, primaryLanguage=self.primaryLanguage, projectsResourcePath=self.projectsResourcePath, projectsUrl=self.projectsUrl, pushedAt=self.pushedAt, resourcePath=self.resourcePath, sshUrl=self.sshUrl, updatedAt=self.updatedAt, url=self.url, viewerCanAdminister=self.viewerCanAdminister, viewerCanCreateProjects=self.viewerCanCreateProjects, viewerCanSubscribe=self.viewerCanSubscribe, viewerCanUpdateTopics=self.viewerCanUpdateTopics, viewerHasStarred=self.viewerHasStarred, viewerPermission=self.viewerPermission, viewerSubscription=self.viewerSubscription)



class ProjectOwner(node):
    """
    Represents an owner of a Project.
    """

    id: ID = None
    projectsResourcePath: URI = None
    projectsUrl: URI = None
    viewerCanCreateProjects: bool = None

    def project(self, number:int) -> Project:
        """
        Find project by number.
        """
        tmpl = "project(number:%(number)s) %(ret)s"
        return self.wrap(tmpl, fn=True, number=number, ret=Project.F())

    def projects(self, first:int, after:str, last:int, before:str, orderBy:ProjectOrder, search:str, states:ProjectState) -> ProjectConnection:
        """
        A list of projects under the owner.
        """
        tmpl = "projects(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s, search:%(search)s, states:%(states)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, search=search, states=states, ret=ProjectConnection.F())

    def render(self):
        return dict(id=self.id, projectsResourcePath=self.projectsResourcePath, projectsUrl=self.projectsUrl, viewerCanCreateProjects=self.viewerCanCreateProjects)



class Project(node):
    """
    Projects manage issues, pull requests and notes within a project owner.
    """

    body: str = None
    bodyHTML: HTML = None
    closed: bool = None
    closedAt: DateTime = None
    createdAt: DateTime = None
    creator: Actor = None
    databaseId: int = None
    id: ID = None
    name: str = None
    number: int = None
    owner: ProjectOwner = None
    resourcePath: URI = None
    state: ProjectState = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanUpdate: bool = None

    def columns(self, first:int, after:str, last:int, before:str) -> ProjectColumnConnection:
        """
        List of columns in the project
        """
        tmpl = "columns(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ProjectColumnConnection.F())

    def pendingCards(self, first:int, after:str, last:int, before:str) -> ProjectCardConnection:
        """
        List of pending cards in this project
        """
        tmpl = "pendingCards(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ProjectCardConnection.F())

    def render(self):
        return dict(body=self.body, bodyHTML=self.bodyHTML, closed=self.closed, closedAt=self.closedAt, createdAt=self.createdAt, creator=self.creator, databaseId=self.databaseId, id=self.id, name=self.name, number=self.number, owner=self.owner, resourcePath=self.resourcePath, state=self.state, updatedAt=self.updatedAt, url=self.url, viewerCanUpdate=self.viewerCanUpdate)



class Closable(node):
    """
    An object that can be closed
    """

    closed: bool = None
    closedAt: DateTime = None

    def render(self):
        return dict(closed=self.closed, closedAt=self.closedAt)



class DateTime(str):
    """
    An ISO-8601 encoded UTC date string.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "DateTime"


class Updatable(node):
    """
    Entities that can be updated.
    """

    viewerCanUpdate: bool = None

    def render(self):
        return dict(viewerCanUpdate=self.viewerCanUpdate)



class ProjectState(node):
    """
    State of the project; either 'open' or 'closed'
    """

    __enum__ = True
    """
    The project is open.
    """
    OPEN = "OPEN"
    """
    The project is closed.
    """
    CLOSED = "CLOSED"

    def render(self):
        return dict()



class HTML(str):
    """
    A string containing HTML code.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "HTML"


class ProjectColumnConnection(node):
    """
    The connection type for ProjectColumn.
    """

    edges: ProjectColumnEdge = None
    nodes: ProjectColumn = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ProjectColumnEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: ProjectColumn = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ProjectColumn(node):
    """
    A column inside a project.
    """

    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None
    name: str = None
    project: Project = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None

    def cards(self, first:int, after:str, last:int, before:str) -> ProjectCardConnection:
        """
        List of cards in the column
        """
        tmpl = "cards(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ProjectCardConnection.F())

    def render(self):
        return dict(createdAt=self.createdAt, databaseId=self.databaseId, id=self.id, name=self.name, project=self.project, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url)



class ProjectCardConnection(node):
    """
    The connection type for ProjectCard.
    """

    edges: ProjectCardEdge = None
    nodes: ProjectCard = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ProjectCardEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: ProjectCard = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ProjectCard(node):
    """
    A card in a project.
    """

    column: ProjectColumn = None
    content: ProjectCardItem = None
    createdAt: DateTime = None
    creator: Actor = None
    databaseId: int = None
    id: ID = None
    note: str = None
    project: Project = None
    projectColumn: ProjectColumn = None
    resourcePath: URI = None
    state: ProjectCardState = None
    updatedAt: DateTime = None
    url: URI = None

    def render(self):
        return dict(column=self.column, content=self.content, createdAt=self.createdAt, creator=self.creator, databaseId=self.databaseId, id=self.id, note=self.note, project=self.project, projectColumn=self.projectColumn, resourcePath=self.resourcePath, state=self.state, updatedAt=self.updatedAt, url=self.url)



class ProjectCardState(node):
    """
    Various content states of a ProjectCard
    """

    __enum__ = True
    """
    The card has content only.
    """
    CONTENT_ONLY = "CONTENT_ONLY"
    """
    The card has a note only.
    """
    NOTE_ONLY = "NOTE_ONLY"
    """
    The card is redacted.
    """
    REDACTED = "REDACTED"

    def render(self):
        return dict()



class ProjectCardItem(str):
    """
    Types that can be inside Project Cards.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "ProjectCardItem"


class Issue(node):
    """
    An Issue is a place to discuss ideas, enhancements, tasks, and bugs for a project.
    """

    activeLockReason: LockReason = None
    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    body: str = None
    bodyHTML: HTML = None
    bodyText: str = None
    closed: bool = None
    closedAt: DateTime = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    databaseId: int = None
    editor: Actor = None
    id: ID = None
    lastEditedAt: DateTime = None
    locked: bool = None
    milestone: Milestone = None
    number: int = None
    publishedAt: DateTime = None
    reactionGroups: ReactionGroup = None
    repository: Repository = None
    resourcePath: URI = None
    state: IssueState = None
    title: str = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanReact: bool = None
    viewerCanSubscribe: bool = None
    viewerCanUpdate: bool = None
    viewerCannotUpdateReasons: None = None
    viewerDidAuthor: bool = None
    viewerSubscription: SubscriptionState = None

    def assignees(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of Users assigned to this object.
        """
        tmpl = "assignees(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def comments(self, first:int, after:str, last:int, before:str) -> IssueCommentConnection:
        """
        A list of comments associated with the Issue.
        """
        tmpl = "comments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=IssueCommentConnection.F())

    def labels(self, first:int, after:str, last:int, before:str) -> LabelConnection:
        """
        A list of labels associated with the object.
        """
        tmpl = "labels(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=LabelConnection.F())

    def participants(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of Users that are participating in the Issue conversation.
        """
        tmpl = "participants(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def projectCards(self, first:int, after:str, last:int, before:str) -> ProjectCardConnection:
        """
        List of project cards associated with this issue.
        """
        tmpl = "projectCards(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ProjectCardConnection.F())

    def reactions(self, first:int, after:str, last:int, before:str, content:ReactionContent, orderBy:ReactionOrder) -> ReactionConnection:
        """
        A list of Reactions left on the Issue.
        """
        tmpl = "reactions(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, content:%(content)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, content=content, orderBy=orderBy, ret=ReactionConnection.F())

    def timeline(self, first:int, after:str, last:int, before:str, since:DateTime) -> IssueTimelineConnection:
        """
        A list of events, comments, commits, etc. associated with the issue.
        """
        tmpl = "timeline(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, since:%(since)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, since=since, ret=IssueTimelineConnection.F())

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(activeLockReason=self.activeLockReason, author=self.author, authorAssociation=self.authorAssociation, body=self.body, bodyHTML=self.bodyHTML, bodyText=self.bodyText, closed=self.closed, closedAt=self.closedAt, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, databaseId=self.databaseId, editor=self.editor, id=self.id, lastEditedAt=self.lastEditedAt, locked=self.locked, milestone=self.milestone, number=self.number, publishedAt=self.publishedAt, reactionGroups=self.reactionGroups, repository=self.repository, resourcePath=self.resourcePath, state=self.state, title=self.title, updatedAt=self.updatedAt, url=self.url, viewerCanReact=self.viewerCanReact, viewerCanSubscribe=self.viewerCanSubscribe, viewerCanUpdate=self.viewerCanUpdate, viewerCannotUpdateReasons=self.viewerCannotUpdateReasons, viewerDidAuthor=self.viewerDidAuthor, viewerSubscription=self.viewerSubscription)



class Assignable(node):
    """
    An object that can have users assigned to it.
    """


    def assignees(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of Users assigned to this object.
        """
        tmpl = "assignees(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def render(self):
        return dict()



class UserConnection(node):
    """
    The connection type for User.
    """

    edges: UserEdge = None
    nodes: User = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class UserEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: User = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PageInfo(node):
    """
    Information about pagination in a connection.
    """

    endCursor: str = None
    hasNextPage: bool = None
    hasPreviousPage: bool = None
    startCursor: str = None

    def render(self):
        return dict(endCursor=self.endCursor, hasNextPage=self.hasNextPage, hasPreviousPage=self.hasPreviousPage, startCursor=self.startCursor)



class Comment(node):
    """
    Represents a comment.
    """

    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    body: str = None
    bodyHTML: HTML = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    editor: Actor = None
    id: ID = None
    lastEditedAt: DateTime = None
    publishedAt: DateTime = None
    updatedAt: DateTime = None
    viewerDidAuthor: bool = None

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(author=self.author, authorAssociation=self.authorAssociation, body=self.body, bodyHTML=self.bodyHTML, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, editor=self.editor, id=self.id, lastEditedAt=self.lastEditedAt, publishedAt=self.publishedAt, updatedAt=self.updatedAt, viewerDidAuthor=self.viewerDidAuthor)



class UserContentEditConnection(node):
    """
    A list of edits to content.
    """

    edges: UserContentEditEdge = None
    nodes: UserContentEdit = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class UserContentEditEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: UserContentEdit = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class UserContentEdit(node):
    """
    An edit on user content
    """

    createdAt: DateTime = None
    editor: Actor = None
    id: ID = None
    updatedAt: DateTime = None

    def render(self):
        return dict(createdAt=self.createdAt, editor=self.editor, id=self.id, updatedAt=self.updatedAt)



class CommentAuthorAssociation(node):
    """
    A comment author association with repository.
    """

    __enum__ = True
    """
    Author is a member of the organization that owns the repository.
    """
    MEMBER = "MEMBER"
    """
    Author is the owner of the repository.
    """
    OWNER = "OWNER"
    """
    Author has been invited to collaborate on the repository.
    """
    COLLABORATOR = "COLLABORATOR"
    """
    Author has previously committed to the repository.
    """
    CONTRIBUTOR = "CONTRIBUTOR"
    """
    Author has not previously committed to the repository.
    """
    FIRST_TIME_CONTRIBUTOR = "FIRST_TIME_CONTRIBUTOR"
    """
    Author has not previously committed to GitHub.
    """
    FIRST_TIMER = "FIRST_TIMER"
    """
    Author has no association with the repository.
    """
    NONE = "NONE"

    def render(self):
        return dict()



class UpdatableComment(node):
    """
    Comments that can be updated.
    """

    viewerCannotUpdateReasons: None = None

    def render(self):
        return dict(viewerCannotUpdateReasons=self.viewerCannotUpdateReasons)



class CommentCannotUpdateReason(node):
    """
    The possible errors that will prevent a user from updating a comment.
    """

    __enum__ = True
    """
    You must be the author or have write access to this repository to update this comment.
    """
    INSUFFICIENT_ACCESS = "INSUFFICIENT_ACCESS"
    """
    Unable to create comment because issue is locked.
    """
    LOCKED = "LOCKED"
    """
    You must be logged in to update this comment.
    """
    LOGIN_REQUIRED = "LOGIN_REQUIRED"
    """
    Repository is under maintenance.
    """
    MAINTENANCE = "MAINTENANCE"
    """
    At least one email address must be verified to update this comment.
    """
    VERIFIED_EMAIL_REQUIRED = "VERIFIED_EMAIL_REQUIRED"

    def render(self):
        return dict()



class Labelable(node):
    """
    An object that can have labels assigned to it.
    """


    def labels(self, first:int, after:str, last:int, before:str) -> LabelConnection:
        """
        A list of labels associated with the object.
        """
        tmpl = "labels(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=LabelConnection.F())

    def render(self):
        return dict()



class LabelConnection(node):
    """
    The connection type for Label.
    """

    edges: LabelEdge = None
    nodes: Label = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class LabelEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Label = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class Label(node):
    """
    A label for categorizing Issues or Milestones with a given Repository.
    """

    color: str = None
    description: str = None
    id: ID = None
    isDefault: bool = None
    name: str = None
    repository: Repository = None

    def issues(self, first:int, after:str, last:int, before:str, labels:str, orderBy:IssueOrder, states:IssueState) -> IssueConnection:
        """
        A list of issues associated with this label.
        """
        tmpl = "issues(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, labels:%(labels)s, orderBy:%(orderBy)s, states:%(states)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, labels=labels, orderBy=orderBy, states=states, ret=IssueConnection.F())

    def pullRequests(self, first:int, after:str, last:int, before:str, states:PullRequestState, labels:str, headRefName:str, baseRefName:str, orderBy:IssueOrder) -> PullRequestConnection:
        """
        A list of pull requests associated with this label.
        """
        tmpl = "pullRequests(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, states:%(states)s, labels:%(labels)s, headRefName:%(headRefName)s, baseRefName:%(baseRefName)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, states=states, labels=labels, headRefName=headRefName, baseRefName=baseRefName, orderBy=orderBy, ret=PullRequestConnection.F())

    def render(self):
        return dict(color=self.color, description=self.description, id=self.id, isDefault=self.isDefault, name=self.name, repository=self.repository)



class IssueConnection(node):
    """
    The connection type for Issue.
    """

    edges: IssueEdge = None
    nodes: Issue = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class IssueEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Issue = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class IssueOrder(node):
    """
    Ways in which lists of issues can be ordered upon return.
    """

    """
    The direction in which to order issues by the specified field.
    """
    direction: OrderDirection = None
    """
    The field in which to order issues by.
    """
    field: IssueOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class IssueOrderField(node):
    """
    Properties by which issue connections can be ordered.
    """

    __enum__ = True
    """
    Order issues by creation time
    """
    CREATED_AT = "CREATED_AT"
    """
    Order issues by update time
    """
    UPDATED_AT = "UPDATED_AT"
    """
    Order issues by comment count
    """
    COMMENTS = "COMMENTS"

    def render(self):
        return dict()



class OrderDirection(node):
    """
    Possible directions in which to order a list of items when provided an `orderBy` argument.
    """

    __enum__ = True
    """
    Specifies an ascending order for a given `orderBy` argument.
    """
    ASC = "ASC"
    """
    Specifies a descending order for a given `orderBy` argument.
    """
    DESC = "DESC"

    def render(self):
        return dict()



class IssueState(node):
    """
    The possible states of an issue.
    """

    __enum__ = True
    """
    An issue that is still open
    """
    OPEN = "OPEN"
    """
    An issue that has been closed
    """
    CLOSED = "CLOSED"

    def render(self):
        return dict()



class PullRequestConnection(node):
    """
    The connection type for PullRequest.
    """

    edges: PullRequestEdge = None
    nodes: PullRequest = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class PullRequestEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: PullRequest = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PullRequest(node):
    """
    A repository pull request.
    """

    activeLockReason: LockReason = None
    additions: int = None
    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    baseRef: Ref = None
    baseRefName: str = None
    baseRefOid: GitObjectID = None
    body: str = None
    bodyHTML: HTML = None
    bodyText: str = None
    changedFiles: int = None
    closed: bool = None
    closedAt: DateTime = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    databaseId: int = None
    deletions: int = None
    editor: Actor = None
    headRef: Ref = None
    headRefName: str = None
    headRefOid: GitObjectID = None
    headRepository: Repository = None
    headRepositoryOwner: RepositoryOwner = None
    id: ID = None
    isCrossRepository: bool = None
    lastEditedAt: DateTime = None
    locked: bool = None
    mergeCommit: Commit = None
    mergeable: MergeableState = None
    merged: bool = None
    mergedAt: DateTime = None
    milestone: Milestone = None
    number: int = None
    potentialMergeCommit: Commit = None
    publishedAt: DateTime = None
    reactionGroups: ReactionGroup = None
    repository: Repository = None
    resourcePath: URI = None
    revertResourcePath: URI = None
    revertUrl: URI = None
    state: PullRequestState = None
    suggestedReviewers: None = None
    title: str = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanReact: bool = None
    viewerCanSubscribe: bool = None
    viewerCanUpdate: bool = None
    viewerCannotUpdateReasons: None = None
    viewerDidAuthor: bool = None
    viewerSubscription: SubscriptionState = None

    def assignees(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of Users assigned to this object.
        """
        tmpl = "assignees(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def comments(self, first:int, after:str, last:int, before:str) -> IssueCommentConnection:
        """
        A list of comments associated with the pull request.
        """
        tmpl = "comments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=IssueCommentConnection.F())

    def commits(self, first:int, after:str, last:int, before:str) -> PullRequestCommitConnection:
        """
        A list of commits present in this pull request's head branch not present in the base branch.
        """
        tmpl = "commits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=PullRequestCommitConnection.F())

    def labels(self, first:int, after:str, last:int, before:str) -> LabelConnection:
        """
        A list of labels associated with the object.
        """
        tmpl = "labels(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=LabelConnection.F())

    def participants(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of Users that are participating in the Pull Request conversation.
        """
        tmpl = "participants(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def projectCards(self, first:int, after:str, last:int, before:str) -> ProjectCardConnection:
        """
        List of project cards associated with this pull request.
        """
        tmpl = "projectCards(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ProjectCardConnection.F())

    def reactions(self, first:int, after:str, last:int, before:str, content:ReactionContent, orderBy:ReactionOrder) -> ReactionConnection:
        """
        A list of Reactions left on the Issue.
        """
        tmpl = "reactions(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, content:%(content)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, content=content, orderBy=orderBy, ret=ReactionConnection.F())

    def reviewRequests(self, first:int, after:str, last:int, before:str) -> ReviewRequestConnection:
        """
        A list of review requests associated with the pull request.
        """
        tmpl = "reviewRequests(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ReviewRequestConnection.F())

    def reviews(self, first:int, after:str, last:int, before:str, states:PullRequestReviewState, author:str) -> PullRequestReviewConnection:
        """
        A list of reviews associated with the pull request.
        """
        tmpl = "reviews(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, states:%(states)s, author:%(author)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, states=states, author=author, ret=PullRequestReviewConnection.F())

    def timeline(self, first:int, after:str, last:int, before:str, since:DateTime) -> PullRequestTimelineConnection:
        """
        A list of events, comments, commits, etc. associated with the pull request.
        """
        tmpl = "timeline(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, since:%(since)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, since=since, ret=PullRequestTimelineConnection.F())

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(activeLockReason=self.activeLockReason, additions=self.additions, author=self.author, authorAssociation=self.authorAssociation, baseRef=self.baseRef, baseRefName=self.baseRefName, baseRefOid=self.baseRefOid, body=self.body, bodyHTML=self.bodyHTML, bodyText=self.bodyText, changedFiles=self.changedFiles, closed=self.closed, closedAt=self.closedAt, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, databaseId=self.databaseId, deletions=self.deletions, editor=self.editor, headRef=self.headRef, headRefName=self.headRefName, headRefOid=self.headRefOid, headRepository=self.headRepository, headRepositoryOwner=self.headRepositoryOwner, id=self.id, isCrossRepository=self.isCrossRepository, lastEditedAt=self.lastEditedAt, locked=self.locked, mergeCommit=self.mergeCommit, mergeable=self.mergeable, merged=self.merged, mergedAt=self.mergedAt, milestone=self.milestone, number=self.number, potentialMergeCommit=self.potentialMergeCommit, publishedAt=self.publishedAt, reactionGroups=self.reactionGroups, repository=self.repository, resourcePath=self.resourcePath, revertResourcePath=self.revertResourcePath, revertUrl=self.revertUrl, state=self.state, suggestedReviewers=self.suggestedReviewers, title=self.title, updatedAt=self.updatedAt, url=self.url, viewerCanReact=self.viewerCanReact, viewerCanSubscribe=self.viewerCanSubscribe, viewerCanUpdate=self.viewerCanUpdate, viewerCannotUpdateReasons=self.viewerCannotUpdateReasons, viewerDidAuthor=self.viewerDidAuthor, viewerSubscription=self.viewerSubscription)



class Lockable(node):
    """
    An object that can be locked.
    """

    activeLockReason: LockReason = None
    locked: bool = None

    def render(self):
        return dict(activeLockReason=self.activeLockReason, locked=self.locked)



class LockReason(node):
    """
    The possible reasons that an issue or pull request was locked.
    """

    __enum__ = True
    """
    The issue or pull request was locked because the conversation was off-topic.
    """
    OFF_TOPIC = "OFF_TOPIC"
    """
    The issue or pull request was locked because the conversation was too heated.
    """
    TOO_HEATED = "TOO_HEATED"
    """
    The issue or pull request was locked because the conversation was resolved.
    """
    RESOLVED = "RESOLVED"
    """
    The issue or pull request was locked because the conversation was spam.
    """
    SPAM = "SPAM"

    def render(self):
        return dict()



class Reactable(node):
    """
    Represents a subject that can be reacted on.
    """

    databaseId: int = None
    id: ID = None
    reactionGroups: ReactionGroup = None
    viewerCanReact: bool = None

    def reactions(self, first:int, after:str, last:int, before:str, content:ReactionContent, orderBy:ReactionOrder) -> ReactionConnection:
        """
        A list of Reactions left on the Issue.
        """
        tmpl = "reactions(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, content:%(content)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, content=content, orderBy=orderBy, ret=ReactionConnection.F())

    def render(self):
        return dict(databaseId=self.databaseId, id=self.id, reactionGroups=self.reactionGroups, viewerCanReact=self.viewerCanReact)



class ReactionGroup(node):
    """
    A group of emoji reactions to a particular piece of content.
    """

    content: ReactionContent = None
    createdAt: DateTime = None
    subject: Reactable = None
    viewerHasReacted: bool = None

    def users(self, first:int, after:str, last:int, before:str) -> ReactingUserConnection:
        """
        Users who have reacted to the reaction subject with the emotion represented by this reaction group
        """
        tmpl = "users(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ReactingUserConnection.F())

    def render(self):
        return dict(content=self.content, createdAt=self.createdAt, subject=self.subject, viewerHasReacted=self.viewerHasReacted)



class ReactionContent(node):
    """
    Emojis that can be attached to Issues, Pull Requests and Comments.
    """

    __enum__ = True
    """
    Represents the 👍 emoji.
    """
    THUMBS_UP = "THUMBS_UP"
    """
    Represents the 👎 emoji.
    """
    THUMBS_DOWN = "THUMBS_DOWN"
    """
    Represents the 😄 emoji.
    """
    LAUGH = "LAUGH"
    """
    Represents the 🎉 emoji.
    """
    HOORAY = "HOORAY"
    """
    Represents the 😕 emoji.
    """
    CONFUSED = "CONFUSED"
    """
    Represents the ❤️ emoji.
    """
    HEART = "HEART"

    def render(self):
        return dict()



class ReactingUserConnection(node):
    """
    The connection type for User.
    """

    edges: ReactingUserEdge = None
    nodes: User = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ReactingUserEdge(node):
    """
    Represents a user that's made a reaction.
    """

    cursor: str = None
    node: User = None
    reactedAt: DateTime = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node, reactedAt=self.reactedAt)



class ReactionConnection(node):
    """
    A list of reactions that have been left on the subject.
    """

    edges: ReactionEdge = None
    nodes: Reaction = None
    pageInfo: PageInfo = None
    totalCount: int = None
    viewerHasReacted: bool = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount, viewerHasReacted=self.viewerHasReacted)



class ReactionEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Reaction = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class Reaction(node):
    """
    An emoji reaction to a particular piece of content.
    """

    content: ReactionContent = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None
    reactable: Reactable = None
    user: User = None

    def render(self):
        return dict(content=self.content, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id, reactable=self.reactable, user=self.user)



class ReactionOrder(node):
    """
    Ways in which lists of reactions can be ordered upon return.
    """

    """
    The direction in which to order reactions by the specified field.
    """
    direction: OrderDirection = None
    """
    The field in which to order reactions by.
    """
    field: ReactionOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class ReactionOrderField(node):
    """
    A list of fields that reactions can be ordered by.
    """

    __enum__ = True
    """
    Allows ordering a list of reactions by when they were created.
    """
    CREATED_AT = "CREATED_AT"

    def render(self):
        return dict()



class RepositoryNode(node):
    """
    Represents a object that belongs to a repository.
    """

    repository: Repository = None

    def render(self):
        return dict(repository=self.repository)



class Subscribable(node):
    """
    Entities that can be subscribed to for web and email notifications.
    """

    id: ID = None
    viewerCanSubscribe: bool = None
    viewerSubscription: SubscriptionState = None

    def render(self):
        return dict(id=self.id, viewerCanSubscribe=self.viewerCanSubscribe, viewerSubscription=self.viewerSubscription)



class SubscriptionState(node):
    """
    The possible states of a subscription.
    """

    __enum__ = True
    """
    The User is only notified when particpating or @mentioned.
    """
    UNSUBSCRIBED = "UNSUBSCRIBED"
    """
    The User is notified of all conversations.
    """
    SUBSCRIBED = "SUBSCRIBED"
    """
    The User is never notified.
    """
    IGNORED = "IGNORED"
    """
    Subscriptions are currently unavailable
    """
    UNAVAILABLE = "UNAVAILABLE"

    def render(self):
        return dict()



class Ref(node):
    """
    Represents a Git reference.
    """

    id: ID = None
    name: str = None
    prefix: str = None
    repository: Repository = None
    target: GitObject = None

    def associatedPullRequests(self, first:int, after:str, last:int, before:str, states:PullRequestState, labels:str, headRefName:str, baseRefName:str, orderBy:IssueOrder) -> PullRequestConnection:
        """
        A list of pull requests with this ref as the head ref.
        """
        tmpl = "associatedPullRequests(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, states:%(states)s, labels:%(labels)s, headRefName:%(headRefName)s, baseRefName:%(baseRefName)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, states=states, labels=labels, headRefName=headRefName, baseRefName=baseRefName, orderBy=orderBy, ret=PullRequestConnection.F())

    def render(self):
        return dict(id=self.id, name=self.name, prefix=self.prefix, repository=self.repository, target=self.target)



class GitObject(node):
    """
    Represents a Git object.
    """

    abbreviatedOid: str = None
    commitResourcePath: URI = None
    commitUrl: URI = None
    id: ID = None
    oid: GitObjectID = None
    repository: Repository = None

    def render(self):
        return dict(abbreviatedOid=self.abbreviatedOid, commitResourcePath=self.commitResourcePath, commitUrl=self.commitUrl, id=self.id, oid=self.oid, repository=self.repository)



class GitObjectID(str):
    """
    A Git object ID.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "GitObjectID"


class Blob(node):
    """
    Represents a Git blob.
    """

    abbreviatedOid: str = None
    byteSize: int = None
    commitResourcePath: URI = None
    commitUrl: URI = None
    id: ID = None
    isBinary: bool = None
    isTruncated: bool = None
    oid: GitObjectID = None
    repository: Repository = None
    text: str = None

    def render(self):
        return dict(abbreviatedOid=self.abbreviatedOid, byteSize=self.byteSize, commitResourcePath=self.commitResourcePath, commitUrl=self.commitUrl, id=self.id, isBinary=self.isBinary, isTruncated=self.isTruncated, oid=self.oid, repository=self.repository, text=self.text)



class Commit(node):
    """
    Represents a Git commit.
    """

    abbreviatedOid: str = None
    additions: int = None
    author: GitActor = None
    authoredByCommitter: bool = None
    authoredDate: DateTime = None
    changedFiles: int = None
    commitResourcePath: URI = None
    commitUrl: URI = None
    committedDate: DateTime = None
    committedViaWeb: bool = None
    committer: GitActor = None
    deletions: int = None
    id: ID = None
    message: str = None
    messageBody: str = None
    messageBodyHTML: HTML = None
    messageHeadline: str = None
    messageHeadlineHTML: HTML = None
    oid: GitObjectID = None
    pushedDate: DateTime = None
    repository: Repository = None
    resourcePath: URI = None
    signature: GitSignature = None
    status: Status = None
    tarballUrl: URI = None
    tree: Tree = None
    treeResourcePath: URI = None
    treeUrl: URI = None
    url: URI = None
    viewerCanSubscribe: bool = None
    viewerSubscription: SubscriptionState = None
    zipballUrl: URI = None

    def blame(self, path:str) -> Blame:
        """
        Fetches `git blame` information.
        """
        tmpl = "blame(path:%(path)s) %(ret)s"
        return self.wrap(tmpl, fn=True, path=path, ret=Blame.F())

    def comments(self, first:int, after:str, last:int, before:str) -> CommitCommentConnection:
        """
        Comments made on the commit.
        """
        tmpl = "comments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=CommitCommentConnection.F())

    def history(self, first:int, after:str, last:int, before:str, path:str, author:CommitAuthor, since:GitTimestamp, until:GitTimestamp) -> CommitHistoryConnection:
        """
        The linear commit history starting from (and including) this commit, in the same order as `git log`.
        """
        tmpl = "history(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, path:%(path)s, author:%(author)s, since:%(since)s, until:%(until)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, path=path, author=author, since=since, until=until, ret=CommitHistoryConnection.F())

    def parents(self, first:int, after:str, last:int, before:str) -> CommitConnection:
        """
        The parents of a commit.
        """
        tmpl = "parents(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=CommitConnection.F())

    def render(self):
        return dict(abbreviatedOid=self.abbreviatedOid, additions=self.additions, author=self.author, authoredByCommitter=self.authoredByCommitter, authoredDate=self.authoredDate, changedFiles=self.changedFiles, commitResourcePath=self.commitResourcePath, commitUrl=self.commitUrl, committedDate=self.committedDate, committedViaWeb=self.committedViaWeb, committer=self.committer, deletions=self.deletions, id=self.id, message=self.message, messageBody=self.messageBody, messageBodyHTML=self.messageBodyHTML, messageHeadline=self.messageHeadline, messageHeadlineHTML=self.messageHeadlineHTML, oid=self.oid, pushedDate=self.pushedDate, repository=self.repository, resourcePath=self.resourcePath, signature=self.signature, status=self.status, tarballUrl=self.tarballUrl, tree=self.tree, treeResourcePath=self.treeResourcePath, treeUrl=self.treeUrl, url=self.url, viewerCanSubscribe=self.viewerCanSubscribe, viewerSubscription=self.viewerSubscription, zipballUrl=self.zipballUrl)



class Tree(node):
    """
    Represents a Git tree.
    """

    abbreviatedOid: str = None
    commitResourcePath: URI = None
    commitUrl: URI = None
    entries: TreeEntry = None
    id: ID = None
    oid: GitObjectID = None
    repository: Repository = None

    def render(self):
        return dict(abbreviatedOid=self.abbreviatedOid, commitResourcePath=self.commitResourcePath, commitUrl=self.commitUrl, entries=self.entries, id=self.id, oid=self.oid, repository=self.repository)



class TreeEntry(node):
    """
    Represents a Git tree entry.
    """

    mode: int = None
    name: str = None
    object: GitObject = None
    oid: GitObjectID = None
    repository: Repository = None
    type: str = None

    def render(self):
        return dict(mode=self.mode, name=self.name, object=self.object, oid=self.oid, repository=self.repository, type=self.type)



class GitActor(node):
    """
    Represents an actor in a Git commit (ie. an author or committer).
    """

    date: GitTimestamp = None
    email: str = None
    name: str = None
    user: User = None

    def avatarUrl(self, size:int) -> URI:
        """
        A URL pointing to the author's public avatar.
        """
        tmpl = "avatarUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def render(self):
        return dict(date=self.date, email=self.email, name=self.name, user=self.user)



class GitTimestamp(str):
    """
    An ISO-8601 encoded date string. Unlike the DateTime type, GitTimestamp is not converted in UTC.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "GitTimestamp"


class CommitConnection(node):
    """
    The connection type for Commit.
    """

    edges: CommitEdge = None
    nodes: Commit = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class CommitEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Commit = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class CommitHistoryConnection(node):
    """
    The connection type for Commit.
    """

    edges: CommitEdge = None
    nodes: Commit = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class CommitAuthor(node):
    """
    Specifies an author for filtering Git commits.
    """

    """
    Email addresses to filter by. Commits authored by any of the specified email addresses will be returned.
    """
    emails: str = None
    """
    ID of a User to filter by. If non-null, only commits authored by this user will be returned. This field takes precedence over emails.
    """
    id: ID = None

    def render(self):
        return dict(emails=self.emails, id=self.id)



class CommitCommentConnection(node):
    """
    The connection type for CommitComment.
    """

    edges: CommitCommentEdge = None
    nodes: CommitComment = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class CommitCommentEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: CommitComment = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class CommitComment(node):
    """
    Represents a comment on a given Commit.
    """

    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    body: str = None
    bodyHTML: HTML = None
    commit: Commit = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    databaseId: int = None
    editor: Actor = None
    id: ID = None
    lastEditedAt: DateTime = None
    path: str = None
    position: int = None
    publishedAt: DateTime = None
    reactionGroups: ReactionGroup = None
    repository: Repository = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanDelete: bool = None
    viewerCanReact: bool = None
    viewerCanUpdate: bool = None
    viewerCannotUpdateReasons: None = None
    viewerDidAuthor: bool = None

    def reactions(self, first:int, after:str, last:int, before:str, content:ReactionContent, orderBy:ReactionOrder) -> ReactionConnection:
        """
        A list of Reactions left on the Issue.
        """
        tmpl = "reactions(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, content:%(content)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, content=content, orderBy=orderBy, ret=ReactionConnection.F())

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(author=self.author, authorAssociation=self.authorAssociation, body=self.body, bodyHTML=self.bodyHTML, commit=self.commit, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, databaseId=self.databaseId, editor=self.editor, id=self.id, lastEditedAt=self.lastEditedAt, path=self.path, position=self.position, publishedAt=self.publishedAt, reactionGroups=self.reactionGroups, repository=self.repository, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url, viewerCanDelete=self.viewerCanDelete, viewerCanReact=self.viewerCanReact, viewerCanUpdate=self.viewerCanUpdate, viewerCannotUpdateReasons=self.viewerCannotUpdateReasons, viewerDidAuthor=self.viewerDidAuthor)



class Deletable(node):
    """
    Entities that can be deleted.
    """

    viewerCanDelete: bool = None

    def render(self):
        return dict(viewerCanDelete=self.viewerCanDelete)



class GitSignature(node):
    """
    Information about a signature (GPG or S/MIME) on a Commit or Tag.
    """

    email: str = None
    isValid: bool = None
    payload: str = None
    signature: str = None
    signer: User = None
    state: GitSignatureState = None

    def render(self):
        return dict(email=self.email, isValid=self.isValid, payload=self.payload, signature=self.signature, signer=self.signer, state=self.state)



class GitSignatureState(node):
    """
    The state of a Git signature.
    """

    __enum__ = True
    """
    Valid signature and verified by GitHub.
    """
    VALID = "VALID"
    """
    Invalid signature.
    """
    INVALID = "INVALID"
    """
    Malformed signature.
    """
    MALFORMED_SIG = "MALFORMED_SIG"
    """
    Key used for signing not known to GitHub.
    """
    UNKNOWN_KEY = "UNKNOWN_KEY"
    """
    Invalid email used for signing.
    """
    BAD_EMAIL = "BAD_EMAIL"
    """
    Email used for signing unverified on GitHub.
    """
    UNVERIFIED_EMAIL = "UNVERIFIED_EMAIL"
    """
    Email used for signing not known to GitHub.
    """
    NO_USER = "NO_USER"
    """
    Unknown signature type.
    """
    UNKNOWN_SIG_TYPE = "UNKNOWN_SIG_TYPE"
    """
    Unsigned.
    """
    UNSIGNED = "UNSIGNED"
    """
    Internal error - the GPG verification service is unavailable at the moment.
    """
    GPGVERIFY_UNAVAILABLE = "GPGVERIFY_UNAVAILABLE"
    """
    Internal error - the GPG verification service misbehaved.
    """
    GPGVERIFY_ERROR = "GPGVERIFY_ERROR"
    """
    The usage flags for the key that signed this don't allow signing.
    """
    NOT_SIGNING_KEY = "NOT_SIGNING_KEY"
    """
    Signing key expired.
    """
    EXPIRED_KEY = "EXPIRED_KEY"

    def render(self):
        return dict()



class Status(node):
    """
    Represents a commit status.
    """

    commit: Commit = None
    contexts: None = None
    id: ID = None
    state: StatusState = None

    def context(self, name:str) -> StatusContext:
        """
        Looks up an individual status context by context name.
        """
        tmpl = "context(name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, name=name, ret=StatusContext.F())

    def render(self):
        return dict(commit=self.commit, contexts=self.contexts, id=self.id, state=self.state)



class StatusState(node):
    """
    The possible commit status states.
    """

    __enum__ = True
    """
    Status is expected.
    """
    EXPECTED = "EXPECTED"
    """
    Status is errored.
    """
    ERROR = "ERROR"
    """
    Status is failing.
    """
    FAILURE = "FAILURE"
    """
    Status is pending.
    """
    PENDING = "PENDING"
    """
    Status is successful.
    """
    SUCCESS = "SUCCESS"

    def render(self):
        return dict()



class StatusContext(node):
    """
    Represents an individual commit status context
    """

    commit: Commit = None
    context: str = None
    createdAt: DateTime = None
    creator: Actor = None
    description: str = None
    id: ID = None
    state: StatusState = None
    targetUrl: URI = None

    def render(self):
        return dict(commit=self.commit, context=self.context, createdAt=self.createdAt, creator=self.creator, description=self.description, id=self.id, state=self.state, targetUrl=self.targetUrl)



class Blame(node):
    """
    Represents a Git blame.
    """

    ranges: None = None

    def render(self):
        return dict(ranges=self.ranges)



class BlameRange(node):
    """
    Represents a range of information from a Git blame.
    """

    age: int = None
    commit: Commit = None
    endingLine: int = None
    startingLine: int = None

    def render(self):
        return dict(age=self.age, commit=self.commit, endingLine=self.endingLine, startingLine=self.startingLine)



class PullRequestState(node):
    """
    The possible states of a pull request.
    """

    __enum__ = True
    """
    A pull request that is still open.
    """
    OPEN = "OPEN"
    """
    A pull request that has been closed without being merged.
    """
    CLOSED = "CLOSED"
    """
    A pull request that has been closed by being merged.
    """
    MERGED = "MERGED"

    def render(self):
        return dict()



class RepositoryOwner(node):
    """
    Represents an owner of a Repository.
    """

    id: ID = None
    login: str = None
    resourcePath: URI = None
    url: URI = None

    def avatarUrl(self, size:int) -> URI:
        """
        A URL pointing to the owner's public avatar.
        """
        tmpl = "avatarUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def pinnedRepositories(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool) -> RepositoryConnection:
        """
        A list of repositories this user has pinned to their profile
        """
        tmpl = "pinnedRepositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, ret=RepositoryConnection.F())

    def repositories(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool, isFork:bool) -> RepositoryConnection:
        """
        A list of repositories that the user owns.
        """
        tmpl = "repositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s, isFork:%(isFork)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, isFork=isFork, ret=RepositoryConnection.F())

    def repository(self, name:str) -> Repository:
        """
        Find Repository.
        """
        tmpl = "repository(name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, name=name, ret=Repository.F())

    def render(self):
        return dict(id=self.id, login=self.login, resourcePath=self.resourcePath, url=self.url)



class RepositoryConnection(node):
    """
    A list of repositories owned by the subject.
    """

    edges: RepositoryEdge = None
    nodes: Repository = None
    pageInfo: PageInfo = None
    totalCount: int = None
    totalDiskUsage: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount, totalDiskUsage=self.totalDiskUsage)



class RepositoryEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Repository = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class RepositoryPrivacy(node):
    """
    The privacy of a repository
    """

    __enum__ = True
    """
    Public
    """
    PUBLIC = "PUBLIC"
    """
    Private
    """
    PRIVATE = "PRIVATE"

    def render(self):
        return dict()



class RepositoryOrder(node):
    """
    Ordering options for repository connections
    """

    """
    The ordering direction.
    """
    direction: OrderDirection = None
    """
    The field to order repositories by.
    """
    field: RepositoryOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class RepositoryOrderField(node):
    """
    Properties by which repository connections can be ordered.
    """

    __enum__ = True
    """
    Order repositories by creation time
    """
    CREATED_AT = "CREATED_AT"
    """
    Order repositories by update time
    """
    UPDATED_AT = "UPDATED_AT"
    """
    Order repositories by push time
    """
    PUSHED_AT = "PUSHED_AT"
    """
    Order repositories by name
    """
    NAME = "NAME"
    """
    Order repositories by number of stargazers
    """
    STARGAZERS = "STARGAZERS"

    def render(self):
        return dict()



class RepositoryAffiliation(node):
    """
    The affiliation of a user to a repository
    """

    __enum__ = True
    """
    Repositories that are owned by the authenticated user.
    """
    OWNER = "OWNER"
    """
    Repositories that the user has been added to as a collaborator.
    """
    COLLABORATOR = "COLLABORATOR"
    """
    Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on.
    """
    ORGANIZATION_MEMBER = "ORGANIZATION_MEMBER"

    def render(self):
        return dict()



class Milestone(node):
    """
    Represents a Milestone object on a given repository.
    """

    closed: bool = None
    closedAt: DateTime = None
    createdAt: DateTime = None
    creator: Actor = None
    description: str = None
    dueOn: DateTime = None
    id: ID = None
    number: int = None
    repository: Repository = None
    resourcePath: URI = None
    state: MilestoneState = None
    title: str = None
    updatedAt: DateTime = None
    url: URI = None

    def issues(self, first:int, after:str, last:int, before:str, labels:str, orderBy:IssueOrder, states:IssueState) -> IssueConnection:
        """
        A list of issues associated with the milestone.
        """
        tmpl = "issues(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, labels:%(labels)s, orderBy:%(orderBy)s, states:%(states)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, labels=labels, orderBy=orderBy, states=states, ret=IssueConnection.F())

    def pullRequests(self, first:int, after:str, last:int, before:str, states:PullRequestState, labels:str, headRefName:str, baseRefName:str, orderBy:IssueOrder) -> PullRequestConnection:
        """
        A list of pull requests associated with the milestone.
        """
        tmpl = "pullRequests(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, states:%(states)s, labels:%(labels)s, headRefName:%(headRefName)s, baseRefName:%(baseRefName)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, states=states, labels=labels, headRefName=headRefName, baseRefName=baseRefName, orderBy=orderBy, ret=PullRequestConnection.F())

    def render(self):
        return dict(closed=self.closed, closedAt=self.closedAt, createdAt=self.createdAt, creator=self.creator, description=self.description, dueOn=self.dueOn, id=self.id, number=self.number, repository=self.repository, resourcePath=self.resourcePath, state=self.state, title=self.title, updatedAt=self.updatedAt, url=self.url)



class MilestoneState(node):
    """
    The possible states of a milestone.
    """

    __enum__ = True
    """
    A milestone that is still open.
    """
    OPEN = "OPEN"
    """
    A milestone that has been closed.
    """
    CLOSED = "CLOSED"

    def render(self):
        return dict()



class MergeableState(node):
    """
    Whether or not a PullRequest can be merged.
    """

    __enum__ = True
    """
    The pull request can be merged.
    """
    MERGEABLE = "MERGEABLE"
    """
    The pull request cannot be merged due to merge conflicts.
    """
    CONFLICTING = "CONFLICTING"
    """
    The mergeability of the pull request is still being calculated.
    """
    UNKNOWN = "UNKNOWN"

    def render(self):
        return dict()



class IssueCommentConnection(node):
    """
    The connection type for IssueComment.
    """

    edges: IssueCommentEdge = None
    nodes: IssueComment = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class IssueCommentEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: IssueComment = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class IssueComment(node):
    """
    Represents a comment on an Issue.
    """

    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    body: str = None
    bodyHTML: HTML = None
    bodyText: str = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    databaseId: int = None
    editor: Actor = None
    id: ID = None
    issue: Issue = None
    lastEditedAt: DateTime = None
    publishedAt: DateTime = None
    pullRequest: PullRequest = None
    reactionGroups: ReactionGroup = None
    repository: Repository = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanDelete: bool = None
    viewerCanReact: bool = None
    viewerCanUpdate: bool = None
    viewerCannotUpdateReasons: None = None
    viewerDidAuthor: bool = None

    def reactions(self, first:int, after:str, last:int, before:str, content:ReactionContent, orderBy:ReactionOrder) -> ReactionConnection:
        """
        A list of Reactions left on the Issue.
        """
        tmpl = "reactions(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, content:%(content)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, content=content, orderBy=orderBy, ret=ReactionConnection.F())

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(author=self.author, authorAssociation=self.authorAssociation, body=self.body, bodyHTML=self.bodyHTML, bodyText=self.bodyText, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, databaseId=self.databaseId, editor=self.editor, id=self.id, issue=self.issue, lastEditedAt=self.lastEditedAt, publishedAt=self.publishedAt, pullRequest=self.pullRequest, reactionGroups=self.reactionGroups, repository=self.repository, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url, viewerCanDelete=self.viewerCanDelete, viewerCanReact=self.viewerCanReact, viewerCanUpdate=self.viewerCanUpdate, viewerCannotUpdateReasons=self.viewerCannotUpdateReasons, viewerDidAuthor=self.viewerDidAuthor)



class IssuePubSubTopic(node):
    """
    The possible PubSub channels for an issue.
    """

    __enum__ = True
    """
    The channel ID for observing issue updates.
    """
    UPDATED = "UPDATED"
    """
    The channel ID for marking an issue as read.
    """
    MARKASREAD = "MARKASREAD"

    def render(self):
        return dict()



class PullRequestReviewConnection(node):
    """
    The connection type for PullRequestReview.
    """

    edges: PullRequestReviewEdge = None
    nodes: PullRequestReview = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class PullRequestReviewEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: PullRequestReview = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PullRequestReview(node):
    """
    A review object for a given pull request.
    """

    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    body: str = None
    bodyHTML: HTML = None
    bodyText: str = None
    commit: Commit = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    databaseId: int = None
    editor: Actor = None
    id: ID = None
    lastEditedAt: DateTime = None
    publishedAt: DateTime = None
    pullRequest: PullRequest = None
    repository: Repository = None
    resourcePath: URI = None
    state: PullRequestReviewState = None
    submittedAt: DateTime = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanDelete: bool = None
    viewerCanUpdate: bool = None
    viewerCannotUpdateReasons: None = None
    viewerDidAuthor: bool = None

    def comments(self, first:int, after:str, last:int, before:str) -> PullRequestReviewCommentConnection:
        """
        A list of review comments for the current pull request review.
        """
        tmpl = "comments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=PullRequestReviewCommentConnection.F())

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(author=self.author, authorAssociation=self.authorAssociation, body=self.body, bodyHTML=self.bodyHTML, bodyText=self.bodyText, commit=self.commit, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, databaseId=self.databaseId, editor=self.editor, id=self.id, lastEditedAt=self.lastEditedAt, publishedAt=self.publishedAt, pullRequest=self.pullRequest, repository=self.repository, resourcePath=self.resourcePath, state=self.state, submittedAt=self.submittedAt, updatedAt=self.updatedAt, url=self.url, viewerCanDelete=self.viewerCanDelete, viewerCanUpdate=self.viewerCanUpdate, viewerCannotUpdateReasons=self.viewerCannotUpdateReasons, viewerDidAuthor=self.viewerDidAuthor)



class PullRequestReviewState(node):
    """
    The possible states of a pull request review.
    """

    __enum__ = True
    """
    A review that has not yet been submitted.
    """
    PENDING = "PENDING"
    """
    An informational review.
    """
    COMMENTED = "COMMENTED"
    """
    A review allowing the pull request to merge.
    """
    APPROVED = "APPROVED"
    """
    A review blocking the pull request from merging.
    """
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    """
    A review that has been dismissed.
    """
    DISMISSED = "DISMISSED"

    def render(self):
        return dict()



class PullRequestReviewCommentConnection(node):
    """
    The connection type for PullRequestReviewComment.
    """

    edges: PullRequestReviewCommentEdge = None
    nodes: PullRequestReviewComment = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class PullRequestReviewCommentEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: PullRequestReviewComment = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PullRequestReviewComment(node):
    """
    A review comment associated with a given repository pull request.
    """

    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    body: str = None
    bodyHTML: HTML = None
    bodyText: str = None
    commit: Commit = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    databaseId: int = None
    diffHunk: str = None
    draftedAt: DateTime = None
    editor: Actor = None
    id: ID = None
    lastEditedAt: DateTime = None
    originalCommit: Commit = None
    originalPosition: int = None
    path: str = None
    position: int = None
    publishedAt: DateTime = None
    pullRequest: PullRequest = None
    pullRequestReview: PullRequestReview = None
    reactionGroups: ReactionGroup = None
    replyTo: PullRequestReviewComment = None
    repository: Repository = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanDelete: bool = None
    viewerCanReact: bool = None
    viewerCanUpdate: bool = None
    viewerCannotUpdateReasons: None = None
    viewerDidAuthor: bool = None

    def reactions(self, first:int, after:str, last:int, before:str, content:ReactionContent, orderBy:ReactionOrder) -> ReactionConnection:
        """
        A list of Reactions left on the Issue.
        """
        tmpl = "reactions(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, content:%(content)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, content=content, orderBy=orderBy, ret=ReactionConnection.F())

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(author=self.author, authorAssociation=self.authorAssociation, body=self.body, bodyHTML=self.bodyHTML, bodyText=self.bodyText, commit=self.commit, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, databaseId=self.databaseId, diffHunk=self.diffHunk, draftedAt=self.draftedAt, editor=self.editor, id=self.id, lastEditedAt=self.lastEditedAt, originalCommit=self.originalCommit, originalPosition=self.originalPosition, path=self.path, position=self.position, publishedAt=self.publishedAt, pullRequest=self.pullRequest, pullRequestReview=self.pullRequestReview, reactionGroups=self.reactionGroups, replyTo=self.replyTo, repository=self.repository, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url, viewerCanDelete=self.viewerCanDelete, viewerCanReact=self.viewerCanReact, viewerCanUpdate=self.viewerCanUpdate, viewerCannotUpdateReasons=self.viewerCannotUpdateReasons, viewerDidAuthor=self.viewerDidAuthor)



class PullRequestPubSubTopic(node):
    """
    The possible PubSub channels for a pull request.
    """

    __enum__ = True
    """
    The channel ID for observing pull request updates.
    """
    UPDATED = "UPDATED"
    """
    The channel ID for marking an pull request as read.
    """
    MARKASREAD = "MARKASREAD"
    """
    The channel ID for observing head ref updates.
    """
    HEAD_REF = "HEAD_REF"

    def render(self):
        return dict()



class PullRequestReviewThread(node):
    """
    A threaded list of comments for a given pull request.
    """

    id: ID = None
    pullRequest: PullRequest = None
    repository: Repository = None

    def comments(self, first:int, after:str, last:int, before:str) -> PullRequestReviewCommentConnection:
        """
        A list of pull request comments associated with the thread.
        """
        tmpl = "comments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=PullRequestReviewCommentConnection.F())

    def render(self):
        return dict(id=self.id, pullRequest=self.pullRequest, repository=self.repository)



class TeamConnection(node):
    """
    The connection type for Team.
    """

    edges: TeamEdge = None
    nodes: Team = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class TeamEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Team = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class Team(node):
    """
    A team of users in an organization.
    """

    combinedSlug: str = None
    createdAt: DateTime = None
    description: str = None
    editTeamResourcePath: URI = None
    editTeamUrl: URI = None
    id: ID = None
    membersResourcePath: URI = None
    membersUrl: URI = None
    name: str = None
    newTeamResourcePath: URI = None
    newTeamUrl: URI = None
    organization: Organization = None
    parentTeam: Team = None
    privacy: TeamPrivacy = None
    repositoriesResourcePath: URI = None
    repositoriesUrl: URI = None
    resourcePath: URI = None
    slug: str = None
    teamsResourcePath: URI = None
    teamsUrl: URI = None
    updatedAt: DateTime = None
    url: URI = None
    viewerCanAdminister: bool = None
    viewerCanSubscribe: bool = None
    viewerSubscription: SubscriptionState = None

    def ancestors(self, first:int, after:str, last:int, before:str) -> TeamConnection:
        """
        A list of teams that are ancestors of this team.
        """
        tmpl = "ancestors(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=TeamConnection.F())

    def avatarUrl(self, size:int) -> URI:
        """
        A URL pointing to the team's avatar.
        """
        tmpl = "avatarUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def childTeams(self, first:int, after:str, last:int, before:str, orderBy:TeamOrder, userLogins:str, immediateOnly:bool) -> TeamConnection:
        """
        List of child teams belonging to this team
        """
        tmpl = "childTeams(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s, userLogins:%(userLogins)s, immediateOnly:%(immediateOnly)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, userLogins=userLogins, immediateOnly=immediateOnly, ret=TeamConnection.F())

    def invitations(self, first:int, after:str, last:int, before:str) -> OrganizationInvitationConnection:
        """
        A list of pending invitations for users to this team
        """
        tmpl = "invitations(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=OrganizationInvitationConnection.F())

    def members(self, first:int, after:str, last:int, before:str, query:str, membership:TeamMembershipType, role:TeamMemberRole) -> TeamMemberConnection:
        """
        A list of users who are members of this team.
        """
        tmpl = "members(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, query:%(query)s, membership:%(membership)s, role:%(role)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, query=query, membership=membership, role=role, ret=TeamMemberConnection.F())

    def repositories(self, first:int, after:str, last:int, before:str, query:str, orderBy:TeamRepositoryOrder) -> TeamRepositoryConnection:
        """
        A list of repositories this team has access to.
        """
        tmpl = "repositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, query:%(query)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, query=query, orderBy=orderBy, ret=TeamRepositoryConnection.F())

    def render(self):
        return dict(combinedSlug=self.combinedSlug, createdAt=self.createdAt, description=self.description, editTeamResourcePath=self.editTeamResourcePath, editTeamUrl=self.editTeamUrl, id=self.id, membersResourcePath=self.membersResourcePath, membersUrl=self.membersUrl, name=self.name, newTeamResourcePath=self.newTeamResourcePath, newTeamUrl=self.newTeamUrl, organization=self.organization, parentTeam=self.parentTeam, privacy=self.privacy, repositoriesResourcePath=self.repositoriesResourcePath, repositoriesUrl=self.repositoriesUrl, resourcePath=self.resourcePath, slug=self.slug, teamsResourcePath=self.teamsResourcePath, teamsUrl=self.teamsUrl, updatedAt=self.updatedAt, url=self.url, viewerCanAdminister=self.viewerCanAdminister, viewerCanSubscribe=self.viewerCanSubscribe, viewerSubscription=self.viewerSubscription)



class TeamPrivacy(node):
    """
    The possible team privacy values.
    """

    __enum__ = True
    """
    A secret team can only be seen by its members.
    """
    SECRET = "SECRET"
    """
    A visible team can be seen and @mentioned by every member of the organization.
    """
    VISIBLE = "VISIBLE"

    def render(self):
        return dict()



class TeamMemberConnection(node):
    """
    The connection type for User.
    """

    edges: TeamMemberEdge = None
    nodes: User = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class TeamMemberEdge(node):
    """
    Represents a user who is a member of a team.
    """

    cursor: str = None
    memberAccessResourcePath: URI = None
    memberAccessUrl: URI = None
    node: User = None
    role: TeamMemberRole = None

    def render(self):
        return dict(cursor=self.cursor, memberAccessResourcePath=self.memberAccessResourcePath, memberAccessUrl=self.memberAccessUrl, node=self.node, role=self.role)



class TeamMemberRole(node):
    """
    The possible team member roles; either 'maintainer' or 'member'.
    """

    __enum__ = True
    """
    A team maintainer has permission to add and remove team members.
    """
    MAINTAINER = "MAINTAINER"
    """
    A team member has no administrative permissions on the team.
    """
    MEMBER = "MEMBER"

    def render(self):
        return dict()



class TeamMembershipType(node):
    """
    Defines which types of team members are included in the returned list. Can be one of IMMEDIATE, CHILD_TEAM or ALL.
    """

    __enum__ = True
    """
    Includes only immediate members of the team.
    """
    IMMEDIATE = "IMMEDIATE"
    """
    Includes only child team members for the team.
    """
    CHILD_TEAM = "CHILD_TEAM"
    """
    Includes immediate and child team members for the team.
    """
    ALL = "ALL"

    def render(self):
        return dict()



class TeamRepositoryConnection(node):
    """
    The connection type for Repository.
    """

    edges: TeamRepositoryEdge = None
    nodes: Repository = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class TeamRepositoryEdge(node):
    """
    Represents a team repository.
    """

    cursor: str = None
    node: Repository = None
    permission: RepositoryPermission = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node, permission=self.permission)



class RepositoryPermission(node):
    """
    The access level to a repository
    """

    __enum__ = True
    """
    Can read, clone, push, and add collaborators
    """
    ADMIN = "ADMIN"
    """
    Can read, clone and push
    """
    WRITE = "WRITE"
    """
    Can read and clone
    """
    READ = "READ"

    def render(self):
        return dict()



class TeamRepositoryOrder(node):
    """
    Ordering options for team repository connections
    """

    """
    The ordering direction.
    """
    direction: OrderDirection = None
    """
    The field to order repositories by.
    """
    field: TeamRepositoryOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class TeamRepositoryOrderField(node):
    """
    Properties by which team repository connections can be ordered.
    """

    __enum__ = True
    """
    Order repositories by creation time
    """
    CREATED_AT = "CREATED_AT"
    """
    Order repositories by update time
    """
    UPDATED_AT = "UPDATED_AT"
    """
    Order repositories by push time
    """
    PUSHED_AT = "PUSHED_AT"
    """
    Order repositories by name
    """
    NAME = "NAME"
    """
    Order repositories by permission
    """
    PERMISSION = "PERMISSION"
    """
    Order repositories by number of stargazers
    """
    STARGAZERS = "STARGAZERS"

    def render(self):
        return dict()



class ProjectConnection(node):
    """
    A list of projects associated with the owner.
    """

    edges: ProjectEdge = None
    nodes: Project = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ProjectEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Project = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ProjectOrder(node):
    """
    Ways in which lists of projects can be ordered upon return.
    """

    """
    The direction in which to order projects by the specified field.
    """
    direction: OrderDirection = None
    """
    The field in which to order projects by.
    """
    field: ProjectOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class ProjectOrderField(node):
    """
    Properties by which project connections can be ordered.
    """

    __enum__ = True
    """
    Order projects by creation time
    """
    CREATED_AT = "CREATED_AT"
    """
    Order projects by update time
    """
    UPDATED_AT = "UPDATED_AT"
    """
    Order projects by name
    """
    NAME = "NAME"

    def render(self):
        return dict()



class OrganizationInvitationConnection(node):
    """
    The connection type for OrganizationInvitation.
    """

    edges: OrganizationInvitationEdge = None
    nodes: OrganizationInvitation = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class OrganizationInvitationEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: OrganizationInvitation = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class OrganizationInvitation(node):
    """
    An Invitation for a user to an organization.
    """

    createdAt: DateTime = None
    email: str = None
    id: ID = None
    invitationType: OrganizationInvitationType = None
    invitee: User = None
    inviter: User = None
    organization: Organization = None
    role: OrganizationInvitationRole = None

    def render(self):
        return dict(createdAt=self.createdAt, email=self.email, id=self.id, invitationType=self.invitationType, invitee=self.invitee, inviter=self.inviter, organization=self.organization, role=self.role)



class Organization(node):
    """
    An account on GitHub, with one or more owners, that has repositories, members and teams.
    """

    databaseId: int = None
    description: str = None
    email: str = None
    id: ID = None
    location: str = None
    login: str = None
    name: str = None
    newTeamResourcePath: URI = None
    newTeamUrl: URI = None
    organizationBillingEmail: str = None
    projectsResourcePath: URI = None
    projectsUrl: URI = None
    resourcePath: URI = None
    samlIdentityProvider: OrganizationIdentityProvider = None
    teamsResourcePath: URI = None
    teamsUrl: URI = None
    url: URI = None
    viewerCanAdminister: bool = None
    viewerCanCreateProjects: bool = None
    viewerCanCreateRepositories: bool = None
    viewerCanCreateTeams: bool = None
    viewerIsAMember: bool = None
    websiteUrl: URI = None

    def avatarUrl(self, size:int) -> URI:
        """
        A URL pointing to the organization's public avatar.
        """
        tmpl = "avatarUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def members(self, first:int, after:str, last:int, before:str) -> UserConnection:
        """
        A list of users who are members of this organization.
        """
        tmpl = "members(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserConnection.F())

    def pinnedRepositories(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool) -> RepositoryConnection:
        """
        A list of repositories this user has pinned to their profile
        """
        tmpl = "pinnedRepositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, ret=RepositoryConnection.F())

    def project(self, number:int) -> Project:
        """
        Find project by number.
        """
        tmpl = "project(number:%(number)s) %(ret)s"
        return self.wrap(tmpl, fn=True, number=number, ret=Project.F())

    def projects(self, first:int, after:str, last:int, before:str, orderBy:ProjectOrder, search:str, states:ProjectState) -> ProjectConnection:
        """
        A list of projects under the owner.
        """
        tmpl = "projects(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s, search:%(search)s, states:%(states)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, search=search, states=states, ret=ProjectConnection.F())

    def repositories(self, first:int, after:str, last:int, before:str, privacy:RepositoryPrivacy, orderBy:RepositoryOrder, affiliations:RepositoryAffiliation, isLocked:bool, isFork:bool) -> RepositoryConnection:
        """
        A list of repositories that the user owns.
        """
        tmpl = "repositories(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, orderBy:%(orderBy)s, affiliations:%(affiliations)s, isLocked:%(isLocked)s, isFork:%(isFork)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, orderBy=orderBy, affiliations=affiliations, isLocked=isLocked, isFork=isFork, ret=RepositoryConnection.F())

    def repository(self, name:str) -> Repository:
        """
        Find Repository.
        """
        tmpl = "repository(name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, name=name, ret=Repository.F())

    def team(self, slug:str) -> Team:
        """
        Find an organization's team by its slug.
        """
        tmpl = "team(slug:%(slug)s) %(ret)s"
        return self.wrap(tmpl, fn=True, slug=slug, ret=Team.F())

    def teams(self, first:int, after:str, last:int, before:str, privacy:TeamPrivacy, role:TeamRole, query:str, userLogins:str, orderBy:TeamOrder, ldapMapped:bool, rootTeamsOnly:bool) -> TeamConnection:
        """
        A list of teams in this organization.
        """
        tmpl = "teams(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, privacy:%(privacy)s, role:%(role)s, query:%(query)s, userLogins:%(userLogins)s, orderBy:%(orderBy)s, ldapMapped:%(ldapMapped)s, rootTeamsOnly:%(rootTeamsOnly)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, privacy=privacy, role=role, query=query, userLogins=userLogins, orderBy=orderBy, ldapMapped=ldapMapped, rootTeamsOnly=rootTeamsOnly, ret=TeamConnection.F())

    def render(self):
        return dict(databaseId=self.databaseId, description=self.description, email=self.email, id=self.id, location=self.location, login=self.login, name=self.name, newTeamResourcePath=self.newTeamResourcePath, newTeamUrl=self.newTeamUrl, organizationBillingEmail=self.organizationBillingEmail, projectsResourcePath=self.projectsResourcePath, projectsUrl=self.projectsUrl, resourcePath=self.resourcePath, samlIdentityProvider=self.samlIdentityProvider, teamsResourcePath=self.teamsResourcePath, teamsUrl=self.teamsUrl, url=self.url, viewerCanAdminister=self.viewerCanAdminister, viewerCanCreateProjects=self.viewerCanCreateProjects, viewerCanCreateRepositories=self.viewerCanCreateRepositories, viewerCanCreateTeams=self.viewerCanCreateTeams, viewerIsAMember=self.viewerIsAMember, websiteUrl=self.websiteUrl)



class MarketplaceListing(node):
    """
    A listing in the GitHub integration marketplace.
    """

    companyUrl: URI = None
    configurationResourcePath: URI = None
    configurationUrl: URI = None
    documentationUrl: URI = None
    extendedDescription: str = None
    extendedDescriptionHTML: HTML = None
    fullDescription: str = None
    fullDescriptionHTML: HTML = None
    hasApprovalBeenRequested: bool = None
    hasPublishedFreeTrialPlans: bool = None
    hasTermsOfService: bool = None
    howItWorks: str = None
    howItWorksHTML: HTML = None
    id: ID = None
    installationUrl: URI = None
    installedForViewer: bool = None
    isApproved: bool = None
    isDelisted: bool = None
    isDraft: bool = None
    isPaid: bool = None
    isRejected: bool = None
    logoBackgroundColor: str = None
    name: str = None
    normalizedShortDescription: str = None
    pricingUrl: URI = None
    primaryCategory: MarketplaceCategory = None
    privacyPolicyUrl: URI = None
    resourcePath: URI = None
    screenshotUrls: None = None
    secondaryCategory: MarketplaceCategory = None
    shortDescription: str = None
    slug: str = None
    statusUrl: URI = None
    supportEmail: str = None
    supportUrl: URI = None
    termsOfServiceUrl: URI = None
    url: URI = None
    viewerCanAddPlans: bool = None
    viewerCanApprove: bool = None
    viewerCanDelist: bool = None
    viewerCanEdit: bool = None
    viewerCanEditCategories: bool = None
    viewerCanEditPlans: bool = None
    viewerCanRedraft: bool = None
    viewerCanReject: bool = None
    viewerCanRequestApproval: bool = None
    viewerHasPurchased: bool = None
    viewerHasPurchasedForAllOrganizations: bool = None
    viewerIsListingAdmin: bool = None

    def logoUrl(self, size:int) -> URI:
        """
        URL for the listing's logo image.
        """
        tmpl = "logoUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def render(self):
        return dict(companyUrl=self.companyUrl, configurationResourcePath=self.configurationResourcePath, configurationUrl=self.configurationUrl, documentationUrl=self.documentationUrl, extendedDescription=self.extendedDescription, extendedDescriptionHTML=self.extendedDescriptionHTML, fullDescription=self.fullDescription, fullDescriptionHTML=self.fullDescriptionHTML, hasApprovalBeenRequested=self.hasApprovalBeenRequested, hasPublishedFreeTrialPlans=self.hasPublishedFreeTrialPlans, hasTermsOfService=self.hasTermsOfService, howItWorks=self.howItWorks, howItWorksHTML=self.howItWorksHTML, id=self.id, installationUrl=self.installationUrl, installedForViewer=self.installedForViewer, isApproved=self.isApproved, isDelisted=self.isDelisted, isDraft=self.isDraft, isPaid=self.isPaid, isRejected=self.isRejected, logoBackgroundColor=self.logoBackgroundColor, name=self.name, normalizedShortDescription=self.normalizedShortDescription, pricingUrl=self.pricingUrl, primaryCategory=self.primaryCategory, privacyPolicyUrl=self.privacyPolicyUrl, resourcePath=self.resourcePath, screenshotUrls=self.screenshotUrls, secondaryCategory=self.secondaryCategory, shortDescription=self.shortDescription, slug=self.slug, statusUrl=self.statusUrl, supportEmail=self.supportEmail, supportUrl=self.supportUrl, termsOfServiceUrl=self.termsOfServiceUrl, url=self.url, viewerCanAddPlans=self.viewerCanAddPlans, viewerCanApprove=self.viewerCanApprove, viewerCanDelist=self.viewerCanDelist, viewerCanEdit=self.viewerCanEdit, viewerCanEditCategories=self.viewerCanEditCategories, viewerCanEditPlans=self.viewerCanEditPlans, viewerCanRedraft=self.viewerCanRedraft, viewerCanReject=self.viewerCanReject, viewerCanRequestApproval=self.viewerCanRequestApproval, viewerHasPurchased=self.viewerHasPurchased, viewerHasPurchasedForAllOrganizations=self.viewerHasPurchasedForAllOrganizations, viewerIsListingAdmin=self.viewerIsListingAdmin)



class OrganizationConnection(node):
    """
    The connection type for Organization.
    """

    edges: OrganizationEdge = None
    nodes: Organization = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class OrganizationEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Organization = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class Bot(node):
    """
    A special type of user which takes actions on behalf of GitHub Apps.
    """

    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None
    login: str = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None

    def avatarUrl(self, size:int) -> URI:
        """
        A URL pointing to the GitHub App's public avatar.
        """
        tmpl = "avatarUrl(size:%(size)s) %(ret)s"
        return self.wrap(tmpl, fn=True, size=size, ret=URI.F())

    def render(self):
        return dict(createdAt=self.createdAt, databaseId=self.databaseId, id=self.id, login=self.login, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url)



class MarketplaceCategory(node):
    """
    A public description of a Marketplace category.
    """

    description: str = None
    howItWorks: str = None
    name: str = None
    primaryListingCount: int = None
    resourcePath: URI = None
    secondaryListingCount: int = None
    slug: str = None
    url: URI = None

    def render(self):
        return dict(description=self.description, howItWorks=self.howItWorks, name=self.name, primaryListingCount=self.primaryListingCount, resourcePath=self.resourcePath, secondaryListingCount=self.secondaryListingCount, slug=self.slug, url=self.url)



class LanguageConnection(node):
    """
    A list of languages associated with the parent.
    """

    edges: LanguageEdge = None
    nodes: Language = None
    pageInfo: PageInfo = None
    totalCount: int = None
    totalSize: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount, totalSize=self.totalSize)



class LanguageEdge(node):
    """
    Represents the language of a repository.
    """

    cursor: str = None
    node: Language = None
    size: int = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node, size=self.size)



class Language(node):
    """
    Represents a given language found in repositories.
    """

    color: str = None
    id: ID = None
    name: str = None

    def render(self):
        return dict(color=self.color, id=self.id, name=self.name)



class Date(str):
    """
    An ISO-8601 encoded date string.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "Date"


class X509Certificate(str):
    """
    A valid x509 certificate string
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "X509Certificate"


class OrganizationIdentityProvider(node):
    """
    An Identity Provider configured to provision SAML and SCIM identities for Organizations
    """

    digestMethod: URI = None
    id: ID = None
    idpCertificate: X509Certificate = None
    issuer: str = None
    organization: Organization = None
    signatureMethod: URI = None
    ssoUrl: URI = None

    def externalIdentities(self, first:int, after:str, last:int, before:str) -> ExternalIdentityConnection:
        """
        External Identities provisioned by this Identity Provider
        """
        tmpl = "externalIdentities(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ExternalIdentityConnection.F())

    def render(self):
        return dict(digestMethod=self.digestMethod, id=self.id, idpCertificate=self.idpCertificate, issuer=self.issuer, organization=self.organization, signatureMethod=self.signatureMethod, ssoUrl=self.ssoUrl)



class ExternalIdentityConnection(node):
    """
    The connection type for ExternalIdentity.
    """

    edges: ExternalIdentityEdge = None
    nodes: ExternalIdentity = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ExternalIdentityEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: ExternalIdentity = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ExternalIdentity(node):
    """
    An external identity provisioned by SAML SSO or SCIM.
    """

    guid: str = None
    id: ID = None
    organizationInvitation: OrganizationInvitation = None
    samlIdentity: ExternalIdentitySamlAttributes = None
    scimIdentity: ExternalIdentityScimAttributes = None
    user: User = None

    def render(self):
        return dict(guid=self.guid, id=self.id, organizationInvitation=self.organizationInvitation, samlIdentity=self.samlIdentity, scimIdentity=self.scimIdentity, user=self.user)



class ExternalIdentitySamlAttributes(node):
    """
    SAML attributes for the External Identity
    """

    nameId: str = None

    def render(self):
        return dict(nameId=self.nameId)



class ExternalIdentityScimAttributes(node):
    """
    SCIM attributes for the External Identity
    """

    username: str = None

    def render(self):
        return dict(username=self.username)



class DefaultRepositoryPermissionField(node):
    """
    The possible default permissions for repositories.
    """

    __enum__ = True
    """
    No access
    """
    NONE = "NONE"
    """
    Can read repos by default
    """
    READ = "READ"
    """
    Can read and write repos by default
    """
    WRITE = "WRITE"
    """
    Can read, write, and administrate repos by default
    """
    ADMIN = "ADMIN"

    def render(self):
        return dict()



class TeamRole(node):
    """
    The role of a user on a team.
    """

    __enum__ = True
    """
    User has admin rights on the team.
    """
    ADMIN = "ADMIN"
    """
    User is a member of the team.
    """
    MEMBER = "MEMBER"

    def render(self):
        return dict()



class TeamOrder(node):
    """
    Ways in which team connections can be ordered.
    """

    """
    The direction in which to order nodes.
    """
    direction: OrderDirection = None
    """
    The field in which to order nodes by.
    """
    field: TeamOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class TeamOrderField(node):
    """
    Properties by which team connections can be ordered.
    """

    __enum__ = True
    """
    Allows ordering a list of teams by name.
    """
    NAME = "NAME"

    def render(self):
        return dict()



class GistConnection(node):
    """
    The connection type for Gist.
    """

    edges: GistEdge = None
    nodes: Gist = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class GistEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Gist = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class Gist(node):
    """
    A Gist.
    """

    createdAt: DateTime = None
    description: str = None
    id: ID = None
    isPublic: bool = None
    name: str = None
    owner: RepositoryOwner = None
    pushedAt: DateTime = None
    updatedAt: DateTime = None
    viewerHasStarred: bool = None

    def comments(self, first:int, after:str, last:int, before:str) -> GistCommentConnection:
        """
        A list of comments associated with the gist
        """
        tmpl = "comments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=GistCommentConnection.F())

    def stargazers(self, first:int, after:str, last:int, before:str, orderBy:StarOrder) -> StargazerConnection:
        """
        A list of users who have starred this starrable.
        """
        tmpl = "stargazers(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, ret=StargazerConnection.F())

    def render(self):
        return dict(createdAt=self.createdAt, description=self.description, id=self.id, isPublic=self.isPublic, name=self.name, owner=self.owner, pushedAt=self.pushedAt, updatedAt=self.updatedAt, viewerHasStarred=self.viewerHasStarred)



class Starrable(node):
    """
    Things that can be starred.
    """

    id: ID = None
    viewerHasStarred: bool = None

    def stargazers(self, first:int, after:str, last:int, before:str, orderBy:StarOrder) -> StargazerConnection:
        """
        A list of users who have starred this starrable.
        """
        tmpl = "stargazers(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, orderBy:%(orderBy)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, orderBy=orderBy, ret=StargazerConnection.F())

    def render(self):
        return dict(id=self.id, viewerHasStarred=self.viewerHasStarred)



class StargazerConnection(node):
    """
    The connection type for User.
    """

    edges: StargazerEdge = None
    nodes: User = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class StargazerEdge(node):
    """
    Represents a user that's starred a repository.
    """

    cursor: str = None
    node: User = None
    starredAt: DateTime = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node, starredAt=self.starredAt)



class StarOrder(node):
    """
    Ways in which star connections can be ordered.
    """

    """
    The direction in which to order nodes.
    """
    direction: OrderDirection = None
    """
    The field in which to order nodes by.
    """
    field: StarOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class StarOrderField(node):
    """
    Properties by which star connections can be ordered.
    """

    __enum__ = True
    """
    Allows ordering a list of stars by when they were created.
    """
    STARRED_AT = "STARRED_AT"

    def render(self):
        return dict()



class GistCommentConnection(node):
    """
    The connection type for GistComment.
    """

    edges: GistCommentEdge = None
    nodes: GistComment = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class GistCommentEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: GistComment = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class GistComment(node):
    """
    Represents a comment on an Gist.
    """

    author: Actor = None
    authorAssociation: CommentAuthorAssociation = None
    body: str = None
    bodyHTML: HTML = None
    createdAt: DateTime = None
    createdViaEmail: bool = None
    databaseId: int = None
    editor: Actor = None
    gist: Gist = None
    id: ID = None
    lastEditedAt: DateTime = None
    publishedAt: DateTime = None
    updatedAt: DateTime = None
    viewerCanDelete: bool = None
    viewerCanUpdate: bool = None
    viewerCannotUpdateReasons: None = None
    viewerDidAuthor: bool = None

    def userContentEdits(self, first:int, after:str, last:int, before:str) -> UserContentEditConnection:
        """
        A list of edits to this content.
        """
        tmpl = "userContentEdits(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=UserContentEditConnection.F())

    def render(self):
        return dict(author=self.author, authorAssociation=self.authorAssociation, body=self.body, bodyHTML=self.bodyHTML, createdAt=self.createdAt, createdViaEmail=self.createdViaEmail, databaseId=self.databaseId, editor=self.editor, gist=self.gist, id=self.id, lastEditedAt=self.lastEditedAt, publishedAt=self.publishedAt, updatedAt=self.updatedAt, viewerCanDelete=self.viewerCanDelete, viewerCanUpdate=self.viewerCanUpdate, viewerCannotUpdateReasons=self.viewerCannotUpdateReasons, viewerDidAuthor=self.viewerDidAuthor)



class GistPrivacy(node):
    """
    The privacy of a Gist
    """

    __enum__ = True
    """
    Public
    """
    PUBLIC = "PUBLIC"
    """
    Secret
    """
    SECRET = "SECRET"
    """
    Gists that are public and secret
    """
    ALL = "ALL"

    def render(self):
        return dict()



class GistOrder(node):
    """
    Ordering options for gist connections
    """

    """
    The ordering direction.
    """
    direction: OrderDirection = None
    """
    The field to order repositories by.
    """
    field: GistOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class GistOrderField(node):
    """
    Properties by which gist connections can be ordered.
    """

    __enum__ = True
    """
    Order gists by creation time
    """
    CREATED_AT = "CREATED_AT"
    """
    Order gists by update time
    """
    UPDATED_AT = "UPDATED_AT"
    """
    Order gists by push time
    """
    PUSHED_AT = "PUSHED_AT"

    def render(self):
        return dict()



class RepositoryInvitation(node):
    """
    An invitation for a user to be added to a repository.
    """

    id: ID = None
    invitee: User = None
    inviter: User = None
    permission: RepositoryPermission = None
    repository: RepositoryInvitationRepository = None

    def render(self):
        return dict(id=self.id, invitee=self.invitee, inviter=self.inviter, permission=self.permission, repository=self.repository)



class RepositoryInvitationRepository(node):
    """
    A subset of repository info shared with potential collaborators.
    """

    createdAt: DateTime = None
    description: str = None
    descriptionHTML: HTML = None
    forkCount: int = None
    hasIssuesEnabled: bool = None
    hasWikiEnabled: bool = None
    homepageUrl: URI = None
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
    pushedAt: DateTime = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None

    def shortDescriptionHTML(self, limit:int) -> HTML:
        """
        A description of the repository, rendered to HTML without any links in it.
        """
        tmpl = "shortDescriptionHTML(limit:%(limit)s) %(ret)s"
        return self.wrap(tmpl, fn=True, limit=limit, ret=HTML.F())

    def render(self):
        return dict(createdAt=self.createdAt, description=self.description, descriptionHTML=self.descriptionHTML, forkCount=self.forkCount, hasIssuesEnabled=self.hasIssuesEnabled, hasWikiEnabled=self.hasWikiEnabled, homepageUrl=self.homepageUrl, isArchived=self.isArchived, isFork=self.isFork, isLocked=self.isLocked, isMirror=self.isMirror, isPrivate=self.isPrivate, license=self.license, licenseInfo=self.licenseInfo, lockReason=self.lockReason, mirrorUrl=self.mirrorUrl, name=self.name, nameWithOwner=self.nameWithOwner, owner=self.owner, pushedAt=self.pushedAt, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url)



class RepositoryInfo(node):
    """
    A subset of repository info.
    """

    createdAt: DateTime = None
    description: str = None
    descriptionHTML: HTML = None
    forkCount: int = None
    hasIssuesEnabled: bool = None
    hasWikiEnabled: bool = None
    homepageUrl: URI = None
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
    pushedAt: DateTime = None
    resourcePath: URI = None
    updatedAt: DateTime = None
    url: URI = None

    def shortDescriptionHTML(self, limit:int) -> HTML:
        """
        A description of the repository, rendered to HTML without any links in it.
        """
        tmpl = "shortDescriptionHTML(limit:%(limit)s) %(ret)s"
        return self.wrap(tmpl, fn=True, limit=limit, ret=HTML.F())

    def render(self):
        return dict(createdAt=self.createdAt, description=self.description, descriptionHTML=self.descriptionHTML, forkCount=self.forkCount, hasIssuesEnabled=self.hasIssuesEnabled, hasWikiEnabled=self.hasWikiEnabled, homepageUrl=self.homepageUrl, isArchived=self.isArchived, isFork=self.isFork, isLocked=self.isLocked, isMirror=self.isMirror, isPrivate=self.isPrivate, license=self.license, licenseInfo=self.licenseInfo, lockReason=self.lockReason, mirrorUrl=self.mirrorUrl, name=self.name, nameWithOwner=self.nameWithOwner, owner=self.owner, pushedAt=self.pushedAt, resourcePath=self.resourcePath, updatedAt=self.updatedAt, url=self.url)



class RepositoryLockReason(node):
    """
    The possible reasons a given repository could be in a locked state.
    """

    __enum__ = True
    """
    The repository is locked due to a move.
    """
    MOVING = "MOVING"
    """
    The repository is locked due to a billing related reason.
    """
    BILLING = "BILLING"
    """
    The repository is locked due to a rename.
    """
    RENAME = "RENAME"
    """
    The repository is locked due to a migration.
    """
    MIGRATING = "MIGRATING"

    def render(self):
        return dict()



class License(node):
    """
    A respository's open source license
    """

    body: str = None
    conditions: None = None
    description: str = None
    featured: bool = None
    hidden: bool = None
    id: ID = None
    implementation: str = None
    key: str = None
    limitations: None = None
    name: str = None
    nickname: str = None
    permissions: None = None
    spdxId: str = None
    url: URI = None

    def render(self):
        return dict(body=self.body, conditions=self.conditions, description=self.description, featured=self.featured, hidden=self.hidden, id=self.id, implementation=self.implementation, key=self.key, limitations=self.limitations, name=self.name, nickname=self.nickname, permissions=self.permissions, spdxId=self.spdxId, url=self.url)



class LicenseRule(node):
    """
    Describes a License's conditions, permissions, and limitations
    """

    description: str = None
    key: str = None
    label: str = None

    def render(self):
        return dict(description=self.description, key=self.key, label=self.label)



class OrganizationInvitationType(node):
    """
    The possible organization invitation types.
    """

    __enum__ = True
    """
    The invitation was to an existing user.
    """
    USER = "USER"
    """
    The invitation was to an email address.
    """
    EMAIL = "EMAIL"

    def render(self):
        return dict()



class OrganizationInvitationRole(node):
    """
    The possible organization invitation roles.
    """

    __enum__ = True
    """
    The user is invited to be a direct member of the organization.
    """
    DIRECT_MEMBER = "DIRECT_MEMBER"
    """
    The user is invited to be an admin of the organization.
    """
    ADMIN = "ADMIN"
    """
    The user is invited to be a billing manager of the organization.
    """
    BILLING_MANAGER = "BILLING_MANAGER"
    """
    The user's previous role will be reinstated.
    """
    REINSTATE = "REINSTATE"

    def render(self):
        return dict()



class PullRequestCommitConnection(node):
    """
    The connection type for PullRequestCommit.
    """

    edges: PullRequestCommitEdge = None
    nodes: PullRequestCommit = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class PullRequestCommitEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: PullRequestCommit = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PullRequestCommit(node):
    """
    Represents a Git commit part of a pull request.
    """

    commit: Commit = None
    id: ID = None
    pullRequest: PullRequest = None
    resourcePath: URI = None
    url: URI = None

    def render(self):
        return dict(commit=self.commit, id=self.id, pullRequest=self.pullRequest, resourcePath=self.resourcePath, url=self.url)



class ReviewRequestConnection(node):
    """
    The connection type for ReviewRequest.
    """

    edges: ReviewRequestEdge = None
    nodes: ReviewRequest = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ReviewRequestEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: ReviewRequest = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ReviewRequest(node):
    """
    A request for a user to review a pull request.
    """

    databaseId: int = None
    id: ID = None
    pullRequest: PullRequest = None
    requestedReviewer: RequestedReviewer = None
    reviewer: User = None

    def render(self):
        return dict(databaseId=self.databaseId, id=self.id, pullRequest=self.pullRequest, requestedReviewer=self.requestedReviewer, reviewer=self.reviewer)



class RequestedReviewer(str):
    """
    Types that can be requested reviewers.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "RequestedReviewer"


class PullRequestTimelineConnection(node):
    """
    The connection type for PullRequestTimelineItem.
    """

    edges: PullRequestTimelineItemEdge = None
    nodes: PullRequestTimelineItem = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class PullRequestTimelineItemEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: PullRequestTimelineItem = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PullRequestTimelineItem(str):
    """
    An item in an pull request timeline
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "PullRequestTimelineItem"


class CommitCommentThread(node):
    """
    A thread of comments on a commit.
    """

    commit: Commit = None
    id: ID = None
    path: str = None
    position: int = None
    repository: Repository = None

    def comments(self, first:int, after:str, last:int, before:str) -> CommitCommentConnection:
        """
        The comments that exist in this thread.
        """
        tmpl = "comments(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=CommitCommentConnection.F())

    def render(self):
        return dict(commit=self.commit, id=self.id, path=self.path, position=self.position, repository=self.repository)



class ClosedEvent(node):
    """
    Represents a 'closed' event on any `Closable`.
    """

    actor: Actor = None
    closable: Closable = None
    closer: Closer = None
    commit: Commit = None
    createdAt: DateTime = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, closable=self.closable, closer=self.closer, commit=self.commit, createdAt=self.createdAt, id=self.id)



class Closer(str):
    """
    The object which triggered a `ClosedEvent`.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "Closer"


class ReopenedEvent(node):
    """
    Represents a 'reopened' event on any `Closable`.
    """

    actor: Actor = None
    closable: Closable = None
    createdAt: DateTime = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, closable=self.closable, createdAt=self.createdAt, id=self.id)



class SubscribedEvent(node):
    """
    Represents a 'subscribed' event on a given `Subscribable`.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    subscribable: Subscribable = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, subscribable=self.subscribable)



class UnsubscribedEvent(node):
    """
    Represents an 'unsubscribed' event on a given `Subscribable`.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    subscribable: Subscribable = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, subscribable=self.subscribable)



class MergedEvent(node):
    """
    Represents a 'merged' event on a given pull request.
    """

    actor: Actor = None
    commit: Commit = None
    createdAt: DateTime = None
    id: ID = None
    mergeRef: Ref = None
    mergeRefName: str = None
    pullRequest: PullRequest = None
    resourcePath: URI = None
    url: URI = None

    def render(self):
        return dict(actor=self.actor, commit=self.commit, createdAt=self.createdAt, id=self.id, mergeRef=self.mergeRef, mergeRefName=self.mergeRefName, pullRequest=self.pullRequest, resourcePath=self.resourcePath, url=self.url)



class ReferencedEvent(node):
    """
    Represents a 'referenced' event on a given `ReferencedSubject`.
    """

    actor: Actor = None
    commit: Commit = None
    commitRepository: Repository = None
    createdAt: DateTime = None
    id: ID = None
    isCrossReference: bool = None
    isCrossRepository: bool = None
    isDirectReference: bool = None
    subject: ReferencedSubject = None

    def render(self):
        return dict(actor=self.actor, commit=self.commit, commitRepository=self.commitRepository, createdAt=self.createdAt, id=self.id, isCrossReference=self.isCrossReference, isCrossRepository=self.isCrossRepository, isDirectReference=self.isDirectReference, subject=self.subject)



class ReferencedSubject(str):
    """
    Any referencable object
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "ReferencedSubject"


class CrossReferencedEvent(node):
    """
    Represents a mention made by one issue or pull request to another.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    isCrossRepository: bool = None
    referencedAt: DateTime = None
    resourcePath: URI = None
    source: ReferencedSubject = None
    target: ReferencedSubject = None
    url: URI = None
    willCloseTarget: bool = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, isCrossRepository=self.isCrossRepository, referencedAt=self.referencedAt, resourcePath=self.resourcePath, source=self.source, target=self.target, url=self.url, willCloseTarget=self.willCloseTarget)



class AssignedEvent(node):
    """
    Represents an 'assigned' event on any assignable object.
    """

    actor: Actor = None
    assignable: Assignable = None
    createdAt: DateTime = None
    id: ID = None
    user: User = None

    def render(self):
        return dict(actor=self.actor, assignable=self.assignable, createdAt=self.createdAt, id=self.id, user=self.user)



class UnassignedEvent(node):
    """
    Represents an 'unassigned' event on any assignable object.
    """

    actor: Actor = None
    assignable: Assignable = None
    createdAt: DateTime = None
    id: ID = None
    user: User = None

    def render(self):
        return dict(actor=self.actor, assignable=self.assignable, createdAt=self.createdAt, id=self.id, user=self.user)



class LabeledEvent(node):
    """
    Represents a 'labeled' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    label: Label = None
    labelable: Labelable = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, label=self.label, labelable=self.labelable)



class UnlabeledEvent(node):
    """
    Represents an 'unlabeled' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    label: Label = None
    labelable: Labelable = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, label=self.label, labelable=self.labelable)



class MilestonedEvent(node):
    """
    Represents a 'milestoned' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    milestoneTitle: str = None
    subject: MilestoneItem = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, milestoneTitle=self.milestoneTitle, subject=self.subject)



class MilestoneItem(str):
    """
    Types that can be inside a Milestone.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "MilestoneItem"


class DemilestonedEvent(node):
    """
    Represents a 'demilestoned' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    milestoneTitle: str = None
    subject: MilestoneItem = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, milestoneTitle=self.milestoneTitle, subject=self.subject)



class RenamedTitleEvent(node):
    """
    Represents a 'renamed' event on a given issue or pull request
    """

    actor: Actor = None
    createdAt: DateTime = None
    currentTitle: str = None
    id: ID = None
    previousTitle: str = None
    subject: RenamedTitleSubject = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, currentTitle=self.currentTitle, id=self.id, previousTitle=self.previousTitle, subject=self.subject)



class RenamedTitleSubject(str):
    """
    An object which has a renamable title
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "RenamedTitleSubject"


class LockedEvent(node):
    """
    Represents a 'locked' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    lockable: Lockable = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, lockable=self.lockable)



class UnlockedEvent(node):
    """
    Represents an 'unlocked' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    lockable: Lockable = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, lockable=self.lockable)



class DeployedEvent(node):
    """
    Represents a 'deployed' event on a given pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    deployment: Deployment = None
    id: ID = None
    pullRequest: PullRequest = None
    ref: Ref = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, deployment=self.deployment, id=self.id, pullRequest=self.pullRequest, ref=self.ref)



class Deployment(node):
    """
    Represents triggered deployment instance.
    """

    commit: Commit = None
    createdAt: DateTime = None
    creator: Actor = None
    databaseId: int = None
    environment: str = None
    id: ID = None
    latestStatus: DeploymentStatus = None
    payload: str = None
    repository: Repository = None
    state: DeploymentState = None

    def statuses(self, first:int, after:str, last:int, before:str) -> DeploymentStatusConnection:
        """
        A list of statuses associated with the deployment.
        """
        tmpl = "statuses(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=DeploymentStatusConnection.F())

    def render(self):
        return dict(commit=self.commit, createdAt=self.createdAt, creator=self.creator, databaseId=self.databaseId, environment=self.environment, id=self.id, latestStatus=self.latestStatus, payload=self.payload, repository=self.repository, state=self.state)



class DeploymentStatusConnection(node):
    """
    The connection type for DeploymentStatus.
    """

    edges: DeploymentStatusEdge = None
    nodes: DeploymentStatus = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class DeploymentStatusEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: DeploymentStatus = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class DeploymentStatus(node):
    """
    Describes the status of a given deployment attempt.
    """

    createdAt: DateTime = None
    creator: Actor = None
    deployment: Deployment = None
    description: str = None
    environmentUrl: URI = None
    id: ID = None
    logUrl: URI = None
    state: DeploymentStatusState = None
    updatedAt: DateTime = None

    def render(self):
        return dict(createdAt=self.createdAt, creator=self.creator, deployment=self.deployment, description=self.description, environmentUrl=self.environmentUrl, id=self.id, logUrl=self.logUrl, state=self.state, updatedAt=self.updatedAt)



class DeploymentStatusState(node):
    """
    The possible states for a deployment status.
    """

    __enum__ = True
    """
    The deployment is pending.
    """
    PENDING = "PENDING"
    """
    The deployment was successful.
    """
    SUCCESS = "SUCCESS"
    """
    The deployment has failed.
    """
    FAILURE = "FAILURE"
    """
    The deployment is inactive.
    """
    INACTIVE = "INACTIVE"
    """
    The deployment experienced an error.
    """
    ERROR = "ERROR"

    def render(self):
        return dict()



class DeploymentState(node):
    """
    The possible states in which a deployment can be.
    """

    __enum__ = True
    """
    The pending deployment was not updated after 30 minutes.
    """
    ABANDONED = "ABANDONED"
    """
    The deployment is currently active.
    """
    ACTIVE = "ACTIVE"
    """
    An inactive transient deployment.
    """
    DESTROYED = "DESTROYED"
    """
    The deployment experienced an error.
    """
    ERROR = "ERROR"
    """
    The deployment has failed.
    """
    FAILURE = "FAILURE"
    """
    The deployment is inactive.
    """
    INACTIVE = "INACTIVE"
    """
    The deployment is pending.
    """
    PENDING = "PENDING"

    def render(self):
        return dict()



class HeadRefDeletedEvent(node):
    """
    Represents a 'head_ref_deleted' event on a given pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    headRef: Ref = None
    headRefName: str = None
    id: ID = None
    pullRequest: PullRequest = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, headRef=self.headRef, headRefName=self.headRefName, id=self.id, pullRequest=self.pullRequest)



class HeadRefRestoredEvent(node):
    """
    Represents a 'head_ref_restored' event on a given pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    pullRequest: PullRequest = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, pullRequest=self.pullRequest)



class HeadRefForcePushedEvent(node):
    """
    Represents a 'head_ref_force_pushed' event on a given pull request.
    """

    actor: Actor = None
    afterCommit: Commit = None
    beforeCommit: Commit = None
    createdAt: DateTime = None
    id: ID = None
    pullRequest: PullRequest = None
    ref: Ref = None

    def render(self):
        return dict(actor=self.actor, afterCommit=self.afterCommit, beforeCommit=self.beforeCommit, createdAt=self.createdAt, id=self.id, pullRequest=self.pullRequest, ref=self.ref)



class BaseRefForcePushedEvent(node):
    """
    Represents a 'base_ref_force_pushed' event on a given pull request.
    """

    actor: Actor = None
    afterCommit: Commit = None
    beforeCommit: Commit = None
    createdAt: DateTime = None
    id: ID = None
    pullRequest: PullRequest = None
    ref: Ref = None

    def render(self):
        return dict(actor=self.actor, afterCommit=self.afterCommit, beforeCommit=self.beforeCommit, createdAt=self.createdAt, id=self.id, pullRequest=self.pullRequest, ref=self.ref)



class ReviewRequestedEvent(node):
    """
    Represents an 'review_requested' event on a given pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    pullRequest: PullRequest = None
    requestedReviewer: RequestedReviewer = None
    subject: User = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, pullRequest=self.pullRequest, requestedReviewer=self.requestedReviewer, subject=self.subject)



class ReviewRequestRemovedEvent(node):
    """
    Represents an 'review_request_removed' event on a given pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    id: ID = None
    pullRequest: PullRequest = None
    requestedReviewer: RequestedReviewer = None
    subject: User = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, id=self.id, pullRequest=self.pullRequest, requestedReviewer=self.requestedReviewer, subject=self.subject)



class ReviewDismissedEvent(node):
    """
    Represents a 'review_dismissed' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None
    message: str = None
    messageHtml: HTML = None
    previousReviewState: PullRequestReviewState = None
    pullRequest: PullRequest = None
    pullRequestCommit: PullRequestCommit = None
    resourcePath: URI = None
    review: PullRequestReview = None
    url: URI = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id, message=self.message, messageHtml=self.messageHtml, previousReviewState=self.previousReviewState, pullRequest=self.pullRequest, pullRequestCommit=self.pullRequestCommit, resourcePath=self.resourcePath, review=self.review, url=self.url)



class BaseRefChangedEvent(node):
    """
    Represents a 'base_ref_changed' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id)



class AddedToProjectEvent(node):
    """
    Represents a 'added_to_project' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id)



class CommentDeletedEvent(node):
    """
    Represents a 'comment_deleted' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id)



class ConvertedNoteToIssueEvent(node):
    """
    Represents a 'converted_note_to_issue' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id)



class IssueOrPullRequest(str):
    """
    Used for return value of Repository.issueOrPullRequest.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "IssueOrPullRequest"


class MentionedEvent(node):
    """
    Represents a 'mentioned' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id)



class MovedColumnsInProjectEvent(node):
    """
    Represents a 'moved_columns_in_project' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id)



class RemovedFromProjectEvent(node):
    """
    Represents a 'removed_from_project' event on a given issue or pull request.
    """

    actor: Actor = None
    createdAt: DateTime = None
    databaseId: int = None
    id: ID = None

    def render(self):
        return dict(actor=self.actor, createdAt=self.createdAt, databaseId=self.databaseId, id=self.id)



class SuggestedReviewer(node):
    """
    A suggestion to review a pull request based on a user's commit history and review comments.
    """

    isAuthor: bool = None
    isCommenter: bool = None
    reviewer: User = None

    def render(self):
        return dict(isAuthor=self.isAuthor, isCommenter=self.isCommenter, reviewer=self.reviewer)



class IssueTimelineConnection(node):
    """
    The connection type for IssueTimelineItem.
    """

    edges: IssueTimelineItemEdge = None
    nodes: IssueTimelineItem = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class IssueTimelineItemEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: IssueTimelineItem = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class IssueTimelineItem(str):
    """
    An item in an issue timeline
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "IssueTimelineItem"


class CollaboratorAffiliation(node):
    """
    Collaborators affiliation level with a subject.
    """

    __enum__ = True
    """
    All outside collaborators of an organization-owned subject.
    """
    OUTSIDE = "OUTSIDE"
    """
    All collaborators with permissions to an organization-owned subject, regardless of organization membership status.
    """
    DIRECT = "DIRECT"
    """
    All collaborators the authenticated user can see.
    """
    ALL = "ALL"

    def render(self):
        return dict()



class DeployKeyConnection(node):
    """
    The connection type for DeployKey.
    """

    edges: DeployKeyEdge = None
    nodes: DeployKey = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class DeployKeyEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: DeployKey = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class DeployKey(node):
    """
    A repository deploy key.
    """

    createdAt: DateTime = None
    id: ID = None
    key: str = None
    readOnly: bool = None
    title: str = None
    verified: bool = None

    def render(self):
        return dict(createdAt=self.createdAt, id=self.id, key=self.key, readOnly=self.readOnly, title=self.title, verified=self.verified)



class RepositoryCollaboratorAffiliation(node):
    """
    The affiliation type between collaborator and repository.
    """

    __enum__ = True
    """
    All collaborators of the repository.
    """
    ALL = "ALL"
    """
    All outside collaborators of an organization-owned repository.
    """
    OUTSIDE = "OUTSIDE"

    def render(self):
        return dict()



class RepositoryTopicConnection(node):
    """
    The connection type for RepositoryTopic.
    """

    edges: RepositoryTopicEdge = None
    nodes: RepositoryTopic = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class RepositoryTopicEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: RepositoryTopic = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class RepositoryTopic(node):
    """
    A repository-topic connects a repository to a topic.
    """

    id: ID = None
    resourcePath: URI = None
    topic: Topic = None
    url: URI = None

    def render(self):
        return dict(id=self.id, resourcePath=self.resourcePath, topic=self.topic, url=self.url)



class Topic(node):
    """
    A topic aggregates entities that are related to a subject.
    """

    id: ID = None
    name: str = None
    relatedTopics: None = None

    def render(self):
        return dict(id=self.id, name=self.name, relatedTopics=self.relatedTopics)



class Release(node):
    """
    A release contains the content for a release.
    """

    author: User = None
    createdAt: DateTime = None
    description: str = None
    id: ID = None
    isDraft: bool = None
    isPrerelease: bool = None
    name: str = None
    publishedAt: DateTime = None
    resourcePath: URI = None
    tag: Ref = None
    updatedAt: DateTime = None
    url: URI = None

    def releaseAssets(self, first:int, after:str, last:int, before:str, name:str) -> ReleaseAssetConnection:
        """
        List of releases assets which are dependent on this release.
        """
        tmpl = "releaseAssets(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s, name:%(name)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, name=name, ret=ReleaseAssetConnection.F())

    def render(self):
        return dict(author=self.author, createdAt=self.createdAt, description=self.description, id=self.id, isDraft=self.isDraft, isPrerelease=self.isPrerelease, name=self.name, publishedAt=self.publishedAt, resourcePath=self.resourcePath, tag=self.tag, updatedAt=self.updatedAt, url=self.url)



class ReleaseAssetConnection(node):
    """
    The connection type for ReleaseAsset.
    """

    edges: ReleaseAssetEdge = None
    nodes: ReleaseAsset = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ReleaseAssetEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: ReleaseAsset = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ReleaseAsset(node):
    """
    A release asset contains the content for a release asset.
    """

    contentType: str = None
    createdAt: DateTime = None
    downloadCount: int = None
    downloadUrl: URI = None
    id: ID = None
    name: str = None
    release: Release = None
    size: int = None
    updatedAt: DateTime = None
    uploadedBy: User = None
    url: URI = None

    def render(self):
        return dict(contentType=self.contentType, createdAt=self.createdAt, downloadCount=self.downloadCount, downloadUrl=self.downloadUrl, id=self.id, name=self.name, release=self.release, size=self.size, updatedAt=self.updatedAt, uploadedBy=self.uploadedBy, url=self.url)



class ProtectedBranchConnection(node):
    """
    The connection type for ProtectedBranch.
    """

    edges: ProtectedBranchEdge = None
    nodes: ProtectedBranch = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ProtectedBranchEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: ProtectedBranch = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ProtectedBranch(node):
    """
    A repository protected branch.
    """

    creator: Actor = None
    hasDismissableStaleReviews: bool = None
    hasRequiredReviews: bool = None
    hasRequiredStatusChecks: bool = None
    hasRestrictedPushes: bool = None
    hasRestrictedReviewDismissals: bool = None
    hasStrictRequiredStatusChecks: bool = None
    id: ID = None
    isAdminEnforced: bool = None
    name: str = None
    repository: Repository = None
    requiredStatusCheckContexts: str = None

    def pushAllowances(self, first:int, after:str, last:int, before:str) -> PushAllowanceConnection:
        """
        A list push allowances for this protected branch.
        """
        tmpl = "pushAllowances(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=PushAllowanceConnection.F())

    def reviewDismissalAllowances(self, first:int, after:str, last:int, before:str) -> ReviewDismissalAllowanceConnection:
        """
        A list review dismissal allowances for this protected branch.
        """
        tmpl = "reviewDismissalAllowances(first:%(first)s, after:%(after)s, last:%(last)s, before:%(before)s) %(ret)s"
        return self.wrap(tmpl, fn=True, first=first, after=after, last=last, before=before, ret=ReviewDismissalAllowanceConnection.F())

    def render(self):
        return dict(creator=self.creator, hasDismissableStaleReviews=self.hasDismissableStaleReviews, hasRequiredReviews=self.hasRequiredReviews, hasRequiredStatusChecks=self.hasRequiredStatusChecks, hasRestrictedPushes=self.hasRestrictedPushes, hasRestrictedReviewDismissals=self.hasRestrictedReviewDismissals, hasStrictRequiredStatusChecks=self.hasStrictRequiredStatusChecks, id=self.id, isAdminEnforced=self.isAdminEnforced, name=self.name, repository=self.repository, requiredStatusCheckContexts=self.requiredStatusCheckContexts)



class ReviewDismissalAllowanceConnection(node):
    """
    The connection type for ReviewDismissalAllowance.
    """

    edges: ReviewDismissalAllowanceEdge = None
    nodes: ReviewDismissalAllowance = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ReviewDismissalAllowanceEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: ReviewDismissalAllowance = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ReviewDismissalAllowance(node):
    """
    A team or user who has the ability to dismiss a review on a protected branch.
    """

    actor: ReviewDismissalAllowanceActor = None
    id: ID = None
    protectedBranch: ProtectedBranch = None

    def render(self):
        return dict(actor=self.actor, id=self.id, protectedBranch=self.protectedBranch)



class ReviewDismissalAllowanceActor(str):
    """
    Types that can be an actor.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "ReviewDismissalAllowanceActor"


class PushAllowanceConnection(node):
    """
    The connection type for PushAllowance.
    """

    edges: PushAllowanceEdge = None
    nodes: PushAllowance = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class PushAllowanceEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: PushAllowance = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PushAllowance(node):
    """
    A team or user who has the ability to push to a protected branch.
    """

    actor: PushAllowanceActor = None
    id: ID = None
    protectedBranch: ProtectedBranch = None

    def render(self):
        return dict(actor=self.actor, id=self.id, protectedBranch=self.protectedBranch)



class PushAllowanceActor(str):
    """
    Types that can be an actor.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "PushAllowanceActor"


class MilestoneConnection(node):
    """
    The connection type for Milestone.
    """

    edges: MilestoneEdge = None
    nodes: Milestone = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class MilestoneEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Milestone = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class MilestoneOrder(node):
    """
    Ordering options for milestone connections.
    """

    """
    The ordering direction.
    """
    direction: OrderDirection = None
    """
    The field to order milestones by.
    """
    field: MilestoneOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class MilestoneOrderField(node):
    """
    Properties by which milestone connections can be ordered.
    """

    __enum__ = True
    """
    Order milestones by when they are due.
    """
    DUE_DATE = "DUE_DATE"
    """
    Order milestones by when they were created.
    """
    CREATED_AT = "CREATED_AT"
    """
    Order milestones by when they were last updated.
    """
    UPDATED_AT = "UPDATED_AT"
    """
    Order milestones by their number.
    """
    NUMBER = "NUMBER"

    def render(self):
        return dict()



class CodeOfConduct(node):
    """
    The Code of Conduct for a repository
    """

    body: str = None
    key: str = None
    name: str = None
    url: URI = None

    def render(self):
        return dict(body=self.body, key=self.key, name=self.name, url=self.url)



class RepositoryCollaboratorConnection(node):
    """
    The connection type for User.
    """

    edges: RepositoryCollaboratorEdge = None
    nodes: User = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class RepositoryCollaboratorEdge(node):
    """
    Represents a user who is a collaborator of a repository.
    """

    cursor: str = None
    node: User = None
    permission: RepositoryPermission = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node, permission=self.permission)



class LanguageOrder(node):
    """
    Ordering options for language connections.
    """

    """
    The ordering direction.
    """
    direction: OrderDirection = None
    """
    The field to order languages by.
    """
    field: LanguageOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class LanguageOrderField(node):
    """
    Properties by which language connections can be ordered.
    """

    __enum__ = True
    """
    Order languages by the size of all files containing the language
    """
    SIZE = "SIZE"

    def render(self):
        return dict()



class RefConnection(node):
    """
    The connection type for Ref.
    """

    edges: RefEdge = None
    nodes: Ref = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class RefEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Ref = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class RefOrder(node):
    """
    Ways in which lists of git refs can be ordered upon return.
    """

    """
    The direction in which to order refs by the specified field.
    """
    direction: OrderDirection = None
    """
    The field in which to order refs by.
    """
    field: RefOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class RefOrderField(node):
    """
    Properties by which ref connections can be ordered.
    """

    __enum__ = True
    """
    Order refs by underlying commit date if the ref prefix is refs/tags/
    """
    TAG_COMMIT_DATE = "TAG_COMMIT_DATE"
    """
    Order refs by their alphanumeric name
    """
    ALPHABETICAL = "ALPHABETICAL"

    def render(self):
        return dict()



class ReleaseConnection(node):
    """
    The connection type for Release.
    """

    edges: ReleaseEdge = None
    nodes: Release = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class ReleaseEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Release = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class ReleaseOrder(node):
    """
    Ways in which lists of releases can be ordered upon return.
    """

    """
    The direction in which to order releases by the specified field.
    """
    direction: OrderDirection = None
    """
    The field in which to order releases by.
    """
    field: ReleaseOrderField = None

    def render(self):
        return dict(direction=self.direction, field=self.field)



class ReleaseOrderField(node):
    """
    Properties by which release connections can be ordered.
    """

    __enum__ = True
    """
    Order releases by creation time
    """
    CREATED_AT = "CREATED_AT"
    """
    Order releases alphabetically by name
    """
    NAME = "NAME"

    def render(self):
        return dict()



class DeploymentConnection(node):
    """
    The connection type for Deployment.
    """

    edges: DeploymentEdge = None
    nodes: Deployment = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class DeploymentEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Deployment = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class GitSSHRemote(str):
    """
    Git SSH string
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "GitSSHRemote"


class TopicConnection(node):
    """
    The connection type for Topic.
    """

    edges: TopicEdge = None
    nodes: Topic = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class TopicEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: Topic = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class RepositoryContributionType(node):
    """
    The reason a repository is listed as 'contributed'.
    """

    __enum__ = True
    """
    Created a commit
    """
    COMMIT = "COMMIT"
    """
    Created an issue
    """
    ISSUE = "ISSUE"
    """
    Created a pull request
    """
    PULL_REQUEST = "PULL_REQUEST"
    """
    Created the repository
    """
    REPOSITORY = "REPOSITORY"
    """
    Reviewed a pull request
    """
    PULL_REQUEST_REVIEW = "PULL_REQUEST_REVIEW"

    def render(self):
        return dict()



class PublicKeyConnection(node):
    """
    The connection type for PublicKey.
    """

    edges: PublicKeyEdge = None
    nodes: PublicKey = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class PublicKeyEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: PublicKey = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class PublicKey(node):
    """
    A user's public key.
    """

    id: ID = None
    key: str = None

    def render(self):
        return dict(id=self.id, key=self.key)



class FollowingConnection(node):
    """
    The connection type for User.
    """

    edges: UserEdge = None
    nodes: User = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class FollowerConnection(node):
    """
    The connection type for User.
    """

    edges: UserEdge = None
    nodes: User = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class StarredRepositoryConnection(node):
    """
    The connection type for Repository.
    """

    edges: StarredRepositoryEdge = None
    nodes: Repository = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class StarredRepositoryEdge(node):
    """
    Represents a starred repository.
    """

    cursor: str = None
    node: Repository = None
    starredAt: DateTime = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node, starredAt=self.starredAt)



class RateLimit(node):
    """
    Represents the client's rate limit.
    """

    cost: int = None
    limit: int = None
    nodeCount: int = None
    remaining: int = None
    resetAt: DateTime = None

    def render(self):
        return dict(cost=self.cost, limit=self.limit, nodeCount=self.nodeCount, remaining=self.remaining, resetAt=self.resetAt)



class SearchResultItemConnection(node):
    """
    A list of results that matched against a search query.
    """

    codeCount: int = None
    edges: SearchResultItemEdge = None
    issueCount: int = None
    nodes: SearchResultItem = None
    pageInfo: PageInfo = None
    repositoryCount: int = None
    userCount: int = None
    wikiCount: int = None

    def render(self):
        return dict(codeCount=self.codeCount, edges=self.edges, issueCount=self.issueCount, nodes=self.nodes, pageInfo=self.pageInfo, repositoryCount=self.repositoryCount, userCount=self.userCount, wikiCount=self.wikiCount)



class SearchResultItemEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: SearchResultItem = None
    textMatches: TextMatch = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node, textMatches=self.textMatches)



class SearchResultItem(str):
    """
    The results of a search.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "SearchResultItem"


class TextMatch(node):
    """
    A text match within a search result.
    """

    fragment: str = None
    highlights: None = None
    property: str = None

    def render(self):
        return dict(fragment=self.fragment, highlights=self.highlights, property=self.property)



class TextMatchHighlight(node):
    """
    Represents a single highlight in a search result match.
    """

    beginIndice: int = None
    endIndice: int = None
    text: str = None

    def render(self):
        return dict(beginIndice=self.beginIndice, endIndice=self.endIndice, text=self.text)



class SearchType(node):
    """
    Represents the individual results of a search.
    """

    __enum__ = True
    """
    Returns results matching issues in repositories.
    """
    ISSUE = "ISSUE"
    """
    Returns results matching repositories.
    """
    REPOSITORY = "REPOSITORY"
    """
    Returns results matching users and organizations on GitHub.
    """
    USER = "USER"

    def render(self):
        return dict()



class MarketplaceListingConnection(node):
    """
    Look up Marketplace Listings
    """

    edges: MarketplaceListingEdge = None
    nodes: MarketplaceListing = None
    pageInfo: PageInfo = None
    totalCount: int = None

    def render(self):
        return dict(edges=self.edges, nodes=self.nodes, pageInfo=self.pageInfo, totalCount=self.totalCount)



class MarketplaceListingEdge(node):
    """
    An edge in a connection.
    """

    cursor: str = None
    node: MarketplaceListing = None

    def render(self):
        return dict(cursor=self.cursor, node=self.node)



class CollectionItemContent(str):
    """
    Types that can be inside Collection Items.
    """


    def render(self):
        return self

    @classmethod
    def F(self):
        return "CollectionItemContent"


class GitHubMetadata(node):
    """
    Represents information about the GitHub instance.
    """

    gitHubServicesSha: str = None
    gitIpAddresses: str = None
    hookIpAddresses: str = None
    importerIpAddresses: str = None
    isPasswordAuthenticationVerifiable: bool = None
    pagesIpAddresses: str = None

    def render(self):
        return dict(gitHubServicesSha=self.gitHubServicesSha, gitIpAddresses=self.gitIpAddresses, hookIpAddresses=self.hookIpAddresses, importerIpAddresses=self.importerIpAddresses, isPasswordAuthenticationVerifiable=self.isPasswordAuthenticationVerifiable, pagesIpAddresses=self.pagesIpAddresses)



class Mutation(node):
    """
    The root query for implementing GraphQL mutations.
    """


    def acceptTopicSuggestion(self, input:AcceptTopicSuggestionInput) -> AcceptTopicSuggestionPayload:
        """
        Applies a suggested topic to the repository.
        """
        tmpl = "acceptTopicSuggestion(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AcceptTopicSuggestionPayload.F())

    def addComment(self, input:AddCommentInput) -> AddCommentPayload:
        """
        Adds a comment to an Issue or Pull Request.
        """
        tmpl = "addComment(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AddCommentPayload.F())

    def addProjectCard(self, input:AddProjectCardInput) -> AddProjectCardPayload:
        """
        Adds a card to a ProjectColumn. Either `contentId` or `note` must be provided but **not** both.
        """
        tmpl = "addProjectCard(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AddProjectCardPayload.F())

    def addProjectColumn(self, input:AddProjectColumnInput) -> AddProjectColumnPayload:
        """
        Adds a column to a Project.
        """
        tmpl = "addProjectColumn(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AddProjectColumnPayload.F())

    def addPullRequestReview(self, input:AddPullRequestReviewInput) -> AddPullRequestReviewPayload:
        """
        Adds a review to a Pull Request.
        """
        tmpl = "addPullRequestReview(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AddPullRequestReviewPayload.F())

    def addPullRequestReviewComment(self, input:AddPullRequestReviewCommentInput) -> AddPullRequestReviewCommentPayload:
        """
        Adds a comment to a review.
        """
        tmpl = "addPullRequestReviewComment(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AddPullRequestReviewCommentPayload.F())

    def addReaction(self, input:AddReactionInput) -> AddReactionPayload:
        """
        Adds a reaction to a subject.
        """
        tmpl = "addReaction(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AddReactionPayload.F())

    def addStar(self, input:AddStarInput) -> AddStarPayload:
        """
        Adds a star to a Starrable.
        """
        tmpl = "addStar(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=AddStarPayload.F())

    def createProject(self, input:CreateProjectInput) -> CreateProjectPayload:
        """
        Creates a new project.
        """
        tmpl = "createProject(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=CreateProjectPayload.F())

    def declineTopicSuggestion(self, input:DeclineTopicSuggestionInput) -> DeclineTopicSuggestionPayload:
        """
        Rejects a suggested topic for the repository.
        """
        tmpl = "declineTopicSuggestion(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=DeclineTopicSuggestionPayload.F())

    def deleteProject(self, input:DeleteProjectInput) -> DeleteProjectPayload:
        """
        Deletes a project.
        """
        tmpl = "deleteProject(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=DeleteProjectPayload.F())

    def deleteProjectCard(self, input:DeleteProjectCardInput) -> DeleteProjectCardPayload:
        """
        Deletes a project card.
        """
        tmpl = "deleteProjectCard(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=DeleteProjectCardPayload.F())

    def deleteProjectColumn(self, input:DeleteProjectColumnInput) -> DeleteProjectColumnPayload:
        """
        Deletes a project column.
        """
        tmpl = "deleteProjectColumn(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=DeleteProjectColumnPayload.F())

    def deletePullRequestReview(self, input:DeletePullRequestReviewInput) -> DeletePullRequestReviewPayload:
        """
        Deletes a pull request review.
        """
        tmpl = "deletePullRequestReview(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=DeletePullRequestReviewPayload.F())

    def dismissPullRequestReview(self, input:DismissPullRequestReviewInput) -> DismissPullRequestReviewPayload:
        """
        Dismisses an approved or rejected pull request review.
        """
        tmpl = "dismissPullRequestReview(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=DismissPullRequestReviewPayload.F())

    def lockLockable(self, input:LockLockableInput) -> LockLockablePayload:
        """
        Lock a lockable object
        """
        tmpl = "lockLockable(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=LockLockablePayload.F())

    def moveProjectCard(self, input:MoveProjectCardInput) -> MoveProjectCardPayload:
        """
        Moves a project card to another place.
        """
        tmpl = "moveProjectCard(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=MoveProjectCardPayload.F())

    def moveProjectColumn(self, input:MoveProjectColumnInput) -> MoveProjectColumnPayload:
        """
        Moves a project column to another place.
        """
        tmpl = "moveProjectColumn(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=MoveProjectColumnPayload.F())

    def removeOutsideCollaborator(self, input:RemoveOutsideCollaboratorInput) -> RemoveOutsideCollaboratorPayload:
        """
        Removes outside collaborator from all repositories in an organization.
        """
        tmpl = "removeOutsideCollaborator(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=RemoveOutsideCollaboratorPayload.F())

    def removeReaction(self, input:RemoveReactionInput) -> RemoveReactionPayload:
        """
        Removes a reaction from a subject.
        """
        tmpl = "removeReaction(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=RemoveReactionPayload.F())

    def removeStar(self, input:RemoveStarInput) -> RemoveStarPayload:
        """
        Removes a star from a Starrable.
        """
        tmpl = "removeStar(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=RemoveStarPayload.F())

    def requestReviews(self, input:RequestReviewsInput) -> RequestReviewsPayload:
        """
        Set review requests on a pull request.
        """
        tmpl = "requestReviews(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=RequestReviewsPayload.F())

    def submitPullRequestReview(self, input:SubmitPullRequestReviewInput) -> SubmitPullRequestReviewPayload:
        """
        Submits a pending pull request review.
        """
        tmpl = "submitPullRequestReview(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=SubmitPullRequestReviewPayload.F())

    def updateProject(self, input:UpdateProjectInput) -> UpdateProjectPayload:
        """
        Updates an existing project.
        """
        tmpl = "updateProject(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=UpdateProjectPayload.F())

    def updateProjectCard(self, input:UpdateProjectCardInput) -> UpdateProjectCardPayload:
        """
        Updates an existing project card.
        """
        tmpl = "updateProjectCard(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=UpdateProjectCardPayload.F())

    def updateProjectColumn(self, input:UpdateProjectColumnInput) -> UpdateProjectColumnPayload:
        """
        Updates an existing project column.
        """
        tmpl = "updateProjectColumn(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=UpdateProjectColumnPayload.F())

    def updatePullRequestReview(self, input:UpdatePullRequestReviewInput) -> UpdatePullRequestReviewPayload:
        """
        Updates the body of a pull request review.
        """
        tmpl = "updatePullRequestReview(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=UpdatePullRequestReviewPayload.F())

    def updatePullRequestReviewComment(self, input:UpdatePullRequestReviewCommentInput) -> UpdatePullRequestReviewCommentPayload:
        """
        Updates a pull request review comment.
        """
        tmpl = "updatePullRequestReviewComment(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=UpdatePullRequestReviewCommentPayload.F())

    def updateSubscription(self, input:UpdateSubscriptionInput) -> UpdateSubscriptionPayload:
        """
        Updates viewers repository subscription state.
        """
        tmpl = "updateSubscription(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=UpdateSubscriptionPayload.F())

    def updateTopics(self, input:UpdateTopicsInput) -> UpdateTopicsPayload:
        """
        Replaces the repository's topics with the given topics.
        """
        tmpl = "updateTopics(input:%(input)s) %(ret)s"
        return self.wrap(tmpl, fn=True, input=input, ret=UpdateTopicsPayload.F())

    def render(self):
        return dict()



class AddReactionPayload(node):
    """
    Autogenerated return type of AddReaction
    """

    clientMutationId: str = None
    reaction: Reaction = None
    subject: Reactable = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, reaction=self.reaction, subject=self.subject)



class AddReactionInput(node):
    """
    Autogenerated input type of AddReaction
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of the emoji to react with.
    """
    content: ReactionContent = None
    """
    The Node ID of the subject to modify.
    """
    subjectId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, content=self.content, subjectId=self.subjectId)



class RemoveReactionPayload(node):
    """
    Autogenerated return type of RemoveReaction
    """

    clientMutationId: str = None
    reaction: Reaction = None
    subject: Reactable = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, reaction=self.reaction, subject=self.subject)



class RemoveReactionInput(node):
    """
    Autogenerated input type of RemoveReaction
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of the emoji to react with.
    """
    content: ReactionContent = None
    """
    The Node ID of the subject to modify.
    """
    subjectId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, content=self.content, subjectId=self.subjectId)



class UpdateSubscriptionPayload(node):
    """
    Autogenerated return type of UpdateSubscription
    """

    clientMutationId: str = None
    subscribable: Subscribable = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, subscribable=self.subscribable)



class UpdateSubscriptionInput(node):
    """
    Autogenerated input type of UpdateSubscription
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The new state of the subscription.
    """
    state: SubscriptionState = None
    """
    The Node ID of the subscribable object to modify.
    """
    subscribableId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, state=self.state, subscribableId=self.subscribableId)



class AddCommentPayload(node):
    """
    Autogenerated return type of AddComment
    """

    clientMutationId: str = None
    commentEdge: IssueCommentEdge = None
    subject: Node = None
    timelineEdge: IssueTimelineItemEdge = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, commentEdge=self.commentEdge, subject=self.subject, timelineEdge=self.timelineEdge)



class AddCommentInput(node):
    """
    Autogenerated input type of AddComment
    """

    """
    The contents of the comment.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Node ID of the subject to modify.
    """
    subjectId: ID = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, subjectId=self.subjectId)



class CreateProjectPayload(node):
    """
    Autogenerated return type of CreateProject
    """

    clientMutationId: str = None
    project: Project = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, project=self.project)



class CreateProjectInput(node):
    """
    Autogenerated input type of CreateProject
    """

    """
    The description of project.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of project.
    """
    name: str = None
    """
    The owner ID to create the project under.
    """
    ownerId: ID = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, name=self.name, ownerId=self.ownerId)



class UpdateProjectPayload(node):
    """
    Autogenerated return type of UpdateProject
    """

    clientMutationId: str = None
    project: Project = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, project=self.project)



class UpdateProjectInput(node):
    """
    Autogenerated input type of UpdateProject
    """

    """
    The description of project.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of project.
    """
    name: str = None
    """
    The Project ID to update.
    """
    projectId: ID = None
    """
    Whether the project is public or not.
    """
    public: bool = None
    """
    Whether the project is open or closed.
    """
    state: ProjectState = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, name=self.name, projectId=self.projectId, public=self.public, state=self.state)



class DeleteProjectPayload(node):
    """
    Autogenerated return type of DeleteProject
    """

    clientMutationId: str = None
    owner: ProjectOwner = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, owner=self.owner)



class DeleteProjectInput(node):
    """
    Autogenerated input type of DeleteProject
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Project ID to update.
    """
    projectId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, projectId=self.projectId)



class AddProjectColumnPayload(node):
    """
    Autogenerated return type of AddProjectColumn
    """

    clientMutationId: str = None
    columnEdge: ProjectColumnEdge = None
    project: Project = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, columnEdge=self.columnEdge, project=self.project)



class AddProjectColumnInput(node):
    """
    Autogenerated input type of AddProjectColumn
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of the column.
    """
    name: str = None
    """
    The Node ID of the project.
    """
    projectId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, name=self.name, projectId=self.projectId)



class MoveProjectColumnPayload(node):
    """
    Autogenerated return type of MoveProjectColumn
    """

    clientMutationId: str = None
    columnEdge: ProjectColumnEdge = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, columnEdge=self.columnEdge)



class MoveProjectColumnInput(node):
    """
    Autogenerated input type of MoveProjectColumn
    """

    """
    Place the new column after the column with this id. Pass null to place it at the front.
    """
    afterColumnId: ID = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The id of the column to move.
    """
    columnId: ID = None

    def render(self):
        return dict(afterColumnId=self.afterColumnId, clientMutationId=self.clientMutationId, columnId=self.columnId)



class UpdateProjectColumnPayload(node):
    """
    Autogenerated return type of UpdateProjectColumn
    """

    clientMutationId: str = None
    projectColumn: ProjectColumn = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, projectColumn=self.projectColumn)



class UpdateProjectColumnInput(node):
    """
    Autogenerated input type of UpdateProjectColumn
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of project column.
    """
    name: str = None
    """
    The ProjectColumn ID to update.
    """
    projectColumnId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, name=self.name, projectColumnId=self.projectColumnId)



class DeleteProjectColumnPayload(node):
    """
    Autogenerated return type of DeleteProjectColumn
    """

    clientMutationId: str = None
    deletedColumnId: ID = None
    project: Project = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, deletedColumnId=self.deletedColumnId, project=self.project)



class DeleteProjectColumnInput(node):
    """
    Autogenerated input type of DeleteProjectColumn
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The id of the column to delete.
    """
    columnId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, columnId=self.columnId)



class AddProjectCardPayload(node):
    """
    Autogenerated return type of AddProjectCard
    """

    cardEdge: ProjectCardEdge = None
    clientMutationId: str = None
    projectColumn: Project = None

    def render(self):
        return dict(cardEdge=self.cardEdge, clientMutationId=self.clientMutationId, projectColumn=self.projectColumn)



class AddProjectCardInput(node):
    """
    Autogenerated input type of AddProjectCard
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The content of the card. Must be a member of the ProjectCardItem union
    """
    contentId: ID = None
    """
    The note on the card.
    """
    note: str = None
    """
    The Node ID of the ProjectColumn.
    """
    projectColumnId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, contentId=self.contentId, note=self.note, projectColumnId=self.projectColumnId)



class UpdateProjectCardPayload(node):
    """
    Autogenerated return type of UpdateProjectCard
    """

    clientMutationId: str = None
    projectCard: ProjectCard = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, projectCard=self.projectCard)



class UpdateProjectCardInput(node):
    """
    Autogenerated input type of UpdateProjectCard
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The note of ProjectCard.
    """
    note: str = None
    """
    The ProjectCard ID to update.
    """
    projectCardId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, note=self.note, projectCardId=self.projectCardId)



class MoveProjectCardPayload(node):
    """
    Autogenerated return type of MoveProjectCard
    """

    cardEdge: ProjectCardEdge = None
    clientMutationId: str = None

    def render(self):
        return dict(cardEdge=self.cardEdge, clientMutationId=self.clientMutationId)



class MoveProjectCardInput(node):
    """
    Autogenerated input type of MoveProjectCard
    """

    """
    Place the new card after the card with this id. Pass null to place it at the top.
    """
    afterCardId: ID = None
    """
    The id of the card to move.
    """
    cardId: ID = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The id of the column to move it into.
    """
    columnId: ID = None

    def render(self):
        return dict(afterCardId=self.afterCardId, cardId=self.cardId, clientMutationId=self.clientMutationId, columnId=self.columnId)



class DeleteProjectCardPayload(node):
    """
    Autogenerated return type of DeleteProjectCard
    """

    clientMutationId: str = None
    column: ProjectColumn = None
    deletedCardId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, column=self.column, deletedCardId=self.deletedCardId)



class DeleteProjectCardInput(node):
    """
    Autogenerated input type of DeleteProjectCard
    """

    """
    The id of the card to delete.
    """
    cardId: ID = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None

    def render(self):
        return dict(cardId=self.cardId, clientMutationId=self.clientMutationId)



class LockLockablePayload(node):
    """
    Autogenerated return type of LockLockable
    """

    clientMutationId: str = None
    lockedRecord: Lockable = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, lockedRecord=self.lockedRecord)



class LockLockableInput(node):
    """
    Autogenerated input type of LockLockable
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    A reason for why the issue or pull request will be locked.
    """
    lockReason: LockReason = None
    """
    ID of the issue or pull request to be locked.
    """
    lockableId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, lockReason=self.lockReason, lockableId=self.lockableId)



class AddPullRequestReviewPayload(node):
    """
    Autogenerated return type of AddPullRequestReview
    """

    clientMutationId: str = None
    pullRequestReview: PullRequestReview = None
    reviewEdge: PullRequestReviewEdge = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestReview=self.pullRequestReview, reviewEdge=self.reviewEdge)



class AddPullRequestReviewInput(node):
    """
    Autogenerated input type of AddPullRequestReview
    """

    """
    The contents of the review body comment.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The review line comments.
    """
    comments: DraftPullRequestReviewComment = None
    """
    The commit OID the review pertains to.
    """
    commitOID: GitObjectID = None
    """
    The event to perform on the pull request review.
    """
    event: PullRequestReviewEvent = None
    """
    The Node ID of the pull request to modify.
    """
    pullRequestId: ID = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, comments=self.comments, commitOID=self.commitOID, event=self.event, pullRequestId=self.pullRequestId)



class PullRequestReviewEvent(node):
    """
    The possible events to perform on a pull request review.
    """

    __enum__ = True
    """
    Submit general feedback without explicit approval.
    """
    COMMENT = "COMMENT"
    """
    Submit feedback and approve merging these changes.
    """
    APPROVE = "APPROVE"
    """
    Submit feedback that must be addressed before merging.
    """
    REQUEST_CHANGES = "REQUEST_CHANGES"
    """
    Dismiss review so it now longer effects merging.
    """
    DISMISS = "DISMISS"

    def render(self):
        return dict()



class DraftPullRequestReviewComment(node):
    """
    Specifies a review comment to be left with a Pull Request Review.
    """

    """
    Body of the comment to leave.
    """
    body: str = None
    """
    Path to the file being commented on.
    """
    path: str = None
    """
    Position in the file to leave a comment on.
    """
    position: int = None

    def render(self):
        return dict(body=self.body, path=self.path, position=self.position)



class SubmitPullRequestReviewPayload(node):
    """
    Autogenerated return type of SubmitPullRequestReview
    """

    clientMutationId: str = None
    pullRequestReview: PullRequestReview = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestReview=self.pullRequestReview)



class SubmitPullRequestReviewInput(node):
    """
    Autogenerated input type of SubmitPullRequestReview
    """

    """
    The text field to set on the Pull Request Review.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The event to send to the Pull Request Review.
    """
    event: PullRequestReviewEvent = None
    """
    The Pull Request Review ID to submit.
    """
    pullRequestReviewId: ID = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, event=self.event, pullRequestReviewId=self.pullRequestReviewId)



class UpdatePullRequestReviewPayload(node):
    """
    Autogenerated return type of UpdatePullRequestReview
    """

    clientMutationId: str = None
    pullRequestReview: PullRequestReview = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestReview=self.pullRequestReview)



class UpdatePullRequestReviewInput(node):
    """
    Autogenerated input type of UpdatePullRequestReview
    """

    """
    The contents of the pull request review body.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Node ID of the pull request review to modify.
    """
    pullRequestReviewId: ID = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, pullRequestReviewId=self.pullRequestReviewId)



class DismissPullRequestReviewPayload(node):
    """
    Autogenerated return type of DismissPullRequestReview
    """

    clientMutationId: str = None
    pullRequestReview: PullRequestReview = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestReview=self.pullRequestReview)



class DismissPullRequestReviewInput(node):
    """
    Autogenerated input type of DismissPullRequestReview
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The contents of the pull request review dismissal message.
    """
    message: str = None
    """
    The Node ID of the pull request review to modify.
    """
    pullRequestReviewId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, message=self.message, pullRequestReviewId=self.pullRequestReviewId)



class DeletePullRequestReviewPayload(node):
    """
    Autogenerated return type of DeletePullRequestReview
    """

    clientMutationId: str = None
    pullRequestReview: PullRequestReview = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestReview=self.pullRequestReview)



class DeletePullRequestReviewInput(node):
    """
    Autogenerated input type of DeletePullRequestReview
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Node ID of the pull request review to delete.
    """
    pullRequestReviewId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestReviewId=self.pullRequestReviewId)



class AddPullRequestReviewCommentPayload(node):
    """
    Autogenerated return type of AddPullRequestReviewComment
    """

    clientMutationId: str = None
    comment: PullRequestReviewComment = None
    commentEdge: PullRequestReviewCommentEdge = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, comment=self.comment, commentEdge=self.commentEdge)



class AddPullRequestReviewCommentInput(node):
    """
    Autogenerated input type of AddPullRequestReviewComment
    """

    """
    The text of the comment.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The SHA of the commit to comment on.
    """
    commitOID: GitObjectID = None
    """
    The comment id to reply to.
    """
    inReplyTo: ID = None
    """
    The relative path of the file to comment on.
    """
    path: str = None
    """
    The line index in the diff to comment on.
    """
    position: int = None
    """
    The Node ID of the review to modify.
    """
    pullRequestReviewId: ID = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, commitOID=self.commitOID, inReplyTo=self.inReplyTo, path=self.path, position=self.position, pullRequestReviewId=self.pullRequestReviewId)



class UpdatePullRequestReviewCommentPayload(node):
    """
    Autogenerated return type of UpdatePullRequestReviewComment
    """

    clientMutationId: str = None
    pullRequestReviewComment: PullRequestReviewComment = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestReviewComment=self.pullRequestReviewComment)



class UpdatePullRequestReviewCommentInput(node):
    """
    Autogenerated input type of UpdatePullRequestReviewComment
    """

    """
    The text of the comment.
    """
    body: str = None
    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Node ID of the comment to modify.
    """
    pullRequestReviewCommentId: ID = None

    def render(self):
        return dict(body=self.body, clientMutationId=self.clientMutationId, pullRequestReviewCommentId=self.pullRequestReviewCommentId)



class RemoveOutsideCollaboratorPayload(node):
    """
    Autogenerated return type of RemoveOutsideCollaborator
    """

    clientMutationId: str = None
    removedUser: User = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, removedUser=self.removedUser)



class RemoveOutsideCollaboratorInput(node):
    """
    Autogenerated input type of RemoveOutsideCollaborator
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The ID of the organization to remove the outside collaborator from.
    """
    organizationId: ID = None
    """
    The ID of the outside collaborator to remove.
    """
    userId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, organizationId=self.organizationId, userId=self.userId)



class RequestReviewsPayload(node):
    """
    Autogenerated return type of RequestReviews
    """

    clientMutationId: str = None
    pullRequest: PullRequest = None
    requestedReviewersEdge: UserEdge = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequest=self.pullRequest, requestedReviewersEdge=self.requestedReviewersEdge)



class RequestReviewsInput(node):
    """
    Autogenerated input type of RequestReviews
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Node ID of the pull request to modify.
    """
    pullRequestId: ID = None
    """
    The Node IDs of the team to request.
    """
    teamIds: ID = None
    """
    Add users to the set rather than replace.
    """
    union: bool = None
    """
    The Node IDs of the user to request.
    """
    userIds: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, pullRequestId=self.pullRequestId, teamIds=self.teamIds, union=self.union, userIds=self.userIds)



class AddStarPayload(node):
    """
    Autogenerated return type of AddStar
    """

    clientMutationId: str = None
    starrable: Starrable = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, starrable=self.starrable)



class AddStarInput(node):
    """
    Autogenerated input type of AddStar
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Starrable ID to star.
    """
    starrableId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, starrableId=self.starrableId)



class RemoveStarPayload(node):
    """
    Autogenerated return type of RemoveStar
    """

    clientMutationId: str = None
    starrable: Starrable = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, starrable=self.starrable)



class RemoveStarInput(node):
    """
    Autogenerated input type of RemoveStar
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Starrable ID to unstar.
    """
    starrableId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, starrableId=self.starrableId)



class AcceptTopicSuggestionPayload(node):
    """
    Autogenerated return type of AcceptTopicSuggestion
    """

    clientMutationId: str = None
    topic: Topic = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, topic=self.topic)



class AcceptTopicSuggestionInput(node):
    """
    Autogenerated input type of AcceptTopicSuggestion
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of the suggested topic.
    """
    name: str = None
    """
    The Node ID of the repository.
    """
    repositoryId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, name=self.name, repositoryId=self.repositoryId)



class DeclineTopicSuggestionPayload(node):
    """
    Autogenerated return type of DeclineTopicSuggestion
    """

    clientMutationId: str = None
    topic: Topic = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, topic=self.topic)



class DeclineTopicSuggestionInput(node):
    """
    Autogenerated input type of DeclineTopicSuggestion
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The name of the suggested topic.
    """
    name: str = None
    """
    The reason why the suggested topic is declined.
    """
    reason: TopicSuggestionDeclineReason = None
    """
    The Node ID of the repository.
    """
    repositoryId: ID = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, name=self.name, reason=self.reason, repositoryId=self.repositoryId)



class TopicSuggestionDeclineReason(node):
    """
    Reason that the suggested topic is declined.
    """

    __enum__ = True
    """
    The suggested topic is not relevant to the repository.
    """
    NOT_RELEVANT = "NOT_RELEVANT"
    """
    The suggested topic is too specific for the repository (e.g. #ruby-on-rails-version-4-2-1).
    """
    TOO_SPECIFIC = "TOO_SPECIFIC"
    """
    The viewer does not like the suggested topic.
    """
    PERSONAL_PREFERENCE = "PERSONAL_PREFERENCE"
    """
    The suggested topic is too general for the repository.
    """
    TOO_GENERAL = "TOO_GENERAL"

    def render(self):
        return dict()



class UpdateTopicsPayload(node):
    """
    Autogenerated return type of UpdateTopics
    """

    clientMutationId: str = None
    invalidTopicNames: str = None
    repository: Repository = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, invalidTopicNames=self.invalidTopicNames, repository=self.repository)



class UpdateTopicsInput(node):
    """
    Autogenerated input type of UpdateTopics
    """

    """
    A unique identifier for the client performing the mutation.
    """
    clientMutationId: str = None
    """
    The Node ID of the repository.
    """
    repositoryId: ID = None
    """
    An array of topic names.
    """
    topicNames: None = None

    def render(self):
        return dict(clientMutationId=self.clientMutationId, repositoryId=self.repositoryId, topicNames=self.topicNames)



class GpgSignature(node):
    """
    Represents a GPG signature on a Commit or Tag.
    """

    email: str = None
    isValid: bool = None
    keyId: str = None
    payload: str = None
    signature: str = None
    signer: User = None
    state: GitSignatureState = None

    def render(self):
        return dict(email=self.email, isValid=self.isValid, keyId=self.keyId, payload=self.payload, signature=self.signature, signer=self.signer, state=self.state)



class SmimeSignature(node):
    """
    Represents an S/MIME signature on a Commit or Tag.
    """

    email: str = None
    isValid: bool = None
    payload: str = None
    signature: str = None
    signer: User = None
    state: GitSignatureState = None

    def render(self):
        return dict(email=self.email, isValid=self.isValid, payload=self.payload, signature=self.signature, signer=self.signer, state=self.state)



class Tag(node):
    """
    Represents a Git tag.
    """

    abbreviatedOid: str = None
    commitResourcePath: URI = None
    commitUrl: URI = None
    id: ID = None
    message: str = None
    name: str = None
    oid: GitObjectID = None
    repository: Repository = None
    tagger: GitActor = None
    target: GitObject = None

    def render(self):
        return dict(abbreviatedOid=self.abbreviatedOid, commitResourcePath=self.commitResourcePath, commitUrl=self.commitUrl, id=self.id, message=self.message, name=self.name, oid=self.oid, repository=self.repository, tagger=self.tagger, target=self.target)



class UnknownSignature(node):
    """
    Represents an unknown signature on a Commit or Tag.
    """

    email: str = None
    isValid: bool = None
    payload: str = None
    signature: str = None
    signer: User = None
    state: GitSignatureState = None

    def render(self):
        return dict(email=self.email, isValid=self.isValid, payload=self.payload, signature=self.signature, signer=self.signer, state=self.state)




query = Query()
mutation = Mutation()
