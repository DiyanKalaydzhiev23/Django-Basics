from django import template
from posts.models import Post

register = template.Library()


class RecentPostsNode(template.Node):
    def __init__(self, count: str, varname: str):
        self.count = int(count)
        self.varname = varname

    def render(self, context):
        recent_posts = Post.objects.order_by('-created_at')[:self.count]
        context[self.varname] = recent_posts
        return ''


# {% recent_posts 5 %}
@register.tag
def get_recent_posts(parser, token):
    try:
        tag_name, count, varname = token.split_contents()  # Everything here is a string
    except ValueError:
        raise template.TemplateSyntaxError(
            "Tag 'get_recent_posts' requires exactly 3 arguments"
        )

    return RecentPostsNode(count, varname)
