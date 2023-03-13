import openai
import spacy
from translate import Translator
from app.ai.WolframeAlpha import WolframAlpha
from app.models.MongoDb import get_openai_key,get_wolframalpha_key

class MicroAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.nlp = spacy.load("en_core_web_sm")

    def get_engine(self, question):
        doc = self.nlp(question)
        if any(token.text.lower() in ['classify', 'categorize', 'group'] for token in doc):
            return "text-davinci-002"
        elif any(token.text.lower() in ['summarize', 'brief', 'short'] for token in doc):
            return "text-davinci-002"
        elif any(token.text.lower() in ['translate', 'conversion'] for token in doc):
            return "text-davinci-002"
        elif any(token.text.lower() in ['solve', 'calculate', 'compute'] for token in doc):
            return "text-davinci-003"
        elif any(token.text.lower() in ['create', 'build', 'design', 'generate'] for token in doc):
            return "davinci-codex"
        else:            
            return "text-davinci-003"

    def generate_answer(self, question):
        wolfram = WolframAlpha(app_id=get_wolframalpha_key())
        answer = wolfram.answer_question(question=question)
        if "Lỗi: " in answer:
            translator = Translator(to_lang='en', from_lang='vi')
            question_en = translator.translate(question)
            engine = self.get_engine(question_en)

            openai.api_key = self.api_key
            completions = openai.Completion.create(
                engine=engine,
                prompt=question_en,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            message = completions.choices[0].text

            result = {'engine': engine, 'question': question, 'answer': message}
            return result
        else:
            result = {'engine': 'WolframAlpha', 'question': question, 'answer': answer}
            return result
