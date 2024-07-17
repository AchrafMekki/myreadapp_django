from django import template

# Singleton
# meaning, each time you add a filter, you need to restart your server
register = template.Library()


@register.filter(name="semi_colon_seperator")
def semi_colon_seperator(value):
    return value.replace(', ', '; ')


@register.filter(name="join_with_comma")
def join_with_comma(value):
    return ', '.join(str(tag) for tag in value.all())







# 'tags': ', '.join(str(tag) for tag in book.tags.all()),
# 'authors': ', '.join(str(author)for author in book.authors.all())