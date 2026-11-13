"""задание 1"""

# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
# def is_admin(func):
#     def wrapper(user):
#         if user.role == "admin":
#             return func(user)
#         else:
#             return "у вас нет доступа"
#     return wrapper
# @is_admin
# def delete_video(user):
#     return "Видео удалено"
#
# admin = User("Ardager", "admin")
# user = User("Bek", "user")
#
# print(delete_video(admin))
# print(delete_video(user))

"""задание 2"""

# import time
#
# def timer(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end = time.time()
#
#         print(result)
#         print(f"Время выполнения: {round(end - start, 1)} секунд")
#
#     return wrapper
#
# @timer
# def download_video():
#     time.sleep(2)
#     return "видео загружено"
#
# download_video()