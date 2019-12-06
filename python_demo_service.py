# Python script for the Python Demo Service

if __name__ == '__main__':
    from systemd import daemon
    import time

    print('Starting up ...')
    time.sleep(10)
    print('Startup complete')
    # Tell systemd that our service is ready
    daemon.notify(daemon.Notification.READY)

    while True:
        print('Hello from the Python Demo Service')
        time.sleep(5)

