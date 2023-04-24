from datetime import datetime, timedelta

def berkley_algorithm(server_time, client1_time, client2_time):
    print(f"Server time: {server_time}")
    print(f"Client 1 time: {client1_time}")
    print(f"Client 2 time: {client2_time}")

    #date format
    fmt = "%M:%S"

    #converting date string into 'date' format
    server_dt = datetime.strptime(server_time, fmt)
    client1_dt = datetime.strptime(client1_time, fmt)
    client2_dt = datetime.strptime(client2_time, fmt)

    #finding the difference between client clocks wrt server clocks
    st1 = client1_dt - server_dt
    st2 = client2_dt - server_dt
    print(f"Time difference of Client 1: {st1.total_seconds()}")
    print(f"Time difference of Client 2: {st2.total_seconds()}")

    #finding fault tolerance average and adjusting all the clocks
    aveg = (st1 + st2)/2
    adj_server = server_dt + aveg
    adj_client1 = client1_dt - st1 + aveg
    adj_client2 = client2_dt - st2 + aveg

    print(f"Adjusted Server time: {adj_server.strftime(fmt)}")
    print(f"Adjusted Client 1 time: {adj_client1.strftime(fmt)}")
    print(f"Adjusted Client 2 time: {adj_client2.strftime(fmt)}")


berkley_algorithm("03:30", "02:50", "02:30")