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

class UpdateStory(object):
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
        'description': 'str',
        'archived': 'bool',
        'labels': 'list[CreateLabelParams]',
        'pull_request_ids': 'list[int]',
        'story_type': 'str',
        'custom_fields': 'list[CustomFieldValueParams]',
        'move_to': 'str',
        'file_ids': 'list[int]',
        'completed_at_override': 'datetime',
        'name': 'str',
        'epic_id': 'int',
        'external_links': 'list[str]',
        'branch_ids': 'list[int]',
        'commit_ids': 'list[int]',
        'requested_by_id': 'str',
        'iteration_id': 'int',
        'started_at_override': 'datetime',
        'group_id': 'str',
        'workflow_state_id': 'int',
        'follower_ids': 'list[str]',
        'owner_ids': 'list[str]',
        'before_id': 'int',
        'estimate': 'int',
        'after_id': 'int',
        'project_id': 'int',
        'linked_file_ids': 'list[int]',
        'deadline': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'archived': 'archived',
        'labels': 'labels',
        'pull_request_ids': 'pull_request_ids',
        'story_type': 'story_type',
        'custom_fields': 'custom_fields',
        'move_to': 'move_to',
        'file_ids': 'file_ids',
        'completed_at_override': 'completed_at_override',
        'name': 'name',
        'epic_id': 'epic_id',
        'external_links': 'external_links',
        'branch_ids': 'branch_ids',
        'commit_ids': 'commit_ids',
        'requested_by_id': 'requested_by_id',
        'iteration_id': 'iteration_id',
        'started_at_override': 'started_at_override',
        'group_id': 'group_id',
        'workflow_state_id': 'workflow_state_id',
        'follower_ids': 'follower_ids',
        'owner_ids': 'owner_ids',
        'before_id': 'before_id',
        'estimate': 'estimate',
        'after_id': 'after_id',
        'project_id': 'project_id',
        'linked_file_ids': 'linked_file_ids',
        'deadline': 'deadline'
    }

    def __init__(self, description=None, archived=None, labels=None, pull_request_ids=None, story_type=None, custom_fields=None, move_to=None, file_ids=None, completed_at_override=None, name=None, epic_id=None, external_links=None, branch_ids=None, commit_ids=None, requested_by_id=None, iteration_id=None, started_at_override=None, group_id=None, workflow_state_id=None, follower_ids=None, owner_ids=None, before_id=None, estimate=None, after_id=None, project_id=None, linked_file_ids=None, deadline=None):  # noqa: E501
        """UpdateStory - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._archived = None
        self._labels = None
        self._pull_request_ids = None
        self._story_type = None
        self._custom_fields = None
        self._move_to = None
        self._file_ids = None
        self._completed_at_override = None
        self._name = None
        self._epic_id = None
        self._external_links = None
        self._branch_ids = None
        self._commit_ids = None
        self._requested_by_id = None
        self._iteration_id = None
        self._started_at_override = None
        self._group_id = None
        self._workflow_state_id = None
        self._follower_ids = None
        self._owner_ids = None
        self._before_id = None
        self._estimate = None
        self._after_id = None
        self._project_id = None
        self._linked_file_ids = None
        self._deadline = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if archived is not None:
            self.archived = archived
        if labels is not None:
            self.labels = labels
        if pull_request_ids is not None:
            self.pull_request_ids = pull_request_ids
        if story_type is not None:
            self.story_type = story_type
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if move_to is not None:
            self.move_to = move_to
        if file_ids is not None:
            self.file_ids = file_ids
        if completed_at_override is not None:
            self.completed_at_override = completed_at_override
        if name is not None:
            self.name = name
        if epic_id is not None:
            self.epic_id = epic_id
        if external_links is not None:
            self.external_links = external_links
        if branch_ids is not None:
            self.branch_ids = branch_ids
        if commit_ids is not None:
            self.commit_ids = commit_ids
        if requested_by_id is not None:
            self.requested_by_id = requested_by_id
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if started_at_override is not None:
            self.started_at_override = started_at_override
        if group_id is not None:
            self.group_id = group_id
        if workflow_state_id is not None:
            self.workflow_state_id = workflow_state_id
        if follower_ids is not None:
            self.follower_ids = follower_ids
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if before_id is not None:
            self.before_id = before_id
        if estimate is not None:
            self.estimate = estimate
        if after_id is not None:
            self.after_id = after_id
        if project_id is not None:
            self.project_id = project_id
        if linked_file_ids is not None:
            self.linked_file_ids = linked_file_ids
        if deadline is not None:
            self.deadline = deadline

    @property
    def description(self):
        """Gets the description of this UpdateStory.  # noqa: E501

        The description of the story.  # noqa: E501

        :return: The description of this UpdateStory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateStory.

        The description of the story.  # noqa: E501

        :param description: The description of this UpdateStory.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def archived(self):
        """Gets the archived of this UpdateStory.  # noqa: E501

        True if the story is archived, otherwise false.  # noqa: E501

        :return: The archived of this UpdateStory.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this UpdateStory.

        True if the story is archived, otherwise false.  # noqa: E501

        :param archived: The archived of this UpdateStory.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def labels(self):
        """Gets the labels of this UpdateStory.  # noqa: E501

        An array of labels attached to the story.  # noqa: E501

        :return: The labels of this UpdateStory.  # noqa: E501
        :rtype: list[CreateLabelParams]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this UpdateStory.

        An array of labels attached to the story.  # noqa: E501

        :param labels: The labels of this UpdateStory.  # noqa: E501
        :type: list[CreateLabelParams]
        """

        self._labels = labels

    @property
    def pull_request_ids(self):
        """Gets the pull_request_ids of this UpdateStory.  # noqa: E501

        An array of IDs of Pull/Merge Requests attached to the story.  # noqa: E501

        :return: The pull_request_ids of this UpdateStory.  # noqa: E501
        :rtype: list[int]
        """
        return self._pull_request_ids

    @pull_request_ids.setter
    def pull_request_ids(self, pull_request_ids):
        """Sets the pull_request_ids of this UpdateStory.

        An array of IDs of Pull/Merge Requests attached to the story.  # noqa: E501

        :param pull_request_ids: The pull_request_ids of this UpdateStory.  # noqa: E501
        :type: list[int]
        """

        self._pull_request_ids = pull_request_ids

    @property
    def story_type(self):
        """Gets the story_type of this UpdateStory.  # noqa: E501

        The type of story (feature, bug, chore).  # noqa: E501

        :return: The story_type of this UpdateStory.  # noqa: E501
        :rtype: str
        """
        return self._story_type

    @story_type.setter
    def story_type(self, story_type):
        """Sets the story_type of this UpdateStory.

        The type of story (feature, bug, chore).  # noqa: E501

        :param story_type: The story_type of this UpdateStory.  # noqa: E501
        :type: str
        """
        allowed_values = ["feature", "chore", "bug"]  # noqa: E501
        if story_type not in allowed_values:
            raise ValueError(
                "Invalid value for `story_type` ({0}), must be one of {1}"  # noqa: E501
                .format(story_type, allowed_values)
            )

        self._story_type = story_type

    @property
    def custom_fields(self):
        """Gets the custom_fields of this UpdateStory.  # noqa: E501

        A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField.  # noqa: E501

        :return: The custom_fields of this UpdateStory.  # noqa: E501
        :rtype: list[CustomFieldValueParams]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this UpdateStory.

        A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField.  # noqa: E501

        :param custom_fields: The custom_fields of this UpdateStory.  # noqa: E501
        :type: list[CustomFieldValueParams]
        """

        self._custom_fields = custom_fields

    @property
    def move_to(self):
        """Gets the move_to of this UpdateStory.  # noqa: E501

        One of \"first\" or \"last\". This can be used to move the given story to the first or last position in the workflow state.  # noqa: E501

        :return: The move_to of this UpdateStory.  # noqa: E501
        :rtype: str
        """
        return self._move_to

    @move_to.setter
    def move_to(self, move_to):
        """Sets the move_to of this UpdateStory.

        One of \"first\" or \"last\". This can be used to move the given story to the first or last position in the workflow state.  # noqa: E501

        :param move_to: The move_to of this UpdateStory.  # noqa: E501
        :type: str
        """
        allowed_values = ["last", "first"]  # noqa: E501
        if move_to not in allowed_values:
            raise ValueError(
                "Invalid value for `move_to` ({0}), must be one of {1}"  # noqa: E501
                .format(move_to, allowed_values)
            )

        self._move_to = move_to

    @property
    def file_ids(self):
        """Gets the file_ids of this UpdateStory.  # noqa: E501

        An array of IDs of files attached to the story.  # noqa: E501

        :return: The file_ids of this UpdateStory.  # noqa: E501
        :rtype: list[int]
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids):
        """Sets the file_ids of this UpdateStory.

        An array of IDs of files attached to the story.  # noqa: E501

        :param file_ids: The file_ids of this UpdateStory.  # noqa: E501
        :type: list[int]
        """

        self._file_ids = file_ids

    @property
    def completed_at_override(self):
        """Gets the completed_at_override of this UpdateStory.  # noqa: E501

        A manual override for the time/date the Story was completed.  # noqa: E501

        :return: The completed_at_override of this UpdateStory.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at_override

    @completed_at_override.setter
    def completed_at_override(self, completed_at_override):
        """Sets the completed_at_override of this UpdateStory.

        A manual override for the time/date the Story was completed.  # noqa: E501

        :param completed_at_override: The completed_at_override of this UpdateStory.  # noqa: E501
        :type: datetime
        """

        self._completed_at_override = completed_at_override

    @property
    def name(self):
        """Gets the name of this UpdateStory.  # noqa: E501

        The title of the story.  # noqa: E501

        :return: The name of this UpdateStory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateStory.

        The title of the story.  # noqa: E501

        :param name: The name of this UpdateStory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def epic_id(self):
        """Gets the epic_id of this UpdateStory.  # noqa: E501

        The ID of the epic the story belongs to.  # noqa: E501

        :return: The epic_id of this UpdateStory.  # noqa: E501
        :rtype: int
        """
        return self._epic_id

    @epic_id.setter
    def epic_id(self, epic_id):
        """Sets the epic_id of this UpdateStory.

        The ID of the epic the story belongs to.  # noqa: E501

        :param epic_id: The epic_id of this UpdateStory.  # noqa: E501
        :type: int
        """

        self._epic_id = epic_id

    @property
    def external_links(self):
        """Gets the external_links of this UpdateStory.  # noqa: E501

        An array of External Links associated with this story.  # noqa: E501

        :return: The external_links of this UpdateStory.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_links

    @external_links.setter
    def external_links(self, external_links):
        """Sets the external_links of this UpdateStory.

        An array of External Links associated with this story.  # noqa: E501

        :param external_links: The external_links of this UpdateStory.  # noqa: E501
        :type: list[str]
        """

        self._external_links = external_links

    @property
    def branch_ids(self):
        """Gets the branch_ids of this UpdateStory.  # noqa: E501

        An array of IDs of Branches attached to the story.  # noqa: E501

        :return: The branch_ids of this UpdateStory.  # noqa: E501
        :rtype: list[int]
        """
        return self._branch_ids

    @branch_ids.setter
    def branch_ids(self, branch_ids):
        """Sets the branch_ids of this UpdateStory.

        An array of IDs of Branches attached to the story.  # noqa: E501

        :param branch_ids: The branch_ids of this UpdateStory.  # noqa: E501
        :type: list[int]
        """

        self._branch_ids = branch_ids

    @property
    def commit_ids(self):
        """Gets the commit_ids of this UpdateStory.  # noqa: E501

        An array of IDs of Commits attached to the story.  # noqa: E501

        :return: The commit_ids of this UpdateStory.  # noqa: E501
        :rtype: list[int]
        """
        return self._commit_ids

    @commit_ids.setter
    def commit_ids(self, commit_ids):
        """Sets the commit_ids of this UpdateStory.

        An array of IDs of Commits attached to the story.  # noqa: E501

        :param commit_ids: The commit_ids of this UpdateStory.  # noqa: E501
        :type: list[int]
        """

        self._commit_ids = commit_ids

    @property
    def requested_by_id(self):
        """Gets the requested_by_id of this UpdateStory.  # noqa: E501

        The ID of the member that requested the story.  # noqa: E501

        :return: The requested_by_id of this UpdateStory.  # noqa: E501
        :rtype: str
        """
        return self._requested_by_id

    @requested_by_id.setter
    def requested_by_id(self, requested_by_id):
        """Sets the requested_by_id of this UpdateStory.

        The ID of the member that requested the story.  # noqa: E501

        :param requested_by_id: The requested_by_id of this UpdateStory.  # noqa: E501
        :type: str
        """

        self._requested_by_id = requested_by_id

    @property
    def iteration_id(self):
        """Gets the iteration_id of this UpdateStory.  # noqa: E501

        The ID of the iteration the story belongs to.  # noqa: E501

        :return: The iteration_id of this UpdateStory.  # noqa: E501
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this UpdateStory.

        The ID of the iteration the story belongs to.  # noqa: E501

        :param iteration_id: The iteration_id of this UpdateStory.  # noqa: E501
        :type: int
        """

        self._iteration_id = iteration_id

    @property
    def started_at_override(self):
        """Gets the started_at_override of this UpdateStory.  # noqa: E501

        A manual override for the time/date the Story was started.  # noqa: E501

        :return: The started_at_override of this UpdateStory.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at_override

    @started_at_override.setter
    def started_at_override(self, started_at_override):
        """Sets the started_at_override of this UpdateStory.

        A manual override for the time/date the Story was started.  # noqa: E501

        :param started_at_override: The started_at_override of this UpdateStory.  # noqa: E501
        :type: datetime
        """

        self._started_at_override = started_at_override

    @property
    def group_id(self):
        """Gets the group_id of this UpdateStory.  # noqa: E501

        The ID of the group to associate with this story  # noqa: E501

        :return: The group_id of this UpdateStory.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateStory.

        The ID of the group to associate with this story  # noqa: E501

        :param group_id: The group_id of this UpdateStory.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def workflow_state_id(self):
        """Gets the workflow_state_id of this UpdateStory.  # noqa: E501

        The ID of the workflow state to put the story in.  # noqa: E501

        :return: The workflow_state_id of this UpdateStory.  # noqa: E501
        :rtype: int
        """
        return self._workflow_state_id

    @workflow_state_id.setter
    def workflow_state_id(self, workflow_state_id):
        """Sets the workflow_state_id of this UpdateStory.

        The ID of the workflow state to put the story in.  # noqa: E501

        :param workflow_state_id: The workflow_state_id of this UpdateStory.  # noqa: E501
        :type: int
        """

        self._workflow_state_id = workflow_state_id

    @property
    def follower_ids(self):
        """Gets the follower_ids of this UpdateStory.  # noqa: E501

        An array of UUIDs of the followers of this story.  # noqa: E501

        :return: The follower_ids of this UpdateStory.  # noqa: E501
        :rtype: list[str]
        """
        return self._follower_ids

    @follower_ids.setter
    def follower_ids(self, follower_ids):
        """Sets the follower_ids of this UpdateStory.

        An array of UUIDs of the followers of this story.  # noqa: E501

        :param follower_ids: The follower_ids of this UpdateStory.  # noqa: E501
        :type: list[str]
        """

        self._follower_ids = follower_ids

    @property
    def owner_ids(self):
        """Gets the owner_ids of this UpdateStory.  # noqa: E501

        An array of UUIDs of the owners of this story.  # noqa: E501

        :return: The owner_ids of this UpdateStory.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this UpdateStory.

        An array of UUIDs of the owners of this story.  # noqa: E501

        :param owner_ids: The owner_ids of this UpdateStory.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids = owner_ids

    @property
    def before_id(self):
        """Gets the before_id of this UpdateStory.  # noqa: E501

        The ID of the story we want to move this story before.  # noqa: E501

        :return: The before_id of this UpdateStory.  # noqa: E501
        :rtype: int
        """
        return self._before_id

    @before_id.setter
    def before_id(self, before_id):
        """Sets the before_id of this UpdateStory.

        The ID of the story we want to move this story before.  # noqa: E501

        :param before_id: The before_id of this UpdateStory.  # noqa: E501
        :type: int
        """

        self._before_id = before_id

    @property
    def estimate(self):
        """Gets the estimate of this UpdateStory.  # noqa: E501

        The numeric point estimate of the story. Can also be null, which means unestimated.  # noqa: E501

        :return: The estimate of this UpdateStory.  # noqa: E501
        :rtype: int
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """Sets the estimate of this UpdateStory.

        The numeric point estimate of the story. Can also be null, which means unestimated.  # noqa: E501

        :param estimate: The estimate of this UpdateStory.  # noqa: E501
        :type: int
        """

        self._estimate = estimate

    @property
    def after_id(self):
        """Gets the after_id of this UpdateStory.  # noqa: E501

        The ID of the story we want to move this story after.  # noqa: E501

        :return: The after_id of this UpdateStory.  # noqa: E501
        :rtype: int
        """
        return self._after_id

    @after_id.setter
    def after_id(self, after_id):
        """Sets the after_id of this UpdateStory.

        The ID of the story we want to move this story after.  # noqa: E501

        :param after_id: The after_id of this UpdateStory.  # noqa: E501
        :type: int
        """

        self._after_id = after_id

    @property
    def project_id(self):
        """Gets the project_id of this UpdateStory.  # noqa: E501

        The ID of the project the story belongs to.  # noqa: E501

        :return: The project_id of this UpdateStory.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateStory.

        The ID of the project the story belongs to.  # noqa: E501

        :param project_id: The project_id of this UpdateStory.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def linked_file_ids(self):
        """Gets the linked_file_ids of this UpdateStory.  # noqa: E501

        An array of IDs of linked files attached to the story.  # noqa: E501

        :return: The linked_file_ids of this UpdateStory.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_file_ids

    @linked_file_ids.setter
    def linked_file_ids(self, linked_file_ids):
        """Sets the linked_file_ids of this UpdateStory.

        An array of IDs of linked files attached to the story.  # noqa: E501

        :param linked_file_ids: The linked_file_ids of this UpdateStory.  # noqa: E501
        :type: list[int]
        """

        self._linked_file_ids = linked_file_ids

    @property
    def deadline(self):
        """Gets the deadline of this UpdateStory.  # noqa: E501

        The due date of the story.  # noqa: E501

        :return: The deadline of this UpdateStory.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this UpdateStory.

        The due date of the story.  # noqa: E501

        :param deadline: The deadline of this UpdateStory.  # noqa: E501
        :type: datetime
        """

        self._deadline = deadline

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
        if issubclass(UpdateStory, dict):
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
        if not isinstance(other, UpdateStory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
