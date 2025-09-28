import re
from .data import get_valid_instructions

def parse_concept_barrier(param):
    """Parse concept barrier syntax for TYPE instruction
    
    Handles:
    - `simple text` (single backticks for simple cases)
    - ```text with ` inside``` (triple backticks when text contains backticks)
    - `text with FORMAT[RANDOM[1,2]]`
    """
    if not param:
        raise ValueError("Empty TYPE parameter")
    
    # Check if it starts and ends with backticks
    if not param.startswith('`'):
        raise ValueError("TYPE parameter must be enclosed in concept barriers (`text` or ```text```)")
    
    # Find the opening barrier (minimum 1 backtick)
    opening_match = re.match(r'^(`+)', param)
    if not opening_match:
        raise ValueError("TYPE parameter must start with backticks (`text`)")
    
    opening_barrier = opening_match.group(1)
    barrier_length = len(opening_barrier)
    
    # Check if it ends with the same number of backticks
    if not param.endswith(opening_barrier):
        raise ValueError(f"TYPE parameter must end with the same barrier: {opening_barrier}")
    
    # Extract the content between barriers
    if len(param) < barrier_length * 2:
        raise ValueError("Invalid concept barrier format")
    
    content = param[barrier_length:-barrier_length]
    
    # Validate emergency case - if content has backticks, barrier must be longer
    if '`' in content and barrier_length == 1:
        raise ValueError("Text contains ` - use triple backticks like ```text with ` inside```")
    elif '```' in content and barrier_length == 3:
        raise ValueError("Text contains ``` - use longer barrier like ````text with ``` inside````")
    
    return {
        'content': content,
        'barrier_length': barrier_length,
        'has_format': 'FORMAT[' in content
    }

def parse_format_keys(text):
    """Parse FORMAT keys within concept barrier content
    
    Handles: FORMAT[RANDOM[1,2,3]] or FORMAT[KEY[value]]
    """
    format_keys = []
    i = 0
    while i < len(text):
        # Look for FORMAT[
        format_start = text.find('FORMAT[', i)
        if format_start == -1:
            break
        
        # Find matching bracket
        bracket_count = 0
        j = format_start + 7  # Start after 'FORMAT['
        start_pos = j
        
        while j < len(text):
            if text[j] == '[':
                bracket_count += 1
            elif text[j] == ']':
                if bracket_count == 0:
                    # Found the matching bracket
                    format_content = text[start_pos:j]
                    full_match = text[format_start:j+1]
                    
                    format_keys.append({
                        'full_match': full_match,
                        'content': format_content,
                        'start': format_start,
                        'end': j+1
                    })
                    i = j + 1
                    break
                else:
                    bracket_count -= 1
            j += 1
        else:
            # No matching bracket found
            i = format_start + 1
    
    return format_keys

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
    
    # Handle TYPE instruction with concept barriers
    if cmd == 'TYPE':
        # Parse and validate concept barrier
        barrier_info = parse_concept_barrier(param_part)
        
        # Parse FORMAT keys if present
        format_keys = []
        if barrier_info['has_format']:
            format_keys = parse_format_keys(barrier_info['content'])
        
        return {
            'command': cmd, 
            'parameter': param_part,
            'barrier_info': barrier_info,
            'format_keys': format_keys
        }
    
    # For escape sequences and SET_WAIT, preserve original case in parameter
    elif cmd in ['ESCAPE_TYPE_START', 'ESCAPE_TYPE_END', 'SET_WAIT']:
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