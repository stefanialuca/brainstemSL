from brainstem.app import Brainstem
from config import settings

brainstem = Brainstem(settings)


if __name__ == '__main__':
    brainstem.run_listener()
