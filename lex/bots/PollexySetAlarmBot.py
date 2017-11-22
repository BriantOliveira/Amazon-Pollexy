from lex.bots import BaseBot


class PollexySetAlarmBot(BaseBot):
    def __init__(self):
        self.bot_name = 'SetAlarmBot'
        super(PollexySetAlarmBot, self).__init__()

    def on_fulfilled(self, last_response):
        print 'All Done!'
        super(PollexySetAlarmBot, self).on_fulfilled(last_response)

    def on_failed(self, last_response):
        print "No help will be provided."
        super(PollexySetAlarmBot, self).on_failed(last_response)

    def on_transition_in(self, last_response):
        pass

    def on_transition_out(self, last_response):
        pass

    def on_cancel(self, last_response):
        pass

    def on_misunderstood(self, last_response):
        pass

    def on_response(self, text, last_response):
        pass

    def register(self):
        super(PollexySetAlarmBot, self).register()
