from django.db import models
from TaAqui.enum import salas

data = models.DateField(
        verbose_name="Data",
        help_text="Selecione uma data.",
    )

class SalaChoices(models.TextChoices):
        # BLOCO 01 – Administrativo
        SALA_101 = "101", "101 – Gestão de Ensino"
        SALA_102 = "102", "102 – Gestão de Extensão e Gestão de Pesquisa"
        SALA_103 = "103", "103 – Sala de atendimentos"
        SALA_104 = "104", "104 – Sala de Professores"
        SALA_105 = "105", "105 – Sala de Professores"
        SALA_106 = "106", "106 – Sala de Professores"
        SALA_107 = "107", "107 – Sala de Professores"
        SALA_108 = "108", "108 – Sala de Professores"
        SALA_109 = "109", "109 – Banheiros"
        SALA_110 = "110", "110 – Sala de Convivência Servidores"
        SALA_111 = "111", "111 – Sala de Professores"
        SALA_112 = "112", "112 – Sala de Professores"
        SALA_113 = "113", "113 – Sala de Professores"
        SALA_114A = "114a", "114a – Recepção"
        SALA_114B = "114b", "114b – Laboratório Aberto"
        SALA_115 = "115", "115 – Direção-geral e Gabinete"
        SALA_116 = "116", "116 – Setor de Comunicação"
        SALA_117 = "117", "117 – Gestão de Pessoas e Gestão de Desenvolvimento Institucional"
        SALA_118 = "118", "118 – Sala de reuniões"
        SALA_119_121 = "119/121", "119/121 – Banheiros"
        SALA_120 = "120", "120 – Coordenadoria de Contratos, Setor de Compras e Licitações e Auditoria"
        SALA_122 = "122", "122 – Gestão de Administração"
 
        # BLOCO 02 – Convivência
        SALA_201 = "201", "201 – Biblioteca"
        SALA_202 = "202", "202 – Sala de Estudos e Co-working"
        SALA_203 = "203", "203 – Sala de Processamento Técnico"
        SALA_204 = "204", "204 – Sala das Coordenações de Curso"
        SALA_205A = "205a", "205a – Núcleo de Estudos e Pesquisa em Gênero e Sexualidade (Nepgs) e Núcleo de Estudos Afro-brasileiros e Indígenas (Neabi)"
        SALA_205B = "205b", "205b – Lanches"
        SALA_206 = "206", "206 – Cantina"
        SALA_207A = "207a", "207a – Banheiro Agênero"
        SALA_207B = "207b", "207b – Banheiro PCD"
        SALA_208 = "208", "208 – Sala de Estudantes"
        SALA_209 = "209", "209 – Sala Limpeza"
        SALA_210 = "210", "210 – Vestiários"
 
        # BLOCO 03 – Salas de aula
        SALA_301 = "301", "301 – Sala de aula"
        SALA_302 = "302", "302 – Sala de aula"
        SALA_303 = "303", "303 – Sala de aula"
        SALA_304 = "304", "304 – Sala de aula"
        SALA_305 = "305", "305 – Sala de aula"
        SALA_306 = "306", "306 – Sala de aula"
        SALA_307 = "307", "307 – Sala de aula"
        SALA_308 = "308", "308 – Banheiros"
        SALA_309 = "309", "309 – Sala de Aula"
        SALA_310 = "310", "310 – Sala de Aula"
        SALA_311 = "311", "311 – Sala de Aula"
        SALA_312 = "312", "312 – Sala de Aula"
 
        # BLOCO 04 – Laboratórios
        SALA_401 = "401", "401 – Laboratório de Redes"
        SALA_402 = "402", "402 – Laboratório de Eletrônica de Potência"
        SALA_403 = "403", "403 – Laboratório de Eletricidade"
        SALA_404 = "404", "404 – Laboratório de Instrumentação"
        SALA_405 = "405", "405 – Núcleo de Atendimento a Pessoas com Necessidades Específicas (Napne)"
        SALA_406 = "406", "406 – Laboratório de Eletrônica Digital"
        SALA_407 = "407", "407 – Departamento de Tecnologia da Informação"
        SALA_408 = "408", "408 – Banheiros"
        SALA_409 = "409", "409 – Laboratório de Informática"
        SALA_410 = "410", "410 – Laboratório de Informática"
        SALA_411 = "411", "411 – Laboratório de Informática"
        SALA_412 = "412", "412 – Laboratório de Informática"
 
        # BLOCO 05 – Salas temáticas
        SALA_501 = "501", "501 – Inovalab"
        SALA_502 = "502", "502 – Laboratório de Gestão e Negócios"
        SALA_503 = "503", "503 – Sala de Robótica"
        SALA_504 = "504", "504 – Sala de Humanidades"
        SALA_505 = "505", "505 – Sala de Matemática"
        SALA_506 = "506", "506 – Sala de aula"
        SALA_507 = "507", "507 – Banheiros"
        SALA_508 = "508", "508 – Laboratório de Ciências"
        SALA_509 = "509", "509 – Laboratório de Idiomas"
        SALA_510 = "510", "510 – Sala de Jogos e Dinâmicas de Grupo"
        SALA_511 = "511", "511 – Incubadora Tecnológica e Social"
        SALA_512 = "512", "512 – Miniauditório"
        SALA_513 = "513", "513 – Auditório Mirelle Barcos Nunes"
        SALA_514A = "514a", "514a – Sala de Teatro"
        SALA_514B = "514b", "514b – Arquivo"
        SALA_515 = "515", "515 – Estúdio Audiovisual"
        SALA_516 = "516", "516 – Sala de Artes"
        SALA_517 = "517", "517 – Laboratório de Turismo, Hospitalidade e Lazer"
        SALA_518 = "518", "518 – Sala de Música"
        SALA_519 = "519", "519 – Núcleo de Arte e Cultura (NAC) e Núcleo de Memória (NuMem)"
 
        # BLOCO 06 – Anexo Administrativo
        SALA_601 = "601", "601 – Coordenadoria de Infraestrutura"
        SALA_602 = "602", "602 – Zeladoria"
        SALA_603 = "603", "603 – Banheiro Infraestrutura"
        SALA_604 = "604", "604 – Depósito Jardinagem"
        SALA_605 = "605", "605 – Banheiro Churrasqueira"
        SALA_606 = "606", "606 – Depósito Limpeza"
        SALA_607 = "607", "607 – Garagem/Depósito"
        SALA_608 = "608", "608 – Garagem Principal"
        SALA_609 = "609", "609 – Cozinha"
        SALA_610 = "610", "610 – Almoxarifado"
 
        # BLOCO 07 – Laboratório de Solos
        SALA_701 = "701", "701 – Sala Multiuso"
        SALA_702 = "702", "702 – Sala de Professores"
        SALA_703 = "703", "703 – Depósito"
        SALA_704 = "704", "704 – Laboratório"
 
    sala = models.CharField(
        max_length=10,
        choices=SalaChoices.choices,
        verbose_name="Sala / Local",
        help_text="Selecione a sala ou local do campus.",
    )

def __str__(self):
        return f"{self.sala} - {self.data}"