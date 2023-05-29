from django.contrib import admin
from diagnosticos.models import (
    ResponsavelTecnico,
    ProdutorRural,
    Propriedade,
    Diagnostico,
)

admin.site.register(ResponsavelTecnico)
admin.site.register(ProdutorRural)
admin.site.register(Propriedade)
admin.site.register(Diagnostico)