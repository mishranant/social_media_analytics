from django.shortcuts import render

def create(request):
    # request.POST['key']
    return render(request, 'posts/create.html', {})

def analysis(request, post_id):
    return render(request, 'posts/analysis.html', {})
