from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

def staff_required(view_func):
    """
    Decorador que verifica si el usuario es staff.
    Redirige al usuario a una página de acceso restringido si no es staff.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=reverse_lazy('notallowed'),  # Página de acceso restringido
        redirect_field_name=None
    )

    return actual_decorator(view_func)