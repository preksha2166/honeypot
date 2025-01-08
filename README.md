# Honeypot-Implementation

In this project, we implemented a Honey-Pot-like server which acts as a proxy server for any main server. Honey-Pot systems are used to track the behavior of attacks targeting main servers. By studying these attack patterns, system designers can develop updates to address system vulnerabilities. As the title states, this is a honeypot-like structure and not an exact honeypot. 

Our system not only records the IPs and locations of potential attackers but also captures screenshots of the user’s system. These images provide valuable insights into unusual activities that may occur. This additional layer of monitoring complements traditional IP tracking by offering a clearer view of malicious activity.

## Flask Integration
We utilized Flask, a lightweight web framework, to manage the HTTP routes and serve as the backbone of our web interface. Flask was used to handle login requests, simulate the user interactions with the honeypot, and manage the backend logic for IP tracking, keylogging, and screenshot capturing.

### Key Features Added Using Flask:
- **Login Page Management:** Flask routes are set up to handle user login attempts.
- **Session Tracking:** Flask manages user sessions to track login attempts and trigger the honeypot mechanism after three failed attempts.
- **Data Handling:** Flask processes the captured data (IP addresses, keylogs, screenshots) and stores it in a structured format (e.g., JSON).
- **API Support:** Flask exposes endpoints to retrieve data for further analysis.

## Working

### **hash.py**

![](/images/1.jpg)
![](/images/2.jpg)

### **Input Given in Python Script**
![](/images/3.jpg)

### **Data Stored in JSON File**
![](/images/13.jpg)

This data stored in the JSON file contains the username and password of a specified user. These credentials are used for logging into the web server via the Flask-based application.

### **Login Page**
Now we enter the credentials from the JSON data to access the login page:

![](/images/4.png)

### **Case i: Correct Username and Password**

![](/images/5.png)

### **Case ii: Incorrect Username or Password**

![](/images/6.png)

Users are given three attempts to log in. If incorrect credentials are entered three times, the honeypot system activates, recording the IP address and other details of the user:

![](/images/7.png)

### **The Keylogger:**

![](/images/8.jpg)
![](/images/9.jpg)

Keylogger captures and stores logs, along with screenshots:

![](/images/10.jpg)

### **Image Capture:**

![](/images/11.jpg)

