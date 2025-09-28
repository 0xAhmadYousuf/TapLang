# TapLang Python Implementation

**🤖 Complete Keyboard Action Language for AI Systems**

Powerful Python interpreter designed for AI agents, web terminals, and automation systems.

## 📁 Package Structure

```
Python/
├── TapLang/              # Core package
│   ├── __init__.py       # Package exports
│   ├── data.py           # Specification data
│   ├── parser.py         # Code parsing & tokenization
│   ├── validator.py      # Instruction validation
│   └── interpreter.py    # Execution engine
├── test.py              # Interactive test tool
├── examples.py          # Live examples
└── README.md            # This file
```

## 🚀 Installation & Usage

### Basic Import
```python
from TapLang import interpret_taplang

# Simple execution
result = interpret_taplang("TYPE[Hello AI] CLICK[ENTER]")
if result['success']:
    for step in result['results']:
        print(step)
else:
    print(f"Error: {result['error']}")
```

### Advanced Usage
```python
from TapLang import interpret_taplang, reset_wait_state

# Complex sequences with timing
code = """
SET_WAIT[RANDOM[100,300]]
TYPE[Starting automation...]
WAIT[]
PRESS[CTRL] CLICK[A] RELEASE[CTRL]
WAIT[]
TYPE[Selected all text]
"""

result = interpret_taplang(code)
```

## 🛠️ Command Line Tools

### Interactive Testing
```bash
# Start interactive mode
python test.py

# Test single command
python test.py "PRESS[CTRL] CLICK[C] RELEASE[CTRL]"

# Run comprehensive test suite
python test.py --test

# View help
python test.py --help
```

### Live Examples
```bash
# See all examples in action
python examples.py
```

## 📝 Complete Language Reference

### Core Instructions

| Instruction | Description | Example |
|-------------|-------------|----------|
| `CLICK[key]` | Press and release key | `CLICK[A]`, `CLICK[ENTER]` |
| `PRESS[key]` | Press and hold key | `PRESS[SHIFT]` |
| `RELEASE[key]` | Release held key | `RELEASE[SHIFT]` |
| `TYPE[```text```]` | Type text with concept barriers | `TYPE[```Hello```]` |
| `WAIT[ms]` | Wait specific time | `WAIT[1000]` |
| `WAIT[]` | Wait default/random time | `WAIT[]` |
| `SET_WAIT[ms]` | Set wait time or random range | `SET_WAIT[500]` |
| `FORMAT[key]` | Dynamic content within barriers | `FORMAT[RANDOM[A,B]]` |
| `SET_WAIT[RANDOM[min,max]]` | Set random wait range | `SET_WAIT[RANDOM[100,1000]]` |
| `FUNCTION[n]` | Press function key Fn | `FUNCTION[1]` to `FUNCTION[12]` |
| `PRESS_LEFT[key]` | Press left-side modifier | `PRESS_LEFT[SHIFT]` |
| `PRESS_RIGHT[key]` | Press right-side modifier | `PRESS_RIGHT[CTRL]` |

### Valid Keys

- **Letters**: A-Z
- **Numbers**: 0-9  
- **Symbols**: `!@#$%^&*()_+-={}[]|\\:;\"'<>?,.~` 
- **Special**: ENTER, SPACE, TAB, BACKSPACE, DELETE, ESC, INSERT, HOME, END, PAGE_UP, PAGE_DOWN
- **Arrows**: UP, DOWN, LEFT, RIGHT
- **Modifiers**: SHIFT, CTRL, ALT, WIN, CMD, META
- **Function**: 1-12 (for FUNCTION[n])

## 💡 Comprehensive Examples

### Basic Operations
```taplang
# Simple typing
TYPE[Hello World]

# Individual key presses
CLICK[H] CLICK[E] CLICK[L] CLICK[L] CLICK[O]

# Special keys
CLICK[ENTER] CLICK[TAB] CLICK[BACKSPACE]
```

### Keyboard Shortcuts
```taplang
# Copy (Ctrl+C)
PRESS[CTRL] CLICK[C] RELEASE[CTRL]

# Paste (Ctrl+V)
PRESS[CTRL] CLICK[V] RELEASE[CTRL]

# Select All (Ctrl+A)
PRESS[CTRL] CLICK[A] RELEASE[CTRL]

# Left Shift + A (for capital A)
PRESS_LEFT[SHIFT] CLICK[A] RELEASE[SHIFT]
```

### Timing Control
```taplang
# Fixed timing
TYPE[Step 1] WAIT[1000] TYPE[Step 2]

# Set default wait time
SET_WAIT[300]
TYPE[Fast] WAIT[] TYPE[Typing] WAIT[] TYPE[Demo]

# Random timing (human-like)
SET_WAIT[RANDOM[100,500]]
TYPE[Random] WAIT[] TYPE[Delays] WAIT[] TYPE[Between] WAIT[] TYPE[Words]
```

### Function Keys & Navigation
```taplang
# Function keys
FUNCTION[1]  # F1
FUNCTION[12] # F12

# Navigation
CLICK[HOME] CLICK[END]
CLICK[UP] CLICK[DOWN] CLICK[LEFT] CLICK[RIGHT]
CLICK[PAGE_UP] CLICK[PAGE_DOWN]
```

### Complex Sequences
```taplang
# Login sequence with realistic timing
SET_WAIT[RANDOM[200,400]]
TYPE[username@example.com]
WAIT[]
CLICK[TAB]
WAIT[]
TYPE[mypassword123]
WAIT[]
CLICK[ENTER]
```

## ⚠️ Error Detection

The interpreter provides comprehensive error detection:

### Common Errors
```python
# Unfinished press operations
result = interpret_taplang("PRESS[CTRL] CLICK[C]")  # Missing RELEASE[CTRL]
print(result['error'])  # "Unfinished PRESS operations: CTRL"

# Invalid keys
result = interpret_taplang("CLICK[INVALID_KEY]")
print(result['error'])  # "Invalid key: INVALID_KEY"

# Syntax errors
result = interpret_taplang("INVALID_CMD[A]")
print(result['error'])  # "Unknown instruction: INVALID_CMD"

# Double press operations
result = interpret_taplang("PRESS[SHIFT] PRESS[SHIFT]")
print(result['error'])  # "Key SHIFT is already held"
```

### Error Categories
- **Syntax Errors**: Invalid instruction format or unknown commands
- **Key Validation**: Invalid key names or missing parameters
- **State Errors**: Unmatched press/release operations, double press operations
- **Parameter Errors**: Invalid ranges, negative wait times

## 🔧 Advanced Features

### State Management
```python
from TapLang import reset_wait_state

# Reset timing state between executions
reset_wait_state()
result = interpret_taplang("WAIT[]")
```

### Custom Validation
```python
from TapLang import parse_taplang, validate_instruction

# Parse without execution
instructions = parse_taplang("TYPE[Hello] CLICK[ENTER]")
for instruction in instructions:
    validate_instruction(instruction)
    print(f"Valid: {instruction}")
```

## Package Benefits

1. **AI-Ready**: Perfect for AI agent keyboard input processing
2. **Modular**: Each component has specific responsibility  
3. **Importable**: Easy integration into Python projects
4. **Cross-Platform**: Consistent across different systems

## Future Distribution
- **🐍 PyPI Package** - Coming soon for `pip install`
- **⚡ C/C++ Implementation** - High-performance native library
- **Volunteers Welcome** - Help bring TapLang to more platforms!