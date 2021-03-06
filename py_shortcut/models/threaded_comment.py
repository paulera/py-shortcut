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

class ThreadedComment(object):
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
        'app_url': 'str',
        'entity_type': 'str',
        'deleted': 'bool',
        'mention_ids': 'list[str]',
        'author_id': 'str',
        'member_mention_ids': 'list[str]',
        'comments': 'list[ThreadedComment]',
        'updated_at': 'datetime',
        'group_mention_ids': 'list[str]',
        'external_id': 'str',
        'id': 'int',
        'created_at': 'datetime',
        'text': 'str'
    }

    attribute_map = {
        'app_url': 'app_url',
        'entity_type': 'entity_type',
        'deleted': 'deleted',
        'mention_ids': 'mention_ids',
        'author_id': 'author_id',
        'member_mention_ids': 'member_mention_ids',
        'comments': 'comments',
        'updated_at': 'updated_at',
        'group_mention_ids': 'group_mention_ids',
        'external_id': 'external_id',
        'id': 'id',
        'created_at': 'created_at',
        'text': 'text'
    }

    def __init__(self, app_url=None, entity_type=None, deleted=None, mention_ids=None, author_id=None, member_mention_ids=None, comments=None, updated_at=None, group_mention_ids=None, external_id=None, id=None, created_at=None, text=None):  # noqa: E501
        """ThreadedComment - a model defined in Swagger"""  # noqa: E501
        self._app_url = None
        self._entity_type = None
        self._deleted = None
        self._mention_ids = None
        self._author_id = None
        self._member_mention_ids = None
        self._comments = None
        self._updated_at = None
        self._group_mention_ids = None
        self._external_id = None
        self._id = None
        self._created_at = None
        self._text = None
        self.discriminator = None
        self.app_url = app_url
        self.entity_type = entity_type
        self.deleted = deleted
        self.mention_ids = mention_ids
        self.author_id = author_id
        self.member_mention_ids = member_mention_ids
        self.comments = comments
        self.updated_at = updated_at
        self.group_mention_ids = group_mention_ids
        self.external_id = external_id
        self.id = id
        self.created_at = created_at
        self.text = text

    @property
    def app_url(self):
        """Gets the app_url of this ThreadedComment.  # noqa: E501

        The Shortcut application url for the Comment.  # noqa: E501

        :return: The app_url of this ThreadedComment.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this ThreadedComment.

        The Shortcut application url for the Comment.  # noqa: E501

        :param app_url: The app_url of this ThreadedComment.  # noqa: E501
        :type: str
        """
        if app_url is None:
            raise ValueError("Invalid value for `app_url`, must not be `None`")  # noqa: E501

        self._app_url = app_url

    @property
    def entity_type(self):
        """Gets the entity_type of this ThreadedComment.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this ThreadedComment.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ThreadedComment.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this ThreadedComment.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def deleted(self):
        """Gets the deleted of this ThreadedComment.  # noqa: E501

        True/false boolean indicating whether the Comment is deleted.  # noqa: E501

        :return: The deleted of this ThreadedComment.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ThreadedComment.

        True/false boolean indicating whether the Comment is deleted.  # noqa: E501

        :param deleted: The deleted of this ThreadedComment.  # noqa: E501
        :type: bool
        """
        if deleted is None:
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    @property
    def mention_ids(self):
        """Gets the mention_ids of this ThreadedComment.  # noqa: E501

        Deprecated: use member_mention_ids.  # noqa: E501

        :return: The mention_ids of this ThreadedComment.  # noqa: E501
        :rtype: list[str]
        """
        return self._mention_ids

    @mention_ids.setter
    def mention_ids(self, mention_ids):
        """Sets the mention_ids of this ThreadedComment.

        Deprecated: use member_mention_ids.  # noqa: E501

        :param mention_ids: The mention_ids of this ThreadedComment.  # noqa: E501
        :type: list[str]
        """
        if mention_ids is None:
            raise ValueError("Invalid value for `mention_ids`, must not be `None`")  # noqa: E501

        self._mention_ids = mention_ids

    @property
    def author_id(self):
        """Gets the author_id of this ThreadedComment.  # noqa: E501

        The unique ID of the Member that authored the Comment.  # noqa: E501

        :return: The author_id of this ThreadedComment.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this ThreadedComment.

        The unique ID of the Member that authored the Comment.  # noqa: E501

        :param author_id: The author_id of this ThreadedComment.  # noqa: E501
        :type: str
        """
        if author_id is None:
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id

    @property
    def member_mention_ids(self):
        """Gets the member_mention_ids of this ThreadedComment.  # noqa: E501

        An array of Member IDs that have been mentioned in this Comment.  # noqa: E501

        :return: The member_mention_ids of this ThreadedComment.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_mention_ids

    @member_mention_ids.setter
    def member_mention_ids(self, member_mention_ids):
        """Sets the member_mention_ids of this ThreadedComment.

        An array of Member IDs that have been mentioned in this Comment.  # noqa: E501

        :param member_mention_ids: The member_mention_ids of this ThreadedComment.  # noqa: E501
        :type: list[str]
        """
        if member_mention_ids is None:
            raise ValueError("Invalid value for `member_mention_ids`, must not be `None`")  # noqa: E501

        self._member_mention_ids = member_mention_ids

    @property
    def comments(self):
        """Gets the comments of this ThreadedComment.  # noqa: E501

        A nested array of threaded comments.  # noqa: E501

        :return: The comments of this ThreadedComment.  # noqa: E501
        :rtype: list[ThreadedComment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ThreadedComment.

        A nested array of threaded comments.  # noqa: E501

        :param comments: The comments of this ThreadedComment.  # noqa: E501
        :type: list[ThreadedComment]
        """
        if comments is None:
            raise ValueError("Invalid value for `comments`, must not be `None`")  # noqa: E501

        self._comments = comments

    @property
    def updated_at(self):
        """Gets the updated_at of this ThreadedComment.  # noqa: E501

        The time/date the Comment was updated.  # noqa: E501

        :return: The updated_at of this ThreadedComment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ThreadedComment.

        The time/date the Comment was updated.  # noqa: E501

        :param updated_at: The updated_at of this ThreadedComment.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def group_mention_ids(self):
        """Gets the group_mention_ids of this ThreadedComment.  # noqa: E501

        An array of Group IDs that have been mentioned in this Comment.  # noqa: E501

        :return: The group_mention_ids of this ThreadedComment.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_mention_ids

    @group_mention_ids.setter
    def group_mention_ids(self, group_mention_ids):
        """Sets the group_mention_ids of this ThreadedComment.

        An array of Group IDs that have been mentioned in this Comment.  # noqa: E501

        :param group_mention_ids: The group_mention_ids of this ThreadedComment.  # noqa: E501
        :type: list[str]
        """
        if group_mention_ids is None:
            raise ValueError("Invalid value for `group_mention_ids`, must not be `None`")  # noqa: E501

        self._group_mention_ids = group_mention_ids

    @property
    def external_id(self):
        """Gets the external_id of this ThreadedComment.  # noqa: E501

        This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :return: The external_id of this ThreadedComment.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ThreadedComment.

        This field can be set to another unique ID. In the case that the Comment has been imported from another tool, the ID in the other tool can be indicated here.  # noqa: E501

        :param external_id: The external_id of this ThreadedComment.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this ThreadedComment.  # noqa: E501

        The unique ID of the Comment.  # noqa: E501

        :return: The id of this ThreadedComment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThreadedComment.

        The unique ID of the Comment.  # noqa: E501

        :param id: The id of this ThreadedComment.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this ThreadedComment.  # noqa: E501

        The time/date the Comment was created.  # noqa: E501

        :return: The created_at of this ThreadedComment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ThreadedComment.

        The time/date the Comment was created.  # noqa: E501

        :param created_at: The created_at of this ThreadedComment.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def text(self):
        """Gets the text of this ThreadedComment.  # noqa: E501

        The text of the Comment.  # noqa: E501

        :return: The text of this ThreadedComment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ThreadedComment.

        The text of the Comment.  # noqa: E501

        :param text: The text of this ThreadedComment.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if issubclass(ThreadedComment, dict):
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
        if not isinstance(other, ThreadedComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
