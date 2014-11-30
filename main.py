from app.logic.model import Model


if __name__ == '__main__':
    Model.initialize(1 * 60 * 60)
    Model.start()
