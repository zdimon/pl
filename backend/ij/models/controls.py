from django.db import models
from django.utils.translation import ugettext_lazy as _
from .catalog import Category, SubCategory

class Control(models.Model):
    TYPE = (
        ('NumericTextbox', _('Numeric textbox')),
        ('Container', _('Container')),
        ('Select', _('Select field')),
        ('Checkbox', _('Checkbox')),
        ('FloatTextbox', _('Float textbox'))
    )
    name = models.CharField(
        max_length=250,
        help_text=_('Name'),
        verbose_name=_('Name')
        )
    alias = models.CharField(
        max_length = 250,
        help_text=_('Alias'),
        verbose_name=_('Alias')
        )
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ManyToManyField(SubCategory)
    type = models.CharField(
        verbose_name=_('Type'),
        choices=TYPE,
        default='one',
        max_length=20)
    
    def __str__(self):
        return self.name

class Option(models.Model):
    control = models.ForeignKey(Control,on_delete=models.CASCADE)
    value = models.CharField( max_length = 250 )
    text = models.TextField( )
    input_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s:%s:%s' % (self.value, self.input_text, self.text)
