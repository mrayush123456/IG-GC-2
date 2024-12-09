from flask import Flask, request, render_template_string, redirect, url_for, flash
import time
import os
import requests

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key for production

# HTML Template for the Web Page
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Automation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #282c34;
            color: #ffffff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #333;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            max-width: 400px;
            width: 100%;
        }
        h1 {
            text-align: center;
            color: #61dafb;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin: 10px 0 5px;
            font-weight: bold;
            color: #61dafb;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        input:focus, select:focus, button:focus {
            outline: none;
            border-color: #61dafb;
            box-shadow: 0 0 5px rgba(97, 218, 251, 0.5);
        }
        button {
            background-color: #61dafb;
            color: #282c34;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #21a1f1;
        }
        .message {
            text-align: center;
            font-size: 14px;
            margin-top: 10px;
        }
        .success {
            color: #4caf50;
        }
        .error {
            color: #f44336;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Instagram Automation</h1>
        <form action="/" method="POST" enctype="multipart/form-data">
            <label for="access_token">Access Token:</label>
            <input type="text" id="access_token" name="access_token" placeholder="Enter extended access token" required>

            <label for="choice">Send To:</label>
            <select id="choice" name="choice" required>
                <option value="inbox">Inbox</option>
                <option value="group">Group</option>
            </select>

            <label for="target_username">Target Username (for Inbox):</label>
            <input type="text" id="target_username" name="target_username" placeholder="Enter target username">

            <label for="thread_id">Thread ID (for Group):</label>
            <input type="text" id="thread_id" name="thread_id" placeholder="Enter group thread ID">

            <label for="haters_name">Haters Name:</label>
            <input type="text" id="haters_name" name="haters_name" placeholder="Enter hater's name" required>

            <label for="message_file">Message File:</label>
            <input type="file" id="message_file" name="message_file" accept=".txt" required>

            <label for="delay">Delay (seconds):</label>
            <input type="number" id="delay" name="delay" placeholder="Enter delay in seconds" required>

            <button type="submit">Start Automation</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="message">
                    {% for category, message in messages %}
                        <p class="{{ category }}">{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
'''

# Endpoint to render the form and process submissions
@app.route("/", methods=["GET", "POST"])
def instagram_automation():
    if request.method == "POST":
        try:
            # Get form data
            access_token = request.form["access_token"]
            choice = request.form["choice"]
            target_username = request.form.get("target_username")
            thread_id = request.form.get("thread_id")
            haters_name = request.form["haters_name"]
            delay = int(request.form["delay"])
            message_file = request.files["message_file"]

            # Read messages from the uploaded file
            messages = message_file.read().decode("utf-8").splitlines()
            if not messages:
                flash("Message file is empty!", "error")
                return redirect(url_for("instagram_automation"))

            # Simulate sending messages using the API
            print(f"[INFO] Using access token: {access_token}")
            for message in messages:
                if choice == "inbox":
                    if not target_username:
                        flash("Target username is required for inbox messaging.", "error")
                        return redirect(url_for("instagram_automation"))
                    print(f"[INFO] Sending to {target_username}'s inbox: {message}")
                elif choice == "group":
                    if not thread_id:
                        flash("Thread ID is required for group messaging.", "error")
                        return redirect(url_for("instagram_automation"))
                    print(f"[INFO] Sending to group thread {thread_id}: {message}")
                else:
                    flash("Invalid choice for messaging.", "error")
                    return redirect(url_for("instagram_automation"))

                # Simulated delay
                print(f"Message sent successfully: {message}")
                time.sleep(delay)

            flash("All messages sent successfully!", "success")
            return redirect(url_for("instagram_automation"))

        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for("instagram_automation"))

    return render_template_string(HTML_TEMPLATE)

from flask import Flask, request, render_template_string, redirect, url_for, flash
import time
import os
import requests

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key for production

# HTML Template for the Web Page
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Automation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #282c34;
            color: #ffffff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #333;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            max-width: 400px;
            width: 100%;
        }
        h1 {
            text-align: center;
            color: #61dafb;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin: 10px 0 5px;
            font-weight: bold;
            color: #61dafb;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        input:focus, select:focus, button:focus {
            outline: none;
            border-color: #61dafb;
            box-shadow: 0 0 5px rgba(97, 218, 251, 0.5);
        }
        button {
            background-color: #61dafb;
            color: #282c34;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #21a1f1;
        }
        .message {
            text-align: center;
            font-size: 14px;
            margin-top: 10px;
        }
        .success {
            color: #4caf50;
        }
        .error {
            color: #f44336;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Instagram Automation</h1>
        <form action="/" method="POST" enctype="multipart/form-data">
            <label for="access_token">Access Token:</label>
            <input type="text" id="access_token" name="access_token" placeholder="Enter extended access token" required>

            <label for="choice">Send To:</label>
            <select id="choice" name="choice" required>
                <option value="inbox">Inbox</option>
                <option value="group">Group</option>
            </select>

            <label for="target_username">Target Username (for Inbox):</label>
            <input type="text" id="target_username" name="target_username" placeholder="Enter target username">

            <label for="thread_id">Thread ID (for Group):</label>
            <input type="text" id="thread_id" name="thread_id" placeholder="Enter group thread ID">

            <label for="haters_name">Haters Name:</label>
            <input type="text" id="haters_name" name="haters_name" placeholder="Enter hater's name" required>

            <label for="message_file">Message File:</label>
            <input type="file" id="message_file" name="message_file" accept=".txt" required>

            <label for="delay">Delay (seconds):</label>
            <input type="number" id="delay" name="delay" placeholder="Enter delay in seconds" required>

            <button type="submit">Start Automation</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="message">
                    {% for category, message in messages %}
                        <p class="{{ category }}">{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
'''

# Endpoint to render the form and process submissions
@app.route("/", methods=["GET", "POST"])
def instagram_automation():
    if request.method == "POST":
        try:
            # Get form data
            access_token = request.form["access_token"]
            choice = request.form["choice"]
            target_username = request.form.get("target_username")
            thread_id = request.form.get("thread_id")
            haters_name = request.form["haters_name"]
            delay = int(request.form["delay"])
            message_file = request.files["message_file"]

            # Read messages from the uploaded file
            messages = message_file.read().decode("utf-8").splitlines()
            if not messages:
                flash("Message file is empty!", "error")
                return redirect(url_for("instagram_automation"))

            # Simulate sending messages using the API
            print(f"[INFO] Using access token: {access_token}")
            for message in messages:
                if choice == "inbox":
                    if not target_username:
                        flash("Target username is required for inbox messaging.", "error")
                        return redirect(url_for("instagram_automation"))
                    print(f"[INFO] Sending to {target_username}'s inbox: {message}")
                elif choice == "group":
                    if not thread_id:
                        flash("Thread ID is required for group messaging.", "error")
                        return redirect(url_for("instagram_automation"))
                    print(f"[INFO] Sending to group thread {thread_id}: {message}")
                else:
                    flash("Invalid choice for messaging.", "error")
                    return redirect(url_for("instagram_automation"))

                # Simulated delay
                print(f"Message sent successfully: {message}")
                time.sleep(delay)

            flash("All messages sent successfully!", "success")
            return redirect(url_for("instagram_automation"))

        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for("instagram_automation"))

    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
