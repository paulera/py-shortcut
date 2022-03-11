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

class HistoryReferenceBranch(object):
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
        'id': 'int',
        'entity_type': 'str',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entity_type',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, id=None, entity_type=None, name=None, url=None):  # noqa: E501
        """HistoryReferenceBranch - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity_type = None
        self._name = None
        self._url = None
        self.discriminator = None
        self.id = id
        self.entity_type = entity_type
        self.name = name
        self.url = url

    @property
    def id(self):
        """Gets the id of this HistoryReferenceBranch.  # noqa: E501

        The ID of the entity referenced.  # noqa: E501

        :return: The id of this HistoryReferenceBranch.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryReferenceBranch.

        The ID of the entity referenced.  # noqa: E501

        :param id: The id of this HistoryReferenceBranch.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this HistoryReferenceBranch.  # noqa: E501

        The type of entity referenced.  # noqa: E501

        :return: The entity_type of this HistoryReferenceBranch.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this HistoryReferenceBranch.

        The type of entity referenced.  # noqa: E501

        :param entity_type: The entity_type of this HistoryReferenceBranch.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this HistoryReferenceBranch.  # noqa: E501

        The name of the entity referenced.  # noqa: E501

        :return: The name of this HistoryReferenceBranch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HistoryReferenceBranch.

        The name of the entity referenced.  # noqa: E501

        :param name: The name of this HistoryReferenceBranch.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this HistoryReferenceBranch.  # noqa: E501

        The external URL for the Branch.  # noqa: E501

        :return: The url of this HistoryReferenceBranch.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HistoryReferenceBranch.

        The external URL for the Branch.  # noqa: E501

        :param url: The url of this HistoryReferenceBranch.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if issubclass(HistoryReferenceBranch, dict):
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
        if not isinstance(other, HistoryReferenceBranch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
