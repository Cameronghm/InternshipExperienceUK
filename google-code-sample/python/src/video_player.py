"""A video player class."""

from .video_library import VideoLibrary
from random import randrange


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here's a list of all available videos:")
        order = []
        i = 0
        for video in self._video_library.get_all_videos():
            order.append([video.title, video])
        order.sort()
        for video in range(len(order)):
            tags = ""
            print("{} ({})".format(order[video][1].title,
                  order[video][1].video_id), end=' ')
            for tag in order[video][1].tags:
                tags = tags + str(tag) + ' '
            print("[{}]".format(tags[:len(tags)-1]))

    def play_video(self, video_id):
        """Plays the respective video."""
        global currently_playing, paused
        videos = self._video_library.get_all_videos()
        video_ids = []
        for video in videos:
            video_ids.append(video.video_id)
        if video_id not in video_ids:
            print("Cannot play video: Video does not exist")
        else:
            try:
                if len(currently_playing) > 0:
                    for video in videos:
                        if (video_id == video.video_id):
                            print("Stopping video: " + currently_playing)
                            currently_playing = video.title
                            print("Playing video: " + currently_playing)
                else:
                    for video in videos:
                        if (video_id == video.video_id):
                            currently_playing = video.title
                            print("Playing video: " + currently_playing)
            except NameError:
                for video in videos:
                    if (video_id == video.video_id):
                        currently_playing = video.title
                        print("Playing video: " + currently_playing)
        paused = False

    def stop_video(self):
        """Stops the current video."""
        global currently_playing, paused
        try:
            if len(currently_playing) > 0:
                print("Stopping video: " + currently_playing)
                paused = False
                currently_playing = ""
            else:
                print("Cannot stop video: No video is currently playing")
        except NameError:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        order = []
        counter = 0
        for video in self._video_library.get_all_videos():
            order.append(video)
            counter = counter + 1
        random = randrange(counter)
        if counter == 0:
            print("No videos available")
        else:
            VideoPlayer.play_video(self, order[random].video_id)

    def pause_video(self):
        """Pauses the current video."""
        global currently_playing
        global paused
        try:
            if (len(currently_playing) > 0) and (paused == False):
                print("Pausing video: " + currently_playing)
                paused = True
            elif (len(currently_playing) > 0) and (paused == True):
                print("Video already paused: " + currently_playing)
            else:
                print("Cannot pause video: No video is currently playing")
        except NameError:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        global currently_playing
        global paused
        try:
            if (len(currently_playing) > 0) and (paused == False):
                print("Cannot continue video: Video is not paused")
            elif (len(currently_playing) > 0) and (paused == True):
                print("Continuing video: " + currently_playing)
                paused = False
            else:
                print("Cannot continue video: No video is currently playing")
        except NameError:
            print("Cannot pause video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        global currently_playing
        global paused
        try:
            if (len(currently_playing) > 0) and (paused == False):
                for video in self._video_library.get_all_videos():
                    if video.title == currently_playing:
                        tags = ""
                        print("Currently playing: {} ({})".format(video.title,
                                                                  video.video_id), end=' ')
                        for tag in video.tags:
                            tags = tags + str(tag) + ' '
                        print("[{}]".format(tags[:len(tags)-1]))
            elif (len(currently_playing) > 0) and (paused == True):
                for video in self._video_library.get_all_videos():
                    if video.title == currently_playing:
                        tags = ""
                        print("Currently playing: {} ({})".format(video.title,
                                                                  video.video_id), end=' ')
                        for tag in video.tags:
                            tags = tags + str(tag) + ' '
                            print("[{}] - PAUSED".format(tags[:len(tags)-1]))
            else:
                print("No video is currently playing")
        except NameError:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
