from django import template


register = template.Library()

@register.inclusion_tag('common/user_info.html', takes_context=True)
def user_info(context, user):
    """
    There are better ways to do this than creating inclusion tag for it
    """
    if user.is_authenticated:
        return {
            "username": user.username,
        }

    return {
        "username": "Anonymous",
    }
