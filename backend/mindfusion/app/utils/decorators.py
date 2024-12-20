from functools import wraps
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.utils import logger

def handle_repository_errors(repo_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"Executing {func.__name__} in {repo_name} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"Executed {func.__name__} in {repo_name} successfully")
                return result
            except SQLAlchemyError as e:
                logger.error(f"Database error in {repo_name}: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Database error in {repo_name}: {str(e)}")
            except Exception as e:
                logger.error(f"Unexpected error in {repo_name}: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Unexpected error in {repo_name}: {str(e)}")
        return wrapper
    return decorator

def handle_service_errors(service_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"Executing {func.__name__} in {service_name} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"Executed {func.__name__} in {service_name} successfully")
                return result
            except ValueError as e:
                logger.error(f"Value error in {service_name}: {str(e)}")
                raise HTTPException(status_code=400, detail=str(e))
            except Exception as e:
                logger.error(f"Unexpected error in {service_name}: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Unexpected error in {service_name}: {str(e)}")
        return wrapper
    return decorator