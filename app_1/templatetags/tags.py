from random import randint, choice
from django import template


register = template.Library()


@register.simple_tag
def random_article():
    return randint(1, 500)


@register.simple_tag
def random_slug():
    letter_bank = [*range(97, 123), *range(65, 91), *range(48, 58), *range(45, 46)]
    return ''.join([chr(choice(letter_bank)) for _ in range(randint(5, 11))])
