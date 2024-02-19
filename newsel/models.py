from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _

# Create your models here.


class News(models.Model):
    title=models.CharField(max_length=250)
    summery=models.TextField(null=True)
    content=models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images')
    source_website = models.CharField(max_length=200,null=True)
    url = models.URLField(null=True, blank=True,)
    created_date = jmodels.jDateTimeField(auto_now_add=True,null=True)
    updated_date = jmodels.jDateTimeField(auto_now=True,null=True)
    published_date =jmodels.jDateTimeField(null=True)
    type_of_news="crawl"
    
    def __str__(self):
         return self.title


class Post(models.Model):
    #folder_name = models.ForeignKey('blog.FolderName', on_delete=models.CASCADE, verbose_name=_('پرونده'))
    folder_name = models.CharField(_('پرونده'), max_length=250)
    #publisher = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='posts_publisher', verbose_name=_('ناشر'))
    publisher= models.CharField(_('ناشر'), max_length=250)
    #author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='posts', verbose_name=_('نویسنده'))
    author= models.CharField(_('نویسنده'), max_length=250)

    ro_titer = models.CharField(_('رو تیتر'), max_length=70, null=True, blank=True)
    h1 = models.CharField(_('تگ h1'), max_length=250, null=True, blank=True)
    slog = models.CharField(_('نامک'), max_length=25, null=True, blank=True,)
    title = models.CharField(_('عنوان'), max_length=250, unique=True)
    #title_tag = models.CharField(max_length=128)
    snippet = models.TextField(_('چکیده'))
    #meta_kword = models.ManyToManyField("attachments.MetaKword", verbose_name=_('کلمه متا'),null=True, blank=True)
    meta_kword=models.CharField(_('کلمه متا'), max_length=70,null=True, blank=True)
    meta_description = models.CharField(_('توضیحات متا'), max_length=127, null=True, blank=True)
    content = models.TextField(_('محتوا'))
    
    #image = models.ForeignKey("attachments.Image", on_delete=models.SET_NULL, null=True, blank=True , verbose_name=_('تصویر'))
    image=models.CharField(_('تصویر'), max_length=70,null=True, blank=True)
    image_url = models.URLField(_('لینک تصویر'), null=True, blank=True)
    #video = models.ForeignKey("attachments.Video", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('ویدیو'))
    video=models.CharField(_('ویدئو'), max_length=70,null=True, blank=True)
    video_url = models.URLField(_('لینک ویدئو'), null=True, blank=True,)
    #url = models.ForeignKey("attachments.URL", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('لینک'))
    url=models.CharField(_('لینک'), max_length=250,null=True, blank=True)
    embed_code = models.TextField(_('کد امبد'), null=True, blank=True, )
    media_description = models.CharField(_('توضیحات رسانه استفاده شده'), max_length=255, null=True, blank=True)
    
    #type_of_news = models.ForeignKey("attachments.TypeOfNews", on_del
    # ete=models.SET_NULL, null=True, blank=True, verbose_name=_('نوع خبر'), default='تجمیعی')
    type_of_news=models.CharField(_('نوع خبر'), max_length=250,null=True, blank=True)
    #source_website = models.ForeignKey("attachments.SourceOfNews", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('منبع خبر'))
    source_website=models.CharField(_('منبع خبر'), max_length=250,null=True, blank=True)
    #tags = models.ManyToManyField("attachments.Tag", limit_choices_to={'confirm': True}, related_name='posts_tag', verbose_name=_('تگ'))
    tags=models.CharField(_(' تگ'), max_length=70)
    
    counted_views = models.IntegerField(_('تعداد بازدید'), null=True, default=0)
    status = models.BooleanField(_('رسیدن زمان انتشار'), null=True,default=False)
    
    confirm_to_post = models.BooleanField(_('پست تایید شده؟'), null=True, default=False,)
    supervisor_to_confirm = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True, related_name='confirmed_posts', verbose_name=_('سرپرست تایید کننده پست'))
    supervisor_to_confirm=models.CharField(_('سرپرست تایید کننده پست'), max_length=250,null=True)
    
    trash = models.BooleanField(_('زباله دان'),  null=True, default=False,)
    
    created_date = jmodels.jDateTimeField(_('تاریخ ایجاد'), auto_now_add=True,null=True)
    updated_date = jmodels.jDateTimeField(_('تاریخ آخرین به روز رسانی'),auto_now=True,null=True)
    published_date = jmodels.jDateTimeField(_('تاریخ انتشار'),)

    def __str__(self):
        return self.title
