import io
import traceback

import serial


def get_firmware_version(serial_port):
    serial_port.write(b'V\n')
    return serial_port.readline()


def enable_reporting(serial_port):
    serial_port.write(b'X01\n')

def create_serial_io_port(serial_device, data_rate):
    port = serial.serial_for_url(serial_device, baudrate=data_rate, timeout=1)
    return io.TextIOWrapper(io.BufferedRWPair(port, port),
                            line_buffering=False,
                            newline='\r\n')


def main(serial_device, data_rate):
    with create_serial_io_port(serial_device, data_rate) as serial_port:
        firmware_version = get_firmware_version(serial_port)
        print(f'Read CUL firmware version: {firmware_version}')

        for line in serial_port:
            try:
                print(f'Received line: {line}')
            except KeyboardInterrupt:
                print('Stopping due to user request...')
                break
            except:
                traceback.print_exc()


if __name__ == '__main__':
    main('/dev/ttyUSB0', 38400)
