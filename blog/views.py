from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView
from pytils.translit import slugify

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Фильтр для вывода на страницу только опубликованных блогов"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Блоги'})
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Добавление просмотра после обновления страницы"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Подробности блога'})
        return context


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'created_at')
    success_url = reverse_lazy('blog:blogs')

    def form_valid(self, form):
        """Создаёт человеко понятный URL"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'created_at', 'is_published')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs')
