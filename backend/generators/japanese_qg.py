from generators.base import QuestionGenerator

class JapaneseQuestionGenerator(QuestionGenerator):
    def generate(self, analysis, max_questions=5):
        questions = []
        for sentence in analysis.get("sentences", []):
            for token in sentence.get("tokens", []):
                ner = token.get("ner")
                if ner and token.get("text"):
                    questions.append({
                        "type": "cloze",
                        "question": sentence["text"].replace(token["text"], "＿＿＿＿", 1),
                        "answer": token["text"],
                        "source": "ner",
                        "entity_type": ner,
                    })
                    if len(questions) >= max_questions:
                        return questions
        return questions

def generate_questions(analysis, max_questions=5):
    return JapaneseQuestionGenerator().generate(analysis, max_questions)
