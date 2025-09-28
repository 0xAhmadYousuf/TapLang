from TapLang import interpret_taplang

print("🎯 SIMPLIFIED CONCEPT BARRIERS TEST")
print("=" * 50)

# Simple cases with single backticks
simple_tests = [
    'TYPE[`Hello`]',
    'TYPE[`Hello World`]', 
    'TYPE[`FORMAT[RANDOM[Alice,Bob,Charlie]]`]',
    'TYPE[`Your number is FORMAT[RANDOM[1,2,3]]`]',
]

print("\n✨ SIMPLE CASES (single backticks):")
for test in simple_tests:
    print(f"\nTesting: {test}")
    try:
        result = interpret_taplang(test)
        if result['success']:
            output = result['results'][0].replace("Typed: '", "").replace("'", "")
            print(f"✅ Success: {output}")
        else:
            print(f"❌ Failed: {result['error']}")
    except Exception as e:
        print(f"❌ Exception: {e}")

# Emergency cases with triple backticks
emergency_tests = [
    'TYPE[```Text with ` single backtick```]',
    'TYPE[````Text with ``` triple backticks````]',
]

print(f"\n🚨 EMERGENCY CASES (when text contains backticks):")
for test in emergency_tests:
    print(f"\nTesting: {test}")
    try:
        result = interpret_taplang(test)
        if result['success']:
            output = result['results'][0].replace("Typed: '", "").replace("'", "")
            print(f"✅ Success: {output}")
        else:
            print(f"❌ Failed: {result['error']}")
    except Exception as e:
        print(f"❌ Exception: {e}")

# Invalid cases
invalid_tests = [
    'TYPE[Hello World]',  # No backticks
    'TYPE[`Text with ` inside`]',  # Need emergency syntax
]

print(f"\n❌ INVALID CASES (should fail):")
for test in invalid_tests:
    print(f"\nTesting: {test}")
    try:
        result = interpret_taplang(test)
        if result['success']:
            print(f"⚠️ Unexpected success: {result['results'][0]}")
        else:
            print(f"✅ Correctly failed: {result['error']}")
    except Exception as e:
        print(f"✅ Correctly failed: {e}")

print(f"\n{'='*50}")
print("🎉 Much simpler now! Single backticks for simple cases! 🚀")