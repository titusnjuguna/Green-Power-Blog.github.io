from django import template
from django.template.defaultfilters import stringfilter 


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def Parag(value,arg):
    word = value.count('')
    if word > 300 :
        return word[:300]
    else:    
        return word[0:]

