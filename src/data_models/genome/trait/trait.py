from __future__ import annotations

from dataclasses import dataclass

from .trait_family import TraitFamily
from .trait_name import TraitName


@dataclass
class Trait:
	"""
	Class for storing a trait, which can affect a blob's
	survival, fertility, attractiveness to mates, etc.
	"""
	name: TraitName
	family: TraitFamily
	value: float | str

