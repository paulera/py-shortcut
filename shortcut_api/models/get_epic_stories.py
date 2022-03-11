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

class GetEpicStories(object):
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
        'includes_description': 'bool'
    }

    attribute_map = {
        'includes_description': 'includes_description'
    }

    def __init__(self, includes_description=None):  # noqa: E501
        """GetEpicStories - a model defined in Swagger"""  # noqa: E501
        self._includes_description = None
        self.discriminator = None
        if includes_description is not None:
            self.includes_description = includes_description

    @property
    def includes_description(self):
        """Gets the includes_description of this GetEpicStories.  # noqa: E501

        A true/false boolean indicating whether to return Stories with their descriptions.  # noqa: E501

        :return: The includes_description of this GetEpicStories.  # noqa: E501
        :rtype: bool
        """
        return self._includes_description

    @includes_description.setter
    def includes_description(self, includes_description):
        """Sets the includes_description of this GetEpicStories.

        A true/false boolean indicating whether to return Stories with their descriptions.  # noqa: E501

        :param includes_description: The includes_description of this GetEpicStories.  # noqa: E501
        :type: bool
        """

        self._includes_description = includes_description

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
        if issubclass(GetEpicStories, dict):
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
        if not isinstance(other, GetEpicStories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
