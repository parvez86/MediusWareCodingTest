from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from product.models import Variant

from product.models import ProductVariantPrice, Product


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['products'] = list(ProductVariantPrice.all())
        return context


class ListProductView(generic.TemplateView):
    template_name = 'products/list.html'
    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Variant.objects.filter(**filter_string)

    def get_context_data(self, **kwargs):
        product_list = Product.objects.all()


        page = self.request.GET.get('page', 1)
        paginator = Paginator(product_list, 2)
        print(paginator.count)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = super(ListProductView, self).get_context_data(**kwargs)
        # variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['products'] = products
        context['count'] = paginator.count
        # context['variants'] =
        context['search'] = {
            "title": "",
            "varint_title": "",
            "price_range": {
                "start": "",
                "end": ""
            },
            "date": ""
        }
        return context

