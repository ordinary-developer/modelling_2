from app.logic.event import Event


class OutcomingFirstEvent(Event):

    #[abstract method implementation]
    def handle_self(self, Model):
        Model.handle_outcoming_first_event(self.time)
