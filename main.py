from memory import add_to_memory, get_memory
from llm_response import get_llm_response

# Available Models with descriptions
available_models = {
    "mistral": {
        "id": "mistralai/Mistral-7B-Instruct-v0.1",
        "desc": "⚡ Mistral 7B – fast and lightweight for general Q&A"
    },
    "mixtral": {
        "id": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "desc": "🧠 Mixtral 8x7B – deeper reasoning, great for summaries and logic"
    },
    "llama": {
        "id": "meta-llama/Llama-3-8b-chat-hf",
        "desc": "💬 LLaMA 3 8B – best at natural conversation and storytelling"
    }
}

# Default model
selected_model_key = "mistral"
selected_model = available_models[selected_model_key]["id"]

print("🤖 Welcome to Multi-Model CLI Chatbot (TogetherAI)")
print("Type '!model model_name' to switch models (options: mistral, mixtral, llama)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You > ").strip()

    if not user_input:
        print("⚠️ Empty input. Try again.")
        continue

    if user_input.lower() == "exit":
        print("👋 Exiting chatbot. Bye!")
        break

    if user_input.lower().startswith("!model"):
        try:
            selected_key = user_input.split(" ", 1)[1].strip().lower()
            if selected_key in available_models:
                selected_model_key = selected_key
                selected_model = available_models[selected_model_key]["id"]
                print(f"✅ Switched to: {selected_model_key.upper()} – {available_models[selected_model_key]['desc']}")
            else:
                print("❌ Invalid model name. Use: mistral, mixtral, or llama")
        except IndexError:
            print("⚠️ Please provide a model name. Example: !model mixtral")
        continue

    add_to_memory(user_input)
    memory_context = "\n".join(get_memory())
    full_prompt = f"{memory_context}\nUser: {user_input}\nAI:"

    response = get_llm_response(full_prompt, model=selected_model)
    print(f"\n🧠 [{selected_model_key.upper()}] > {response}\n")
