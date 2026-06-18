from django.db import models

contato = models.CharField(
        max_length=150,
        verbose_name="E-mail ou Telefone",
        help_text="Informe um e-mail (ex: nome@dominio.com) ou um telefone (ex: (51) 99999-9999).",
    )

def __str__(self):
    return f"{self.contato}"

