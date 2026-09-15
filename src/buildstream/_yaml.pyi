#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


from enum import Enum, auto
from typing import Optional, runtime_checkable, Protocol, Any, Mapping

from ruamel import yaml
from .node import MappingNode, _SYNTHETIC_FILE_INDEX

class RepresenterState(Enum):
    doc = auto()
    init= auto()
    stream= auto()
    wait_key= auto()
    wait_list_item= auto()
    wait_value= auto()

class Representer:
    state: RepresenterState
    output: list
    keys: list
    def handle_event(self, event): ...
    def get_output(self) ->  MappingNode | None: ...


def load(filename: str, shortname: str, copy_tree: bool = False, project: Optional[object] = None) -> MappingNode: ...
def load_data(data:str, file_index:int=_SYNTHETIC_FILE_INDEX, file_name:str|None=None,copy_tree:bool=False) -> MappingNode: ...
def prepare_roundtrip_yaml() -> yaml.YAML: ...
def roundtrip_load(filename:str, allow_missing:bool=False) -> MappingNode: ...
@runtime_checkable
class Writeable(Protocol):
    """
    Stub class for classes that have a write method
    """
    def write(self,str): ...

def roundtrip_dump(contents:MappingNode, file:str|Writeable|None=None): ...
def roundtrip_dump_string(node: MappingNode) -> str: ...
