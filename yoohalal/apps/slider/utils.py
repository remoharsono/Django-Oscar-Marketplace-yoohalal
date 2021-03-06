import os

from django.utils.translation import ugettext_lazy as _
from django.db.models.fields.files import FileField
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils.safestring import mark_safe


class AdminThumbnailMixin(object):
    thumbnail_options = {'size': (60, 60)}
    thumbnail_image_field_name = 'image'
    thumbnail_alt_field_name = None

    def _thumb(self, image, options={'size': (60, 60)}, alt=None):
        from easy_thumbnails.files import get_thumbnailer

        media = getattr(settings, 'THUMBNAIL_MEDIA_URL', settings.MEDIA_URL)
        attrs = []
        try:
            src = "%s%s" % (media, get_thumbnailer(image).get_thumbnail(options))
        except:
            src = ""

        if alt is not None: attrs.append('alt="%s"' % alt)

        return mark_safe('<img src="%s" %s />' % (src, " ".join(attrs)))

    def thumbnail(self, obj):
        kwargs = {'options': self.thumbnail_options}
        if self.thumbnail_alt_field_name:
            kwargs['alt'] = getattr(obj, self.thumbnail_alt_field_name)
        return self._thumb(getattr(obj, self.thumbnail_image_field_name), **kwargs)
    thumbnail.allow_tags = True
    thumbnail.short_description = _('Thumbnail')


def file_cleanup(sender, **kwargs):
    for fieldname in [f.name for f in sender._meta.get_fields()]:
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
        if field and isinstance(field, FileField):
            inst = kwargs['instance']
            f = getattr(inst, fieldname)
            m = inst.__class__._default_manager
            if hasattr(f, 'path') and os.path.exists(f.path) \
                and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
                .exclude(pk=inst._get_pk_val()):
                    try:
                        #os.remove(f.path)
                        default_storage.delete(f.path)
                    except:
                        pass