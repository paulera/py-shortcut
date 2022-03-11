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

class CreateStories(object):
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
        'stories': 'list[CreateStoryParams]'
    }

    attribute_map = {
        'stories': 'stories'
    }

    def __init__(self, stories=None):  # noqa: E501
        """CreateStories - a model defined in Swagger"""  # noqa: E501
        self._stories = None
        self.discriminator = None
        self.stories = stories

    @property
    def stories(self):
        """Gets the stories of this CreateStories.  # noqa: E501

        An array of stories to be created.  # noqa: E501

        :return: The stories of this CreateStories.  # noqa: E501
        :rtype: list[CreateStoryParams]
        """
        return self._stories

    @stories.setter
    def stories(self, stories):
        """Sets the stories of this CreateStories.

        An array of stories to be created.  # noqa: E501

        :param stories: The stories of this CreateStories.  # noqa: E501
        :type: list[CreateStoryParams]
        """
        if stories is None:
            raise ValueError("Invalid value for `stories`, must not be `None`")  # noqa: E501

        self._stories = stories

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
        if issubclass(CreateStories, dict):
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
        if not isinstance(other, CreateStories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other