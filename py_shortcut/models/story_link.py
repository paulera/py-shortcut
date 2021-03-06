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

class StoryLink(object):
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
        'id': 'int',
        'subject_id': 'int',
        'subject_workflow_state_id': 'int',
        'verb': 'str',
        'object_id': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'id': 'id',
        'subject_id': 'subject_id',
        'subject_workflow_state_id': 'subject_workflow_state_id',
        'verb': 'verb',
        'object_id': 'object_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, entity_type=None, id=None, subject_id=None, subject_workflow_state_id=None, verb=None, object_id=None, created_at=None, updated_at=None):  # noqa: E501
        """StoryLink - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._id = None
        self._subject_id = None
        self._subject_workflow_state_id = None
        self._verb = None
        self._object_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.entity_type = entity_type
        self.id = id
        self.subject_id = subject_id
        self.subject_workflow_state_id = subject_workflow_state_id
        self.verb = verb
        self.object_id = object_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def entity_type(self):
        """Gets the entity_type of this StoryLink.  # noqa: E501

        A string description of this resource.  # noqa: E501

        :return: The entity_type of this StoryLink.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this StoryLink.

        A string description of this resource.  # noqa: E501

        :param entity_type: The entity_type of this StoryLink.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def id(self):
        """Gets the id of this StoryLink.  # noqa: E501

        The unique identifier of the Story Link.  # noqa: E501

        :return: The id of this StoryLink.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoryLink.

        The unique identifier of the Story Link.  # noqa: E501

        :param id: The id of this StoryLink.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def subject_id(self):
        """Gets the subject_id of this StoryLink.  # noqa: E501

        The ID of the subject Story.  # noqa: E501

        :return: The subject_id of this StoryLink.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this StoryLink.

        The ID of the subject Story.  # noqa: E501

        :param subject_id: The subject_id of this StoryLink.  # noqa: E501
        :type: int
        """
        if subject_id is None:
            raise ValueError("Invalid value for `subject_id`, must not be `None`")  # noqa: E501

        self._subject_id = subject_id

    @property
    def subject_workflow_state_id(self):
        """Gets the subject_workflow_state_id of this StoryLink.  # noqa: E501

        The workflow state of the \"subject\" story.  # noqa: E501

        :return: The subject_workflow_state_id of this StoryLink.  # noqa: E501
        :rtype: int
        """
        return self._subject_workflow_state_id

    @subject_workflow_state_id.setter
    def subject_workflow_state_id(self, subject_workflow_state_id):
        """Sets the subject_workflow_state_id of this StoryLink.

        The workflow state of the \"subject\" story.  # noqa: E501

        :param subject_workflow_state_id: The subject_workflow_state_id of this StoryLink.  # noqa: E501
        :type: int
        """
        if subject_workflow_state_id is None:
            raise ValueError("Invalid value for `subject_workflow_state_id`, must not be `None`")  # noqa: E501

        self._subject_workflow_state_id = subject_workflow_state_id

    @property
    def verb(self):
        """Gets the verb of this StoryLink.  # noqa: E501

        How the subject Story acts on the object Story. This can be \"blocks\", \"duplicates\", or \"relates to\".  # noqa: E501

        :return: The verb of this StoryLink.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this StoryLink.

        How the subject Story acts on the object Story. This can be \"blocks\", \"duplicates\", or \"relates to\".  # noqa: E501

        :param verb: The verb of this StoryLink.  # noqa: E501
        :type: str
        """
        if verb is None:
            raise ValueError("Invalid value for `verb`, must not be `None`")  # noqa: E501

        self._verb = verb

    @property
    def object_id(self):
        """Gets the object_id of this StoryLink.  # noqa: E501

        The ID of the object Story.  # noqa: E501

        :return: The object_id of this StoryLink.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this StoryLink.

        The ID of the object Story.  # noqa: E501

        :param object_id: The object_id of this StoryLink.  # noqa: E501
        :type: int
        """
        if object_id is None:
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501

        self._object_id = object_id

    @property
    def created_at(self):
        """Gets the created_at of this StoryLink.  # noqa: E501

        The time/date when the Story Link was created.  # noqa: E501

        :return: The created_at of this StoryLink.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StoryLink.

        The time/date when the Story Link was created.  # noqa: E501

        :param created_at: The created_at of this StoryLink.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this StoryLink.  # noqa: E501

        The time/date when the Story Link was last updated.  # noqa: E501

        :return: The updated_at of this StoryLink.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this StoryLink.

        The time/date when the Story Link was last updated.  # noqa: E501

        :param updated_at: The updated_at of this StoryLink.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(StoryLink, dict):
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
        if not isinstance(other, StoryLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
