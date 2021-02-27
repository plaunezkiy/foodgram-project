from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Recipe


class MainMixin:
    template = 'main.html'
    card_template = 'recipe_card.html'
    queryset = Recipe.objects.all()
    tags = True
    profile = False

    def get(self, request):
        request.session.setdefault('purchases', value=[])
        items = self.queryset
        if self.tags:
            request.session.setdefault(
                'tag_list',
                value=['breakfast', 'lunch', 'dinner']
            )
            tag_list = request.session['tag_list']
            query = Q()
            for i in tag_list:
                query.add(Q(tags__contains=i), Q.OR)
            items = items.filter(query)

        paginator = Paginator(items, 6)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(
            request,
            self.template,
            context=
            {
                'title': self.title,
                'tab': self.tab,
                'page': page,
                'paginator': paginator,
                'tags': self.tags,
                'card_tmp': self.card_template,
                'profile': self.profile,
            }
        )
