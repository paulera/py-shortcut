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

class StoryStats(object):
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
        'num_related_documents': 'int'
    }

    attribute_map = {
        'num_related_documents': 'num_related_documents'
    }

    def __init__(self, num_related_documents=None):  # noqa: E501
        """StoryStats - a model defined in Swagger"""  # noqa: E501
        self._num_related_documents = None
        self.discriminator = None
        self.num_related_documents = num_related_documents

    @property
    def num_related_documents(self):
        """Gets the num_related_documents of this StoryStats.  # noqa: E501

        The number of documents related to this Story.  # noqa: E501

        :return: The num_related_documents of this StoryStats.  # noqa: E501
        :rtype: int
        """
        return self._num_related_documents

    @num_related_documents.setter
    def num_related_documents(self, num_related_documents):
        """Sets the num_related_documents of this StoryStats.

        The number of documents related to this Story.  # noqa: E501

        :param num_related_documents: The num_related_documents of this StoryStats.  # noqa: E501
        :type: int
        """
        if num_related_documents is None:
            raise ValueError("Invalid value for `num_related_documents`, must not be `None`")  # noqa: E501

        self._num_related_documents = num_related_documents

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
        if issubclass(StoryStats, dict):
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
        if not isinstance(other, StoryStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
