from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "ChatGPT", "image_generation", "cloud_vision"],
        transitions=[
            {
                "trigger": "advance",
                "source": ["user", "ChatGPT", "image_generation", "cloud_vision"],
                "dest": "ChatGPT",
                "conditions": "is_going_to_ChatGPT",
            },
            {
                "trigger": "advance",
                "source": ["user", "ChatGPT", "image_generation", "cloud_vision"],
                "dest": "image_generation",
                "conditions": "is_going_to_image_generation",
            },
            {
                "trigger": "advance",
                "source": ["user", "ChatGPT", "image_generation", "cloud_vision"],
                "dest": "cloud_vision",
                "conditions": "is_going_to_cloud_vision",
            },
            {
                "trigger": "advance",
                "source": "ChatGPT",
                "dest": "ChatGPT",
                "conditions": "is_message",
            },
            {
                "trigger": "advance",
                "source": "image_generation",
                "dest": "image_generation",
                "conditions": "is_message",
            },
            {
                "trigger": "advance",
                "source": "cloud_vision",
                "dest": "cloud_vision",
                "conditions": "is_image",
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine