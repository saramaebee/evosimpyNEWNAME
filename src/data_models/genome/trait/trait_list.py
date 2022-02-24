from __future__ import annotations

import json
from dataclasses import dataclass

from .trait import Trait


@dataclass
class TraitList:
	traits: list[Trait]

	def to_json(self) -> str:
		"""
		Converts the TraitList object to a json string.

		:return: The json string.
		"""
		return json.dumps([{
				'name': trait.name.value,
				'family': trait.family.value,
				'value': trait.value
		} for trait in self.traits])

	@classmethod
	def from_json(cls, json_string: str) -> TraitList:
		"""
		Converts a json string to a TraitList object.

		:param json_string: The json string.
		:return: The TraitList object.
		"""
		json_dict = json.loads(json_string)
		return cls(traits=[Trait(**trait) for trait in json_dict])

	@classmethod
	def from_dict(cls, json_dict: dict) -> TraitList:
		"""
		Converts a JSON dictionary to an AttractionList object.

		:param json_dict: The JSON dictionary to convert.
		:return: The AttractionList object.
		"""
		return cls.from_json(json.dumps(json_dict))

	def to_dict(self) -> dict:
		"""
		Converts the TraitList object to a JSON dictionary.

		:return: The JSON dictionary.
		"""
		return json.loads(self.to_json())
