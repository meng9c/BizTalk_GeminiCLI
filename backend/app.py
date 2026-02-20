import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
# from groq import Groq

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__)
# frontend/ 디렉토리를 정적 폴더로 설정
CORS(app)

# Groq API 클라이언트 초기화 (실제 API 키 사용)
# api_key = os.environ.get("GROQ_API_KEY")
# if not api_key:
#     print("경고: GROQ_API_KEY가 .env 파일에 설정되지 않았습니다.")
#     # 개발/테스트용 임시 키나 오류 처리를 여기에 추가할 수 있습니다.
# client = Groq(api_key=api_key)

@app.route('/')
def index():
    # frontend/index.html을 서비스하기 위한 설정이지만,
    # Vercel 배포 시에는 보통 정적 파일과 API가 분리되므로 Flask에서 직접 서빙하는 것은 주된 목적이 아님.
    # 개발 편의를 위해 루트 경로 접속 시 간단한 메시지를 반환합니다.
    return "Welcome to BizTone Converter Backend!"

@app.route('/api/convert', methods=['POST'])
def convert_text():
    """
    사용자로부터 텍스트와 변환 대상(페르소나)을 받아,
    Groq AI를 통해 변환된 텍스트를 반환하는 API 엔드포인트.
    1단계에서는 더미 응답을 반환합니다.
    """
    data = request.json
    if not data or 'text' not in data or 'persona' not in data:
        return jsonify({"error": "'text'와 'persona' 필드가 필요합니다."}), 400

    original_text = data.get('text')
    persona = data.get('persona')

    # 1단계: 실제 Groq API 연동 대신 더미(dummy) 데이터 반환
    # Sprint 3에서 실제 변환 로직으로 교체될 예정입니다.
    dummy_response = f"입력 텍스트: '{original_text}'
    페르소나: '{persona}'에 맞춰 변환된 결과입니다. (이것은 더미 응답입니다.)"

    return jsonify({
        "original_text": original_text,
        "converted_text": dummy_response,
        "persona": persona
    })

if __name__ == '__main__':
    # Vercel 환경에서는 이 부분이 실행되지 않음.
    # 로컬 개발 시 `flask run` 또는 `python backend/app.py`로 서버를 실행.
    app.run(debug=True, port=5001)
