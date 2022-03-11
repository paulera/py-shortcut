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

class Identity(object):
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
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, entity_type=None, name=None, type=None):  # noqa: E501
        """Identity - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._name = None
        self._type = None
        self.discriminator = None
        self.entity_type = entity_type
        self.name = name
        self.type = type

    @property
    def entity_type(self):
        """Gets the entity_type of this Identity.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Identity.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this Identity.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this Identity.  # noqa: E501

        This is your login in VCS.  # noqa: E501

        :return: The name of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Identity.

        This is your login in VCS.  # noqa: E501

        :param name: The name of this Identity.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Identity.  # noqa: E501

        The type of Identity; currently only type is github.  # noqa: E501

        :return: The type of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Identity.

        The type of Identity; currently only type is github.  # noqa: E501

        :param type: The type of this Identity.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(Identity, dict):
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
        if not isinstance(other, Identity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other