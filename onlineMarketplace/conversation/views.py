from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm

@login_required
def new_conversation(request,item_pk):
    item = get_object_or_404(Item,pk=item_pk)

    # if you are the owner you should not be able to visit this page
    if item.created_by == request.user:
        return redirect('dashboard:index')

    # get all the conversation
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    # if already in the conversation redirect to conversation

    if conversations:
        return redirect('conversation:detail',pk=conversations.first().id) # redirect to conversation with the click in contact seller

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid(): #create new conversation
            conversation = Conversation.objects.create(item=item)
            # lets add owners/you to the members list
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html',{
        'form':form
    })

@login_required
def inbox(request):
    # get all the conversation without filter
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations' : conversations
    })

# lets talk to each other
@login_required
def detail(request,pk): # this pk is conversations
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail',pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request,'conversation/detail.html',{
        'conversation' : conversation,
        'form' : form
    })





