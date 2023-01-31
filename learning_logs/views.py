from django.shortcuts import render, redirect

from .forms import TopicForm
from .models import Topic


def main(request):
    """Main page of 'Learning Log'."""
    return render(request, 'learning_logs/main.html')


def topics(request):
    """Show all the articles."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context=context)


def topic(request, topic_id):
    """Show one certain article."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context=context)


def new_topic(request):
    """Add a new topid."""
    if request.method != 'POST':
        # No data was sent; create empty form
        form = TopicForm()
    else:
        # POST was sent; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Show empty form or invalid.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context=context)
