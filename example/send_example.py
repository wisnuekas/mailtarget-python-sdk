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