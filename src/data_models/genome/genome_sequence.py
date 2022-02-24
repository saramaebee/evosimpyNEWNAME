from __future__ import annotations
from dataclasses import dataclass, field
from base64 import b64encode, b64decode

import json

from attraction.attraction_list import AttractionList
from trait.trait_list import TraitList


@dataclass
class GenomeSequence:
	"""
	Class for storing a genome sequence, which can affect one or more traits.
	"""
	attraction_traits: AttractionList
	traits: TraitList
	value: float | str
	sequence: str = field(init=False, default_factory=lambda: '')

	def __post_init__(self):
		"""
		Initializes the sequence attribute.
		"""
		self.sequence = self.generate_sequence_string()


	def __str__(self):
		return "GenomeSequence(attraction_traits={}, sequence={}, traits={}, value={})".format(self.attraction_traits, self.sequence, self.traits, self.value)

	@classmethod
	def from_sequence(cls, sequence: str) -> GenomeSequence:
		""" Takes in sequence and returns GenomeSequence object. """
		decoded_sequence = b64decode(sequence)
		json_dict = json.loads(decoded_sequence)
		return GenomeSequence.from_json_string(json_dict)

	def generate_sequence_string(self) -> str:
		"""
		Converts a GenomeSequence object to a sequence string.

		:return: { attraction_traits, sequence, traits, value }
		"""
		json_string = json.dumps(json.loads(self.to_json_string()).pop('sequence'))
		return b64encode(json_string.encode('utf-8')).decode('utf-8')

	@classmethod
	def from_json_string(cls, _json_dict: str) -> GenomeSequence:
		"""Converts a JSON dictionary to a GenomeSequence object.

		:param _json_dict: The JSON dictionary to convert.
		:return: The GenomeSequence object.
		"""
		json_dict = {**json.loads(_json_dict)}
		return GenomeSequence(
			attraction_traits=AttractionList.from_dict(json_dict["attraction_traits"]),
			traits=TraitList.from_dict(json_dict["traits"]),
			value=json_dict["value"]
		)

	def to_json_string(self) -> str:
		"""
		Converts a GenomeSequence object to a JSON dictionary.

		:return: { attraction_traits, sequence, traits, value }
		"""
		return json.dumps({
			'attraction_traits': self.attraction_traits,
			'sequence': self.sequence,
			'traits': self.traits.to_dict(),
			'value': self.value
		})


@dataclass
class Mutation:
	rate: float
	strength: float


