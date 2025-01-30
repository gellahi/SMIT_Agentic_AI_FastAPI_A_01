import time
from fastapi import Request

async def logging_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    print(f"Path: {request.url.path}")
    print(f"Method: {request.method}")
    print(f"Process Time: {process_time:.4f} seconds")
    
    return response