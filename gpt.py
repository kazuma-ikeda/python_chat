from openai import OpenAI
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAIクライアントの初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # または使用したいモデル
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "申し訳ありません。エラーが発生しました。"