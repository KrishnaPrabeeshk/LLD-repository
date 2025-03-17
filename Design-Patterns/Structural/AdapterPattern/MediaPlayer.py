# Target interface that the client expects
class MediaPlayer:
    def play(self,audio_type,file_name):
        pass

# This is the Adaptee class
# The Adaptee class that provides methods in a different format
class AdvancedMediaPlayer:
    def playMp4(self,file_name):
        print("Playing MP4 file: ",file_name)
    def playVLC(self,file_name):
        print("Playing VLC file: ",file_name)

# This is the adapter class
# The Adapter class that allows the Adaptee to work with the MediaPlayer interface
class MediaAdapter(MediaPlayer):
    def __init__(self,audio_type):
        self.advanced_media_player = None
        if audio_type.lower() == "mp4" or audio_type.lower() == "vlc":
            self.advanced_media_player = AdvancedMediaPlayer()
    
    def play(self, audio_type, file_name):
        # We call the required method based on the audio type
        if audio_type.lower() == "mp4":
            self.advanced_media_player.playMp4(file_name)
        elif audio_type.lower() == "vlc":
            self.advanced_media_player.playVLC(file_name)
        else:
            print("Invalid file format!")

#The client code
class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.media_adapter = None
    def play(self,audio_type,file_name):
        if audio_type.lower() == "mp3":
            print(f"Playing MP3 file: {file_name}")
        else: 
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type,file_name)


# Testing the Adapter 
audio_player = AudioPlayer()

audio_player.play("MP3","song.mp3")
audio_player.play("Mp4","movie.mp4")
audio_player.play("VlC","documentary.vlc")
audio_player.play("avi","video.avi")