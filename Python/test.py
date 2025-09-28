#!/usr/bin/env python3
"""
TapLang Interactive Test Tool
Simple test interface for TapLang interpreter
"""

from TapLang import interpret_taplang
import sys

def print_help():
    print("""
TapLang Test Tool
=================

Instructions:
- CLICK[key]     : Press and release key
- PRESS[key]     : Press and hold key  
- RELEASE[key]   : Release held key
- TYPE[text]     : Type text
- WAIT[ms]       : Wait specific milliseconds
- WAIT[]         : Wait default/random time (after SET_WAIT)
- SET_WAIT[ms]   : Set default wait time
- SET_WAIT[RANDOM[min,max]] : Set random wait range
- FUNCTION[1-12] : Press function key
- PRESS_LEFT[key]: Press left modifier
- PRESS_RIGHT[key]: Press right modifier

Examples:
  TYPE[Hello World]
  PRESS[CTRL] CLICK[C] RELEASE[CTRL]
  SET_WAIT[500] WAIT[] WAIT[] TYPE[Done]
  SET_WAIT[RANDOM[100,1000]] WAIT[] TYPE[Random timing]
  TYPE[RANDOM[Hello,Hi,Hey]] WAIT[200] TYPE[RANDOM[World,Earth]]
  FUNCTION[1] WAIT[1000] FUNCTION[2]
  ESCAPE_TYPE_START[Text with CLICK[A] keywords] ESCAPE_TYPE_END[~]

Commands:
  help     : Show this help
  examples : Show example codes
  quit/exit: Exit program
""")

def show_examples():
    examples = [
        ("Basic concept barriers", "TYPE[`Hello`] CLICK[SPACE] TYPE[`World`]"),
        ("FORMAT with RANDOM", "TYPE[`Hello FORMAT[RANDOM[Alice,Bob,Charlie]]`]"),
        ("Copy shortcut", "PRESS[CTRL] CLICK[C] RELEASE[CTRL]"),
        ("Function keys", "FUNCTION[1] WAIT[500] FUNCTION[12]"),
        ("Left shift", "PRESS_LEFT[SHIFT] CLICK[A] RELEASE[SHIFT]"),
        ("Multiple symbols", "CLICK[!] CLICK[@] CLICK[#] CLICK[$]"),
        ("With delays", "TYPE[`Username`] WAIT[1000] CLICK[TAB] TYPE[`Password`]"),
        ("Escape sequence", "ESCAPE_TYPE_START[This has PRESS[X] keywords] ESCAPE_TYPE_END[~]"),
        ("Navigation", "CLICK[HOME] PRESS[SHIFT] CLICK[END] RELEASE[SHIFT]"),
        ("Arrow keys", "CLICK[UP] CLICK[UP] CLICK[DOWN] CLICK[LEFT] CLICK[RIGHT]"),
        ("Missing concept barriers", 'TYPE[Hello World]'),
        ("Mismatched barriers", 'TYPE[`Hello World``]'),
        ("Emergency case needed", 'TYPE[`Text with ` backticks`]'),
        ("Empty RANDOM", 'TYPE[`FORMAT[RANDOM[]]`]'),
        ("Complex FORMAT", "TYPE[`Number FORMAT[RANDOM[1,2,3]] and letter FORMAT[RANDOM[A,B,C]]`]"),
    ]
    
    print("\nExample TapLang Codes:")
    print("=" * 50)
    for name, code in examples:
        print(f"\n{name}:")
        print(f"  {code}")
        result = interpret_taplang(code)
        if result['success']:
            print(f"  ✓ Valid ({result['instructions']} instructions)")
        else:
            print(f"  ✗ Error: {result['error']}")

