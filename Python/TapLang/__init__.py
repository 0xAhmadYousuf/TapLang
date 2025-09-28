"""
TapLang - Keyboard Action Language for AI Systems
================================================

🤖 Designed primarily for AI agents, web terminals, and automation systems.

A lightweight language for representing keyboard actions in a standardized form.
Perfect for AI agents that need to understand and execute keyboard sequences.

Example usage:
    from TapLang import interpret_taplang
    
    result = interpret_taplang("TYPE[Hello] CLICK[SPACE] TYPE[World]")
    if result['success']:
        for step in result['results']:
            print(step)
"""

from .interpreter import interpret_taplang, parse_taplang, execute_instruction, reset_wait_state
from .validator import validate_instruction, load_spec
from .parser import parse_instruction

__version__ = "1.0.0"
__author__ = "TapLang Project"

# Main exports
__all__ = [
    'interpret_taplang',
    'parse_taplang', 
    'parse_instruction',
    'validate_instruction',
    'execute_instruction',
    'reset_wait_state',
    'load_spec'
]