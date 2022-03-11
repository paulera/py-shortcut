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

class HistoryChangesStory(object):
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
        'description': 'StoryHistoryChangeOldNewStr',
        'archived': 'StoryHistoryChangeOldNewBool',
        'started': 'StoryHistoryChangeOldNewBool',
        'task_ids': 'StoryHistoryChangeAddsRemovesInt',
        'mention_ids': 'StoryHistoryChangeAddsRemovesUuid',
        'story_type': 'StoryHistoryChangeOldNewStr',
        'name': 'StoryHistoryChangeOldNewStr',
        'completed': 'StoryHistoryChangeOldNewBool',
        'blocker': 'StoryHistoryChangeOldNewBool',
        'epic_id': 'StoryHistoryChangeOldNewInt',
        'branch_ids': 'StoryHistoryChangeAddsRemovesInt',
        'commit_ids': 'StoryHistoryChangeAddsRemovesInt',
        'requested_by_id': 'StoryHistoryChangeOldNewUuid',
        'iteration_id': 'StoryHistoryChangeOldNewInt',
        'label_ids': 'StoryHistoryChangeAddsRemovesInt',
        'workflow_state_id': 'StoryHistoryChangeOldNewInt',
        'object_story_link_ids': 'StoryHistoryChangeAddsRemovesInt',
        'follower_ids': 'StoryHistoryChangeAddsRemovesUuid',
        'owner_ids': 'StoryHistoryChangeAddsRemovesUuid',
        'estimate': 'StoryHistoryChangeOldNewInt',
        'subject_story_link_ids': 'StoryHistoryChangeAddsRemovesInt',
        'blocked': 'StoryHistoryChangeOldNewBool',
        'project_id': 'StoryHistoryChangeOldNewInt',
        'deadline': 'StoryHistoryChangeOldNewStr'
    }

    attribute_map = {
        'description': 'description',
        'archived': 'archived',
        'started': 'started',
        'task_ids': 'task_ids',
        'mention_ids': 'mention_ids',
        'story_type': 'story_type',
        'name': 'name',
        'completed': 'completed',
        'blocker': 'blocker',
        'epic_id': 'epic_id',
        'branch_ids': 'branch_ids',
        'commit_ids': 'commit_ids',
        'requested_by_id': 'requested_by_id',
        'iteration_id': 'iteration_id',
        'label_ids': 'label_ids',
        'workflow_state_id': 'workflow_state_id',
        'object_story_link_ids': 'object_story_link_ids',
        'follower_ids': 'follower_ids',
        'owner_ids': 'owner_ids',
        'estimate': 'estimate',
        'subject_story_link_ids': 'subject_story_link_ids',
        'blocked': 'blocked',
        'project_id': 'project_id',
        'deadline': 'deadline'
    }

    def __init__(self, description=None, archived=None, started=None, task_ids=None, mention_ids=None, story_type=None, name=None, completed=None, blocker=None, epic_id=None, branch_ids=None, commit_ids=None, requested_by_id=None, iteration_id=None, label_ids=None, workflow_state_id=None, object_story_link_ids=None, follower_ids=None, owner_ids=None, estimate=None, subject_story_link_ids=None, blocked=None, project_id=None, deadline=None):  # noqa: E501
        """HistoryChangesStory - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._archived = None
        self._started = None
        self._task_ids = None
        self._mention_ids = None
        self._story_type = None
        self._name = None
        self._completed = None
        self._blocker = None
        self._epic_id = None
        self._branch_ids = None
        self._commit_ids = None
        self._requested_by_id = None
        self._iteration_id = None
        self._label_ids = None
        self._workflow_state_id = None
        self._object_story_link_ids = None
        self._follower_ids = None
        self._owner_ids = None
        self._estimate = None
        self._subject_story_link_ids = None
        self._blocked = None
        self._project_id = None
        self._deadline = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if archived is not None:
            self.archived = archived
        if started is not None:
            self.started = started
        if task_ids is not None:
            self.task_ids = task_ids
        if mention_ids is not None:
            self.mention_ids = mention_ids
        if story_type is not None:
            self.story_type = story_type
        if name is not None:
            self.name = name
        if completed is not None:
            self.completed = completed
        if blocker is not None:
            self.blocker = blocker
        if epic_id is not None:
            self.epic_id = epic_id
        if branch_ids is not None:
            self.branch_ids = branch_ids
        if commit_ids is not None:
            self.commit_ids = commit_ids
        if requested_by_id is not None:
            self.requested_by_id = requested_by_id
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if label_ids is not None:
            self.label_ids = label_ids
        if workflow_state_id is not None:
            self.workflow_state_id = workflow_state_id
        if object_story_link_ids is not None:
            self.object_story_link_ids = object_story_link_ids
        if follower_ids is not None:
            self.follower_ids = follower_ids
        if owner_ids is not None:
            self.owner_ids = owner_ids
        if estimate is not None:
            self.estimate = estimate
        if subject_story_link_ids is not None:
            self.subject_story_link_ids = subject_story_link_ids
        if blocked is not None:
            self.blocked = blocked
        if project_id is not None:
            self.project_id = project_id
        if deadline is not None:
            self.deadline = deadline

    @property
    def description(self):
        """Gets the description of this HistoryChangesStory.  # noqa: E501


        :return: The description of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewStr
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HistoryChangesStory.


        :param description: The description of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewStr
        """

        self._description = description

    @property
    def archived(self):
        """Gets the archived of this HistoryChangesStory.  # noqa: E501


        :return: The archived of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewBool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this HistoryChangesStory.


        :param archived: The archived of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewBool
        """

        self._archived = archived

    @property
    def started(self):
        """Gets the started of this HistoryChangesStory.  # noqa: E501


        :return: The started of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewBool
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this HistoryChangesStory.


        :param started: The started of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewBool
        """

        self._started = started

    @property
    def task_ids(self):
        """Gets the task_ids of this HistoryChangesStory.  # noqa: E501


        :return: The task_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesInt
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        """Sets the task_ids of this HistoryChangesStory.


        :param task_ids: The task_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesInt
        """

        self._task_ids = task_ids

    @property
    def mention_ids(self):
        """Gets the mention_ids of this HistoryChangesStory.  # noqa: E501


        :return: The mention_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesUuid
        """
        return self._mention_ids

    @mention_ids.setter
    def mention_ids(self, mention_ids):
        """Sets the mention_ids of this HistoryChangesStory.


        :param mention_ids: The mention_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesUuid
        """

        self._mention_ids = mention_ids

    @property
    def story_type(self):
        """Gets the story_type of this HistoryChangesStory.  # noqa: E501


        :return: The story_type of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewStr
        """
        return self._story_type

    @story_type.setter
    def story_type(self, story_type):
        """Sets the story_type of this HistoryChangesStory.


        :param story_type: The story_type of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewStr
        """

        self._story_type = story_type

    @property
    def name(self):
        """Gets the name of this HistoryChangesStory.  # noqa: E501


        :return: The name of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewStr
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HistoryChangesStory.


        :param name: The name of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewStr
        """

        self._name = name

    @property
    def completed(self):
        """Gets the completed of this HistoryChangesStory.  # noqa: E501


        :return: The completed of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewBool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this HistoryChangesStory.


        :param completed: The completed of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewBool
        """

        self._completed = completed

    @property
    def blocker(self):
        """Gets the blocker of this HistoryChangesStory.  # noqa: E501


        :return: The blocker of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewBool
        """
        return self._blocker

    @blocker.setter
    def blocker(self, blocker):
        """Sets the blocker of this HistoryChangesStory.


        :param blocker: The blocker of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewBool
        """

        self._blocker = blocker

    @property
    def epic_id(self):
        """Gets the epic_id of this HistoryChangesStory.  # noqa: E501


        :return: The epic_id of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewInt
        """
        return self._epic_id

    @epic_id.setter
    def epic_id(self, epic_id):
        """Sets the epic_id of this HistoryChangesStory.


        :param epic_id: The epic_id of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewInt
        """

        self._epic_id = epic_id

    @property
    def branch_ids(self):
        """Gets the branch_ids of this HistoryChangesStory.  # noqa: E501


        :return: The branch_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesInt
        """
        return self._branch_ids

    @branch_ids.setter
    def branch_ids(self, branch_ids):
        """Sets the branch_ids of this HistoryChangesStory.


        :param branch_ids: The branch_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesInt
        """

        self._branch_ids = branch_ids

    @property
    def commit_ids(self):
        """Gets the commit_ids of this HistoryChangesStory.  # noqa: E501


        :return: The commit_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesInt
        """
        return self._commit_ids

    @commit_ids.setter
    def commit_ids(self, commit_ids):
        """Sets the commit_ids of this HistoryChangesStory.


        :param commit_ids: The commit_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesInt
        """

        self._commit_ids = commit_ids

    @property
    def requested_by_id(self):
        """Gets the requested_by_id of this HistoryChangesStory.  # noqa: E501


        :return: The requested_by_id of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewUuid
        """
        return self._requested_by_id

    @requested_by_id.setter
    def requested_by_id(self, requested_by_id):
        """Sets the requested_by_id of this HistoryChangesStory.


        :param requested_by_id: The requested_by_id of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewUuid
        """

        self._requested_by_id = requested_by_id

    @property
    def iteration_id(self):
        """Gets the iteration_id of this HistoryChangesStory.  # noqa: E501


        :return: The iteration_id of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewInt
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this HistoryChangesStory.


        :param iteration_id: The iteration_id of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewInt
        """

        self._iteration_id = iteration_id

    @property
    def label_ids(self):
        """Gets the label_ids of this HistoryChangesStory.  # noqa: E501


        :return: The label_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesInt
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        """Sets the label_ids of this HistoryChangesStory.


        :param label_ids: The label_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesInt
        """

        self._label_ids = label_ids

    @property
    def workflow_state_id(self):
        """Gets the workflow_state_id of this HistoryChangesStory.  # noqa: E501


        :return: The workflow_state_id of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewInt
        """
        return self._workflow_state_id

    @workflow_state_id.setter
    def workflow_state_id(self, workflow_state_id):
        """Sets the workflow_state_id of this HistoryChangesStory.


        :param workflow_state_id: The workflow_state_id of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewInt
        """

        self._workflow_state_id = workflow_state_id

    @property
    def object_story_link_ids(self):
        """Gets the object_story_link_ids of this HistoryChangesStory.  # noqa: E501


        :return: The object_story_link_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesInt
        """
        return self._object_story_link_ids

    @object_story_link_ids.setter
    def object_story_link_ids(self, object_story_link_ids):
        """Sets the object_story_link_ids of this HistoryChangesStory.


        :param object_story_link_ids: The object_story_link_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesInt
        """

        self._object_story_link_ids = object_story_link_ids

    @property
    def follower_ids(self):
        """Gets the follower_ids of this HistoryChangesStory.  # noqa: E501


        :return: The follower_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesUuid
        """
        return self._follower_ids

    @follower_ids.setter
    def follower_ids(self, follower_ids):
        """Sets the follower_ids of this HistoryChangesStory.


        :param follower_ids: The follower_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesUuid
        """

        self._follower_ids = follower_ids

    @property
    def owner_ids(self):
        """Gets the owner_ids of this HistoryChangesStory.  # noqa: E501


        :return: The owner_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesUuid
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this HistoryChangesStory.


        :param owner_ids: The owner_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesUuid
        """

        self._owner_ids = owner_ids

    @property
    def estimate(self):
        """Gets the estimate of this HistoryChangesStory.  # noqa: E501


        :return: The estimate of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewInt
        """
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        """Sets the estimate of this HistoryChangesStory.


        :param estimate: The estimate of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewInt
        """

        self._estimate = estimate

    @property
    def subject_story_link_ids(self):
        """Gets the subject_story_link_ids of this HistoryChangesStory.  # noqa: E501


        :return: The subject_story_link_ids of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeAddsRemovesInt
        """
        return self._subject_story_link_ids

    @subject_story_link_ids.setter
    def subject_story_link_ids(self, subject_story_link_ids):
        """Sets the subject_story_link_ids of this HistoryChangesStory.


        :param subject_story_link_ids: The subject_story_link_ids of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeAddsRemovesInt
        """

        self._subject_story_link_ids = subject_story_link_ids

    @property
    def blocked(self):
        """Gets the blocked of this HistoryChangesStory.  # noqa: E501


        :return: The blocked of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewBool
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this HistoryChangesStory.


        :param blocked: The blocked of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewBool
        """

        self._blocked = blocked

    @property
    def project_id(self):
        """Gets the project_id of this HistoryChangesStory.  # noqa: E501


        :return: The project_id of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewInt
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this HistoryChangesStory.


        :param project_id: The project_id of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewInt
        """

        self._project_id = project_id

    @property
    def deadline(self):
        """Gets the deadline of this HistoryChangesStory.  # noqa: E501


        :return: The deadline of this HistoryChangesStory.  # noqa: E501
        :rtype: StoryHistoryChangeOldNewStr
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this HistoryChangesStory.


        :param deadline: The deadline of this HistoryChangesStory.  # noqa: E501
        :type: StoryHistoryChangeOldNewStr
        """

        self._deadline = deadline

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
        if issubclass(HistoryChangesStory, dict):
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
        if not isinstance(other, HistoryChangesStory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other