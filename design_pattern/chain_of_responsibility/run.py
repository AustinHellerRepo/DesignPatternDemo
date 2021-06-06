from __future__ import annotations
from design_pattern.chain_of_responsibility.implementation import PartOfSpeech, RandomWordMadlibPart, SentenceFragmentMadlibPart, Word


_all_possible_words = [
	Word(
		part_of_speech=PartOfSpeech.Noun,
		text="tree"
	),
	Word(
		part_of_speech=PartOfSpeech.Noun,
		text="foot"
	),
	Word(
		part_of_speech=PartOfSpeech.Adjective,
		text="blue"
	),
	Word(
		part_of_speech=PartOfSpeech.Adjective,
		text="big"
	),
	Word(
		part_of_speech=PartOfSpeech.Verb,
		text="run"
	),
	Word(
		part_of_speech=PartOfSpeech.Verb,
		text="speak"
	),
	Word(
		part_of_speech=PartOfSpeech.Adverb,
		text="softly"
	),
	Word(
		part_of_speech=PartOfSpeech.Adverb,
		text="quickly"
	)
]


_madlib = SentenceFragmentMadlibPart(
	fragment="It was on Tuesday that the "
)
_ = _madlib.set_next(RandomWordMadlibPart(
	part_of_speech=PartOfSpeech.Noun
))
_ = _.set_next(SentenceFragmentMadlibPart(
	fragment=" decided to "
))
_ = _.set_next(RandomWordMadlibPart(
	part_of_speech=PartOfSpeech.Verb
))
_ = _.set_next(SentenceFragmentMadlibPart(
	fragment=" "
))
_ = _.set_next(RandomWordMadlibPart(
	part_of_speech=PartOfSpeech.Adverb
))
_ = _.set_next(SentenceFragmentMadlibPart(
	fragment=" and walk over to the "
))
_ = _.set_next(RandomWordMadlibPart(
	part_of_speech=PartOfSpeech.Adjective
))
_ = _.set_next(SentenceFragmentMadlibPart(
	fragment=" "
))
_ = _.set_next(RandomWordMadlibPart(
	part_of_speech=PartOfSpeech.Noun
))
_ = _.set_next(SentenceFragmentMadlibPart(
	fragment="."
))

_processed_chain = _madlib.process_chain(_all_possible_words)
_sentence = "".join(_processed_chain)
print(_sentence)
