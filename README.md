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

## System requirements
To get the docx python package to work you need to install some xml-related libs in linux.

This can be done by running

```plaintext
sudo apt-get install libxml2-dev libxslt1-dev
```
