# coding: utf-8

"""
    Shortcut API

    Shortcut API  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PullRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_type': 'str',
        'closed': 'bool',
        'merged': 'bool',
        'num_added': 'int',
        'branch_id': 'int',
        'number': 'int',
        'branch_name': 'str',
        'target_branch_name': 'str',
        'num_commits': 'int',
        'title': 'str',
        'updated_at': 'datetime',
        'draft': 'bool',
        'id': 'int',
        'vcs_labels': 'list[PullRequestLabel]',
        'url': 'str',
        'num_removed': 'int',
        'review_status': 'str',
        'num_modified': 'int',
        'build_status': 'str',
        'target_branch_id': 'int',
        'repository_id': 'int',
        'created_at': 'datetime'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'closed': 'closed',
        'merged': 'merged',
        'num_added': 'num_added',
        'branch_id': 'branch_id',
        'number': 'number',
        'branch_name': 'branch_name',
        'target_branch_name': 'target_branch_name',
        'num_commits': 'num_commits',
        'title': 'title',
        'updated_at': 'updated_at',
        'draft': 'draft',
        'id': 'id',
        'vcs_labels': 'vcs_labels',
        'url': 'url',
        'num_removed': 'num_removed',
        'review_status': 'review_status',
        'num_modified': 'num_modified',
        'build_status': 'build_status',
        'target_branch_id': 'target_branch_id',
        'repository_id': 'repository_id',
        'created_at': 'created_at'
    }

    def __init__(self, entity_type=None, closed=None, merged=None, num_added=None, branch_id=None, number=None, branch_name=None, target_branch_name=None, num_commits=None, title=None, updated_at=None, draft=None, id=None, vcs_labels=None, url=None, num_removed=None, review_status=None, num_modified=None, build_status=None, target_branch_id=None, repository_id=None, created_at=None):  # noqa: E501
        """PullRequest - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._closed = None
        self._merged = None
        self._num_added = None
        self._branch_id = None
        self._number = None
        self._branch_name = None
        self._target_branch_name = None
        self._num_commits = None
        self._title = None
        self._updated_at = None
        self._draft = None
        self._id = None
        self._vcs_labels = None
        self._url = None
        self._num_removed = None
        self._review_status = None
        self._num_modified = None
        self._build_status = None
        self._target_branch_id = None
        self._repository_id = None
        self._created_at = None
        self.discriminator = None
        self.entity_type = entity_type
        self.closed = closed
        self.merged = merged
        self.num_added = num_added
        self.branch_id = branch_id
        self.number = number
        self.branch_name = branch_name
        self.target_branch_name = target_branch_name
        self.num_commits = num_commits
        self.title = title
        self.updated_at = updated_at
        self.draft = draft
        self.id = id
        if vcs_labels is not None:
            self.vcs_labels = vcs_labels
        self.url = url
        self.num_removed = num_removed
        if review_status is not None:
            self.review_status = review_status
        self.num_modified = num_modified
        if build_status is not None:
            self.build_status = build_status
        self.target_branch_id = target_branch_id
        self.repository_id = repository_id
        self.created_at = created_at

    @property
    def entity_type(self):
        """Gets the entity_type of this PullRequest.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this PullRequest.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this PullRequest.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def closed(self):
        """Gets the closed of this PullRequest.  # noqa: E501

        True/False boolean indicating whether the VCS pull request has been closed.  # noqa: E501

        :return: The closed of this PullRequest.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this PullRequest.

        True/False boolean indicating whether the VCS pull request has been closed.  # noqa: E501

        :param closed: The closed of this PullRequest.  # noqa: E501
        :type: bool
        """
        if closed is None:
            raise ValueError("Invalid value for `closed`, must not be `None`")  # noqa: E501

        self._closed = closed

    @property
    def merged(self):
        """Gets the merged of this PullRequest.  # noqa: E501

        True/False boolean indicating whether the VCS pull request has been merged.  # noqa: E501

        :return: The merged of this PullRequest.  # noqa: E501
        :rtype: bool
        """
        return self._merged

    @merged.setter
    def merged(self, merged):
        """Sets the merged of this PullRequest.

        True/False boolean indicating whether the VCS pull request has been merged.  # noqa: E501

        :param merged: The merged of this PullRequest.  # noqa: E501
        :type: bool
        """
        if merged is None:
            raise ValueError("Invalid value for `merged`, must not be `None`")  # noqa: E501

        self._merged = merged

    @property
    def num_added(self):
        """Gets the num_added of this PullRequest.  # noqa: E501

        Number of lines added in the pull request, according to VCS.  # noqa: E501

        :return: The num_added of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_added

    @num_added.setter
    def num_added(self, num_added):
        """Sets the num_added of this PullRequest.

        Number of lines added in the pull request, according to VCS.  # noqa: E501

        :param num_added: The num_added of this PullRequest.  # noqa: E501
        :type: int
        """
        if num_added is None:
            raise ValueError("Invalid value for `num_added`, must not be `None`")  # noqa: E501

        self._num_added = num_added

    @property
    def branch_id(self):
        """Gets the branch_id of this PullRequest.  # noqa: E501

        The ID of the branch for the particular pull request.  # noqa: E501

        :return: The branch_id of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this PullRequest.

        The ID of the branch for the particular pull request.  # noqa: E501

        :param branch_id: The branch_id of this PullRequest.  # noqa: E501
        :type: int
        """
        if branch_id is None:
            raise ValueError("Invalid value for `branch_id`, must not be `None`")  # noqa: E501

        self._branch_id = branch_id

    @property
    def number(self):
        """Gets the number of this PullRequest.  # noqa: E501

        The pull request's unique number ID in VCS.  # noqa: E501

        :return: The number of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PullRequest.

        The pull request's unique number ID in VCS.  # noqa: E501

        :param number: The number of this PullRequest.  # noqa: E501
        :type: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def branch_name(self):
        """Gets the branch_name of this PullRequest.  # noqa: E501

        The name of the branch for the particular pull request.  # noqa: E501

        :return: The branch_name of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this PullRequest.

        The name of the branch for the particular pull request.  # noqa: E501

        :param branch_name: The branch_name of this PullRequest.  # noqa: E501
        :type: str
        """
        if branch_name is None:
            raise ValueError("Invalid value for `branch_name`, must not be `None`")  # noqa: E501

        self._branch_name = branch_name

    @property
    def target_branch_name(self):
        """Gets the target_branch_name of this PullRequest.  # noqa: E501

        The name of the target branch for the particular pull request.  # noqa: E501

        :return: The target_branch_name of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_branch_name

    @target_branch_name.setter
    def target_branch_name(self, target_branch_name):
        """Sets the target_branch_name of this PullRequest.

        The name of the target branch for the particular pull request.  # noqa: E501

        :param target_branch_name: The target_branch_name of this PullRequest.  # noqa: E501
        :type: str
        """
        if target_branch_name is None:
            raise ValueError("Invalid value for `target_branch_name`, must not be `None`")  # noqa: E501

        self._target_branch_name = target_branch_name

    @property
    def num_commits(self):
        """Gets the num_commits of this PullRequest.  # noqa: E501

        The number of commits on the pull request.  # noqa: E501

        :return: The num_commits of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_commits

    @num_commits.setter
    def num_commits(self, num_commits):
        """Sets the num_commits of this PullRequest.

        The number of commits on the pull request.  # noqa: E501

        :param num_commits: The num_commits of this PullRequest.  # noqa: E501
        :type: int
        """
        if num_commits is None:
            raise ValueError("Invalid value for `num_commits`, must not be `None`")  # noqa: E501

        self._num_commits = num_commits

    @property
    def title(self):
        """Gets the title of this PullRequest.  # noqa: E501

        The title of the pull request.  # noqa: E501

        :return: The title of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PullRequest.

        The title of the pull request.  # noqa: E501

        :param title: The title of this PullRequest.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this PullRequest.  # noqa: E501

        The time/date the pull request was created.  # noqa: E501

        :return: The updated_at of this PullRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PullRequest.

        The time/date the pull request was created.  # noqa: E501

        :param updated_at: The updated_at of this PullRequest.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def draft(self):
        """Gets the draft of this PullRequest.  # noqa: E501

        True/False boolean indicating whether the VCS pull request is in the draft state.  # noqa: E501

        :return: The draft of this PullRequest.  # noqa: E501
        :rtype: bool
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this PullRequest.

        True/False boolean indicating whether the VCS pull request is in the draft state.  # noqa: E501

        :param draft: The draft of this PullRequest.  # noqa: E501
        :type: bool
        """
        if draft is None:
            raise ValueError("Invalid value for `draft`, must not be `None`")  # noqa: E501

        self._draft = draft

    @property
    def id(self):
        """Gets the id of this PullRequest.  # noqa: E501

        The unique ID associated with the pull request in Shortcut.  # noqa: E501

        :return: The id of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PullRequest.

        The unique ID associated with the pull request in Shortcut.  # noqa: E501

        :param id: The id of this PullRequest.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def vcs_labels(self):
        """Gets the vcs_labels of this PullRequest.  # noqa: E501

        An array of PullRequestLabels attached to the PullRequest.  # noqa: E501

        :return: The vcs_labels of this PullRequest.  # noqa: E501
        :rtype: list[PullRequestLabel]
        """
        return self._vcs_labels

    @vcs_labels.setter
    def vcs_labels(self, vcs_labels):
        """Sets the vcs_labels of this PullRequest.

        An array of PullRequestLabels attached to the PullRequest.  # noqa: E501

        :param vcs_labels: The vcs_labels of this PullRequest.  # noqa: E501
        :type: list[PullRequestLabel]
        """

        self._vcs_labels = vcs_labels

    @property
    def url(self):
        """Gets the url of this PullRequest.  # noqa: E501

        The URL for the pull request.  # noqa: E501

        :return: The url of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PullRequest.

        The URL for the pull request.  # noqa: E501

        :param url: The url of this PullRequest.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def num_removed(self):
        """Gets the num_removed of this PullRequest.  # noqa: E501

        Number of lines removed in the pull request, according to VCS.  # noqa: E501

        :return: The num_removed of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_removed

    @num_removed.setter
    def num_removed(self, num_removed):
        """Sets the num_removed of this PullRequest.

        Number of lines removed in the pull request, according to VCS.  # noqa: E501

        :param num_removed: The num_removed of this PullRequest.  # noqa: E501
        :type: int
        """
        if num_removed is None:
            raise ValueError("Invalid value for `num_removed`, must not be `None`")  # noqa: E501

        self._num_removed = num_removed

    @property
    def review_status(self):
        """Gets the review_status of this PullRequest.  # noqa: E501

        The status of the review for the pull request.  # noqa: E501

        :return: The review_status of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this PullRequest.

        The status of the review for the pull request.  # noqa: E501

        :param review_status: The review_status of this PullRequest.  # noqa: E501
        :type: str
        """

        self._review_status = review_status

    @property
    def num_modified(self):
        """Gets the num_modified of this PullRequest.  # noqa: E501

        Number of lines modified in the pull request, according to VCS.  # noqa: E501

        :return: The num_modified of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_modified

    @num_modified.setter
    def num_modified(self, num_modified):
        """Sets the num_modified of this PullRequest.

        Number of lines modified in the pull request, according to VCS.  # noqa: E501

        :param num_modified: The num_modified of this PullRequest.  # noqa: E501
        :type: int
        """
        if num_modified is None:
            raise ValueError("Invalid value for `num_modified`, must not be `None`")  # noqa: E501

        self._num_modified = num_modified

    @property
    def build_status(self):
        """Gets the build_status of this PullRequest.  # noqa: E501

        The status of the Continuous Integration workflow for the pull request.  # noqa: E501

        :return: The build_status of this PullRequest.  # noqa: E501
        :rtype: str
        """
        return self._build_status

    @build_status.setter
    def build_status(self, build_status):
        """Sets the build_status of this PullRequest.

        The status of the Continuous Integration workflow for the pull request.  # noqa: E501

        :param build_status: The build_status of this PullRequest.  # noqa: E501
        :type: str
        """

        self._build_status = build_status

    @property
    def target_branch_id(self):
        """Gets the target_branch_id of this PullRequest.  # noqa: E501

        The ID of the target branch for the particular pull request.  # noqa: E501

        :return: The target_branch_id of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._target_branch_id

    @target_branch_id.setter
    def target_branch_id(self, target_branch_id):
        """Sets the target_branch_id of this PullRequest.

        The ID of the target branch for the particular pull request.  # noqa: E501

        :param target_branch_id: The target_branch_id of this PullRequest.  # noqa: E501
        :type: int
        """
        if target_branch_id is None:
            raise ValueError("Invalid value for `target_branch_id`, must not be `None`")  # noqa: E501

        self._target_branch_id = target_branch_id

    @property
    def repository_id(self):
        """Gets the repository_id of this PullRequest.  # noqa: E501

        The ID of the repository for the particular pull request.  # noqa: E501

        :return: The repository_id of this PullRequest.  # noqa: E501
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this PullRequest.

        The ID of the repository for the particular pull request.  # noqa: E501

        :param repository_id: The repository_id of this PullRequest.  # noqa: E501
        :type: int
        """
        if repository_id is None:
            raise ValueError("Invalid value for `repository_id`, must not be `None`")  # noqa: E501

        self._repository_id = repository_id

    @property
    def created_at(self):
        """Gets the created_at of this PullRequest.  # noqa: E501

        The time/date the pull request was created.  # noqa: E501

        :return: The created_at of this PullRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PullRequest.

        The time/date the pull request was created.  # noqa: E501

        :param created_at: The created_at of this PullRequest.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PullRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PullRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
