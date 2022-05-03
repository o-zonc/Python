import json

with open("Asterisk\songdo.json", "r", encoding="utf8") as f:
  data = f.read()
  jsdt = json.loads(data)

source = input("출발지: ")
# 출발지를 입력받은 뒤
for i in range(len(jsdt["Building"])):
  if jsdt["Building"][i]["name"] == source:
    source_id = jsdt["Building"][i]["id"]