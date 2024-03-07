from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


def index(request):
    pet_name_pattern = request.GET.get('pet_name_pattern', None)
    pet_photo = PetPhoto.objects.all()

    if pet_name_pattern:
        pet_photo = pet_photo.filter(tagged_pets__name__icontains=pet_name_pattern)

    comment_form = CommentForm()

    context = {
        'pet_photo': pet_photo,
        'pet_name_pattern': pet_name_pattern,
        'comment_form': comment_form,
    }
    return render(request, "common/index.html", context=context)


def like_pet_photo(request, pk):
    # pet_photo_like = PhotoLike.objects.first(pk=pk, user=request.user)
    pet_photo_like = PhotoLike.objects.filter(to_photo_id=pk).first()

    if pet_photo_like:
        # dislike
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(to_photo_id=pk)

    return redirect(request.META['HTTP_REFERER'] + f"#photo-{pk}")


def add_comment(request, pk):
    if request.method == "POST":
        pet_photo_comment = PetPhoto.objects.filter(id=pk).first()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = pet_photo_comment
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#photo-{pk}')
