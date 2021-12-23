def vkontakte(groupID,x,group_id,text):
    try:
        session = vk.Session(access_token='12889afe99326a10ad61a839b75566d7a4579653c1056345b7538e5fe8f62cf95529b973487a4bd78f440')
        vk_api = vk.API(session, v="5.131")
        upload_url = vk_api.photos.getWallUploadServer(group_id=group_id)['upload_url']
        data = []
        photo_id = 0
        attachments = []
        foto = ''
        if x == 0:
            foto = str(groupID[1])
        else:
            foto = '206751676'
        request = requests.post(upload_url, files={'photo': open('/home/toor/JPG/' + foto + ".jpg", "rb")})
        params = {'server': request.json()['server'],
        'photo': request.json()['photo'],
        'hash': request.json()['hash'],
        'group_id': group_id}
        data.append(vk_api.photos.saveWallPhoto(**params))
        photo_id = data[0][0]['id']
        attachments.append('photo' + str(data[0][0]['owner_id']) + '_' + str(photo_id))
        attachments.reverse()   # разворачиваем список
        params = {'attachments': attachments,
        'message': text,
        'owner_id': '-' + group_id,
        'from_group': '1'}
        result = vk_api.wall.post(**params)
        return result
    except Exception:
        return False
