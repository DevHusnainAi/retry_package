import asyncio
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

# Define an asynchronous function with retry behavior
@retry(
    retry=retry_if_exception_type(ValueError),  # Retry only on ValueError
    stop=stop_after_attempt(4),                # Stop after 3 attempts
    wait=wait_fixed(2),                        # Wait 2 seconds between retries
    reraise=True                               # Reraise the last exception if all retries fail
)
async def process_data():
    print("Attempting to process data...")
    # Forcefully raise a ValueError to test retry behavior
    raise ValueError("Processing error occurred")

# Run the asynchronous function
async def main():
    try:
        result = await process_data()
        print(result)
    except ValueError as e:
        print(f"Operation failed after retries: {e}")

# Execute the main function
asyncio.run(main())