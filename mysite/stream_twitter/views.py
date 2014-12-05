from django.shortcuts import render
from django.views.generic.edit import CreateView
from stream_twitter.models import Follow
from stream_twitter.models import Tweet
from django.contrib.auth.models import User
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager


def profile_feed(request, username=None):
    enricher = Enrich()
    user = User.objects.get(username=username)
    feed = feed_manager.get_user_feed(user.id)
    activities = feed.get(limit=25)['results']
    enricher.enrich_activities(activities)
    context = {
        'activities': activities
    }
    return render(request, 'tweets.html', context)


class TweetView(CreateView):
    model = Tweet
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tweet, self).form_valid(form)
