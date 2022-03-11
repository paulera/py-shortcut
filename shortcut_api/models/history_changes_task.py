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

class HistoryChangesTask(object):
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
        'complete': 'StoryHistoryChangeOldNewBool',
        'description': 'StoryHistoryChangeOldNewStr',
        'mention_ids': 'StoryHistoryChangeAddsRemovesUuid',
        'owner_ids': 'StoryHistoryChangeAddsRemovesUuid'
    }

    attribute_map = {
        'complete': 'complete',
        'description': 'description',
        'mention_ids': 'mention_ids',
        'owner_ids': 'owner_ids'
    }

    def __init__(self, complete=None, description=None, mention_ids=None, owner_ids=None):  # noqa: E501
        """HistoryChangesTask - a model defined in Swagger"""  # noqa: E501
        self._complete = None
        self._description = None
        self._mention_ids = None
        self._owner_ids = None
        self.discriminator = None
        if complete is not None:
            self.complete = complete
        if description is not None:
            self.description = description
        if mention_ids is not None:
            self.mention_ids = mention_ids
        if owner_ids is not None:
            self.owner_ids = owner_ids

    @property
    def complete(self):
        """Gets the complete of this HistoryChangesTask.  # noqa: E501


        :return: The complete of this HistoryChangesTask.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewBool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this HistoryChangesTask.


        :param complete: The complete of this HistoryChangesTask.  # noqa: E501
        :type: StoryHistoryChangeOldNewBool
        """

        self._complete = complete

    @property
    def description(self):
        """Gets the description of this HistoryChangesTask.  # noqa: E501


        :return: The description of this HistoryChangesTask.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewStr
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HistoryChangesTask.


        :param description: The description of this HistoryChangesTask.  # noqa: E501
        :type: StoryHistoryChangeOldNewStr
        """

        self._description = description

    @property
    def mention_ids(self):
        """Gets the mention_ids of this HistoryChangesTask.  # noqa: E501


        :return: The mention_ids of this HistoryChangesTask.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesUuid
        """
        return self._mention_ids

    @mention_ids.setter
    def mention_ids(self, mention_ids):
        """Sets the mention_ids of this HistoryChangesTask.


        :param mention_ids: The mention_ids of this HistoryChangesTask.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesUuid
        """

        self._mention_ids = mention_ids

    @property
    def owner_ids(self):
        """Gets the owner_ids of this HistoryChangesTask.  # noqa: E501


        :return: The owner_ids of this HistoryChangesTask.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesUuid
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this HistoryChangesTask.


        :param owner_ids: The owner_ids of this HistoryChangesTask.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesUuid
        """

        self._owner_ids = owner_ids

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
        if issubclass(HistoryChangesTask, dict):
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
        if not isinstance(other, HistoryChangesTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
