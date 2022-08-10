import engtoipa as ipa
import json

mapping = {
 "ə": "ö",
 "ɪ": "e",
 "ɑ": "a",
 "æ": "ä",
 "ɔ": "o",
 "ʊ": "u",
 "ʧ": "ts",
 "ð": "t",
 "ɛ": "e",
 "ʤ": "ts",
 "ŋ": "ng",
 "ʃ": "sh",
 "θ": "t",
 "ʒ": "s",
 "b": "p",
 "z": "s",
 "w": "v",
 "ˌ": "",
 "*": "",
 "'": "",
 "ˈ": ""
}

def conv_line(s):
  s_ipa = ipa.convert(s)
  ttable = s_ipa.maketrans(mapping)
  return s_ipa.translate(ttable)

def conv(s):
  rows = s.splitlines()
  r = list(map(conv_line, rows))
  return '\n'.join(r)

def lambda_handler(event, context):
  body = json.loads(event["body"])
  responseBody = json.dumps({
    "output": conv(body["input"])
  },ensure_ascii=False)
  return {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    },
    "body": responseBody
  }

if __name__ == "__main__":
  print(lambda_handler({"body": "{ \"input\": \"laughing\" }"}, None))