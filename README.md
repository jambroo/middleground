# middleground
middleground is a Python module for converting various document types to a normalised plaintext. Example input will be JSON, RTF, PDF, XML, XLS, DOC, PPT, PSD and XCF. The output will be plaintext without structure.

Example of input for JSON mode is
```json
{
    "example": {
        "title": "example glossary"
    }
}
```

Output:

```plaintext
example
    title    example glossary
```
