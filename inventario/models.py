from django.db import models

class Recepcion(models.Model):
    # ¡LISTO! Quitamos el "unique=True". Ahora puedes repetir guías sin que el sistema te bloquee.
    guia_rastreo = models.CharField(max_length=100, verbose_name="Guía de Paquetería o Folio Interno")
    proyecto = models.CharField(max_length=100, verbose_name="Proyecto Asignado")
    origen = models.CharField(max_length=100, verbose_name="Origen / Proveedor (Ej. IBM, Irium)", blank=True)
    fecha_recepcion = models.DateField(verbose_name="Fecha de Recepción")
    creado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recepción (Guía/Caja)"
        verbose_name_plural = "1. Recepciones (Entradas)"

    def __str__(self):
        return f"Guía: {self.guia_rastreo} - {self.proyecto}"

class Equipo(models.Model):
    TIPO_OPCIONES = [
        ('CPU', 'CPU / Computadora'),
        ('ESCANER', 'Escáner'),
        ('MONITOR', 'Monitor'),
        ('CAJON', 'Cajón de Dinero'),
        ('IMPRESORA', 'Impresora'),
        ('OTRO', 'Componente / Otro'),
    ]

    recepcion = models.ForeignKey(Recepcion, on_delete=models.CASCADE, related_name='equipos', verbose_name="Guía de Entrada / Proyecto")
    tipo_item = models.CharField(max_length=20, choices=TIPO_OPCIONES, default='CPU', verbose_name="Tipo de Artículo")
    
    equipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    serie = models.CharField(max_length=100, verbose_name="Serie Principal")
    serie_remplazo = models.CharField(max_length=100, blank=True, null=True)
    diagnostico = models.TextField()
    estatus = models.CharField(max_length=50) 
    
    # --- COMPONENTES CPU ---
    fuente = models.BooleanField(default=False, verbose_name="Fuente")
    ventilador = models.BooleanField(default=False, verbose_name="Ventilador")
    ssd = models.BooleanField(default=False, verbose_name="SSD")
    extensor = models.BooleanField(default=False, verbose_name="Extensor")
    gabinete = models.BooleanField(default=False, verbose_name="Gabinete")
    disipador = models.BooleanField(default=False, verbose_name="Disipador")
    mb = models.BooleanField(default=False, verbose_name="MB")
    memoria_ram = models.BooleanField(default=False, verbose_name="Memoria RAM")
    adaptador_red = models.BooleanField(default=False, verbose_name="Adaptador Red")
    n_serie_fuente = models.CharField(max_length=100, blank=True)
    n_serie_mb = models.CharField(max_length=100, blank=True)
    n_serie_ram = models.CharField(max_length=100, blank=True)
    n_serie_ssd = models.CharField(max_length=100, blank=True)
    n_serie_gabinete = models.CharField(max_length=100, blank=True)

    # --- COMPONENTES ESCÁNER ---
    cable_usb = models.BooleanField(default=False, verbose_name="Cable de Datos (USB)")
    base_escaner = models.BooleanField(default=False, verbose_name="Base del Escáner")
    placa_interna = models.BooleanField(default=False, verbose_name="Placa Interna (Hardware)")

    # --- COMPONENTES MONITOR ---
    base_monitor = models.BooleanField(default=False, verbose_name="Base del Monitor")
    cable_hdmi = models.BooleanField(default=False, verbose_name="Cable HDMI")
    cable_corriente = models.BooleanField(default=False, verbose_name="Cable de Corriente")

    # --- COMPONENTES CAJÓN DE DINERO ---
    bandeja_interna = models.BooleanField(default=False, verbose_name="Bandeja Interna")
    llave = models.BooleanField(default=False, verbose_name="Llave")
    cable_cajon = models.BooleanField(default=False, verbose_name="Cable de Cajón")

    # --- COMPONENTES IMPRESORA ---
    navaja = models.BooleanField(default=False, verbose_name="Navaja (Corte)")
    sensor_papel = models.BooleanField(default=False, verbose_name="Sensor de Papel")
    plancha_termica = models.BooleanField(default=False, verbose_name="Plancha Térmica")
    motor = models.BooleanField(default=False, verbose_name="Motor")
    placa = models.BooleanField(default=False, verbose_name="Placa (Motherboard)")
    modulo_boton = models.BooleanField(default=False, verbose_name="Módulo de Botones")
    
    inge = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Equipo / Periférico"
        verbose_name_plural = "2. Inventario (CPUs y Periféricos)"

    def __str__(self):
        return f"[{self.tipo_item}] {self.serie} - {self.recepcion.proyecto}"

class EquipoImagen(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='equipos_evidencias/%Y/%m/%d/', verbose_name="Fotografía de Evidencia")
    descripcion = models.CharField(max_length=200, blank=True, verbose_name="Descripción opcional")
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Evidencia Fotográfica"
        verbose_name_plural = "Evidencias Fotográficas"

    def __str__(self):
        return f"Evidencia de {self.equipo.serie}"

class Pallet(models.Model):
    folio = models.CharField(max_length=50, unique=True, verbose_name="Folio del Envío (Ej. PAL-001)")
    destino = models.CharField(max_length=100, verbose_name="Destino (Ej. Irium, IBM)")
    fecha_envio = models.DateField(verbose_name="Fecha de Envío")
    equipos = models.ManyToManyField(Equipo, blank=True, related_name='pallets', verbose_name="Artículos Asignados")
    creado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pallet de Envío"
        verbose_name_plural = "3. Pallets de Envío (Salidas)"

    def __str__(self):
        return f"{self.folio} - {self.destino}"