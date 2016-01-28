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
A fully functioning [Apache Tika](https://tika.apache.org/) server is required for this to work. The server configuration can be set in config.py (see config.py sample for an example).

You can use a pre-configured Apache Tika server Docker image: [https://hub.docker.com/r/logicalspark/docker-tikaserver/](https://hub.docker.com/r/logicalspark/docker-tikaserver/).
