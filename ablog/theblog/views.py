from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import post, category, Comment
from .forms import formpost, editpost, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#def home(request):
#    return render(request, 'home.html', {})

class AcercaDeView(TemplateView): #'acerca de'
    template_name = 'acerca_de.html'

class ContactoView(TemplateView): #contacto
    template_name = 'contacto.html'

def LikeView(request, pk):
    post_instance=get_object_or_404(post, id=request.POST.get('post_id'))
    liked=False

    if post_instance.likes.filter(id=request.user.id).exists():
        post_instance.likes.remove(request.user)
        liked=False
    else:
        post_instance.likes.add(request.user)
        liked=True

    #post_instance.likes.add(request.user)
    return HttpResponseRedirect(reverse('detalle-articulo', args=[str(pk)]))

'''
def LikeView(request, pk):
    post = get_object_or_404(post, id=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detalle-articulo', args=[str(pk)]))
'''

class HomeView(ListView):
    model=post 
    template_name='home.html'
    cats=category.objects.all()
    ordering=['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu=category.objects.all()
        context=super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        return context

def categoryListView(request):
    cat_menu_list=category.objects.all() 
    return render(request, 'categorias_list.html', {'cat_menu_list':cat_menu_list})

def categoryView(request, cats):
    category_posts=post.objects.filter(category=cats) 
    return render(request, 'categorias.html', {'cats':cats.title(), 'category_posts':category_posts})

class detalle_articulo_View(DetailView):
    model=post
    template_name='detalle_articulo.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu=category.objects.all()
        context=super(detalle_articulo_View, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context['cat_menu']=cat_menu
        context['total_likes']=total_likes
        context['liked']=liked
        return context
    


class agregar_post_View(CreateView):
    model=post
    form_class=formpost
    template_name='agregar_post.html'
    #fields='__all__'

class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='add_comment.html'
    #fields='__all__'
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('home')


class categoria_post_View(CreateView):
    model=category
    #form_class=formpost
    template_name='agregar_categoria.html'
    fields='__all__'

class update_post_View(UpdateView):
    model=post
    form_class=editpost
    template_name='update_post.html'
    #fields=['title', 'body']

class eliminar_post_View(DeleteView):
    model=post
    template_name='eliminar_post.html'
    success_url=reverse_lazy('home')

