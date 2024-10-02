import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Add middleware / listeners here
@app.message("안녕")
def say_hello(message, say):
    user = message['user']
    
    say(f"Hi there, <@{user}>!")

@app.command("/add")
def addString(ack, body, client):
    ack()
    client.views_open(
        
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "My App"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Welcome to a modal with _blocks_"},
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Click me!"},
                        "action_id": "button_abc"
                    }
                },
                {
                    "type": "input",
                    "block_id": "input_c",
                    "label": {"type": "plain_text", "text": "What are your hopes and dreams?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                }
            ]
        }
    )

if __name__ == "__main__":
  
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()



# {
#     'token': 'oqGdO5M317P0Lf0tQHcx0Rgw',
#     'team_id': 'T04TJPBA943',
#     'team_domain': 'myidolhq',
#     'channel_id': 'C05LGNV396E',
#     'channel_name': '99-진행-상황',
#     'user_id': 'U04TJT5C1B4',
#     'user_name': 'rlaehrbs9569',
#     'command': '/add',
#     'text': '',
#     'api_app_id': 'A07NXBWSTRR',
#     'is_enterprise_install': 'false',
#     'response_url': 'https://hooks.slack.com/commands/T04TJPBA943/7781414701926/V5TzH0c1H3jbuJk0qiftoFmU',
#     'trigger_id': '7787945573699.4936793349139.bf21c8d720ef03e124687014e3362f47'
#     }
