from django.db import models

# Create your models here.

class Terra(models.Model):
    MUNICIPIOS = (
			('Abreulândia','Abreulândia'),
('Aguiarnópolis','Aguiarnópolis'),
('Aliança do Tocantins','Aliança do Tocantins'),
('Almas','Almas'),
('Alvorada','Alvorada'),
('Ananás','Ananás'),
('Angico','Angico'),
('Aparecida do Rio Negro','Aparecida do Rio Negro'),
('Aragominas','Aragominas'),
('Araguacema','Araguacema'),
('Araguaçu','Araguaçu'),
('Araguaína','Araguaína'),
('Araguanã','Araguanã'),
('Araguatins','Araguatins'),
('Arapoema','Arapoema'),
('Arraias','Arraias'),
('Augustinópolis','Augustinópolis'),
('Aurora do Tocantins','Aurora do Tocantins'),
('Axixá do Tocantins','Axixá do Tocantins'),
('Babaçulândia','Babaçulândia'),
('Bandeirantes do Tocantins','Bandeirantes do Tocantins'),
('Barra do Ouro','Barra do Ouro'),
('Barrolândia','Barrolândia'),
('Bernardo Sayão','Bernardo Sayão'),
('Bom Jesus do Tocantins','Bom Jesus do Tocantins'),
('Brasilândia do Tocantins','Brasilândia do Tocantins'),
('Brejinho de Nazaré','Brejinho de Nazaré'),
('Buriti do Tocantins','Buriti do Tocantins'),
('Cachoeirinha','Cachoeirinha'),
('Campos Lindos','Campos Lindos'),
('Cariri do Tocantins','Cariri do Tocantins'),
('Carmolândia','Carmolândia'),
('Carrasco Bonito','Carrasco Bonito'),
('Caseara','Caseara'),
('Centenário','Centenário'),
('Chapada da Natividade','Chapada da Natividade'),
('Chapada de Areia','Chapada de Areia'),
('Colinas do Tocantins','Colinas do Tocantins'),
('Colméia','Colméia'),
('Combinado','Combinado'),
('Conceição do Tocantins','Conceição do Tocantins'),
('Couto Magalhães','Couto Magalhães'),
('Cristalândia','Cristalândia'),
('Crixás do Tocantins','Crixás do Tocantins'),
('Darcinópolis','Darcinópolis'),
('Dianópolis','Dianópolis'),
('Divinópolis do Tocantins','Divinópolis do Tocantins'),
('Dois Irmãos do Tocantins','Dois Irmãos do Tocantins'),
('Dueré','Dueré'),
('Esperantina','Esperantina'),
('Fátima','Fátima'),
('Figueirópolis','Figueirópolis'),
('Filadélfia','Filadélfia'),
('Formoso do Araguaia','Formoso do Araguaia'),
('Fortaleza do Tabocão','Fortaleza do Tabocão'),
('Goianorte','Goianorte'),
('Goiatins','Goiatins'),
('Guaraí','Guaraí'),
('Gurupi','Gurupi'),
('Ipueiras','Ipueiras'),
('Itacajá','Itacajá'),
('Itaguatins','Itaguatins'),
('Itapiratins','Itapiratins'),
('Itaporã do Tocantins','Itaporã do Tocantins'),
('Jaú do Tocantins','Jaú do Tocantins'),
('Juarina','Juarina'),
('Lagoa da Confusão','Lagoa da Confusão'),
('Lagoa do Tocantins','Lagoa do Tocantins'),
('Lajeado','Lajeado'),
('Lavandeira','Lavandeira'),
('Lizarda','Lizarda'),
('Luzinópolis','Luzinópolis'),
('Marianópolis do Tocantins','Marianópolis do Tocantins'),
('Mateiros','Mateiros'),
('Maurilândia do Tocantins','Maurilândia do Tocantins'),
('Miracema do Tocantins','Miracema do Tocantins'),
('Miranorte','Miranorte'),
('Monte do Carmo','Monte do Carmo'),
('Monte Santo do Tocantins','Monte Santo do Tocantins'),
('Muricilândia','Muricilândia'),
('Natividade','Natividade'),
('Nazaré','Nazaré'),
('Nova Olinda','Nova Olinda'),
('Nova Rosalândia','Nova Rosalândia'),
('Novo Acordo','Novo Acordo'),
('Novo Alegre','Novo Alegre'),
('Novo Jardim','Novo Jardim'),
('Oliveira de Fátima','Oliveira de Fátima'),
('Palmas','Palmas'),
('Palmeirante','Palmeirante'),
('Palmeiras do Tocantins','Palmeiras do Tocantins'),
('Palmeirópolis','Palmeirópolis'),
('Paraíso do Tocantins','Paraíso do Tocantins'),
('Paranã','Paranã'),
('Pau D Arco','Pau D Arco'),
('Pedro Afonso','Pedro Afonso'),
('Peixe','Peixe'),
('Pequizeiro','Pequizeiro'),
('Pindorama do Tocantins','Pindorama do Tocantins'),
('Piraquê','Piraquê'),
('Pium','Pium'),
('Ponte Alta do Bom Jesus','Ponte Alta do Bom Jesus'),
('Ponte Alta do Tocantins','Ponte Alta do Tocantins'),
('Porto Alegre do Tocantins','Porto Alegre do Tocantins'),
('Porto Nacional','Porto Nacional'),
('Praia Norte','Praia Norte'),
('Presidente Kennedy','Presidente Kennedy'),
('Pugmil','Pugmil'),
('Recursolândia','Recursolândia'),
('Riachinho','Riachinho'),
('Rio da Conceição','Rio da Conceição'),
('Rio dos Bois','Rio dos Bois'),
('Rio Sono','Rio Sono'),
('Sampaio','Sampaio'),
('Sandolândia','Sandolândia'),
('Santa Fé do Araguaia','Santa Fé do Araguaia'),
('Santa Maria do Tocantins','Santa Maria do Tocantins'),
('Santa Rita do Tocantins','Santa Rita do Tocantins'),
('Santa Rosa do Tocantins','Santa Rosa do Tocantins'),
('Santa Tereza do Tocantins','Santa Tereza do Tocantins'),
('Santa Terezinha do Tocantins','Santa Terezinha do Tocantins'),
('São Bento do Tocantins','São Bento do Tocantins'),
('São Félix do Tocantins','São Félix do Tocantins'),
('São Miguel do Tocantins','São Miguel do Tocantins'),
('São Salvador do Tocantins','São Salvador do Tocantins'),
('São Sebastião do Tocantins','São Sebastião do Tocantins'),
('São Valério','São Valério'),
('Silvanópolis','Silvanópolis'),
('Sítio Novo do Tocantins','Sítio Novo do Tocantins'),
('Sucupira','Sucupira'),
('Taguatinga','Taguatinga'),
('Taipas do Tocantins','Taipas do Tocantins'),
('Talismã','Talismã'),
('Tocantínia','Tocantínia'),
('Tocantinópolis','Tocantinópolis'),
('Tupirama','Tupirama'),
('Tupiratins','Tupiratins'),
('Wanderlândia','Wanderlândia'),
('Xambioá','Xambioá'),
			) 

    municipio = models.CharField(max_length=200,null=True, choices=MUNICIPIOS)
    loteamento = models.CharField(max_length=200,null=True)
    numero = models.FloatField(null=True)
    area = models.FloatField(null=True)
    valor = models.FloatField(null=True)
    def __str__(self):
        return self.municipio

class Interessado (models.Model):
    nome = models.CharField(max_length=200,null=True)
    cpf = models.CharField(max_length=14,null=True, unique=True, default='Somente numeros')
    email = models.EmailField(null=True)
    telefone = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nome

class Setor (models.Model):
    nome = models.CharField(max_length=200,null=True)
    sigla = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.sigla

class Processo (models.Model):
    STATUS = (
			('Finalizado', 'Finalizado'),
			('Pendente', 'Pendente'),
			('Cancelado', 'Cancelado'),
			)
    interessado = models.ManyToManyField(Interessado)
    terra = models.ForeignKey(Terra, null=True, on_delete=models.SET_NULL)
    setor = models.ForeignKey(Setor, null=True, on_delete=models.SET_NULL)
    numeroProcesso = models.CharField(max_length=200,null=True)
    dataProcesso = models.DateField(null=True)
    numFolhas = models.FloatField(null=True)
    numeroTitulo = models.CharField(max_length=200, blank=True)
    dataTitulo = models.DateField(null=True, blank=True)
    folha = models.FloatField(null=True, blank=True)
    livro = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    observação = models.CharField(max_length=200, null=True, blank=True)
    #pdf = models.FileField(upload_to='titulo/pdfs/')

    def __str__(self):
        return self.numeroProcesso
