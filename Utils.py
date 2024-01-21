import json
from difflib import get_close_matches


def load_knowledge_base(file_path: str):
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


def chat_bot(data) -> str:
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    user_input = data.question
    answer = data.answer
    if answer:
        knowledge_base["questions"].append({"question": user_input, "answer": answer})
        save_knowledge_base("knowledge_base.json", knowledge_base)
        return "Thank you! I learned a new response!"
    else:
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            return answer
        else:
            return "I don\'t know the answer. Can you teach me?"
