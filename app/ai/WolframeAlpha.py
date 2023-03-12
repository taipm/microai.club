import spacy
import wolframalpha
import certifi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# class WolframAlpha:
#     def __init__(self, app_id):
#         self.app_id = app_id
#         self.client = wolframalpha.Client(self.app_id)
#         self.nlp = spacy.load("en_core_web_sm")
#     def classify_question(self, question):
#         doc = self.nlp(question)
#         for ent in doc.ents:
#             #if ent.label_ in ["MATH_SYMBOL", "QUANTITY", "DATE", "TIME", "PERSON", "ORG"]:
#                 return True
#         return False

#     def answer_question(self, question, format="plaintext"):
#         if self.classify_question(question):
#             res = self.client.query(question)
#             answer = next(res.results).text
#             if format == "image":
#                 answer = next(res.results).image
#             return answer
#         else:
#             return "I'm sorry, I cannot answer that question."

#     def authenticate(self):
#         try:
#             self.client.query("test")
#             return True
#         except:
#             return False

#     def set_format(self, format):
#         self.format = format

#     def set_app_id(self, app_id):
#         self.app_id = app_id
#         self.client = wolframalpha.Client(self.app_id)

# w = WolframAlpha()
# a = w.answer_question('1+1')
# print(a)


import wolframalpha

class WolframAlpha:
    def __init__(self, app_id):
        self.client = wolframalpha.Client(app_id)
        
    def answer_question(self, question):
        # Kiểm tra xem câu hỏi có hợp lệ không
        if not question.strip():
            return "Lỗi: Không có câu hỏi được cung cấp."
        
        # Gửi câu hỏi đến WolframAlpha
        res = self.client.query(question)
        
        # Kiểm tra xem kết quả trả về có hợp lệ không
        if not res.success:
            return "Lỗi: Không thể trả lời câu hỏi này."
        
        # Lấy kết quả đầu tiên
        result = next(res.results, None)
        
        # Kiểm tra xem kết quả trả về có hợp lệ không
        if result is None or result.text.strip() == "":
            return "Lỗi: Không có kết quả phù hợp được tìm thấy."
        
        # Trả về kết quả
        return result.text


