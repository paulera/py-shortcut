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

class UpdateStories(object):
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
        'archived': 'bool',
        'story_ids': 'list[int]',
        'story_type': 'str',
        'move_to': 'str',
        'follower_ids_add': 'list[str]',
        'epic_id': 'int',
        'external_links': 'list[str]',
        'follower_ids_remove': 'list[str]',
        'requested_by_id': 'str',
        'iteration_id': 'int',
        'custom_fields_remove': 'list[CustomFieldValueParams]',
        'labels_add': 'list[CreateLabelParams]',
        'group_id': 'str',
        'workflow_state_id': 'int',
        'before_id': 'int',
        'estimate': 'int',
        'after_id': 'int',
        'owner_ids_remove': 'list[str]',
        'custom_fields_add': 'list[CustomFieldValueParams]',
        'project_id': 'int',
        'labels_remove': 'list[CreateLabelParams]',
        'deadline': 'datetime',
        'owner_ids_add': 'list[str]'
    }

    attribute_map = {
        'archived': 'archived',
        'story_ids': 'story_ids',
        'story_type': 'story_type',
        'move_to': 'move_to',
        'follower_ids_add': 'follower_ids_add',
        'epic_id': 'epic_id',
        'external_links': 'external_links',
        'follower_ids_remove': 'follower_ids_remove',
        'requested_by_id': 'requested_by_id',
        'iteration_id': 'iteration_id',
        'custom_fields_remove': 'custom_fields_remove',
        'labels_add': 'labels_add',
        'group_id': 'group_id',
        'workflow_state_id': 'workflow_state_id',
        'before_id': 'before_id',
        'estimate': 'estimate',
        'after_id': 'after_id',
        'owner_ids_remove': 'owner_ids_remove',
        'custom_fields_add': 'custom_fields_add',
        'project_id': 'project_id',
        'labels_remove': 'labels_remove',
        'deadline': 'deadline',
        'owner_ids_add': 'owner_ids_add'
    }

    def __init__(self, archived=None, story_ids=None, story_type=None, move_to=None, follower_ids_add=None, epic_id=None, external_links=None, follower_ids_remove=None, requested_by_id=None, iteration_id=None, custom_fields_remove=None, labels_add=None, group_id=None, workflow_state_id=None, before_id=None, estimate=None, after_id=None, owner_ids_remove=None, custom_fields_add=None, project_id=None, labels_remove=None, deadline=None, owner_ids_add=None):  # noqa: E501
        """UpdateStories - a model defined in Swagger"""  # noqa: E501
        self._archived = None
        self._story_ids = None
        self._story_type = None
        self._move_to = None
        self._follower_ids_add = None
        self._epic_id = None
        self._external_links = None
        self._follower_ids_remove = None
        self._requested_by_id = None
        self._iteration_id = None
        self._custom_fields_remove = None
        self._labels_add = None
        self._group_id = None
        self._workflow_state_id = None
        self._before_id = None
        self._estimate = None
        self._after_id = None
        self._owner_ids_remove = None
        self._custom_fields_add = None
        self._project_id = None
        self._labels_remove = None
        self._deadline = None
        self._owner_ids_add = None
        self.discriminator = None
        if archived is not None:
            self.archived = archived
        self.story_ids = story_ids
        if story_type is not None:
            self.story_type = story_type
        if move_to is not None:
            self.move_to = move_to
        if follower_ids_add is not None:
            self.follower_ids_add = follower_ids_add
        if epic_id is not None:
            self.epic_id = epic_id
        if external_links is not None:
            self.external_links = external_links
        if follower_ids_remove is not None:
            self.follower_ids_remove = follower_ids_remove
        if requested_by_id is not None:
            self.requested_by_id = requested_by_id
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if custom_fields_remove is not None:
            self.custom_fields_remove = custom_fields_remove
        if labels_add is not None:
            self.labels_add = labels_add
        if group_id is not None:
            self.group_id = group_id
        if workflow_state_id is not None:
            self.workflow_state_id = workflow_state_id
        if before_id is not None:
            self.before_id = before_id
        if estimate is not None:
            self.estimate = estimate
        if after_id is not None:
            self.after_id = after_id
        if owner_ids_remove is not None:
            self.owner_ids_remove = owner_ids_remove
        if custom_fields_add is not None:
            self.custom_fields_add = custom_fields_add
        if project_id is not None:
            self.project_id = project_id
        if labels_remove is not None:
            self.labels_remove = labels_remove
        if deadline is not None:
            self.deadline = deadline
        if owner_ids_add is not None:
            self.owner_ids_add = owner_ids_add

    @property
    def archived(self):
        """Gets the archived of this UpdateStories.  # noqa: E501

        If the Stories should be archived or not.  # noqa: E501

        :return: The archived of this UpdateStories.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this UpdateStories.

        If the Stories should be archived or not.  # noqa: E501

        :param archived: The archived of this UpdateStories.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def story_ids(self):
        """Gets the story_ids of this UpdateStories.  # noqa: E501

        The Ids of the Stories you wish to update.  # noqa: E501

        :return: The story_ids of this UpdateStories.  # noqa: E501
        :rtype: list[int]
        """
        return self._story_ids

    @story_ids.setter
    def story_ids(self, story_ids):
        """Sets the story_ids of this UpdateStories.

        The Ids of the Stories you wish to update.  # noqa: E501

        :param story_ids: The story_ids of this UpdateStories.  # noqa: E501
        :type: list[int]
        """
        if story_ids is None:
            raise ValueError("Invalid value for `story_ids`, must not be `None`")  # noqa: E501

        self._story_ids = story_ids

    @property
    def story_type(self):
        """Gets the story_type of this UpdateStories.  # noqa: E501

        The type of story (feature, bug, chore).  # noqa: E501

        :return: The story_type of this UpdateStories.  # noqa: E501
        :rtype: str
        """
        return self._story_type

    @story_type.setter
    def story_type(self, story_type):
        """Sets the story_type of this UpdateStories.

        The type of story (feature, bug, chore).  # noqa: E501

        :param story_type: The story_type of this UpdateStories.  # noqa: E501
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
    def move_to(self):
        """Gets the move_to of this UpdateStories.  # noqa: E501

        One of \"first\" or \"last\". This can be used to move the given story to the first or last position in the workflow state.  # noqa: E501

        :return: The move_to of this UpdateStories.  # noqa: E501
        :rtype: str
        """
        return self._move_to

    @move_to.setter
    def move_to(self, move_to):
        """Sets the move_to of this UpdateStories.

        One of \"first\" or \"last\". This can be used to move the given story to the first or last position in the workflow state.  # noqa: E501

        :param move_to: The move_to of this UpdateStories.  # noqa: E501
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
    def follower_ids_add(self):
        """Gets the follower_ids_add of this UpdateStories.  # noqa: E501

        The UUIDs of the new followers to be added.  # noqa: E501

        :return: The follower_ids_add of this UpdateStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._follower_ids_add

    @follower_ids_add.setter
    def follower_ids_add(self, follower_ids_add):
        """Sets the follower_ids_add of this UpdateStories.

        The UUIDs of the new followers to be added.  # noqa: E501

        :param follower_ids_add: The follower_ids_add of this UpdateStories.  # noqa: E501
        :type: list[str]
        """

        self._follower_ids_add = follower_ids_add

    @property
    def epic_id(self):
        """Gets the epic_id of this UpdateStories.  # noqa: E501

        The ID of the epic the story belongs to.  # noqa: E501

        :return: The epic_id of this UpdateStories.  # noqa: E501
        :rtype: int
        """
        return self._epic_id

    @epic_id.setter
    def epic_id(self, epic_id):
        """Sets the epic_id of this UpdateStories.

        The ID of the epic the story belongs to.  # noqa: E501

        :param epic_id: The epic_id of this UpdateStories.  # noqa: E501
        :type: int
        """

        self._epic_id = epic_id

    @property
    def external_links(self):
        """Gets the external_links of this UpdateStories.  # noqa: E501

        An array of External Links associated with this story.  # noqa: E501

        :return: The external_links of this UpdateStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_links

    @external_links.setter
    def external_links(self, external_links):
        """Sets the external_links of this UpdateStories.

        An array of External Links associated with this story.  # noqa: E501

        :param external_links: The external_links of this UpdateStories.  # noqa: E501
        :type: list[str]
        """

        self._external_links = external_links

    @property
    def follower_ids_remove(self):
        """Gets the follower_ids_remove of this UpdateStories.  # noqa: E501

        The UUIDs of the followers to be removed.  # noqa: E501

        :return: The follower_ids_remove of this UpdateStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._follower_ids_remove

    @follower_ids_remove.setter
    def follower_ids_remove(self, follower_ids_remove):
        """Sets the follower_ids_remove of this UpdateStories.

        The UUIDs of the followers to be removed.  # noqa: E501

        :param follower_ids_remove: The follower_ids_remove of this UpdateStories.  # noqa: E501
        :type: list[str]
        """

        self._follower_ids_remove = follower_ids_remove

    @property
    def requested_by_id(self):
        """Gets the requested_by_id of this UpdateStories.  # noqa: E501

        The ID of the member that requested the story.  # noqa: E501

        :return: The requested_by_id of this UpdateStories.  # noqa: E501
        :rtype: str
        """
        return self._requested_by_id

    @requested_by_id.setter
    def requested_by_id(self, requested_by_id):
        """Sets the requested_by_id of this UpdateStories.

        The ID of the member that requested the story.  # noqa: E501

        :param requested_by_id: The requested_by_id of this UpdateStories.  # noqa: E501
        :type: str
        """

        self._requested_by_id = requested_by_id

    @property
    def iteration_id(self):
        """Gets the iteration_id of this UpdateStories.  # noqa: E501

        The ID of the iteration the story belongs to.  # noqa: E501

        :return: The iteration_id of this UpdateStories.  # noqa: E501
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this UpdateStories.

        The ID of the iteration the story belongs to.  # noqa: E501

        :param iteration_id: The iteration_id of this UpdateStories.  # noqa: E501
        :type: int
        """

        self._iteration_id = iteration_id

    @property
    def custom_fields_remove(self):
        """Gets the custom_fields_remove of this UpdateStories.  # noqa: E501

        A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField.  # noqa: E501

        :return: The custom_fields_remove of this UpdateStories.  # noqa: E501
        :rtype: list[CustomFieldValueParams]
        """
        return self._custom_fields_remove

    @custom_fields_remove.setter
    def custom_fields_remove(self, custom_fields_remove):
        """Sets the custom_fields_remove of this UpdateStories.

        A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField.  # noqa: E501

        :param custom_fields_remove: The custom_fields_remove of this UpdateStories.  # noqa: E501
        :type: list[CustomFieldValueParams]
        """

        self._custom_fields_remove = custom_fields_remove

    @property
    def labels_add(self):
        """Gets the labels_add of this UpdateStories.  # noqa: E501

        An array of labels to be added.  # noqa: E501

        :return: The labels_add of this UpdateStories.  # noqa: E501
        :rtype: list[CreateLabelParams]
        """
        return self._labels_add

    @labels_add.setter
    def labels_add(self, labels_add):
        """Sets the labels_add of this UpdateStories.

        An array of labels to be added.  # noqa: E501

        :param labels_add: The labels_add of this UpdateStories.  # noqa: E501
        :type: list[CreateLabelParams]
        """

        self._labels_add = labels_add

    @property
    def group_id(self):
        """Gets the group_id of this UpdateStories.  # noqa: E501

        The Id of the Group the Stories should belong to.  # noqa: E501

        :return: The group_id of this UpdateStories.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateStories.

        The Id of the Group the Stories should belong to.  # noqa: E501

        :param group_id: The group_id of this UpdateStories.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def workflow_state_id(self):
        """Gets the workflow_state_id of this UpdateStories.  # noqa: E501

        The ID of the workflow state to put the stories in.  # noqa: E501

        :return: The workflow_state_id of this UpdateStories.  # noqa: E501
        :rtype: int
        """
        return self._workflow_state_id

    @workflow_state_id.setter
    def workflow_state_id(self, workflow_state_id):
        """Sets the workflow_state_id of this UpdateStories.

        The ID of the workflow state to put the stories in.  # noqa: E501

        :param workflow_state_id: The workflow_state_id of this UpdateStories.  # noqa: E501
        :type: int
        """

        self._workflow_state_id = workflow_state_id

    @property
    def before_id(self):
        """Gets the before_id of this UpdateStories.  # noqa: E501

        The ID of the story that the stories are to be moved before.  # noqa: E501

        :return: The before_id of this UpdateStories.  # noqa: E501
        :rtype: int
        """
        return self._before_id

    @before_id.setter
    def before_id(self, before_id):
        """Sets the before_id of this UpdateStories.

        The ID of the story that the stories are to be moved before.  # noqa: E501

        :param before_id: The before_id of this UpdateStories.  # noqa: E501
        :type: int
        """

        self._before_id = before_id

    @property
    def estimate(self):
        """Gets the estimate of this UpdateStories.  # noqa: E501

        The numeric point estimate of the story. Can also be null, which means unestimated.  # noqa: E501

        :return: The estimate of this UpdateStories.  # noqa: E501
        :rtype: int
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """Sets the estimate of this UpdateStories.

        The numeric point estimate of the story. Can also be null, which means unestimated.  # noqa: E501

        :param estimate: The estimate of this UpdateStories.  # noqa: E501
        :type: int
        """

        self._estimate = estimate

    @property
    def after_id(self):
        """Gets the after_id of this UpdateStories.  # noqa: E501

        The ID of the story that the stories are to be moved below.  # noqa: E501

        :return: The after_id of this UpdateStories.  # noqa: E501
        :rtype: int
        """
        return self._after_id

    @after_id.setter
    def after_id(self, after_id):
        """Sets the after_id of this UpdateStories.

        The ID of the story that the stories are to be moved below.  # noqa: E501

        :param after_id: The after_id of this UpdateStories.  # noqa: E501
        :type: int
        """

        self._after_id = after_id

    @property
    def owner_ids_remove(self):
        """Gets the owner_ids_remove of this UpdateStories.  # noqa: E501

        The UUIDs of the owners to be removed.  # noqa: E501

        :return: The owner_ids_remove of this UpdateStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids_remove

    @owner_ids_remove.setter
    def owner_ids_remove(self, owner_ids_remove):
        """Sets the owner_ids_remove of this UpdateStories.

        The UUIDs of the owners to be removed.  # noqa: E501

        :param owner_ids_remove: The owner_ids_remove of this UpdateStories.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids_remove = owner_ids_remove

    @property
    def custom_fields_add(self):
        """Gets the custom_fields_add of this UpdateStories.  # noqa: E501

        A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField.  # noqa: E501

        :return: The custom_fields_add of this UpdateStories.  # noqa: E501
        :rtype: list[CustomFieldValueParams]
        """
        return self._custom_fields_add

    @custom_fields_add.setter
    def custom_fields_add(self, custom_fields_add):
        """Sets the custom_fields_add of this UpdateStories.

        A map specifying a CustomField ID and CustomFieldEnumValue ID that represents an assertion of some value for a CustomField.  # noqa: E501

        :param custom_fields_add: The custom_fields_add of this UpdateStories.  # noqa: E501
        :type: list[CustomFieldValueParams]
        """

        self._custom_fields_add = custom_fields_add

    @property
    def project_id(self):
        """Gets the project_id of this UpdateStories.  # noqa: E501

        The ID of the Project the Stories should belong to.  # noqa: E501

        :return: The project_id of this UpdateStories.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateStories.

        The ID of the Project the Stories should belong to.  # noqa: E501

        :param project_id: The project_id of this UpdateStories.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def labels_remove(self):
        """Gets the labels_remove of this UpdateStories.  # noqa: E501

        An array of labels to be removed.  # noqa: E501

        :return: The labels_remove of this UpdateStories.  # noqa: E501
        :rtype: list[CreateLabelParams]
        """
        return self._labels_remove

    @labels_remove.setter
    def labels_remove(self, labels_remove):
        """Sets the labels_remove of this UpdateStories.

        An array of labels to be removed.  # noqa: E501

        :param labels_remove: The labels_remove of this UpdateStories.  # noqa: E501
        :type: list[CreateLabelParams]
        """

        self._labels_remove = labels_remove

    @property
    def deadline(self):
        """Gets the deadline of this UpdateStories.  # noqa: E501

        The due date of the story.  # noqa: E501

        :return: The deadline of this UpdateStories.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this UpdateStories.

        The due date of the story.  # noqa: E501

        :param deadline: The deadline of this UpdateStories.  # noqa: E501
        :type: datetime
        """

        self._deadline = deadline

    @property
    def owner_ids_add(self):
        """Gets the owner_ids_add of this UpdateStories.  # noqa: E501

        The UUIDs of the new owners to be added.  # noqa: E501

        :return: The owner_ids_add of this UpdateStories.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids_add

    @owner_ids_add.setter
    def owner_ids_add(self, owner_ids_add):
        """Sets the owner_ids_add of this UpdateStories.

        The UUIDs of the new owners to be added.  # noqa: E501

        :param owner_ids_add: The owner_ids_add of this UpdateStories.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids_add = owner_ids_add

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
        if issubclass(UpdateStories, dict):
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
        if not isinstance(other, UpdateStories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
