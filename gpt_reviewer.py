import openai
import sys
import os

# OpenAI API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code(file_content):
    try:
        # GPT-4o 모델을 사용하여 코드 리뷰 수행
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "당신은 iOS 개발 경력이 10년 이상인 시니어 개발자입니다. "
                        "아래 코드를 리뷰하고, 코드 품질 향상을 위한 의견, 코드 스타일, "
                        "최적화 제안 및 잠재적인 버그에 대한 피드백을 제공해주세요."
                    )
                },
                {
                    "role": "user",
                    "content": f"코드:\n{file_content}\n\n피드백:"
                }
            ],
            max_tokens=1000,  # 응답 길이를 적절히 설정
            temperature=0.2,  # 낮은 온도로 응답의 신뢰도를 높임
        )
        # GPT의 응답 내용을 반환
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error while reviewing code: {str(e)}"

if __name__ == "__main__":
    # 첫 번째 인자로 파일 경로를 받아 코드 내용 읽기
    file_path = sys.argv[1]
    try:
        with open(file_path, "r") as file:
            content = file.read()
        # 코드 리뷰 결과를 출력
        review = review_code(content)
        print(f"Code Review for {file_path}:\n\n{review}")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error while processing file {file_path}: {str(e)}")
