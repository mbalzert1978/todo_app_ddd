class SharedKernelError(Exception):
    """Base Todo Error class for other exceptions."""


class WrongType(SharedKernelError):
    """Raised when an object is of the wrong type."""
