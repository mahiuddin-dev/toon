from openai import OpenAI
from toon import encode, decode
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()


def extract_data_with_toon(raw_data):
    toon_data = encode(raw_data)
    # toon_data = raw_data
    messages=[
        {
            "role": "user",
            "content": f"Extract and structure this data:\n\n{toon_data}\n\nReturn in same format."
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        max_tokens=500,
        temperature=0.3
    )
    assistant_reply = response.choices[0].message.content
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens
    print("Input tokens:", input_tokens)
    print("Output tokens:", output_tokens)
    print("Total tokens:", total_tokens)
    final_response = decode(assistant_reply)
    # final_response = assistant_reply
    return final_response


messy_data = {
    "records": [
        {"raw": "2024-01-15 | Alice | 95000"},
        {"raw": "2024-02-20 | Bob | 87000"},
        {"raw": "2024-02-21 | Rana | 88000"},
        {"raw": "2024-02-22 | Kabir | 87000"},
        {"raw": "2024-02-23 | Kamal | 87000"},
    ]
}

result = extract_data_with_toon(messy_data)
print(result)
