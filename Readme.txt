This is a "Simple Chat" application built in Python.

--You can use any python web framework (Flask/Django etc.) to run this script online.
--You can run this script offline using the text editor of your choice (PyCharm/Jupyter Notebook, etc.).

A. To Run This app:
    1. Make sure you run Server.Py and Client.Py on separate windows.
    2. Run Server.py First, it will give you the Hostname.
    3. Next, Run Client.py and paste the Server Hostname.
    4. Start Chatting.


B. To Run This Script in C-panel:

    1. Go to the directory of your choice.
    2. Upload server.py and client.py
    3. Change permission of both files to 755.
    4. Create an .htaccess file with following code:

                Options +ExecCGI
                AddHandler cgi-script .py

    5. Loop to: A.


    Sajjal Neupane
    linkedin.in/mrsajjal