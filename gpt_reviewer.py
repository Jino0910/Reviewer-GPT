import openai
import sys
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

def prompt(file_content):
    return (
        "아래 코드를 리뷰하고, 코드 품질 향상을 위한 의견, 코드 스타일, "
        "최적화 제안 및 잠재적인 버그에 대한 피드백을 제공해주세요.\n\n"
        "코드:\n"
        f"{file_content}\n\n"
        "피드백:"
    )

def review_code(file_content):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "당신은 iOS 개발 경력이 10년 이상인 시니어 개발자입니다."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt(file_content)},
                    ],
                }
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
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
