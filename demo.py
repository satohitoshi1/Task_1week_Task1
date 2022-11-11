from PIL import Image
import io
import requests

url = "https://dog.ceo/api/breeds/image/random"

# (1)APIを実行
responce = requests.get(url)

# (2) 返ってきたJSONを処理
jsonObj = responce.json()
ImageUrl = jsonObj["message"]
strImageURL = str(ImageUrl)

# (3) 画像URLから画像表示
file = io.BytesIO(requests.get(strImageURL).content)
img = Image.open(file)
img.show()
