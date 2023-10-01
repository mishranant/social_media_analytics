import re, json
from django import forms
from .models import Post
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError

class PostCreationForm(forms.Form):
    id = forms.UUIDField()
    content = forms.CharField()

#  Post Creation (POST /api/v1/posts/): Accept a JSON payload with text content and a unique identifier.
@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
        except ValueError:
            return HttpResponseServerError('Unable to parse request body')
        
        form = PostCreationForm(request_data)
        if form.is_valid():
            id = form.cleaned_data['id']
            content = form.cleaned_data['content']
            
            try:
                Post(id=id, content=content).save()
                return HttpResponse('Successfully created a new post')
            except IntegrityError:
                return HttpResponseServerError('Unable to save the post due to uniqueness constraint')
        else:
            return HttpResponseServerError('Invalid request body')

# Post Analysis (GET /api/v1/posts/{id}/analysis/): Provide an analysis endpoint that returns the number of words and average word length in a post.
def analysis(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    words = re.findall(r'\w+', post.content)
    word_count = len(words)
    avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    
    return render(request, 'posts/analysis.html', {'content': post.content, 'word_count': word_count, 'avg_word_length': avg_word_length})
