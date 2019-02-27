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


class UpdateQnaDTO(Model):
    """PATCH Body schema for Update Qna List.

    :param id: Unique id for the Q-A
    :type id: int
    :param answer: Answer text
    :type answer: str
    :param source: Source from which Q-A was indexed. eg.
     https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs
    :type source: str
    :param questions: List of questions associated with the answer.
    :type questions:
     ~azure.cognitiveservices.knowledge.qnamaker.models.UpdateQnaDTOQuestions
    :param metadata: List of metadata associated with the answer to be updated
    :type metadata:
     ~azure.cognitiveservices.knowledge.qnamaker.models.UpdateQnaDTOMetadata
    """

    _validation = {
        'id': {'maximum': 2147483647, 'minimum': 0},
        'source': {'max_length': 300},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'answer': {'key': 'answer', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'questions': {'key': 'questions', 'type': 'UpdateQnaDTOQuestions'},
        'metadata': {'key': 'metadata', 'type': 'UpdateQnaDTOMetadata'},
    }

    def __init__(self, **kwargs):
        super(UpdateQnaDTO, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.answer = kwargs.get('answer', None)
        self.source = kwargs.get('source', None)
        self.questions = kwargs.get('questions', None)
        self.metadata = kwargs.get('metadata', None)
