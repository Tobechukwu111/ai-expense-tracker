import time
from fastapi import Request

async def timing_middleware(request: Request, call_next):
    # 1. start stopwatch
    start = time.perf_counter()
    
    # 2. let the request go through normally
    response = await call_next(request)
    
    # 3. stop stopwatch and calculate time
    process_time = time.perf_counter() - start
    
    # 4. stamp the time on the response
    response.headers["X-Process-Time"] = str(process_time)
    
    return response