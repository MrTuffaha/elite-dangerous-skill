from mycroft import MycroftSkill, intent_file_handler


class EliteDangerous(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dangerous.elite.intent')
    def handle_dangerous_elite(self, message):
        self.speak_dialog('dangerous.elite')


def create_skill():
    return EliteDangerous()

