# ITRANS Transliteration Parser Design

## Overview
A Python library and CLI tool to convert ITRANS ASCII text into Unicode for major Brahmic scripts.

---

## Supported Scripts
- Devanagari
- Bengali
- Tamil
- Telugu
- Kannada
- Malayalam
- Gujarati
- Gurmukhi
- Oriya
- Sinhala

---

## Architecture

```mermaid
flowchart TD
    A[User Input (CLI or API)] --> B[Tokenizer]
    B --> C[ITRANS Tokens]
    C --> D[Script Mapper]
    D --> E[Unicode Code Points]
    E --> F[Output Unicode Text]
    G[Script Selection] --> D
    G --> CLI
    CLI[CLI Options] --> A
```

- **Tokenizer:** Segments input into valid ITRANS tokens (e.g., 'aa', 'kSh', 'j~n')
- **Script Mapper:** Maps tokens to Unicode code points for the chosen script
- **Output Generator:** Combines code points into a Unicode string
- **CLI/API:** Interface for user input, script selection, and output

---

## Implementation Phases

### Phase 1: Core Engine
- Develop tokenizer for ITRANS sequences
- Create mapping tables for Devanagari
- Implement transliteration logic for Devanagari

### Phase 2: Multi-script Support
- Extend mapping tables to other scripts
- Modularize script selection

### Phase 3: CLI Tool
- Build CLI with options:
  - Input file or string
  - Output file or stdout
  - Target script selection
- Error handling and help documentation

### Phase 4: Packaging
- Package as a Python library
- Provide API functions
- Include tests and examples

---

## Mapping Tables

Centralized dictionary of ITRANS tokens to Unicode code points per script.

Example:
```python
mappings = {
    'Devanagari': {'aa': 'आ', 'ii': 'ई', 'kSh': 'क्ष', ...},
    'Bengali': {'aa': 'আ', 'ii': 'ঈ', 'kSh': 'ক্ষ', ...},
    ...
}
```

---

## Additional Considerations
- Handle ambiguities and context-sensitive rules
- Support nasalization, conjuncts, diacritics
- Unicode normalization
- Extensibility for future scripts or schemes

---

## Summary
A modular, extensible Python-based transliteration parser for ITRANS, supporting multiple Indic scripts with both library and CLI interfaces.