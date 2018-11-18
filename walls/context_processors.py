from .models import Categories

def add_variable_to_context(request):
    return {
        'categories': Categories.objects.filter(active=True)
    }