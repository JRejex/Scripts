## File Parsers
----------------------------
**File/Directory Parsers to identify key information for forensics analysts**

```
Tools:
- FileForensicsProcessor.py
- Digital_img_Finder.py
```

# FileForensicsProcessor.py
Takes user input to identify the Directory path to be checked and the hashing algorithm to utilize (default SHA384).\
Python script will process a directory and identify files forensic artifacts.
- FilePath 
- FileSize 
- Timestamps
- Owner
- FileMode
- Hex Header
- FileHash



# Digital_img_Finder.py
Process a directory and identify digital image files.\
Utilizes Pillow (PIL Fork) python library. \
Returns the following output upon identification: 
- Extension
- Format
- Width
- Height
- Mode
