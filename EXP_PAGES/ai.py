import subprocess

def explain_brainfuck():
    result = subprocess.run(['ollama', 'chat', '--model', 'llama2', '--messages', '[{"role": "user", "content": "What is Brainfuck programming?"}]'], capture_output=True, text=True, check=True)
    return result.stdout

if __name__ == "__main__":
    explanation = explain_brainfuck()
    print(explanation)