from analyzers.base import TextAnalyzer

try:
    import spacy
except ImportError:
    spacy = None

class JapaneseAnalyzer(TextAnalyzer):
    def __init__(self):
        self.nlp = None
        if spacy is not None:
            try:
                self.nlp = spacy.load("ja_ginza")
            except Exception:
                self.nlp = None

    def analyze(self, text: str):
        if self.nlp is None:
            return {"language": "ja", "engine": "fallback", "text": text, "sentences": []}
        doc = self.nlp(text)
        sentences = []
        for sent in doc.sents:
            tokens = []
            for token in sent:
                tokens.append({
                    "text": token.text,
                    "lemma": token.lemma_,
                    "pos": token.pos_,
                    "dep": token.dep_,
                    "head": token.head.text,
                    "ner": token.ent_type_,
                })
            sentences.append({"text": sent.text, "tokens": tokens})
        return {"language": "ja", "engine": "ginza", "text": text, "sentences": sentences}

_analyzer = JapaneseAnalyzer()

def analyze_text(text: str):
    return _analyzer.analyze(text)
