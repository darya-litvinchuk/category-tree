""" This module contains exceptions, that can rise within this application."""


class ServiceException(Exception):
    """Base exception for other class of exceptions."""

    code = "base_service_error"

    def __init__(self, message: str):
        self.msg = message
        super().__init__(self.msg)


class DuplicationException(ServiceException):
    """Raises, when user tries to add duplicates to the database."""

    code = "duplication_error"

    def __init__(self):
        self.msg = "Category already exists"
        super().__init__(self.msg)


class LogicalException(ServiceException):
    """Raises, when user tries to perform an illogical operation."""

    code = "logical_error"

    def __init__(self, message: str):
        self.msg = message
        super().__init__(self.msg)


class NotFoundException(ServiceException):
    """Raises, when user trying to get an object that is not in the database."""

    code = "not_found_error"

    def __init__(self, category_id: int):
        self.msg = f"Category {category_id} does not exist"
        super().__init__(self.msg)
