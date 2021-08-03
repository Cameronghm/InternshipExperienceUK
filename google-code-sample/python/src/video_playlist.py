"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name):
        self.name = name
        self.videos = []

    def addvideo(self, video):
        self.videos.append(video)

    def listallvideo_ids(self):
        video_ids = []
        for video in self.videos:
            video_ids.append(video.video_id)
        return video_ids

    def displayname(self):
        return self.name

    def anyvideos(self):
        if len(self.videos) == 0:
            return False
        else:
            return True

    def returnvideos(self):
        return self.videos

    def removevideo(self, video_id):
        for video in self.videos:
            if video.video_id == video_id:
                self.videos.remove(video)

    def checkvideo(self, video_id):
        contained = False
        for video in self.videos:
            if video.video_id == video_id:
                contained = True
        return contained

    def clear(self):
        self.videos = []
