import openai
import sys
import os

# OpenAI API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code(file_content):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=(
                "당신은 iOS 개발 경력이 10년 이상인 시니어 개발자입니다. "
                "아래 코드를 리뷰하고, 코드 품질 향상을 위한 의견, 코드 스타일, "
                "최적화 제안 및 잠재적인 버그에 대한 피드백을 제공해주세요.\n\n"
                "코드:\n"
                f"{file_content}\n\n"
                "피드백:"
            ),
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error while reviewing code: {str(e)}"

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        content = file.read()
    review = review_code(content)
    print(f"Code Review for {file_path}:\n\n{review}")
