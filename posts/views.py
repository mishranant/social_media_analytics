from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import json, re

#  Post Creation (POST /api/v1/posts/): Accept a JSON payload with text content and a unique identifier.
@csrf_exempt
def create(request):
    if request.method == 'POST':
        requestBody = json.loads(request.body)
        Post(id=requestBody['id'], content=requestBody['content']).save()
        return HttpResponse('successfully created a new post')

# Post Analysis (GET /api/v1/posts/{id}/analysis/): Provide an analysis endpoint that returns the number of words and average word length in a post.
@csrf_exempt
def analysis(request, post_id):
    post = Post.objects.get(pk=post_id)
    words = re.findall(r'\w+', post.content)
    word_count = len(words)
    avg_word_length = sum([len(x) for x in words]) / word_count
    return render(request, 'posts/analysis.html', {'content': post.content, 'word_count': word_count, 'avg_word_length': avg_word_length})
