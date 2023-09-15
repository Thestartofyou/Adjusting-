import random
import time

# Function to simulate mooring status
def check_mooring_status():
    # Simulate depth and temperature readings
    depth = random.uniform(5.0, 20.0)  # Depth in meters (randomized for simulation)
    temperature = random.uniform(5.0, 30.0)  # Temperature in Celsius (randomized for simulation)

    return depth, temperature

# Function to log mooring status
def log_mooring_status(depth, temperature):
    # Replace this with your actual logging mechanism (e.g., write to a file or send to a remote server)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - Depth: {depth} meters, Temperature: {temperature}°C"
    print(log_message)  # For demonstration, print the log message to the console

# Main function for continuous monitoring
def main():
    while True:
        depth, temperature = check_mooring_status()
        log_mooring_status(depth, temperature)
        time.sleep(60)  # Wait for 60 seconds before checking again (adjust as needed)

if __name__ == "__main__":
    main()

