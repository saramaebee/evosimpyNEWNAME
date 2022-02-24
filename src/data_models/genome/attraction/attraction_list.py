from __future__ import annotations

import json
from dataclasses import dataclass

from .attraction import Attraction


@dataclass
class AttractionList:
	attractions: list[Attraction]

	def to_json(self) -> str:
		"""
		Converts AttractionList object to a JSON dictionary.

		:return: { trait, lower_bound, upper_bound, potential_values }
		"""
		return json.dumps([{
			'trait': attraction.trait,
			'lower_bound': attraction.lower_bound,
			'upper_bound': attraction.upper_bound,
			'potential_values': attraction.potential_values
		} for attraction in self.attractions])

	@classmethod
	def from_json(cls, json_string: str) -> AttractionList:
		"""
		Converts a JSON dictionary to an AttractionList object.

		:param json_string: The JSON dictionary to convert.
		:return: The AttractionList object.
		"""
		json_dict = json.loads(json_string)
		return cls(
			attractions=[Attraction(**attraction) for attraction in json_dict]
		)

	@classmethod
	def from_dict(cls, json_dict: dict) -> AttractionList:
		"""
		Converts a JSON dictionary to an AttractionList object.

		:param json_dict: The JSON dictionary to convert.
		:return: The AttractionList object.
		"""
		return cls.from_json(json.dumps(json_dict))
