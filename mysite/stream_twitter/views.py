from django.shortcuts import render
from django.views.generic.edit import CreateView
from stream_twitter.models import Follow
from stream_twitter.models import Tweet
from django.contrib.auth.models import User
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager


class FollowView(CreateView):
    model = Follow
    fields = ['target']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tweet, self).form_valid(form)


class TweetView(CreateView):
    model = Tweet
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tweet, self).form_valid(form)

# def profile_feed(request, username=None):
#     enricher = Enrich()
#     user = User.objects.get(username=username)
#     feed = feed_manager.get_user_feed(user.id)
#     activities = feed.get(limit=25)['results']
#     enricher.enrich_activities(activities)
#     context = {
#         'activities': activities
#     }
#     return render(request, 'tweets.html', context)

# def timeline(request):
#     enricher = Enrich()
#     feed = feed_manager.get_news_feeds(request.user.id)['flat']
#     activities = feed.get(limit=25)['results']
#     enricher.enrich_activities(activities)
#     context = {
#         'activities': activities
#     }
#     return render(request, 'timeline.html', context)


def hashtag(request, hashtag):
    enricher = Enrich()
    feed = feed_manager.get_feed('hashtag', hashtag)
    activities = feed.get(limit=25)['results']
    enricher.enrich_activities(activities)
    context = {
        'activities': activities
    }
    return render(request, 'hashtag.html', context)