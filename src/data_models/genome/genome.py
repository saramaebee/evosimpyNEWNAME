from dataclasses import dataclass

from .chromosome import Chromosome


@dataclass
class Genome:
	sequences: list[Chromosome]

	@classmethod
	def from_genetic_string(cls, genetic_string: str) -> 'Genome':
		"""
		Creates a Genome from a genetic string.

		:param genetic_string: The genetic string to create the genome from.
		:return: A Genome object.
		"""
		sequences = []
		for sequence in genetic_string.split('.'):
			sequences.append(Chromosome.from_sequence(sequence))
		return cls(sequences)

	def to_genetic_string(self) -> str:
		"""
		Returns the genetic string of the genome.

		:return: The genetic string of the genome.
		"""
		return '.'.join([sequence.sequence for sequence in self.sequences])
