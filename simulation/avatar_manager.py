class AvatarManager(object):
    def __init__(self, initial_avatars):
        self.avatarsById = {p.id: p for p in initial_avatars}

    def player_changed_code(playerId, code):
        avatar = self.avatarsById[playerId]
        avatar.set_code(code)

