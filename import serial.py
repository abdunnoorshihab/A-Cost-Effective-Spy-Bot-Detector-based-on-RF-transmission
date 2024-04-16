import serial
import csv
import time

# Set up serial connection
ser = serial.Serial('COMX', 9600)  # Replace 'COMX' with your Arduino's serial port

# Open CSV file for writing
csv_file = open('data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp', 'Data'])  # Write header to CSV file

try:
    while True:
        # Read data from Arduino
        data = ser.readline().decode().strip()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')  # Get current timestamp
        
        # Write data to CSV file
        csv_writer.writerow([timestamp, data])
        csv_file.flush()  # Flush buffer to ensure data is written immediately
        
        # Print data to console
        print(f'{timestamp}: {data}')

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    # Close serial connection and CSV file
    ser.close()
    csv_file.close()
