datas=[]
session = vk.Session(access_token='')
vk_api = vk.API(session, v="5.131")

def share_vk(self):

    groupID = []
    groupID.append(self.share_vacancy_id.country_region_vacancy.group_id)
    groupID.append(self.share_vacancy_id.category_vacancy_id.group_id)
    text = self.share_vacancy_id.name.name + '\n' + 'Зарплата от ' + str(self.share_vacancy_id.salary_from) + ' до ' + str(self.share_vacancy_id.salary>        +'\n'+ 'Описание' + '\n' + self.share_vacancy_id.note + '\n' + 'Ссылка на вакансию' + '\n' + self.link_to_vacancy
    result =''
    for x in range(len(groupID)):
        upload_url = vk_api.photos.getWallUploadServer(group_id=groupID[x])['upload_url']
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
            'group_id': groupID[x]}
        data.append(vk_api.photos.saveWallPhoto(**params))
        photo_id = data[0][0]['id']
        attachments.append('photo' + str(data[0][0]['owner_id']) + '_' + str(photo_id))
        attachments.reverse()   # разворачиваем список
        params = {'attachments': attachments,
        'message': text,
        'owner_id': '-' + groupID[x],
        'from_group': '1'}
        result = vk_api.wall.post(**params)
        self.is_completed = True
        self.share_date_vk = datetime.datetime.now()
        if x == 0:
            self.link_share_category_post = self.share_vacancy_id.category_vacancy_id.link_category_vk_vacancy+'?w=wall-'+str(groupID[x])+'_'+str(resul>
        else:
            self.link_share_region_post = self.share_vacancy_id.country_region_vacancy.link_region_vk_vacancy +'?w=wall-'+str(groupID[x])+'_'+str(resul>