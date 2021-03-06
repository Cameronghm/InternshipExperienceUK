"""A video player class."""

from os import remove
from .video_library import VideoLibrary
from random import randrange
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = ""
        self.paused = False
        self.playlists = []
        self.playlist_names = []
        self.flagged = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here's a list of all available videos:")
        order = []
        for video in self._video_library.get_all_videos():
            order.append([video.title, video])
        order.sort()
        for video in range(len(order)):
            tags = ""
            print("{} ({})".format(order[video][1].title,
                  order[video][1].video_id), end=' ')
            for tag in order[video][1].tags:
                tags = tags + str(tag) + ' '
            print("[{}]".format(tags[:len(tags)-1]), end='')
            flagged_videos = []
            for videos in self.flagged:
                flagged_videos.append(videos[0])
            id = order[video][1].video_id
            if id in flagged_videos:
                print(" - FLAGGED (reason: " +
                      self.flagged[flagged_videos.index(id)][1] + ")")
            else:
                print("")

    def play_video(self, video_id):
        """Plays the respective video."""
        videos = self._video_library.get_all_videos()
        video_ids = []
        for video in videos:
            video_ids.append(video.video_id)
        if video_id not in video_ids:
            print("Cannot play video: Video does not exist")
        else:
            flagged = False
            reason = ""
            for video in self.flagged:
                if video_id == video[0]:
                    flagged = True
                    reason = video[1]
            if flagged:
                print(
                    "Cannot play video: Video is currently flagged (reason: " + reason + ")")
            else:
                try:
                    if len(self.currently_playing) > 0:
                        for video in videos:
                            if (video_id == video.video_id):
                                print("Stopping video: " +
                                      self.currently_playing)
                                self.currently_playing = video.title
                                print("Playing video: " +
                                      self.currently_playing)
                    else:
                        for video in videos:
                            if (video_id == video.video_id):
                                self.currently_playing = video.title
                                print("Playing video: " +
                                      self.currently_playing)
                except NameError:
                    for video in videos:
                        if (video_id == video.video_id):
                            self.currently_playing = video.title
                            print("Playing video: " + self.currently_playing)
            self.paused = False

    def stop_video(self):
        """Stops the current video."""
        try:
            if len(self.currently_playing) > 0:
                print("Stopping video: " + self.currently_playing)
                self.paused = False
                self.currently_playing = ""
            else:
                print("Cannot stop video: No video is currently playing")
        except NameError:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        order = []
        counter = 0
        flagged_videos = []
        for video in self.flagged:
            flagged_videos.append(video[0])
        for video in self._video_library.get_all_videos():
            if video.video_id not in flagged_videos:
                order.append(video)
                counter = counter + 1
        if len(order) == 0:
            print("No videos available")
        else:
            random = randrange(counter)
            if counter == 0:
                print("No videos available")
            else:
                VideoPlayer.play_video(self, order[random].video_id)

    def pause_video(self):
        """Pauses the current video."""
        try:
            if (len(self.currently_playing) > 0) and (self.paused == False):
                print("Pausing video: " + self.currently_playing)
                self.paused = True
            elif (len(self.currently_playing) > 0) and (self.paused == True):
                print("Video already paused: " + self.currently_playing)
            else:
                print("Cannot pause video: No video is currently playing")
        except NameError:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        try:
            if (len(self.currently_playing) > 0) and (self.paused == False):
                print("Cannot continue video: Video is not paused")
            elif (len(self.currently_playing) > 0) and (self.paused == True):
                print("Continuing video: " + self.currently_playing)
                self.paused = False
            else:
                print("Cannot continue video: No video is currently playing")
        except NameError:
            print("Cannot pause video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        try:
            if (len(self.currently_playing) > 0) and (self.paused == False):
                for video in self._video_library.get_all_videos():
                    if video.title == self.currently_playing:
                        tags = ""
                        print("Currently playing: {} ({})".format(video.title,
                                                                  video.video_id), end=' ')
                        for tag in video.tags:
                            tags = tags + str(tag) + ' '
                        print("[{}]".format(tags[:len(tags)-1]))
            elif (len(self.currently_playing) > 0) and (self.paused == True):
                for video in self._video_library.get_all_videos():
                    if video.title == self.currently_playing:
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
        playlist_name_copy = playlist_name
        if (playlist_name_copy.lower() not in self.playlist_names):
            self.playlist_names.append(playlist_name_copy.lower())
            self.playlists.append(Playlist(playlist_name))
            print("Successfully created new playlist: " + playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.

        Detect if video is inside playlist
        Add video to playlist
        """
        playlist_name_copy = playlist_name
        if (playlist_name_copy.lower() not in self.playlist_names):
            print("Cannot add video to " + playlist_name +
                  ": Playlist does not exist")
        else:
            flagged = False
            reason = ""
            for video in self.flagged:
                if video_id == video[0]:
                    flagged = True
                    reason = video[1]
            if flagged:
                print(
                    "Cannot add video to " + playlist_name + ": Video is currently flagged (reason: " + reason + ")")
            else:
                video_ids = []
                videos = []
                for video in self._video_library.get_all_videos():
                    video_ids.append(video.video_id)
                    videos.append(video)
                if video_id not in video_ids:
                    print("Cannot add video to " + playlist_name +
                          ": Video does not exist")
                else:
                    video_idlist = self.playlists[self.playlist_names.index(
                        playlist_name_copy.lower())].listallvideo_ids()
                    if video_id in video_idlist:
                        print("Cannot add video to " + playlist_name +
                              ": Video already added")
                    else:
                        self.playlists[self.playlist_names.index(
                            playlist_name_copy.lower())].videos.append(videos[video_ids.index(video_id)])
                        print("Added video to " + playlist_name + ": " +
                              videos[video_ids.index(video_id)].title)

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            playlist_names = []
            for playlist in self.playlists:
                playlist_names.append(playlist.displayname())
            playlist_names.sort()
            for playlist_name in playlist_names:
                print(playlist_name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_copy = playlist_name
        if playlist_name_copy.lower() not in self.playlist_names:
            print("Cannot show playlist " + playlist_name +
                  ": Playlist does not exist")
        else:
            if not self.playlists[self.playlist_names.index(
                    playlist_name_copy.lower())].anyvideos():
                print("Showing playlist: " + playlist_name)
                print("No videos here yet")
            else:
                videos = self.playlists[self.playlist_names.index(
                    playlist_name_copy.lower())].returnvideos()
                print("Showing playlist: " + playlist_name)
                for video in videos:
                    tags = ""
                    print("{} ({})".format(video.title, video.video_id), end=' ')
                    for tag in video.tags:
                        tags = tags + str(tag) + ' '
                    print("[{}]".format(tags[:len(tags)-1]), end='')
                    flagged_videos = []
                    for videos in self.flagged:
                        flagged_videos.append(videos[0])
                    id = video.video_id
                    if id in flagged_videos:
                        print(" - FLAGGED (reason: " +
                              self.flagged[flagged_videos.index(id)][1] + ")")
                    else:
                        print("")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_name_copy = playlist_name
        if playlist_name_copy.lower() not in self.playlist_names:
            print("Cannot remove video from " + playlist_name +
                  ": Playlist does not exist")
        else:
            video_ids = []
            videos = []
            for video in self._video_library.get_all_videos():
                video_ids.append(video.video_id)
                videos.append(video)
            if video_id not in video_ids:
                print("Cannot remove video from " + playlist_name +
                      ": Video does not exist")
            else:
                if not self.playlists[self.playlist_names.index(
                        playlist_name_copy.lower())].checkvideo(video_id):
                    print("Cannot remove video from " +
                          playlist_name + ": Video is not in playlist")
                else:
                    self.playlists[self.playlist_names.index(
                        playlist_name_copy.lower())].removevideo(video_id)
                    print("Removed video from " + playlist_name +
                          ": " + videos[video_ids.index(video_id)].title)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_copy = playlist_name
        if playlist_name_copy.lower() not in self.playlist_names:
            print("Cannot clear playlist " + playlist_name +
                  ": Playlist does not exist")
        else:
            self.playlists[self.playlist_names.index(
                playlist_name_copy.lower())].clear()
            print("Successfully removed all videos from " + playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_copy = playlist_name
        if playlist_name_copy.lower() not in self.playlist_names:
            print("Cannot delete playlist " + playlist_name +
                  ": Playlist does not exist")
        else:
            playlist = self.playlists[self.playlist_names.index(
                playlist_name_copy.lower())]
            self.playlists.pop(self.playlist_names.index(
                playlist_name_copy.lower()))
            self.playlist_names.remove(playlist_name_copy.lower())
            del playlist
            print("Deleted playlist: " + playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        search_term_copy = search_term
        videos = self._video_library.get_all_videos()
        video_titles = []
        counter = 1
        flagged_videos = []
        for flagged in self.flagged:
            flagged_videos.append(flagged[0])
        for video in videos:
            if (search_term_copy.lower() in video.title.lower()) and (video.video_id not in flagged_videos):
                video_titles.append([])
                video_titles[counter-1].append(counter)
                video_titles[counter-1].append(video)
                counter = counter + 1
        if len(video_titles) == 0:
            print("No search results for " + search_term)
        else:
            print("Here are the results for " + search_term + ":")
            for video in video_titles:
                tags = ""
                print(str(video[0]) + ") {} ({})".format(video[1].title,
                                                         video[1].video_id), end=' ')
                for tag in video[1].tags:
                    tags = tags + str(tag) + ' '
                print("[{}]".format(tags[:len(tags)-1]))
            print(
                "Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input("")
            if answer.isnumeric():
                if not ((int(answer) < 1) or (int(answer) > len(video_titles))):
                    self.play_video(video_titles[int(answer)-1][1].video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        video_tag_copy = video_tag
        videos = self._video_library.get_all_videos()
        video_tags = []
        counter = 1
        flagged_videos = []
        for flagged in self.flagged:
            flagged_videos.append(flagged[0])
        for video in videos:
            for tag in video.tags:
                if (video_tag_copy.lower() == tag.lower()) and (video.video_id not in flagged_videos):
                    video_tags.append([])
                    video_tags[counter-1].append(counter)
                    video_tags[counter-1].append(video)
                    counter = counter + 1
                    break
        if len(video_tags) == 0:
            print("No search results for " + video_tag)
        else:
            print("Here are the results for " + video_tag + ":")
            for video in video_tags:
                tags = ""
                print(str(video[0]) + ") {} ({})".format(video[1].title,
                                                         video[1].video_id), end=' ')
                for tag in video[1].tags:
                    tags = tags + str(tag) + ' '
                print("[{}]".format(tags[:len(tags)-1]))
            print(
                "Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input("")
            if answer.isnumeric():
                if not ((int(answer) < 1) or (int(answer) > len(video_tags))):
                    self.play_video(video_tags[int(answer)-1][1].video_id)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.

        """
        video_ids = []
        videos = []
        for video in self._video_library.get_all_videos():
            video_ids.append(video.video_id)
            videos.append(video)
        if video_id not in video_ids:
            print("Cannot flag video: Video does not exist")
        else:
            already_flagged = False
            for video in self.flagged:
                if video_id == video[0]:
                    already_flagged = True
            if already_flagged:
                print("Cannot flag video: Video is already flagged")
            else:
                if self.currently_playing == videos[video_ids.index(video_id)].title:
                    self.stop_video()
                if flag_reason == "":
                    self.flagged.append([video_id, "Not supplied"])
                    print("Successfully flagged video: " +
                          videos[video_ids.index(video_id)].title + " (reason: Not supplied)")
                else:
                    self.flagged.append([video_id, flag_reason])
                    print("Successfully flagged video: " + videos[video_ids.index(
                        video_id)].title + " (reason: " + flag_reason + ")")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.

        cannot remove not flagged
        removed flag

        """
        video_ids = []
        videos = []
        for video in self._video_library.get_all_videos():
            video_ids.append(video.video_id)
            videos.append(video)
        if video_id not in video_ids:
            print("Cannot remove flag from video: Video does not exist")
        else:
            already_flagged = False
            for video in self.flagged:
                if video_id == video[0]:
                    already_flagged = True
            if not already_flagged:
                print("Cannot remove flag from video: Video is not flagged")
            else:
                flagged = []
                for video in self.flagged:
                    flagged.append(video[0])
                self.flagged.pop(flagged.index(video_id))
                print("Successfully removed flag from video: " +
                      videos[video_ids.index(video_id)].title)
