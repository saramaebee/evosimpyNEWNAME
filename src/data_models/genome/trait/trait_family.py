from __future__ import annotations

from enum import Enum, unique


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
