from mycroft import MycroftSkill, intent_file_handler


class DeviceControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.device.intent')
    def handle_control_device(self, message):
        self.speak_dialog('control.device')


def create_skill():
    return DeviceControl()

