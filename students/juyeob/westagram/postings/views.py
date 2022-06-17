import json, bcrypt, jwt, re, datetime

from django.http     import JsonResponse, HttpResponse
from json.decoder    import JSONDecodeError
from django.views    import View
from django.conf     import settings


from postings.models import Post, Comment, Like
from core.utils      import login_decorator

class PostingView(View):
    #def json_default(value):
     #   if isinstance(value, datetime.date):
      #      return value.strftime('%Y-%m-%d')
       # raise TypeError('not JSON serializable')
    #data = {'date': datetime.date.today()}
    #json_data = json.dumps(data, default=json_default)



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
            contents = contents,

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