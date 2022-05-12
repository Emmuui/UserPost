def upload_to_userprofile(instance, file):
    """ Путь к аватару пользователя """

    return f'profile/{instance.user}/avatar/{file}'


def upload_image_publication(instance, file):
    """ Путь к изображению публикации пользователя """

    return f'profile/{instance.user}/publication/{instance.title}/{file}'
