
from src.controllers.voice_controller import VoiceController

def main():
    controller = VoiceController()
    controller.handle_voice_command()

if __name__ == "__main__":
    main()
