import random
from .parser import parse_instruction, tokenize_code
from .validator import validate_instruction

# Global state for SET_WAIT
_default_wait_time = None
_random_wait_range = None

def execute_instruction(instruction):
    """Execute a single instruction (simulation)"""
    global _default_wait_time, _random_wait_range
    
    cmd = instruction['command']
    param = instruction['parameter']
    
    if cmd == 'CLICK':
        return f"Clicked key: {param}"
    elif cmd == 'PRESS':
        return f"Pressing key: {param}"
    elif cmd == 'RELEASE':
        return f"Released key: {param}"
    elif cmd == 'TYPE':
        if param.upper().startswith('RANDOM[') and param.endswith(']'):
            # Handle RANDOM[option1,option2,option3]
            options_part = param[7:-1]
            options = [opt.strip() for opt in options_part.split(',')]
            selected = random.choice(options)
            return f"Typed: '{selected}' (random from {len(options)} options)"
        else:
            return f"Typed: '{param}'"
    elif cmd == 'WAIT':
        if param:  # WAIT[specific_time]
            return f"Waited: {param}ms"
        else:  # WAIT[] - use default or random
            if _random_wait_range:
                wait_time = random.randint(_random_wait_range[0], _random_wait_range[1])
                return f"Waited: {wait_time}ms (random)"
            elif _default_wait_time:
                return f"Waited: {_default_wait_time}ms (default)"
            else:
                return "Waited: 0ms (no default set)"
    elif cmd == 'SET_WAIT':
        if param.upper().startswith('RANDOM['):
            # Parse RANDOM[min,max]
            range_part = param[7:-1]
            parts = range_part.split(',')
            min_val = int(parts[0].strip())
            max_val = int(parts[1].strip())
            _random_wait_range = (min_val, max_val)
            _default_wait_time = None
            return f"Set random wait range: {min_val}-{max_val}ms"
        else:
            # Fixed wait time
            _default_wait_time = int(param)
            _random_wait_range = None
            return f"Set default wait time: {param}ms"
    elif cmd == 'FUNCTION':
        return f"Pressed F{param}"
    elif cmd in ['PRESS_LEFT', 'PRESS_RIGHT']:
        side = cmd.split('_')[1].lower()
        return f"Pressed {side} {param}"
    
    return f"Executed: {cmd}[{param}]"

def reset_wait_state():
    """Reset wait state (useful for testing)"""
    global _default_wait_time, _random_wait_range
    _default_wait_time = None
    _random_wait_range = None

def parse_taplang(code):
    """Parse TapLang code and return list of instructions"""
    instructions = []
    held_keys = set()  # Track held keys
    in_escape = False
    escape_buffer = ""
    
    tokens = tokenize_code(code)
    
    for token in tokens:
        if not token:
            continue
            
        try:
            parsed = parse_instruction(token)
            if not parsed:
                continue
                
            validate_instruction(parsed)
            
            cmd = parsed['command']
            param = parsed['parameter']
            
            # Handle escape sequences
            if cmd == 'ESCAPE_TYPE_START':
                in_escape = True
                escape_buffer = param
                continue
            elif cmd == 'ESCAPE_TYPE_END':
                if not in_escape:
                    raise ValueError("ESCAPE_TYPE_END without ESCAPE_TYPE_START")
                instructions.append({
                    'command': 'TYPE',
                    'parameter': escape_buffer,
                    'original': f"ESCAPE_TYPE_START[{escape_buffer}] ESCAPE_TYPE_END[{param}]"
                })
                in_escape = False
                escape_buffer = ""
                continue
            
            if in_escape:
                raise ValueError("Instructions not allowed inside escape sequence")
            
            # Track held keys
            if cmd in ['PRESS', 'PRESS_LEFT', 'PRESS_RIGHT']:
                if param in held_keys:
                    raise ValueError(f"Key {param} is already pressed")
                held_keys.add(param)
            elif cmd == 'RELEASE':
                if param not in held_keys:
                    raise ValueError(f"Cannot release {param} - not currently pressed")
                held_keys.remove(param)
            
            instructions.append({
                'command': cmd,
                'parameter': param,
                'original': token
            })
            
        except ValueError as e:
            raise ValueError(f"Error in '{token}': {e}")
    
    # Check for unfinished presses
    if held_keys:
        raise ValueError(f"Unfinished PRESS operations: {', '.join(held_keys)}")
    
    if in_escape:
        raise ValueError("Unfinished escape sequence - missing ESCAPE_TYPE_END")
    
    return instructions

def interpret_taplang(code):
    """Main interpreter function"""
    try:
        instructions = parse_taplang(code)
        results = []
        
        for instruction in instructions:
            result = execute_instruction(instruction)
            results.append(result)
        
        return {
            'success': True,
            'instructions': len(instructions),
            'results': results
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'instructions': 0,
            'results': []
        }