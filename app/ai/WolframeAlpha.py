import spacy
import wolframalpha
import certifi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

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


