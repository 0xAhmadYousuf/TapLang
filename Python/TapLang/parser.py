import re
from .data import get_valid_instructions

def parse_instruction(instruction):
    """Parse a single instruction like CLICK[A] or TYPE[Hello]"""
    original_instruction = instruction.strip()
    instruction_upper = instruction.strip().upper()
    
    if not instruction:
        return None
        
    # Find the command and parameter with bracket matching
    if '[' not in instruction or not instruction.endswith(']'):
        raise ValueError(f"Invalid instruction format: {instruction}")
    
    bracket_pos = instruction.find('[')
    cmd = instruction[:bracket_pos].upper()
    param_part = instruction[bracket_pos+1:-1]  # Remove [ and ]
    
    if cmd not in get_valid_instructions():
        raise ValueError(f"Unknown instruction: {cmd}")
    
    # For escape sequences and SET_WAIT, preserve original case in parameter
    if cmd in ['ESCAPE_TYPE_START', 'ESCAPE_TYPE_END', 'TYPE', 'SET_WAIT']:
        param = param_part  # Keep original case and nested brackets
    else:
        param = param_part.upper()
    
    return {'command': cmd, 'parameter': param}

def tokenize_code(code):
    """Split TapLang code into tokens, handling nested brackets"""
    tokens = []
    current_token = ""
    bracket_count = 0
    in_escape = False
    
    i = 0
    while i < len(code):
        char = code[i]
        
        # Check for escape sequences
        if not in_escape and code[i:].upper().startswith('ESCAPE_TYPE_START['):
            in_escape = True
            # Find the complete escape sequence
            start = i
            bracket_count = 0
            j = i
            while j < len(code):
                if code[j] == '[':
                    bracket_count += 1
                elif code[j] == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        break
                j += 1
            
            # Add the ESCAPE_TYPE_START token
            tokens.append(code[start:j+1])
            i = j + 1
            
            # Skip spaces
            while i < len(code) and code[i] == ' ':
                i += 1
                
            # Find ESCAPE_TYPE_END
            if i < len(code) and code[i:].upper().startswith('ESCAPE_TYPE_END['):
                start = i
                bracket_count = 0
                j = i
                while j < len(code):
                    if code[j] == '[':
                        bracket_count += 1
                    elif code[j] == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            break
                    j += 1
                tokens.append(code[start:j+1])
                i = j + 1
                in_escape = False
            continue
        
        if char == '[':
            bracket_count += 1
            current_token += char
        elif char == ']':
            bracket_count -= 1
            current_token += char
        elif char == ' ' and bracket_count == 0:
            if current_token.strip():
                tokens.append(current_token.strip())
            current_token = ""
        else:
            current_token += char
        
        i += 1
    
    if current_token.strip():
        tokens.append(current_token.strip())
    
    return [token for token in tokens if token]