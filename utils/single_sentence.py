from dataclasses import dataclass
from typing import Callable, Set, List, Iterable

import spacy
from spacy.tokens.token import Token
from spacy.tokens.doc import Doc
from spacy.tokens.span import Span


@dataclass
class SingleSentence(object):
    root: Token
    subtree: Set[spacy.tokens.token.Token]
    
    @property
    def start_idx(self):
        """
        Returns position (index) in original document where the single sentence begins.
        """
        return min(self.subtree, key=lambda token: token.i).i
    
    @property
    def end_index(self):
        """
        Returns last position (index) of the single sentence in original document.
        """
        return max(self.subtree, key=lambda token: token.i).i
    
    @property
    def tokens(self):
        """
        Return list of tokens.
        """
        return sorted(list(self.subtree), key=lambda token: token.idx)


def default_root_finding_strategy(token: Token) -> bool:
    return (token.pos_ in {'VERB', 'ADJ'} and token.dep_ in {'ccomp', 'conj'}) or token.dep_=='ROOT'


class SingleSentenceSplitter(object):
    """
    Splits complex sentences into single-verb sentences using provided root-finding strategy.
    Strategy is a function that, given a Token, shou
    ld return True if this token is a root of a sentence.
    """
    def __init__(self, root_finding_strategy: Callable[[Token], bool]=default_root_finding_strategy):
        self.root_finding_strategy = root_finding_strategy

    def _get_single_sentences(self, sent: Span) -> List[SingleSentence]:
        """
        Find roots of possible single sentences given the root finding strategy.
        """
        return [
            SingleSentence(token, set(token.subtree))
            for token in sent 
            if self.root_finding_strategy(token)
        ]

    def _make_unique(self, single_sents: List[SingleSentence]) -> List[SingleSentence]:
        """
        Remove subsentences from their parent sentences so that each word is mapped 
        to one and only one single sentence.
        """
        for i, s1 in enumerate(single_sents):
            for j, s2 in enumerate(single_sents[:i]):
                assert(j<i)
                #if s1.subtree.issubset(s2.subtree):
                if s1.root in s2.subtree:
                    single_sents[j].subtree = single_sents[j].subtree - s1.subtree
                #if s2.subtree.issubset(s1.subtree):
                if s2.root in s1.subtree:
                    single_sents[i].subtree = single_sents[i].subtree - s2.subtree
        return single_sents

    def __call__(self, doc: Doc) -> Iterable[Span]:
        """
        Perform sentence splitting on a given document.
        """
        for sent in doc.sents:
            separated_sents = self._make_unique(self._get_single_sentences(doc))
            for single_sent in separated_sents:
                #yield doc[single_sent.start_idx:single_sent.end_index]
                yield single_sent.tokens



def run_example():
    """ 
    Usage example.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("When I want to split a sentence, I apply my custom subsentencizer and wait for the results to be yielded.")
    sss = SingleSentenceSplitter()  # pass custom root finding strategy here if necessary
    for single_sent in sss(doc):
        print(f"type={type(single_sent)}, n_words={len(single_sent)}, text={single_sent}")


if __name__ == '__main__':
    run_example()