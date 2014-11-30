from app.logic.event import Event


class OutcomingSecondEvent(Event):

    #[abstract method implementation]
    def handle_self(self, Model):
        Model.handle_incoming_event(self.time)
