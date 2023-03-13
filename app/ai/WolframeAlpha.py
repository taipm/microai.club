import spacy
import wolframalpha
import certifi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class WolframAlpha:
    def __init__(self, app_id):
        self.client = wolframalpha.Client(app_id)
    def answer_question(self, question):
        res = self.client.query(question)
        results = []

        # Lấy danh sách các pods có kết quả trả về
        for pod in res.pods:
            # Lấy danh sách các subpod bên trong pod
            for subpod in pod.subpods:
                # Thêm nội dung của subpod vào danh sách kết quả
                # if subpod.img:
                #     # Lấy đường dẫn tới hình ảnh tương ứng với kết quả
                #     img_url = subpod.img.src
                #     # Tạo thẻ HTML để hiển thị hình ảnh
                #     img_html = f'<img src="{img_url}" alt="{pod.title}">'
                #     # Thêm thẻ HTML vào danh sách kết quả
                #     results.append(img_html)
                if subpod.plaintext:
                    # Thêm nội dung của subpod vào danh sách kết quả
                    results.append(subpod.plaintext)

        # Kiểm tra xem có kết quả nào được tìm thấy hay không
        if not results:
            return "Lỗi: Không có kết quả phù hợp được tìm thấy."

        # Chuyển đổi danh sách kết quả thành chuỗi HTML và trả về
        return "<br>".join(results)



