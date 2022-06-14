#from django.contrib.auth import get_user_model
#from django.test import TestCase, Client

#from ..models import Group, Post

#User = get_user_model()


#class PostsURLTests(TestCase):
    #@classmethod
    #def setUpClass(cls):
        #super().setUpClass()
        #cls.user = User.objects.create_user(username='authorized_user')
        #cls.group = Group.objects.create(
        #    title='Группа',
        #    slug='test_slug',
        #    description='Тестовое описание',
        #)
        # Создадим запись в БД для проверки доступности адреса task/test-slug/
        #cls.post = Post.objects.create(
        #    author=cls.user,
       #     group=cls.group,
      #      text='Тестовый текст',

     #   )

    #def setUp(self):
        # Создаем неавторизованный клиент
        #self.guest_client = Client()
        # Создаем пользователя
        #self.user = User.objects.create_user(username='HasNoName')
        # Создаем второй клиент
        #self.authorized_client = Client()
        # Авторизуем пользователя
        #self.authorized_client.force_login(self.user)
        #self.guest_url = {
         #   '/': 'posts/index.html',
        #    '/group/test_slug/': 'posts/group_list.html',
       #     '/profile/authorized_user/': 'posts/profile.html',
      #      f'/posts/{PostsUrlTests.post.id}/': 'posts/post_detail.html'
     #   }

    #self.auth_user_url = {
    #    '/create/': 'posts/post_create.html',
    #    f'/posts/{PostsUrlTests.post.id}/edit/': 'posts/post_create.html',
    #}

    #def test_guest_url_code_200(self):
        #for path in self.guest_url.keys():
       #     with self.subtest(path=path):
      #          response = self.guest_client.get(path)
     #           self.assertEqual(response.status_code, 200, f'Статус страницы {path} не равен 200')

    #def test_auth_url_code_200(self):
   #     for path in self.auth_user_url.keys():
  #          with self.subtest(path=path):
 #               response = self.authorized_client.get(path)
#                self.assertEqual(response.status_code, 200, f'Статус страницы {path} не равен 200')
