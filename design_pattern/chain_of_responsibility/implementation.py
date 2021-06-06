from __future__ import annotations
from design_pattern.chain_of_responsibility.framework import ChainLink
from typing import List
from enum import Enum, auto
from abc import ABC, abstractmethod
import random


class PartOfSpeech(Enum):
	"""
	This is the part of speech for a given word.
	"""

	Noun = auto(),
	Verb = auto(),
	Adjective = auto(),
	Adverb = auto()


class Word():
	"""
	This class represents a single word.
	"""

	def __init__(self, *, part_of_speech: PartOfSpeech, text: str):

		self.__part_of_speech = part_of_speech
		self.__text = text

	def get_part_of_speech(self) -> PartOfSpeech:
		return self.__part_of_speech

	def get_text(self) -> str:
		return self.__text


class SentenceFragmentMadlibPart(ChainLink):
	"""
	This class represents a static fragment of text.
	"""

	def __init__(self, *, fragment: str):
		super().__init__()

		self.__fragment = fragment

	def process_chain_link(self, *args, **kwargs):
		return self.__fragment


class RandomWordMadlibPart(ChainLink):
	"""
	This class represents a random possible word based on the provided part of speech.
	"""

	def __init__(self, *, part_of_speech: PartOfSpeech):
		super().__init__()

		self.__part_of_speech = part_of_speech

	def process_chain_link(self, *args, **kwargs):
		"""
		This basic example assumes that the complete list of possible parts of speech are in the first element of args
		"""
		_all_possible_parts_of_speech = args[0]  # type: List[Word]
		_possible_words = [_word for _word in _all_possible_parts_of_speech if _word.get_part_of_speech() == self.__part_of_speech]
		_chosen_word = random.choice(_possible_words)  # type: Word
		return _chosen_word.get_text()
