"""
Copyright 2017 Neural Networks and Deep Learning lab, MIPT

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from deeppavlov.core.models.component import Component
from deeppavlov.core.common.registry import register


@register("split_tokenizer")
class SplitTokenizer(Component):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, batch, *args, **kwargs):
        if isinstance(batch, (list, tuple)):
            return [self(line) for line in batch]
        else:
            return batch.split()