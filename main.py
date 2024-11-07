from pymavlink import mavutil

try:
    # Start a connection to SITL over TCP
    the_connection = mavutil.mavlink_connection('tcp:127.0.0.1:14550')
    
    # Attempt to receive a heartbeat
    print("Waiting for heartbeat...")
    the_connection.wait_heartbeat()
    print("Heartbeat received from system (system %u component %u)" %
          (the_connection.target_system, the_connection.target_component))
    
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
    msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)
    


except ConnectionResetError as e:
    print("Connection was reset or closed by the peer:", e)
except Exception as e:
    print("An error occurred:", e)
