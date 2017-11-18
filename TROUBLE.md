1. Main problem was running tests in travis to soon.
On boot the container opened the port, but the service inside the container did not up yet,
which made the connection to fail. After adding some sleep time to testing script the problem solved.

