import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Groq API 클라이언트 초기화 (실제 API 키 사용)
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("경고: GROQ_API_KEY가 .env 파일에 설정되지 않았습니다.")
client = Groq(api_key=api_key)

# 페르소나별 시스템 프롬프트 정의
SYSTEM_PROMPTS = {
    "upward": "당신은 직장 상사에게 보고하기 위한 정중하고 전문적인 어투의 비즈니스 문서를 작성하는 AI 어시스턴트입니다. 핵심 내용을 명확히 전달하되, 예의 바른 표현을 사용하세요.",
    "lateral": "당신은 동료와 원활한 협업을 위해 친절하고 명확하게 소통하는 AI 어시스턴트입니다. 요청 사항이나 공유할 내용을 간결하고 이해하기 쉽게 작성하세요.",
    "external": "당신은 고객에게 회사의 전문성과 신뢰감을 보여주는 AI 어시스턴트입니다. 극존칭을 사용하여 정중하고 상세하게 안내하며, 긍정적인 고객 경험을 만드는 데 집중하세요."
}


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/convert', methods=['POST'])
def convert_text():
    """
    사용자로부터 텍스트와 변환 대상(페르소나)을 받아,
    Groq AI를 통해 변환된 텍스트를 반환하는 API 엔드포인트.
    """
    data = request.json
    if not data or 'text' not in data or 'persona' not in data:
        return jsonify({"error": "'text'와 'persona' 필드가 필요합니다."}), 400

    original_text = data.get('text')
    persona = data.get('persona', 'lateral')  # 기본값으로 'lateral' 설정

    if persona not in SYSTEM_PROMPTS:
        return jsonify({"error": "지원하지 않는 'persona' 값입니다."}), 400

    system_prompt = SYSTEM_PROMPTS[persona]

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": f"다음 문장을 비즈니스 상황에 맞게 변환해 주세요:\n\n{original_text}",
                }
            ],
            model="moonshotai/kimi-k2-instruct-0905",
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        converted_text = chat_completion.choices[0].message.content
        return jsonify({
            "original_text": original_text,
            "converted_text": converted_text,
            "persona": persona
        })

    except Exception as e:
        print(f"Groq API 호출 중 오류 발생: {e}")
        return jsonify({"error": "AI 모델을 호출하는 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."}), 500


if __name__ == '__main__':
    # Vercel 환경에서는 이 부분이 실행되지 않음.
    # 로컬 개발 시 `flask run` 또는 `python backend/app.py`로 서버를 실행.
    app.run(debug=True, port=5000)
