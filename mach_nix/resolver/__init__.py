from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Iterable, Set

from packaging.version import Version

from mach_nix.data.providers import ProviderInfo
from mach_nix.requirements import Requirement


@dataclass
class ResolvedPkg:
    name: str
    ver: Version
    build_inputs: List[str]
    prop_build_inputs: List[str]
    is_root: bool
    provider_info: ProviderInfo
    extras_selected: List[str]
    # contains direct or indirect children wich have been diconnected due to circular deps
    removed_circular_deps: Set[str] = field(default_factory=set)


class Resolver(ABC):

    @abstractmethod
    def resolve(self, reqs: Iterable[Requirement]) -> List[ResolvedPkg]:
        pass
