from TapLang import interpret_taplang

# Test basic concept barriers
test_cases = [
    'TYPE[```Hello World```]',
    'TYPE[```FORMAT[RANDOM[Alice,Bob,Charlie]]```]',
    'TYPE[````Text with ``` inside````]'
]

for case in test_cases:
    print(f"\nTesting: {case}")
    try:
        result = interpret_taplang(case)
        if result['success']:
            print(f"✅ SUCCESS: {result['results'][0]}")
        else:
            print(f"❌ ERROR: {result['error']}")
    except Exception as e:
        print(f"❌ EXCEPTION: {e}")

# Test old syntax (should fail)
old_tests = [
    'TYPE[Hello World]',
    'TYPE[RANDOM[Alice,Bob]]'
]

print("\n" + "="*50)
print("Testing OLD SYNTAX (should fail):")

for case in old_tests:
    print(f"\nTesting: {case}")
    try:
        result = interpret_taplang(case)
        if result['success']:
            print(f"⚠️ UNEXPECTED SUCCESS: {result['results'][0]}")
        else:
            print(f"✅ CORRECTLY FAILED: {result['error']}")
    except Exception as e:
        print(f"✅ CORRECTLY FAILED: {e}")