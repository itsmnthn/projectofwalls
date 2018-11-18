from django.utils.text import slugify
import os
from uuid import uuid4


def unique_slug_generator(model_instance, title, slug_field):
    """Slugify the title

    Arguments:
        model_instance {class} -- instance of the model class
        title {str} -- Field that will be slugified
        slug_field {model.SlugField} -- Field that stores slugified title
    """
    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug


def upload_image(instance, filename):
    """Creates the path of image and renames the image

    Arguments:
        instance {reference} -- instance of the model to access the model fields
        filename {str} -- file name that user uploaded
    """
    extention = filename.split('.')[-1]
    try:
        if instance.slug:
            filename = "{}.{}".format(instance.slug.replace(' ', '-'), extention)
        else:
            filename = '{}.{}'.format(uuid4().hex, extention)
    except:
        if instance:
            filename = "{}.{}".format(instance.get_name().replace(' ', '-'), extention)
        else:
            filename = '{}.{}'.format(uuid4().hex, extention)

    return os.path.join(instance.upload_to(), filename)
