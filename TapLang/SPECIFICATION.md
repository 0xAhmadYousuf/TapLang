# TapLang Specification - The Backbone

This document explains the core specification that serves as the backbone of the TapLang keyboard action language.

## Purpose

The `TapLang.json` file serves as the **reference specification** for the TapLang language. It defines:

- **Language metadata** (version, description, case sensitivity)
- **Core instructions** and their meanings
- **Valid key definitions** organized by category
- **Syntax rules** and validation requirements
- **Usage examples** for each instruction type

## Structure Overview

### Language Definition
```json
{
  "language": {
    "name": "TapLang",
    "version": "1.0.0", 
    "description": "Simple keyboard action language",
    "case_sensitive": false
  }
}
```

### Instructions Catalog
Defines all valid TapLang instructions:
- **CLICK[key]** - Press and release
- **PRESS[key]** / **RELEASE[key]** - Press operations
- **TYPE[text]** - Text input
- **WAIT[ms]** / **SET_WAIT[config]** - Timing control
- **FUNCTION[1-12]** - Function keys
- **PRESS_LEFT[key]** / **PRESS_RIGHT[key]** - Side-specific modifiers
- **ESCAPE_TYPE_START/END** - Escape sequences

### Key Categories
Organizes all valid keys into logical groups:
- **letters**: A-Z alphabet
- **numbers**: 0-9 digits  
- **symbols**: Punctuation and special characters
- **special**: ENTER, SPACE, TAB, etc.
- **arrows**: UP, DOWN, LEFT, RIGHT
- **modifiers**: SHIFT, CTRL, ALT, WIN, CMD, META
- **function_keys**: 1-12 for FUNCTION[n] instruction

### Rules and Validation
Defines behavioral rules:
- Press/Release matching requirements
- Case insensitivity handling
- Escape sequence usage guidelines

### Examples Repository
Provides reference examples for each instruction type and common usage patterns.

## Implementation Notes

While this JSON serves as the **authoritative specification**, actual implementations may:

1. **Convert to native data structures** (e.g., Python dictionaries)
2. **Optimize for performance** (e.g., pre-compiled regex patterns)
3. **Extend with additional features** while maintaining backward compatibility
4. **Validate against this specification** as the source of truth

## Versioning

The specification follows semantic versioning:
- **Major**: Breaking changes to instruction syntax or behavior
- **Minor**: New instructions or features (backward compatible)  
- **Patch**: Bug fixes, documentation updates, example additions

## Usage as Backbone

This specification serves multiple purposes:

1. **Documentation**: Human-readable reference for the language
2. **Validation**: Programmatic checking of TapLang code
3. **Tooling**: IDE support, syntax highlighting, auto-completion
4. **Testing**: Reference for creating comprehensive test suites
5. **Portability**: Standard for implementing TapLang in other languages

The JSON format ensures the specification is both human-readable and machine-parseable, making it easy to use across different tools and implementations.