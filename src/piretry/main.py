import asyncio
import random
from piretry import retry_decorator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Counter to keep track of attempts
attempt_counter = 0

# Define an asynchronous function with retry behavior
@retry_decorator(
    retry_count=3,                   # Maximum number of retry attempts
    error_list=[ValueError],         # List of exceptions to catch
    delay=2.0,                       # Initial delay between retries (seconds)
    backoff_factor=1.0,              # No exponential backoff
    on_retry=lambda e, attempt: print(f"Retry {attempt} due to {e}")  # Callback before each retry
)
async def process_data():
    global attempt_counter
    attempt_counter += 1
    print(f"Attempt {attempt_counter}: Processing data...")
    # Simulate a function that may raise a ValueError
    if attempt_counter < 3:  # Succeed on the third attempt
        raise ValueError("Processing error occurred")
    return "Data processed successfully"

# Run the asynchronous function
async def main():
    try:
        result = await process_data()
        print(result)
    except ValueError as e:
        print(f"Operation failed after retries: {e}")

# Execute the main function
asyncio.run(main())
