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

class HistoryActionTaskCreate(object):
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
        'entity_type': 'str',
        'mention_ids': 'list[str]',
        'group_mention_ids': 'list[str]',
        'owner_ids': 'list[str]',
        'id': 'int',
        'action': 'str',
        'complete': 'bool',
        'deadline': 'str'
    }

    attribute_map = {
        'description': 'description',
        'entity_type': 'entity_type',
        'mention_ids': 'mention_ids',
        'group_mention_ids': 'group_mention_ids',
        'owner_ids': 'owner_ids',
        'id': 'id',
        'action': 'action',
        'complete': 'complete',
        'deadline': 'deadline'
    }

    def __init__(self, description=None, entity_type=None, mention_ids=None, group_mention_ids=None, owner_ids=None, id=None, action=None, complete=None, deadline=None):  # noqa: E501
        """HistoryActionTaskCreate - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._entity_type = None
        self._mention_ids = None
        self._group_mention_ids = None
        self._owner_ids = None
        self._id = None
        self._action = None
        self._complete = None
        self._deadline = None
        self.discriminator = None
        self.description = description
        self.entity_type = entity_type
        if mention_ids is not None:
            self.mention_ids = mention_ids
        if group_mention_ids is not None:
            self.group_mention_ids = group_mention_ids
        if owner_ids is not None:
            self.owner_ids = owner_ids
        self.id = id
        self.action = action
        self.complete = complete
        if deadline is not None:
            self.deadline = deadline

    @property
    def description(self):
        """Gets the description of this HistoryActionTaskCreate.  # noqa: E501

        The description of the Task.  # noqa: E501

        :return: The description of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HistoryActionTaskCreate.

        The description of the Task.  # noqa: E501

        :param description: The description of this HistoryActionTaskCreate.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def entity_type(self):
        """Gets the entity_type of this HistoryActionTaskCreate.  # noqa: E501

        The type of entity referenced.  # noqa: E501

        :return: The entity_type of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this HistoryActionTaskCreate.

        The type of entity referenced.  # noqa: E501

        :param entity_type: The entity_type of this HistoryActionTaskCreate.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def mention_ids(self):
        """Gets the mention_ids of this HistoryActionTaskCreate.  # noqa: E501

        An array of Member IDs that represent who has been mentioned in the Task.  # noqa: E501

        :return: The mention_ids of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._mention_ids

    @mention_ids.setter
    def mention_ids(self, mention_ids):
        """Sets the mention_ids of this HistoryActionTaskCreate.

        An array of Member IDs that represent who has been mentioned in the Task.  # noqa: E501

        :param mention_ids: The mention_ids of this HistoryActionTaskCreate.  # noqa: E501
        :type: list[str]
        """

        self._mention_ids = mention_ids

    @property
    def group_mention_ids(self):
        """Gets the group_mention_ids of this HistoryActionTaskCreate.  # noqa: E501

        An array of Groups IDs that represent which have been mentioned in the Task.  # noqa: E501

        :return: The group_mention_ids of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_mention_ids

    @group_mention_ids.setter
    def group_mention_ids(self, group_mention_ids):
        """Sets the group_mention_ids of this HistoryActionTaskCreate.

        An array of Groups IDs that represent which have been mentioned in the Task.  # noqa: E501

        :param group_mention_ids: The group_mention_ids of this HistoryActionTaskCreate.  # noqa: E501
        :type: list[str]
        """

        self._group_mention_ids = group_mention_ids

    @property
    def owner_ids(self):
        """Gets the owner_ids of this HistoryActionTaskCreate.  # noqa: E501

        An array of Member IDs that represent the Task's owners.  # noqa: E501

        :return: The owner_ids of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this HistoryActionTaskCreate.

        An array of Member IDs that represent the Task's owners.  # noqa: E501

        :param owner_ids: The owner_ids of this HistoryActionTaskCreate.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids = owner_ids

    @property
    def id(self):
        """Gets the id of this HistoryActionTaskCreate.  # noqa: E501

        The ID of the entity referenced.  # noqa: E501

        :return: The id of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryActionTaskCreate.

        The ID of the entity referenced.  # noqa: E501

        :param id: The id of this HistoryActionTaskCreate.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def action(self):
        """Gets the action of this HistoryActionTaskCreate.  # noqa: E501

        The action of the entity referenced.  # noqa: E501

        :return: The action of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HistoryActionTaskCreate.

        The action of the entity referenced.  # noqa: E501

        :param action: The action of this HistoryActionTaskCreate.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["create"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def complete(self):
        """Gets the complete of this HistoryActionTaskCreate.  # noqa: E501

        Whether or not the Task is complete.  # noqa: E501

        :return: The complete of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this HistoryActionTaskCreate.

        Whether or not the Task is complete.  # noqa: E501

        :param complete: The complete of this HistoryActionTaskCreate.  # noqa: E501
        :type: bool
        """
        if complete is None:
            raise ValueError("Invalid value for `complete`, must not be `None`")  # noqa: E501

        self._complete = complete

    @property
    def deadline(self):
        """Gets the deadline of this HistoryActionTaskCreate.  # noqa: E501

        A timestamp that represent's the Task's deadline.  # noqa: E501

        :return: The deadline of this HistoryActionTaskCreate.  # noqa: E501
        :rtype: str
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this HistoryActionTaskCreate.

        A timestamp that represent's the Task's deadline.  # noqa: E501

        :param deadline: The deadline of this HistoryActionTaskCreate.  # noqa: E501
        :type: str
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
        if issubclass(HistoryActionTaskCreate, dict):
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
        if not isinstance(other, HistoryActionTaskCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