def interactive_mode():
    print("TapLang Interactive Tester")
    print("Type 'help' for instructions, 'quit' to exit")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\nTapLang> ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
                
            elif user_input.lower() in ['help', 'h']:
                print_help()
                continue
                
            elif user_input.lower() in ['examples', 'ex']:
                show_examples()
                continue
                
            # Test the TapLang code
            print(f"\nParsing: {user_input}")
            result = interpret_taplang(user_input)
            
            if result['success']:
                print(f"✓ SUCCESS - Executed {result['instructions']} instruction(s)")
                print("\nExecution trace:")
                for i, step in enumerate(result['results'], 1):
                    print(f"  {i}. {step}")
            else:
                print(f"✗ ERROR: {result['error']}")
                print("\nTips:")
                print("- Check instruction spelling (CLICK, PRESS, TYPE, etc.)")
                print("- Ensure all PRESS operations have matching RELEASE")
                print("- Use valid key names (A-Z, 0-9, ENTER, SPACE, etc.)")
                print("- Check bracket syntax: INSTRUCTION[parameter]")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

def test_mode():
    """Run predefined tests"""
    print("TapLang Test Suite")
    print("=" * 40)
    
    # Valid tests
    valid_tests = [
        "TYPE[`Hello World`]",
        "CLICK[A] CLICK[B] CLICK[C]",
        "PRESS[SHIFT] CLICK[A] RELEASE[SHIFT]", 
        "FUNCTION[1] WAIT[1000] FUNCTION[12]",
        "PRESS_LEFT[CTRL] CLICK[C] RELEASE[CTRL]",
        "CLICK[!] CLICK[@] CLICK[#]",
        "TYPE[`Test`] CLICK[TAB] TYPE[`Password`] CLICK[ENTER]",
        "ESCAPE_TYPE_START[Text with PRESS[X]] ESCAPE_TYPE_END[~]",
        "CLICK[HOME] CLICK[END] CLICK[UP] CLICK[DOWN]",
        "TYPE[`Hello FORMAT[RANDOM[Alice,Bob]]`]",
        "TYPE[```Text with ` backticks```]"
    ]
    
    # Invalid tests (should fail)
    invalid_tests = [
        ("PRESS[CTRL]", "Unfinished press"),
        ("RELEASE[SHIFT]", "Release without press"), 
        ("CLICK[INVALID_KEY]", "Invalid key"),
        ("INVALID_CMD[A]", "Invalid instruction"),
        ("CLICK[]", "Missing parameter"),
        ("FUNCTION[13]", "Invalid function key"),
        ("WAIT[-100]", "Negative wait time"),
        ("ESCAPE_TYPE_START[text]", "Unfinished escape"),
        ("PRESS[A] PRESS[A]", "Double press same key"),
        ("TYPE[Hello World]", "Missing concept barriers"),
        ("TYPE[``Hello``]", "Invalid barrier length"),
        ("TYPE[```Hello``]", "Mismatched barriers"),
        ("TYPE[```Text with ``` backticks```]", "Need emergency barrier"),
        ("TYPE[```FORMAT[RANDOM[]]```]", "Empty RANDOM in FORMAT")
    ]
    
    print("\n🟢 VALID CODE TESTS:")
    passed = 0
    for code in valid_tests:
        print(f"Testing: {code}")
        result = interpret_taplang(code)
        if result['success']:
            print(f"✓ Success - {result['instructions']} instructions")
            passed += 1
        else:
            print(f"✗ Error: {result['error']}")
        print()
    
    print(f"\n🔴 INVALID CODE TESTS:")
    for code, reason in invalid_tests:
        print(f"\nTesting (should fail - {reason}): {code}")
        result = interpret_taplang(code)
        if not result['success']:
            print(f"✓ Correctly failed: {result['error']}")
        else:
            print(f"✗ Should have failed but didn't!")
    
    print(f"\n📊 SUMMARY: {passed}/{len(valid_tests)} valid tests passed")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-t', '--test']:
            test_mode()
        elif sys.argv[1] in ['-h', '--help']:
            print_help()
        else:
            # Interpret command line argument as TapLang code
            code = ' '.join(sys.argv[1:])
            result = interpret_taplang(code)
            if result['success']:
                print("SUCCESS:")
                for step in result['results']:
                    print(f"  {step}")
            else:
                print(f"ERROR: {result['error']}")
                sys.exit(1)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()