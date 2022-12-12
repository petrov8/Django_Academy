from support.base.template_tag import register


@register.simple_tag(name="format_date")
def return_formatted_date(d):
    return d.strftime("%d %b %Y")

