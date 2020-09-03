from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
class ShowHidePasswordWidget(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        super().render(name, value, attrs)
        flat_attrs = flatatt(attrs)
        html = '''
<input %(attrs)s name="password" type="password" value="%(value)s"/>
<span id="__action__%(id)s__show_button">
<a href="javascript:show_pwd_%(id)s()">Show</a></span>
<span id="__action__%(id)s__hide_button" style="display:none;">
<a href="javascript:hide_pwd_%(id)s()">Hide</a></span>
<script type="text/javascript">
function show_pwd_%(id)s() {
    document.getElementById("%(id)s").setAttribute('type', 'text');
    document.getElementById("__action__%(id)s__show_button")
        .style.display="none";
    document.getElementById("__action__%(id)s__hide_button")
        .style.display=null;
}
function hide_pwd_%(id)s() {
    document.getElementById("%(id)s").setAttribute('type', 'password');
    document.getElementById("__action__%(id)s__hide_button")
        .style.display="none";
    document.getElementById("__action__%(id)s__show_button")
        .style.display=null;
}
</script>
        ''' % {
            'attrs': flat_attrs,
            'id': attrs['id'],
            'value': value,
        }
        return mark_safe(html)