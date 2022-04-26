from django import forms

from .models import Post


class PostModelForm(forms.ModelForm):
    tags = forms.CharField(label='tag', required=False)

    class Meta:
        model = Post
        fields = ["title", "image"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) <= 3:
            raise forms.ValidationError(
                "Length has to be more than 3 character"
            )
        return title
