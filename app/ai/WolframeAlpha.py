import spacy
import wolframalpha
import certifi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class WolframAlpha:
    def __init__(self, app_id):
        self.client = wolframalpha.Client(app_id)
        
    def answer_question(self, question):      
        if not question.strip():
            return "Lỗi: Không có câu hỏi được cung cấp."
        
        # Gửi câu hỏi đến WolframAlpha
        res = self.client.query(question)
        results = []
        # Kiểm tra xem kết quả trả về có hợp lệ không
        if not res.success:
            return "Lỗi: Không thể trả lời câu hỏi này."
        
        # Lấy danh sách các pods có kết quả trả về
        for pod in res.pods:
            # Lấy danh sách các subpod bên trong pod
            for subpod in pod.subpods:
                # Thêm nội dung của subpod vào danh sách kết quả            
                if subpod.plaintext:
                    results.append(subpod.plaintext)
                    
        # Kiểm tra xem có kết quả nào được tìm thấy hay không
        if not results:
            return "Lỗi: Không có kết quả phù hợp được tìm thấy."
        
        # Chuyển đổi danh sách kết quả thành chuỗi và trả về
        return "\n".join(results)        


