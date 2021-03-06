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

class DeleteStories(object):
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
        'story_ids': 'list[int]'
    }

    attribute_map = {
        'story_ids': 'story_ids'
    }

    def __init__(self, story_ids=None):  # noqa: E501
        """DeleteStories - a model defined in Swagger"""  # noqa: E501
        self._story_ids = None
        self.discriminator = None
        self.story_ids = story_ids

    @property
    def story_ids(self):
        """Gets the story_ids of this DeleteStories.  # noqa: E501

        An array of IDs of Stories to delete.  # noqa: E501

        :return: The story_ids of this DeleteStories.  # noqa: E501
        :rtype: list[int]
        """
        return self._story_ids

    @story_ids.setter
    def story_ids(self, story_ids):
        """Sets the story_ids of this DeleteStories.

        An array of IDs of Stories to delete.  # noqa: E501

        :param story_ids: The story_ids of this DeleteStories.  # noqa: E501
        :type: list[int]
        """
        if story_ids is None:
            raise ValueError("Invalid value for `story_ids`, must not be `None`")  # noqa: E501

        self._story_ids = story_ids

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
        if issubclass(DeleteStories, dict):
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
        if not isinstance(other, DeleteStories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
