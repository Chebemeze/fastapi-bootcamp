import asyncio, time

async def check_sensor_status(sensor_name, delay):
    """A coroutine simulating an IoT hardware status check."""
    print(f"Querying {sensor_name}...")
    await asyncio.sleep(delay) # Pause here, letting other sensors be queried
    print(f"{sensor_name} Query complete")
    return f"{sensor_name}"

async def main():
    start_time = time.time() #start time

    # creating the multiple corountines
    results = await asyncio.gather(
        check_sensor_status("Boiler_temp", 2),
        check_sensor_status("Water_pressure", 1),
        check_sensor_status("Cup_dispenser", 1.5)
    )

    print("Audit Results:", results)
    print(f"Total time elapsed: {time.time()- start_time:.2f} seconds.")

# Execute the main entry-point coroutine
asyncio.run(main())