from django.http import JsonResponse
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()

    category_id = request.GET.get("category")
    active = request.GET.get("active")
    search = request.GET.get("search")

    if category_id:
        products = products.filter(category_id=category_id)

    if active:
        if active.lower() == "true":
            products = products.filter(is_active=True)
        elif active.lower() == "false":
            products = products.filter(is_active=False)

    if search:
        products = products.filter(name__icontains=search)

    data = []

    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id,
        })

    return JsonResponse(data, safe=False)

    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id,
        })

    return JsonResponse(data, safe=False)


def product_detail(request, id):
    try:
        p = Product.objects.get(id=id)
        data = {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'})


def category_list(request):
    categories = Category.objects.all()
    data = []

    for c in categories:
        data.append({
            'id': c.id,
            'name': c.name,
        })

    return JsonResponse(data, safe=False)


def category_detail(request, id):
    try:
        c = Category.objects.get(id=id)
        data = {
            'id': c.id,
            'name': c.name,
        }
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'})


def category_products(request, id):
    try:
        c = Category.objects.get(id=id)
        products = c.products.all()
        data = []

        for p in products:
            data.append({
                'id': p.id,
                'name': p.name,
                'price': p.price,
                'description': p.description,
                'count': p.count,
                'is_active': p.is_active,
                'category_id': p.category.id,
            })

        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'})