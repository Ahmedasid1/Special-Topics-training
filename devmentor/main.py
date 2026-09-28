from ollama import Client

from config import MODEL_NAME
from prompts import GOODBYE_PROMPT, SYSTEM_PROMPT


def initialize_chat() -> tuple[Client, list[dict[str, str]]]:
	return Client(), [{"role": "system", "content": SYSTEM_PROMPT}]


def get_ai_response(
	user_input: str,
	messages: list[dict[str, str]],
	client: Client,
) -> str:
	messages.append({"role": "user", "content": user_input})
	try:
		response = client.chat(model=MODEL_NAME, messages=messages)
	except Exception:
		messages.pop()
		raise
	assistant_response = response.message.content
	messages.append({"role": "assistant", "content": assistant_response})
	return assistant_response


def reset_conversation(messages: list[dict[str, str]]) -> None:
	messages[:] = [{"role": "system", "content": SYSTEM_PROMPT}]
	print("Conversation reset.")


def display_history(messages: list[dict[str, str]]) -> None:
	history = [message for message in messages if message["role"] != "system"]
	if not history:
		print("No conversation history.")
		return

	for number, message in enumerate(history, start=1):
		print(f"{number}. {message['role'].upper()}: {message['content']}")


def process_user_input(
	user_input: str,
	messages: list[dict[str, str]],
	client: Client,
) -> bool:
	command = user_input.lower()
	if command == "/exit":
		print("Goodbye!")
		return False
	if command in {"exit", "quit"}:
		print(GOODBYE_PROMPT)
		return False
	if command == "/history":
		display_history(messages)
		return True
	if command == "/reset":
		reset_conversation(messages)
		return True
	if not user_input.strip():
		print("Please enter a question.")
		return True

	try:
		answer = get_ai_response(user_input, messages, client)
	except Exception as error:
		error_details = str(getattr(error, "error", error))
		is_model_not_found = (
			getattr(error, "status_code", None) == 404
			or ("model" in error_details.lower() and "not found" in error_details.lower())
		)
		if is_model_not_found:
			print("Model not found.")
			print("Please check the configured model name.")
		else:
			print("Unable to connect to Ollama.")
			print("Make sure Ollama is running and try again.")
		return True

	print(f"DevMentor: {answer}")
	return True


def main() -> None:
	client, messages = initialize_chat()
	while True:
		user_input = input("You: ").strip()
		if not process_user_input(user_input, messages, client):
			break


if __name__ == "__main__":
	main()
