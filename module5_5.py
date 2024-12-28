import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        self.current_user = None
        for i in self.users:
            if i.nickname == nickname:
                if i.password == hash(password):
                    self.current_user = i
                else:
                    self.current_user = None
                break

    def register(self, nickname, password, age):
        found_user = False
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                found_user = True
        if not found_user:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)

    def get_videos(self, key_word):
        finded_videos = []
        for i in self.videos:
            if i.title.upper().find(key_word.upper()):
                finded_videos.append(i.title)
        return finded_videos

    def watch_video(self, key_word):
        for i in self.videos:
            if i.title.find(key_word) != -1:
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    break
                elif self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break
                else:
                    for t in range(0, i.duration):
                        time.sleep(1)
                        i.time_now = t
                        print(t + 1, end=' ')
                    print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


