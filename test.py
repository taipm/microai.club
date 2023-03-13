import json
import spacy
import wolframalpha
import certifi
import ssl
import wikipedia
import requests

ssl._create_default_https_context = ssl._create_unverified_context
WOLFRAM_APPID = 'APER4E-58XJGHAVAK'

client = wolframalpha.Client(WOLFRAM_APPID)

def search_wiki(keyword):
    try:
        page = wikipedia.page(keyword)
        return page.summary
    except:
        return "No result from Wikipedia."

def remove_brackets(variable):
    return variable.split('(')[0]

def resolve_list_or_dict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext']

def get_primary_image_url(title):
    url = 'http://en.wikipedia.org/w/api.php'
    data = {'action':'query', 'prop':'pageimages','format':'json','piprop':'original','titles':title}
    try:
        res = requests.get(url, params=data)
        key = list(res.json()['query']['pages'].keys())[0]
        imageUrl = res.json()['query']['pages'][key]['original']['source']
        return imageUrl
    except Exception as err:
        return None

def get_wolframalpha_result(query):
    res = client.query(query)
    results = []
    
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



    # # Truy cập các trường và giá trị trong đối tượng Python
    # success = data['@success']
    # error = data['@error']
    # numpods = data['@numpods']
    # datatypes = data['@datatypes']
    # timedout = data['@timedout']
    # inputstring = data['@inputstring']
    # pod = data['pod']

    # # Truy cập các trường và giá trị trong mảng pod
    # title = pod[0]['@title']
    # scanner = pod[0]['@scanner']
    # id = pod[0]['@id']
    # position = pod[0]['@position']
    # error_pod = pod[0]['@error']
    # numsubpods = pod[0]['@numsubpods']
    # subpod = pod[0]['subpod']

    # # Truy cập các trường và giá trị trong subpod
    # title_subpod = subpod['@title']
    # img = subpod['img']
    # plaintext = subpod['plaintext']

    # subpods = data['pod'][0]['subpod']

    # # In từng hàng dữ liệu
    # for subpod in subpods:
    #     print(f"Title: {subpod['@title']}\nPlaintext: {subpod['plaintext']}\n")
    # #print(res)
    # return res

   
def get_wolframalpha_result(query):
    res = client.query(query)
    results = []

    # Lấy danh sách các pods có kết quả trả về
    for pod in res.pods:
        # Lấy danh sách các subpod bên trong pod
        for subpod in pod.subpods:
            # Thêm nội dung của subpod vào danh sách kết quả
            if subpod.img:
                # Lấy đường dẫn tới hình ảnh tương ứng với kết quả
                img_url = subpod.img.src
                # Tạo thẻ HTML để hiển thị hình ảnh
                img_html = f'<img src="{img_url}" alt="{pod.title}">'
                # Thêm thẻ HTML vào danh sách kết quả
                results.append(img_html)
            elif subpod.plaintext:
                # Thêm nội dung của subpod vào danh sách kết quả
                results.append(subpod.plaintext)

    # Kiểm tra xem có kết quả nào được tìm thấy hay không
    if not results:
        return "Lỗi: Không có kết quả phù hợp được tìm thấy."

    # Chuyển đổi danh sách kết quả thành chuỗi HTML và trả về
    return "<br>".join(results)

q = "Solve x^2 - 3x - 7 = 0"
result = get_wolframalpha_result(query=q)
print(result) # Paris