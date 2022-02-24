from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, unique

import json


@unique
class TraitName(Enum):
	"""
	Enum for storing the possible values for a trait.

	Values should be lower-cased and should be unique.
	"""
	SIZE = 'size'
	SPEED = 'speed'
	ENERGY = 'energy'
	VISION = 'vision'
	SIGHT = 'sight'
	HEALTH = 'health'
	ALTRUISM = 'altruism'
	COOPERATION = 'cooperation'
	ATTRACTIVENESS = 'attractiveness'
	FERTILITY = 'fertility'
	ENJOYMENT_FROM_SEX = 'sex_enjoyment'
	MUTATION = 'mutation'


@unique
class TraitFamily(Enum):
	"""
	Enum for storing the possible families a trait may belong to.

	Values should be lower-cased and should be unique.
	"""
	FERTILITY = 'fertility'
	MUTATIONS = 'mutations'
	PERSONALITY = 'personality'
	SEX = 'sex'
	SURVIVAL = 'survival'


@dataclass
class Trait:
	"""
	Class for storing a trait, which can affect a blob's
	survival, fertility, attractiveness to mates, etc.
	"""
	name: TraitName
	family: TraitFamily
	value: float | str

	def __str__(self):
		return 'Trait(name={}, value={})'.format(self.name, self.value)

	@classmethod
	def from_json_string(cls, _json_dict: str) -> 'Trait':
		""" Takes JSON string and returns Trait object. """
		json_dict = json.loads(_json_dict)
		return Trait(
			name=TraitName(json_dict['name'].lower()),
			value=json_dict['value'],
			family=TraitFamily(json_dict['family'].lower())
		)

	def to_json_string(self) -> str:
		"""
		Converts a Trait object to a JSON dictionary.
		:return: The JSON dictionary.
		"""
		return json.dumps(self.__dict__)

@dataclass
class TraitList:
	list: list[Trait]

	def to_json(self) -> str:
		"""
		Converts the TraitList object to a json string.

		:return: The json string.
		"""
		return json.dumps(self.to_dict())

	def to_dict(self) -> dict:
		return { list : [trait.__dict__ for trait in self.list] }
