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

class Profile(object):
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
        'deactivated': 'bool',
        'two_factor_auth_activated': 'bool',
        'mention_name': 'str',
        'name': 'str',
        'gravatar_hash': 'str',
        'id': 'str',
        'display_icon': 'Icon',
        'email_address': 'str'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'deactivated': 'deactivated',
        'two_factor_auth_activated': 'two_factor_auth_activated',
        'mention_name': 'mention_name',
        'name': 'name',
        'gravatar_hash': 'gravatar_hash',
        'id': 'id',
        'display_icon': 'display_icon',
        'email_address': 'email_address'
    }

    def __init__(self, entity_type=None, deactivated=None, two_factor_auth_activated=None, mention_name=None, name=None, gravatar_hash=None, id=None, display_icon=None, email_address=None):  # noqa: E501
        """Profile - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._deactivated = None
        self._two_factor_auth_activated = None
        self._mention_name = None
        self._name = None
        self._gravatar_hash = None
        self._id = None
        self._display_icon = None
        self._email_address = None
        self.discriminator = None
        self.entity_type = entity_type
        self.deactivated = deactivated
        if two_factor_auth_activated is not None:
            self.two_factor_auth_activated = two_factor_auth_activated
        self.mention_name = mention_name
        self.name = name
        self.gravatar_hash = gravatar_hash
        self.id = id
        self.display_icon = display_icon
        self.email_address = email_address

    @property
    def entity_type(self):
        """Gets the entity_type of this Profile.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Profile.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this Profile.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def deactivated(self):
        """Gets the deactivated of this Profile.  # noqa: E501

        A true/false boolean indicating whether the Member has been deactivated within Shortcut.  # noqa: E501

        :return: The deactivated of this Profile.  # noqa: E501
        :rtype: bool
        """
        return self._deactivated

    @deactivated.setter
    def deactivated(self, deactivated):
        """Sets the deactivated of this Profile.

        A true/false boolean indicating whether the Member has been deactivated within Shortcut.  # noqa: E501

        :param deactivated: The deactivated of this Profile.  # noqa: E501
        :type: bool
        """
        if deactivated is None:
            raise ValueError("Invalid value for `deactivated`, must not be `None`")  # noqa: E501

        self._deactivated = deactivated

    @property
    def two_factor_auth_activated(self):
        """Gets the two_factor_auth_activated of this Profile.  # noqa: E501

        If Two Factor Authentication is activated for this User.  # noqa: E501

        :return: The two_factor_auth_activated of this Profile.  # noqa: E501
        :rtype: bool
        """
        return self._two_factor_auth_activated

    @two_factor_auth_activated.setter
    def two_factor_auth_activated(self, two_factor_auth_activated):
        """Sets the two_factor_auth_activated of this Profile.

        If Two Factor Authentication is activated for this User.  # noqa: E501

        :param two_factor_auth_activated: The two_factor_auth_activated of this Profile.  # noqa: E501
        :type: bool
        """

        self._two_factor_auth_activated = two_factor_auth_activated

    @property
    def mention_name(self):
        """Gets the mention_name of this Profile.  # noqa: E501

        The Member's username within the Organization.  # noqa: E501

        :return: The mention_name of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._mention_name

    @mention_name.setter
    def mention_name(self, mention_name):
        """Sets the mention_name of this Profile.

        The Member's username within the Organization.  # noqa: E501

        :param mention_name: The mention_name of this Profile.  # noqa: E501
        :type: str
        """
        if mention_name is None:
            raise ValueError("Invalid value for `mention_name`, must not be `None`")  # noqa: E501

        self._mention_name = mention_name

    @property
    def name(self):
        """Gets the name of this Profile.  # noqa: E501

        The Member's name within the Organization.  # noqa: E501

        :return: The name of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Profile.

        The Member's name within the Organization.  # noqa: E501

        :param name: The name of this Profile.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def gravatar_hash(self):
        """Gets the gravatar_hash of this Profile.  # noqa: E501

        This is the gravatar hash associated with email_address.  # noqa: E501

        :return: The gravatar_hash of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._gravatar_hash

    @gravatar_hash.setter
    def gravatar_hash(self, gravatar_hash):
        """Sets the gravatar_hash of this Profile.

        This is the gravatar hash associated with email_address.  # noqa: E501

        :param gravatar_hash: The gravatar_hash of this Profile.  # noqa: E501
        :type: str
        """
        if gravatar_hash is None:
            raise ValueError("Invalid value for `gravatar_hash`, must not be `None`")  # noqa: E501

        self._gravatar_hash = gravatar_hash

    @property
    def id(self):
        """Gets the id of this Profile.  # noqa: E501

        The unique identifier of the profile.  # noqa: E501

        :return: The id of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Profile.

        The unique identifier of the profile.  # noqa: E501

        :param id: The id of this Profile.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_icon(self):
        """Gets the display_icon of this Profile.  # noqa: E501


        :return: The display_icon of this Profile.  # noqa: E501
        :rtype: Icon
        """
        return self._display_icon

    @display_icon.setter
    def display_icon(self, display_icon):
        """Sets the display_icon of this Profile.


        :param display_icon: The display_icon of this Profile.  # noqa: E501
        :type: Icon
        """
        if display_icon is None:
            raise ValueError("Invalid value for `display_icon`, must not be `None`")  # noqa: E501

        self._display_icon = display_icon

    @property
    def email_address(self):
        """Gets the email_address of this Profile.  # noqa: E501

        The primary email address of the Member with the Organization.  # noqa: E501

        :return: The email_address of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Profile.

        The primary email address of the Member with the Organization.  # noqa: E501

        :param email_address: The email_address of this Profile.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

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
        if issubclass(Profile, dict):
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
        if not isinstance(other, Profile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
