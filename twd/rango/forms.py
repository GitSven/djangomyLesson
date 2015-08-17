# -*-coding:utf-8-*-

from django import forms

from .models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='请输入类别名')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields = ('name',)

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')

        if name and not name.strip():
            name = name.strip()
            cleaned_data['name'] = name

        return cleaned_data


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='请输入文章标题')
    url = forms.URLField(max_length=200, help_text='请输入文章链接')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data
