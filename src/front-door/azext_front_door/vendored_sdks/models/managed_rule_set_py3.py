# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagedRuleSet(Model):
    """Base class for all types of ManagedRuleSet.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureManagedRuleSet

    All required parameters must be populated in order to send to Azure.

    :param priority: Describes priority of the rule
    :type priority: int
    :param version: defines version of the ruleset
    :type version: int
    :param rule_set_type: Required. Constant filled by server.
    :type rule_set_type: str
    """

    _validation = {
        'rule_set_type': {'required': True},
    }

    _attribute_map = {
        'priority': {'key': 'priority', 'type': 'int'},
        'version': {'key': 'version', 'type': 'int'},
        'rule_set_type': {'key': 'ruleSetType', 'type': 'str'},
    }

    _subtype_map = {
        'rule_set_type': {'AzureManagedRuleSet': 'AzureManagedRuleSet'}
    }

    def __init__(self, *, priority: int=None, version: int=None, **kwargs) -> None:
        super(ManagedRuleSet, self).__init__(**kwargs)
        self.priority = priority
        self.version = version
        self.rule_set_type = None
