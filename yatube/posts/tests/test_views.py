# from django.contrib.auth import get_user_model
# from django.test import Client, TestCase
# from django.urls import reverse
# from ..models import Group, Post
# User = get_user_model()
#
#
# class PostPagesTests(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         # Создадим запись в БД
#         cls.group = Group.objects.create(
#             title='Заголовок',
#             description='Текст',
#             slug='test-slug',
#         )
#         cls.user = User.objects.create_user(
#             username='author'
#         )
#         cls.post = Post.objects.create(
#             author = cls.user,
#             group = cls.group,
#             text = 'text'
#         )
#
#     def setUp(self):
#         # Создаем авторизованный клиент
#         self.user = User.objects.create_user(username='NoName')
#         self.authorized_client = Client()
#         self.authorized_client.force_login(self.user)
#
#
#     #def test_views_use_correct_template(self):
#         #templates_pages_names = {
#            # reverse('posts:index'): 'posts/index.html',
#            # reverse('posts:group_list',
#            #         kwargs={'slug': self.group.slug}): 'posts/group_list.html',
#             #reverse('posts:post_create'): 'posts/create_post.html',
#            # reverse('posts:profile',
#             #        kwargs={'username': self.user.username}): 'posts/profile.html',
#            # reverse(
#            #     'posts:post_detail', kwargs={'post_id': '1'}
#            # ): 'posts/post_detail.html',
#        # }
#         #for reverse_name, template in templates_pages_names.items():
#             #with self.subTest(reverse_name=reverse_name):
#                 #response = self.authorized_client.get(reverse_name)
#                 #self.assertTemplateUsed(response, template)
#
#     def test_index_page_show_correct_context(self):
#         response = self.authorized_client.get(reverse('posts:index'))
#         first_object = response.context['page_obj'][0]
#         post_text_0 = first_object.text
#         self.assertEqual(post_text_0, 'text')
#
#     def test_profile_page_show_correct_context(self):
#         response = self.authorized_client.get(reverse('posts:profile'))
#         first_object = response.context['page_obj'][0]
#         post_author_0 = first_object.author
#         post_text_0 = first_object.text
#         self.assertEqual(post_author_0,self.post.author)
#         self.assertEqual(post_text_0,self.post.text)
#
#     def test_group_list_show_correct_context(self):
#         response = self.authorized_client.get('posts:group_list')
#         first_object = response.get['page_obj'][0]
#         post_text = first_object.text
#         post_title = first_object.group.title
#         self.assertEqual(post_title, 'Заголовок')
#         self.assertEqual(post_text,'text')
#
#     def test_post_edit_page_show_correct_context(self):
#         response = self.authorized_client.get(
#             reverse('posts:post_edit',kwargs ={'post_id':self.post.id})
#         )
#         form_fields = {
#             'text':forms.fields.CharField,
#             'group':forms.fields.ChoiceField
#         }
#
#         for value, expected in form_fields.items():
#             with self.subTest(value=value):
#                 form_field = response.context.get('form').fields.get(value)
#                 self.assertIsInstance(form_field,expected)
#
#
#     def test_post_create_page_show_correct_context(self):
#         response = self.authorized_client.get(
#             reverse('posts:post_create')
#         )
#         form_fields = {
#             'text':forms.fields.CharField,
#             'group':forms.fields.ChoiceField,
#         }
#
#         for value, expected in form_fields.items():
#             with self.subTest(value=value):
#                 form_field = response.context.get('form').fields.get(value)
#                 self.assertIsInstance(form_field,expected)
#
#
#
#     def test_group_posts_show_correct_context(self):
#         response = self.authorized_client.get(reverse('posts:post_detail'))
#         first_object = response.context['page_obj'][0]
#         self.assertEqual(first_object.text, self.post.text)
#         # self.assertEqual(first_object.group.slug, self.group.slug)
#         # self.assertEqual(first_object.group.title, self.group.title)



