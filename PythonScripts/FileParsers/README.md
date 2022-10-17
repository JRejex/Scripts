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

Example Output:
![FileForensicsProcessor_Screenshot](https://user-images.githubusercontent.com/42547204/196284418-dcb096b3-c542-4f63-856a-3a24b56e4c64.JPG)


# Digital_img_Finder.py
Process a directory and identify digital image files.\
Utilizes Pillow (PIL Fork) python library. \
Returns the following output upon identification: 
- Extension
- Format
- Width
- Height
- Mode

Example Output:
![Digital_img_Finder](https://user-images.githubusercontent.com/42547204/196284049-5532d10e-7297-4033-84cd-912f20b975a1.JPG)
