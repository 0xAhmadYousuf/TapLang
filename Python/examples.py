#!/usr/bin/env python3
"""
TapLang Usage Examples
Simple examples showing how to use the TapLang package
"""

from TapLang import interpret_taplang, reset_wait_state

def run_example(name, code):
    """Run a single example"""
    print(f"\n{name}:")
    print(f"Code: {code}")
    
    # Reset wait state for clean example runs
    reset_wait_state()
    
    result = interpret_taplang(code)
    if result['success']:
        print(f"SUCCESS ({result['instructions']} instructions)")
        for step in result['results']:
            print(f"  -> {step}")
    else:
        print(f"ERROR: {result['error']}")

def main():
    """Run all examples"""
    print("TapLang Examples")
    print("=" * 50)
    
    examples = [
        ("Basic Typing", "TYPE[Hello World]"),
        ("Key Sequence", "CLICK[H] CLICK[E] CLICK[L] CLICK[L] CLICK[O]"),
        ("Copy Shortcut", "PRESS[CTRL] CLICK[C] RELEASE[CTRL]"),
        ("Function Keys", "FUNCTION[1] WAIT[1000] FUNCTION[12]"),
        ("Left Modifier", "PRESS_LEFT[SHIFT] CLICK[A] RELEASE[SHIFT]"),
        ("Symbols", "CLICK[!] CLICK[@] CLICK[#] CLICK[$]"),
        ("With Delays", "TYPE[User] WAIT[500] CLICK[TAB] TYPE[Pass]"),
        ("Set Wait Fixed", "SET_WAIT[300] WAIT[] WAIT[] TYPE[Done]"),
        ("Set Wait Random", "SET_WAIT[RANDOM[100,500]] WAIT[] WAIT[] TYPE[Random]"),
        ("Type Random Text", "TYPE[RANDOM[Hello,Hi,Hey]] WAIT[200] TYPE[RANDOM[World,Earth,Universe]]"),
        ("Navigation", "CLICK[HOME] CLICK[END] CLICK[UP] CLICK[DOWN]"),
    ]
    
    for name, code in examples:
        run_example(name, code)
    
    print(f"\n{'='*50}")
    print("All examples completed!")

if __name__ == "__main__":
    main()