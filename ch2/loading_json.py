import json


text_json = '''{
    "demo":"Processing JSON",
    "instructor":"Michael Kennedy",
    "duration":5.0
}'''


print(type(text_json), text_json)

data = json.loads(text_json)
print(type(data), data)