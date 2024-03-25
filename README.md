# Mailtarget Python SDK

The Mailtarget Python SDK enable NodeJs developer to work with Mailtarget API efficiently.

## Getting Started

### Requirement
Python 3

### Installation
To install the SDK to your project, you could get the package from PyPi via following command.
```sh
pip install mailtarget_sdk
```
or
You can clone this repository and install it manual to your env
```sh
git clone https://
cd mailtarget-pyhton-sdk
pip install .
```

### Authentication
You have to create a [mailtarget](https://app.mailtarget.co/) account to get an API Key.
To manage your API Key navigate to the page by clicking ***Configuration*** on the navbar in the mailtarget dashboard
and then select API Key.

## Setup Client

### Basic Usage
```python
from mailtarget_sdk import Layang, Message, Address

layang = Layang("your_api_key")
content = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Layang</title>
    </head>
    <body style="font-family: "Roboto", "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif">
        <h1>Hello World!!!</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <br/><br/>
        <p style="color: #8A8A8A">powered by <a target="_blank" href="https://mailtarget.co" style="color: #8A8A8A">mailtarget</a></p>
    </body>
    </html>
"""

newMessage = Message(
    subject= "Hello from Python SDK",
    to=[Address(email = "recipient@gmail.com", name="Wisnu")],
    from_address=Address(email = "no-reply@test1.sender.mtarget.dev", name="Python"),
    body_html=content
)

response = layang.send(message=newMessage)

print(f'response {response}')
```