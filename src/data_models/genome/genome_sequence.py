from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import json

from src.data_models.genome.trait import Trait, TraitList


def list_of_traits_from_dict(trait_dict: dict) -> list[Trait]:
	"""
	Converts a dictionary of traits to a list of Trait objects.


	:param trait_dict: The json dict of traits.
	:return: The list of Trait objects.
	"""
	traits = []
	for trait_name, trait_values in trait_dict.items():
		traits.append(Trait(trait_name, trait_values))
	return traits  # type: ignore




@dataclass
class GenomeSequence:
	"""
	Class for storing a genome sequence, which can affect one or more traits.
	"""
	attraction_traits: list[Attraction]
	sequence: str
	traits: TraitList
	value: float | str

	def __str__(self):
		return "GenomeSequence(attraction_traits={}, sequence={}, traits={}, value={})".format(self.attraction_traits, self.sequence, self.traits, self.value)

	@classmethod
	def from_sequence(cls, sequence: str) -> GenomeSequence:
		""" Takes in sequence and returns GenomeSequence object. """
		# TODO: Figure out a way to encode traits into a sequence.
		...

	@classmethod
	def from_json_string(cls, _json_dict: str) -> GenomeSequence:
		"""Converts a JSON dictionary to a GenomeSequence object.

		:param _json_dict: The JSON dictionary to convert.
		:return: The GenomeSequence object.
		"""
		json_dict = json.loads(_json_dict)
		return GenomeSequence(
			attraction_traits=list_of_traits_from_dict(json_dict["attraction_traits"]),
			sequence=json_dict["sequence"],
			traits=list_of_traits_from_dict(json_dict["traits"]),
			value=json_dict["value"]
		)

	def to_json_string(self) -> str:
		"""
		Converts a GenomeSequence object to a JSON dictionary.

		:return: { attraction_traits, sequence, traits, value }
		"""
		return json.dumps({
			"attraction_traits": self.attraction_traits,
			"sequence": self.sequence,
			"traits": self.traits.to_dict(),
			"value": self.value
		})


@dataclass
class Mutation:
	rate: float
	strength: float

@dataclass
class Attraction:
	"""
	Attraction type, stores the expected values of the trait.
	"""
	trait: str
	lower_bound: Optional[float] = None
	upper_bound: Optional[float] = None
	potential_values: Optional[list[str]] = None

@dataclass
class AttractionList:
	attractions: list[Attraction]

	def to_json(self) -> str:
		"""
		Converts AttractionList object to a JSON dictionary.

		:return: { trait, lower_bound, upper_bound, potential_values }
		"""
		return json.dumps([{
			"trait": attraction.trait,
			"lower_bound": attraction.lower_bound,
			"upper_bound": attraction.upper_bound,
			"potential_values": attraction.potential_values
		} for attraction in self.attractions])

	@classmethod
	def from_json(cls, _json_dict: str) -> AttractionList:
		"""
		Converts a JSON dictionary to an AttractionList object.

		:param _json_dict: The JSON dictionary to convert.
		:return: The AttractionList object.
		"""
		json_dict = json.loads(_json_dict)
		return AttractionList(
			attractions=[Attraction(
				trait=attraction["trait"],
				lower_bound=attraction["lower_bound"],
				upper_bound=attraction["upper_bound"],
				potential_values=attraction["potential_values"]
			) for attraction in json_dict]
		)
