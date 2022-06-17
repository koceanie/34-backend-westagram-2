import json, bcrypt, jwt, re, datetime

from django.http     import JsonResponse, HttpResponse
from json.decoder    import JSONDecodeError
from django.views    import View
from django.conf     import settings


from postings.models import Post, Comment
from core.utils      import login_decorator

class PostingView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        writer = request.user
        image_url = data['image_url']
        contents = data['contents']

        if contents == None :
            return JsonResponse({"message" : "ERROR_NONE_CONTENTS"}, status = 400)
        
        Post.objects.create(
            writer = writer,
            image_url = image_url,
            contents = contents

        )

        return HttpResponse(status = 200)
    
    def get(self, request):
        result = []
        
        result = [
            {
                'writer' : post.writer.email,
                'image_url' : post.image_url,
                'contents' : post.contents,
                'created_time' : post.created_time

            }for post in Post.objects.all()
        ]

        return JsonResponse({'result':result}, status = 200)


class CommentView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)

        post = Post.objects.get(id=data['post'])
        writer = request.user
        contents = data['contents']

        if contents == None :
            return JsonResponse({"message" : "ERROR_NONE_CONTENTS"}, status = 400)
        
        Comment.objects.create(
            writer = writer,
            post = post,
            contents = contents
        )

        return HttpResponse(status = 200)
        


"""
class LikeView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        post = Post.objects.all()

        post_id = data['post_id']
        writer_id = request.user

        Like.objects.create(
            post_id = post_id,
            user_id = writer_id
        )

        return HttpResponse(status = 200)

"""
