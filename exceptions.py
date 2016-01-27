"""
Exceptions used with python-docx.
The base exception class is PythonDocxError.

They forgot to include this in their lib
"""


class PythonDocxError(Exception):
    """
    Generic error class.
    """


class PendingDeprecationWarning(PythonDocxError):
    """
    Raised when a tool pending deprecation is used.
    """


class InvalidSpanError(PythonDocxError):
    """
    Raised when an invalid merge region is specified in a request to merge
    table cells.
    """


class InvalidXmlError(PythonDocxError):
    """
    Raised when invalid XML is encountered, such as on attempt to access a
    missing required child element
    """
