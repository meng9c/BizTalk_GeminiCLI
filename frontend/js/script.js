document.addEventListener('DOMContentLoaded', () => {
    const convertButton = document.getElementById('convertButton');
    const inputText = document.getElementById('inputText');
    const outputText = document.getElementById('outputText');
    const personaSelector = document.getElementById('personaSelector');

    // 변환하기 버튼 클릭 이벤트 리스너
    convertButton.addEventListener('click', () => {
        const text = inputText.value;
        const persona = personaSelector.value;

        if (!text.trim()) {
            alert('변환할 텍스트를 입력해주세요.');
            return;
        }

        // Sprint 2에서 실제 API 호출 로직으로 대체될 예정입니다.
        // 현재는 더미 데이터를 사용하여 프론트엔드-백엔드 연동을 테스트합니다.
        callConversionAPI(text, persona);
    });

    /**
     * 백엔드 API를 호출하여 텍스트 변환을 요청하는 함수
     * @param {string} text - 변환할 원문 텍스트
     * @param {string} persona - 변환 대상 (upward, lateral, external)
     */
    async function callConversionAPI(text, persona) {
        const API_URL = 'http://127.0.0.1:5000/api/convert'; // 로컬 Flask 서버 주소

        // 로딩 상태 표시 (Sprint 2에서 구현)
        outputText.textContent = '변환 중...';
        convertButton.disabled = true;

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: text,
                    persona: persona,
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || '알 수 없는 오류가 발생했습니다.');
            }

            const data = await response.json();
            
            // 변환된 텍스트를 결과 영역에 표시
            outputText.textContent = data.converted_text;

        } catch (error) {
            // 오류 발생 시 메시지 표시
            outputText.textContent = `오류: ${error.message}`;
            console.error('API 호출 중 오류 발생:', error);
        } finally {
            // 로딩 상태 해제 (Sprint 2에서 구현)
            convertButton.disabled = false;
        }
    }
});
