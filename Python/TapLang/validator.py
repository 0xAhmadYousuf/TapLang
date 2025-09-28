from .data import get_valid_keys, get_spec

def validate_instruction(parsed):
    """Validate a parsed instruction"""
    cmd = parsed['command']
    param = parsed['parameter']
    spec = get_spec()
    
    if cmd in ['CLICK', 'PRESS', 'RELEASE', 'PRESS_LEFT', 'PRESS_RIGHT']:
        if not param:
            raise ValueError(f"{cmd} requires a key parameter")
        if param not in get_valid_keys():
            raise ValueError(f"Invalid key: {param}")
    
    elif cmd == 'FUNCTION':
        if param not in spec['keys']['function_keys']:
            raise ValueError(f"Invalid function key: F{param}. Must be 1-12")
    
    elif cmd == 'TYPE':
        if not param:
            raise ValueError("TYPE requires text parameter")
        
        # Require concept barrier format
        if 'barrier_info' not in parsed:
            raise ValueError("TYPE requires concept barrier format: TYPE[`text`] (use backticks)")
        
        barrier_info = parsed['barrier_info']
        format_keys = parsed.get('format_keys', [])
        
        # Validate barrier format was parsed correctly
        if not barrier_info:
            raise ValueError("TYPE with concept barriers requires valid ```text``` format")
        
        # Validate FORMAT keys
        for format_key in format_keys:
            format_content = format_key['content']
            
            # Validate RANDOM within FORMAT
            if format_content.upper().startswith('RANDOM[') and format_content.endswith(']'):
                options_part = format_content[7:-1]
                if not options_part:
                    raise ValueError("FORMAT[RANDOM[]] requires at least one option")
                options = [opt.strip() for opt in options_part.split(',')]
                if len(options) < 1:
                    raise ValueError("FORMAT[RANDOM[]] requires at least one option")
    
    elif cmd == 'WAIT':
        if param:  # WAIT[ms] - specific time
            try:
                ms = int(param)
                if ms < 0:
                    raise ValueError("WAIT time must be positive")
            except ValueError:
                raise ValueError(f"WAIT requires positive integer: {param}")
        # WAIT[] - use default time (no validation needed)
    
    elif cmd == 'SET_WAIT':
        if not param:
            raise ValueError("SET_WAIT requires a parameter")
        
        # Check for RANDOM[min,max] format
        if param.upper().startswith('RANDOM[') and param.endswith(']'):
            range_part = param[7:-1]  # Extract "min,max"
            try:
                parts = range_part.split(',')
                if len(parts) != 2:
                    raise ValueError("RANDOM requires exactly 2 numbers: min,max")
                min_val = int(parts[0].strip())
                max_val = int(parts[1].strip())
                if min_val < 0 or max_val < 0:
                    raise ValueError("RANDOM values must be positive")
                if min_val >= max_val:
                    raise ValueError("RANDOM min must be less than max")
            except (ValueError, IndexError):
                raise ValueError(f"Invalid RANDOM format: {param}")
        else:
            # Fixed wait time
            try:
                ms = int(param)
                if ms < 0:
                    raise ValueError("SET_WAIT time must be positive")
            except ValueError:
                raise ValueError(f"SET_WAIT requires positive integer or RANDOM[min,max]: {param}")
    
    elif cmd in ['ESCAPE_TYPE_START', 'ESCAPE_TYPE_END']:
        pass  # No validation needed for escape sequences
    
    return True

# Re-export for compatibility
def load_spec():
    """Load specification (compatibility function)"""
    return get_spec()