from TapLang.parser import parse_instruction, tokenize_code
import json

test_input = 'TYPE[```Hello World```]'

print(f"Testing input: {test_input}")
print("="*50)

# Test tokenization
print("\n1. Tokenization:")
try:
    tokens = tokenize_code(test_input)
    print(f"Tokens: {tokens}")
except Exception as e:
    print(f"Tokenization error: {e}")

# Test parsing
print("\n2. Parsing:")
try:
    parsed = parse_instruction(test_input)
    print(f"Parsed result:")
    for key, value in parsed.items():
        if key == 'barrier_info':
            print(f"  {key}: {json.dumps(value, indent=2)}")
        else:
            print(f"  {key}: {value}")
except Exception as e:
    print(f"Parsing error: {e}")

# Test with FORMAT
print("\n" + "="*50)
format_test = 'TYPE[```Hello FORMAT[RANDOM[Alice,Bob]]```]'
print(f"Testing FORMAT: {format_test}")

try:
    parsed = parse_instruction(format_test)
    print(f"Parsed result:")
    for key, value in parsed.items():
        if isinstance(value, (dict, list)):
            print(f"  {key}: {json.dumps(value, indent=2)}")
        else:
            print(f"  {key}: {value}")
except Exception as e:
    print(f"Parsing error: {e}")