memory = []

def add_to_memory(text):
    memory.append(text)
    if len(memory) > 3:
        memory.pop(0)
    with open("memory_log.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(memory))

def get_memory():
    return memory
