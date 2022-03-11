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

class IterationSlim(object):
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
        'labels': 'list[Label]',
        'mention_ids': 'list[str]',
        'member_mention_ids': 'list[str]',
        'name': 'str',
        'label_ids': 'list[int]',
        'updated_at': 'datetime',
        'group_mention_ids': 'list[str]',
        'end_date': 'datetime',
        'follower_ids': 'list[str]',
        'group_ids': 'list[str]',
        'start_date': 'datetime',
        'status': 'str',
        'id': 'int',
        'stats': 'IterationStats',
        'created_at': 'datetime'
    }

    attribute_map = {
        'app_url': 'app_url',
        'entity_type': 'entity_type',
        'labels': 'labels',
        'mention_ids': 'mention_ids',
        'member_mention_ids': 'member_mention_ids',
        'name': 'name',
        'label_ids': 'label_ids',
        'updated_at': 'updated_at',
        'group_mention_ids': 'group_mention_ids',
        'end_date': 'end_date',
        'follower_ids': 'follower_ids',
        'group_ids': 'group_ids',
        'start_date': 'start_date',
        'status': 'status',
        'id': 'id',
        'stats': 'stats',
        'created_at': 'created_at'
    }

    def __init__(self, app_url=None, entity_type=None, labels=None, mention_ids=None, member_mention_ids=None, name=None, label_ids=None, updated_at=None, group_mention_ids=None, end_date=None, follower_ids=None, group_ids=None, start_date=None, status=None, id=None, stats=None, created_at=None):  # noqa: E501
        """IterationSlim - a model defined in Swagger"""  # noqa: E501
        self._app_url = None
        self._entity_type = None
        self._labels = None
        self._mention_ids = None
        self._member_mention_ids = None
        self._name = None
        self._label_ids = None
        self._updated_at = None
        self._group_mention_ids = None
        self._end_date = None
        self._follower_ids = None
        self._group_ids = None
        self._start_date = None
        self._status = None
        self._id = None
        self._stats = None
        self._created_at = None
        self.discriminator = None
        self.app_url = app_url
        self.entity_type = entity_type
        self.labels = labels
        self.mention_ids = mention_ids
        self.member_mention_ids = member_mention_ids
        self.name = name
        self.label_ids = label_ids
        self.updated_at = updated_at
        self.group_mention_ids = group_mention_ids
        self.end_date = end_date
        self.follower_ids = follower_ids
        self.group_ids = group_ids
        self.start_date = start_date
        self.status = status
        self.id = id
        self.stats = stats
        self.created_at = created_at

    @property
    def app_url(self):
        """Gets the app_url of this IterationSlim.  # noqa: E501

        The Shortcut application url for the Iteration.  # noqa: E501

        :return: The app_url of this IterationSlim.  # noqa: E501
        :rtype: str
        """
        return self._app_url

    @app_url.setter
    def app_url(self, app_url):
        """Sets the app_url of this IterationSlim.

        The Shortcut application url for the Iteration.  # noqa: E501

        :param app_url: The app_url of this IterationSlim.  # noqa: E501
        :type: str
        """
        if app_url is None:
            raise ValueError("Invalid value for `app_url`, must not be `None`")  # noqa: E501

        self._app_url = app_url

    @property
    def entity_type(self):
        """Gets the entity_type of this IterationSlim.  # noqa: E501

        A string description of this resource  # noqa: E501

        :return: The entity_type of this IterationSlim.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this IterationSlim.

        A string description of this resource  # noqa: E501

        :param entity_type: The entity_type of this IterationSlim.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def labels(self):
        """Gets the labels of this IterationSlim.  # noqa: E501

        An array of labels attached to the iteration.  # noqa: E501

        :return: The labels of this IterationSlim.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IterationSlim.

        An array of labels attached to the iteration.  # noqa: E501

        :param labels: The labels of this IterationSlim.  # noqa: E501
        :type: list[Label]
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def mention_ids(self):
        """Gets the mention_ids of this IterationSlim.  # noqa: E501

        Deprecated: use member_mention_ids.  # noqa: E501

        :return: The mention_ids of this IterationSlim.  # noqa: E501
        :rtype: list[str]
        """
        return self._mention_ids

    @mention_ids.setter
    def mention_ids(self, mention_ids):
        """Sets the mention_ids of this IterationSlim.

        Deprecated: use member_mention_ids.  # noqa: E501

        :param mention_ids: The mention_ids of this IterationSlim.  # noqa: E501
        :type: list[str]
        """
        if mention_ids is None:
            raise ValueError("Invalid value for `mention_ids`, must not be `None`")  # noqa: E501

        self._mention_ids = mention_ids

    @property
    def member_mention_ids(self):
        """Gets the member_mention_ids of this IterationSlim.  # noqa: E501

        An array of Member IDs that have been mentioned in the Story description.  # noqa: E501

        :return: The member_mention_ids of this IterationSlim.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_mention_ids

    @member_mention_ids.setter
    def member_mention_ids(self, member_mention_ids):
        """Sets the member_mention_ids of this IterationSlim.

        An array of Member IDs that have been mentioned in the Story description.  # noqa: E501

        :param member_mention_ids: The member_mention_ids of this IterationSlim.  # noqa: E501
        :type: list[str]
        """
        if member_mention_ids is None:
            raise ValueError("Invalid value for `member_mention_ids`, must not be `None`")  # noqa: E501

        self._member_mention_ids = member_mention_ids

    @property
    def name(self):
        """Gets the name of this IterationSlim.  # noqa: E501

        The name of the iteration.  # noqa: E501

        :return: The name of this IterationSlim.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IterationSlim.

        The name of the iteration.  # noqa: E501

        :param name: The name of this IterationSlim.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label_ids(self):
        """Gets the label_ids of this IterationSlim.  # noqa: E501

        An array of label ids attached to the iteration.  # noqa: E501

        :return: The label_ids of this IterationSlim.  # noqa: E501
        :rtype: list[int]
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        """Sets the label_ids of this IterationSlim.

        An array of label ids attached to the iteration.  # noqa: E501

        :param label_ids: The label_ids of this IterationSlim.  # noqa: E501
        :type: list[int]
        """
        if label_ids is None:
            raise ValueError("Invalid value for `label_ids`, must not be `None`")  # noqa: E501

        self._label_ids = label_ids

    @property
    def updated_at(self):
        """Gets the updated_at of this IterationSlim.  # noqa: E501

        The instant when this iteration was last updated.  # noqa: E501

        :return: The updated_at of this IterationSlim.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IterationSlim.

        The instant when this iteration was last updated.  # noqa: E501

        :param updated_at: The updated_at of this IterationSlim.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def group_mention_ids(self):
        """Gets the group_mention_ids of this IterationSlim.  # noqa: E501

        An array of Group IDs that have been mentioned in the Story description.  # noqa: E501

        :return: The group_mention_ids of this IterationSlim.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_mention_ids

    @group_mention_ids.setter
    def group_mention_ids(self, group_mention_ids):
        """Sets the group_mention_ids of this IterationSlim.

        An array of Group IDs that have been mentioned in the Story description.  # noqa: E501

        :param group_mention_ids: The group_mention_ids of this IterationSlim.  # noqa: E501
        :type: list[str]
        """
        if group_mention_ids is None:
            raise ValueError("Invalid value for `group_mention_ids`, must not be `None`")  # noqa: E501

        self._group_mention_ids = group_mention_ids

    @property
    def end_date(self):
        """Gets the end_date of this IterationSlim.  # noqa: E501

        The date this iteration begins.  # noqa: E501

        :return: The end_date of this IterationSlim.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this IterationSlim.

        The date this iteration begins.  # noqa: E501

        :param end_date: The end_date of this IterationSlim.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def follower_ids(self):
        """Gets the follower_ids of this IterationSlim.  # noqa: E501

        An array of UUIDs for any Members listed as Followers.  # noqa: E501

        :return: The follower_ids of this IterationSlim.  # noqa: E501
        :rtype: list[str]
        """
        return self._follower_ids

    @follower_ids.setter
    def follower_ids(self, follower_ids):
        """Sets the follower_ids of this IterationSlim.

        An array of UUIDs for any Members listed as Followers.  # noqa: E501

        :param follower_ids: The follower_ids of this IterationSlim.  # noqa: E501
        :type: list[str]
        """
        if follower_ids is None:
            raise ValueError("Invalid value for `follower_ids`, must not be `None`")  # noqa: E501

        self._follower_ids = follower_ids

    @property
    def group_ids(self):
        """Gets the group_ids of this IterationSlim.  # noqa: E501

        An array of UUIDs for any Groups you want to add as Followers. Currently, only one Group association is presented in our web UI.  # noqa: E501

        :return: The group_ids of this IterationSlim.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this IterationSlim.

        An array of UUIDs for any Groups you want to add as Followers. Currently, only one Group association is presented in our web UI.  # noqa: E501

        :param group_ids: The group_ids of this IterationSlim.  # noqa: E501
        :type: list[str]
        """
        if group_ids is None:
            raise ValueError("Invalid value for `group_ids`, must not be `None`")  # noqa: E501

        self._group_ids = group_ids

    @property
    def start_date(self):
        """Gets the start_date of this IterationSlim.  # noqa: E501

        The date this iteration begins.  # noqa: E501

        :return: The start_date of this IterationSlim.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this IterationSlim.

        The date this iteration begins.  # noqa: E501

        :param start_date: The start_date of this IterationSlim.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this IterationSlim.  # noqa: E501

        The status of the iteration. Values are either \"unstarted\", \"started\", or \"done\".  # noqa: E501

        :return: The status of this IterationSlim.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IterationSlim.

        The status of the iteration. Values are either \"unstarted\", \"started\", or \"done\".  # noqa: E501

        :param status: The status of this IterationSlim.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def id(self):
        """Gets the id of this IterationSlim.  # noqa: E501

        The ID of the iteration.  # noqa: E501

        :return: The id of this IterationSlim.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IterationSlim.

        The ID of the iteration.  # noqa: E501

        :param id: The id of this IterationSlim.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def stats(self):
        """Gets the stats of this IterationSlim.  # noqa: E501


        :return: The stats of this IterationSlim.  # noqa: E501
        :rtype: IterationStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this IterationSlim.


        :param stats: The stats of this IterationSlim.  # noqa: E501
        :type: IterationStats
        """
        if stats is None:
            raise ValueError("Invalid value for `stats`, must not be `None`")  # noqa: E501

        self._stats = stats

    @property
    def created_at(self):
        """Gets the created_at of this IterationSlim.  # noqa: E501

        The instant when this iteration was created.  # noqa: E501

        :return: The created_at of this IterationSlim.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IterationSlim.

        The instant when this iteration was created.  # noqa: E501

        :param created_at: The created_at of this IterationSlim.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(IterationSlim, dict):
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
        if not isinstance(other, IterationSlim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
