from django.shortcuts import render, redirect
from django.http import JsonResponse


from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.http import JsonResponse

from django.utils import timezone

from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import json



llm = LlamaCpp(
    model_path = "/media/dinesh/01DA36534F599F70/model/mistral-7b-instruct-v0.2.Q8_0.gguf",
    n_gpu_layers=-1,
    n_batch=512,
    n_ctx=2048,
    f16_kv=True,
    # callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    verbose=True,
)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)

def ask_openai(message):
    answer = conversation.predict(input=message)
    return answer

# Create your views here.

def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chats/chatbot.html', {'chats': chats})



def modify_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data['text']
        print('text', text)
        final = f"""

        {text} 
        
        As a content rephraser, your goal is to make the paragraph above easy to understand for everyone. 
        Try to explain it in simple terms and make sure it's clear. Aim for at least 500 words in your explanation. do not include any html tags in the text
        
        
        """
        res = llm.invoke(final)
        print('res', res)
        return JsonResponse({'response': res})



# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('chatbot')
#         else:
#             error_message = 'Invalid username or password'
#             return render(request, 'login.html', {'error_message': error_message})
#     else:
#         return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             try:
#                 user = User.objects.create_user(username, email, password1)
#                 user.save()
#                 auth.login(request, user)
#                 return redirect('chatbot')
#             except:
#                 error_message = 'Error creating account'
#                 return render(request, 'register.html', {'error_message': error_message})
#         else:
#             error_message = 'Password dont match'
#             return render(request, 'register.html', {'error_message': error_message})
#     return render(request, 'register.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('login')
