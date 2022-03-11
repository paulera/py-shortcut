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

class CreateCommentComment(object):
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
        'text': 'str',
        'author_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'external_id': 'str'
    }

    attribute_map = {
        'text': 'text',
        'author_id': 'author_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'external_id': 'external_id'
    }

    def __init__(self, text=None, author_id=None, created_at=None, updated_at=None, external_id=None):  # noqa: E501
        """CreateCommentComment - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._author_id = None
        self._created_at = None
        self._updated_at = None
        self._external_id = None
        self.discriminator = None
        self.text = text
        if author_id is not None:
            self.author_id = author_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if external_id is not None:
            self.external_id = external_id

    @property
    def text(self):
        """Gets the text of this CreateCommentComment.  # noqa: E501

        The comment text.  # noqa: E501

        :return: The text of this CreateCommentComment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CreateCommentComment.

        The comment text.  # noqa: E501

        :param text: The text of this CreateCommentComment.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def author_id(self):
        """Gets the author_id of this CreateCommentComment.  # noqa: E501

        The Member ID of the Comment's author. Defaults to the user identified by the API token.  # noqa: E501

        :return: The author_id of this CreateCommentComment.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this CreateCommentComment.

        The Member ID of the Comment's author. Defaults to the user identified by the API token.  # noqa: E501

        :param author_id: The author_id of this CreateCommentComment.  # noqa: E501
        :type: str
        """

        self._author_id = author_id

    @property
    def created_at(self):
        """Gets the created_at of this CreateCommentComment.  # noqa: E501

        Defaults to the time/date the comment is created, but can be set to reflect another date.  # noqa: E501

        :return: The created_at of this CreateCommentComment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateCommentComment.

        Defaults to the time/date the comment is created, but can be set to reflect another date.  # noqa: E501

        :param created_at: The created_at of this CreateCommentComment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateCommentComment.  # noqa: E501

        Defaults to the time/date the comment is last updated, but can be set to reflect another date.  # noqa: E501

        :return: The updated_at of this CreateCommentComment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateCommentComment.

        Defaults to the time/date the comment is last updated, but can be set to reflect another date.  # noqa: E501

        :param updated_at: The updated_at of this CreateCommentComment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def external_id(self):
        """Gets the external_id of this CreateCommentComment.  # noqa: E501

        This field can be set to another unique ID. In the case that the comment has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this CreateCommentComment.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateCommentComment.

        This field can be set to another unique ID. In the case that the comment has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this CreateCommentComment.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(CreateCommentComment, dict):
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
        if not isinstance(other, CreateCommentComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other