import openai
from django.shortcuts import render ,redirect
from django.shortcuts import render
import requests


def generate_social_post(request):
    openai.api_key = "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"
    social_topic = request.GET.get("social_topic")

    prompt = f"Generate a social media post named {social_topic}:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        
        n=1,
        stop=None,
        temperature=0.5,
    )
    your_blog = response["choices"][0]["text"].strip()
    return render(request, 'a.html', {'your_blog': your_blog})


def blog_post(request):
    openai.api_key = "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"
    topic = request.GET.get("topic")
    prompt = f"Generate a post about {topic}:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    post = response["choices"][0]["text"].strip()
    return render(request, 'a.html', {'post': post})


# product discriptions writting tools
def generate_description(request):
    openai.api_key = "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"
    product_title = request.GET.get("product_title")
    prompt = f"Generate a post about {product_title}:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    description = response["choices"][0]["text"].strip()
    return render(request, 'a.html', {'description': description})





def home(request):
    return render(request,'a.html')

